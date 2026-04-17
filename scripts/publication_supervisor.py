#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import pathlib
import shlex
import signal
import subprocess
import sys
import time
from dataclasses import dataclass
from typing import Sequence

import publication_runtime as pr


ROOT = pr.ROOT
STOP_MARKER = ROOT / ".stop_harness"
CYCLE_LOG = pr.LOGS / "cycle.log"

DEFAULT_HEARTBEAT_SECS = int(os.environ.get("AUTOMATH_RUNNER_HEARTBEAT_SECS", "15"))
DEFAULT_STALE_LEASE_SECS = int(os.environ.get("AUTOMATH_RUNNER_STALE_LEASE_SECS", "180"))
DEFAULT_STALL_SECS = int(os.environ.get("AUTOMATH_RUNNER_STALL_SECS", "180"))
DEFAULT_KILL_GRACE_SECS = int(os.environ.get("AUTOMATH_RUNNER_KILL_GRACE_SECS", "10"))
DEFAULT_SLEEP_SECONDS = int(os.environ.get("AUTOMATH_SLEEP_SECONDS", "60"))


def env_flag(name: str, default: bool = False) -> bool:
    raw = os.environ.get(name)
    if raw is None:
        return default
    return raw.strip().lower() not in {"0", "false", "no", "off"}


def now_str() -> str:
    return pr.now_str()


def append_cycle_log(message: str, *, run_id: str | None = None, cycle_id: str | None = None) -> None:
    rendered = pr.format_runtime_message(message, run_id=run_id, cycle_id=cycle_id)
    CYCLE_LOG.parent.mkdir(parents=True, exist_ok=True)
    with CYCLE_LOG.open("a", encoding="utf-8") as fh:
        fh.write(f"{rendered}\n")
    print(rendered)


def stop_harness_enabled() -> bool:
    normalized = os.environ.get("AUTOMATH_ENABLE_STOP_HARNESS", "1").strip().lower()
    return normalized not in {"0", "false", "no", "off"}


def pgid_alive(pgid: int | None) -> bool:
    if pgid is None or pgid <= 0:
        return False
    try:
        os.killpg(pgid, 0)
    except OSError:
        return False
    return True


def signal_process_group(pgid: int | None, sig: signal.Signals) -> bool:
    if pgid is None or pgid <= 0:
        return False
    try:
        os.killpg(pgid, sig)
    except ProcessLookupError:
        return False
    return True


def file_age_fallback(path: pathlib.Path) -> float | None:
    return pr.file_age_seconds(path)


def stale_age_seconds(lease: dict[str, object]) -> float:
    heartbeat_age = pr.iso_age_seconds(lease.get("last_heartbeat_at") if isinstance(lease.get("last_heartbeat_at"), str) else None)
    if heartbeat_age is not None:
        return heartbeat_age
    for candidate in [pr.HEARTBEAT_PATH, pr.LEASE_PATH, pr.LEASE_LOCK_PATH]:
        age = file_age_fallback(candidate)
        if age is not None:
            return age
    return float("inf")


def active_slugs_from_heartbeat(heartbeat: dict[str, object]) -> list[str]:
    active_workers = heartbeat.get("active_workers")
    slugs: list[str] = []
    if isinstance(active_workers, list):
        for item in active_workers:
            if isinstance(item, dict):
                slug = item.get("slug")
                if isinstance(slug, str) and slug.strip():
                    slugs.append(slug.strip())
    if slugs:
        return sorted(set(slugs))
    active_slug = heartbeat.get("active_slug")
    if isinstance(active_slug, str):
        return sorted({part.strip() for part in active_slug.split(",") if part.strip()})
    return []


def default_child_command(extra_args: Sequence[str]) -> list[str]:
    quoted_args = " ".join(shlex.quote(arg) for arg in extra_args)
    command = 'if [[ -f "$HOME/.elan/env" ]]; then source "$HOME/.elan/env"; fi; python3 scripts/automath_cycle.py'
    if quoted_args:
        command += f" {quoted_args}"
    return ["bash", "-lc", command]


def configured_child_command(extra_args: Sequence[str]) -> list[str]:
    override = os.environ.get("AUTOMATH_SUPERVISOR_CHILD_CMD", "").strip()
    if override:
        return ["bash", "-lc", override]
    return default_child_command(extra_args)


@dataclass
class CycleOutcome:
    cycle_id: str
    status: str
    returncode: int
    salvage_path: pathlib.Path | None = None


class LeaseError(RuntimeError):
    pass


class PublicationSupervisor:
    def __init__(self, mode: str, *, cycles: int | None, child_args: Sequence[str], verbose: bool = False):
        self.mode = mode
        self.cycles = cycles
        self.child_args = list(child_args)
        self.run_id = pr.make_run_id()
        self.pid = os.getpid()
        self.pgid = pr.process_group_id(self.pid)
        self.heartbeat_secs = DEFAULT_HEARTBEAT_SECS
        self.stale_lease_secs = DEFAULT_STALE_LEASE_SECS
        self.stall_secs = DEFAULT_STALL_SECS
        self.kill_grace_secs = DEFAULT_KILL_GRACE_SECS
        self.sleep_seconds = DEFAULT_SLEEP_SECONDS
        self.verbose = verbose or env_flag("AUTOMATH_VERBOSE", default=False)
        self.verbose_interval_secs = int(
            os.environ.get(
                "AUTOMATH_VERBOSE_INTERVAL_SECS",
                str(max(self.heartbeat_secs, 15)),
            )
        )
        self._lease_started_at = pr.now_iso()
        self._last_verbose_key: tuple[object, ...] | None = None
        self._last_verbose_emit_monotonic = 0.0

    def verbose_print(self, message: str, *, cycle_id: str | None = None) -> None:
        if not self.verbose:
            return
        rendered = pr.format_runtime_message(f"[verbose] {message}", run_id=self.run_id, cycle_id=cycle_id)
        print(rendered, flush=True)

    def _worker_summary(self, heartbeat: dict[str, object]) -> str | None:
        active_workers = heartbeat.get("active_workers")
        if not isinstance(active_workers, list) or not active_workers:
            return None
        labels: list[str] = []
        for item in active_workers:
            if not isinstance(item, dict):
                continue
            role = str(item.get("worker_role") or "worker")
            slug = str(item.get("slug") or "?")
            labels.append(f"{role}:{slug}")
        if not labels:
            return None
        return ",".join(labels)

    def maybe_emit_verbose_progress(
        self,
        *,
        cycle_id: str,
        proc: subprocess.Popen[str],
        heartbeat: dict[str, object],
        heartbeat_age: float | None,
    ) -> None:
        if not self.verbose:
            return
        state = heartbeat.get("state") or "unknown"
        stage = heartbeat.get("stage") or "unknown"
        slug = heartbeat.get("active_slug") or "(none)"
        stdout_log = heartbeat.get("stdout_log") or "(none)"
        worker_summary = self._worker_summary(heartbeat)
        stdout_age = pr.iso_age_seconds(
            heartbeat.get("last_stdout_mtime") if isinstance(heartbeat.get("last_stdout_mtime"), str) else None,
            default=None,
        )
        key = (
            state,
            stage,
            slug,
            stdout_log,
            worker_summary,
            heartbeat.get("manager_pid") or proc.pid,
            heartbeat.get("stage_child_pid"),
        )
        now_monotonic = time.monotonic()
        should_emit = key != self._last_verbose_key
        if not should_emit and now_monotonic - self._last_verbose_emit_monotonic >= self.verbose_interval_secs:
            should_emit = True
        if not should_emit:
            return
        self._last_verbose_key = key
        self._last_verbose_emit_monotonic = now_monotonic

        parts = [
            f"state={state}",
            f"stage={stage}",
            f"slug={slug}",
            f"manager_pid={heartbeat.get('manager_pid') or proc.pid}",
        ]
        if heartbeat.get("stage_child_pid"):
            parts.append(f"stage_child_pid={heartbeat.get('stage_child_pid')}")
        if heartbeat_age is not None:
            parts.append(f"heartbeat_age={heartbeat_age:.0f}s")
        if stdout_age is not None:
            parts.append(f"stdout_age={stdout_age:.0f}s")
        if worker_summary:
            parts.append(f"workers={worker_summary}")
        if stdout_log and stdout_log != "(none)":
            parts.append(f"log={stdout_log}")
        self.verbose_print("progress: " + " | ".join(parts), cycle_id=cycle_id)

    def _lease_payload(self, *, cycle_id: str | None = None, last_heartbeat_at: str | None = None) -> dict[str, object]:
        return {
            "run_id": self.run_id,
            "pid": self.pid,
            "pgid": self.pgid,
            "started_at": self._lease_started_at,
            "last_heartbeat_at": last_heartbeat_at or pr.now_iso(),
            "mode": self.mode,
            "cwd": str(ROOT),
            "cycle_id": cycle_id,
        }

    def refresh_lease(self, *, cycle_id: str | None = None, last_heartbeat_at: str | None = None) -> None:
        pr.write_json_atomic(
            pr.LEASE_PATH,
            self._lease_payload(cycle_id=cycle_id, last_heartbeat_at=last_heartbeat_at),
        )

    def release_lease(self) -> None:
        try:
            pr.LEASE_PATH.unlink()
        except FileNotFoundError:
            pass
        try:
            pr.LEASE_LOCK_PATH.unlink()
        except FileNotFoundError:
            pass

    def acquire_lease(self) -> None:
        pr.ensure_runtime_layout()
        reclaimed = False
        stale_snapshot: dict[str, object] | None = None
        while True:
            try:
                fd = os.open(pr.LEASE_LOCK_PATH, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o644)
            except FileExistsError:
                lease = pr.load_lease()
                owner_pid = lease.get("pid") if isinstance(lease.get("pid"), int) else None
                age = stale_age_seconds(lease)
                owner_alive = pr.process_is_alive(owner_pid)
                if owner_alive:
                    message = (
                        f"refusing to start {self.mode}: live main publication lease held by pid {owner_pid} "
                        f"(run {lease.get('run_id', 'unknown')})."
                    )
                    append_cycle_log(message, run_id=self.run_id)
                    pr.emit_event(
                        "lease_refused",
                        run_id=self.run_id,
                        held_by_run_id=lease.get("run_id"),
                        held_by_pid=owner_pid,
                        held_by_mode=lease.get("mode"),
                        lease_last_heartbeat_at=lease.get("last_heartbeat_at"),
                    )
                    raise LeaseError(message)
                if age > self.stale_lease_secs:
                    stale_snapshot = lease
                    try:
                        pr.LEASE_LOCK_PATH.unlink()
                    except FileNotFoundError:
                        pass
                    reclaimed = True
                    continue
                message = (
                    f"refusing to start {self.mode}: main publication lease is ambiguous and not yet stale "
                    f"(owner pid {owner_pid or 'unknown'}, heartbeat age {age:.1f}s)."
                )
                append_cycle_log(message, run_id=self.run_id)
                pr.emit_event(
                    "lease_refused",
                    run_id=self.run_id,
                    held_by_run_id=lease.get("run_id"),
                    held_by_pid=owner_pid,
                    held_by_mode=lease.get("mode"),
                    lease_last_heartbeat_at=lease.get("last_heartbeat_at"),
                )
                raise LeaseError(message)
            else:
                os.close(fd)
                break

        self.refresh_lease(cycle_id=None)
        if reclaimed:
            append_cycle_log("reclaimed stale main publication lease.", run_id=self.run_id)
            pr.emit_event(
                "lease_reclaimed",
                run_id=self.run_id,
                stale_lease=stale_snapshot or {},
                pid=self.pid,
                pgid=self.pgid,
                mode=self.mode,
            )
        else:
            append_cycle_log("acquired main publication lease.", run_id=self.run_id)
            pr.emit_event(
                "lease_acquired",
                run_id=self.run_id,
                pid=self.pid,
                pgid=self.pgid,
                mode=self.mode,
            )

    def should_stop_before_cycle(self) -> bool:
        return stop_harness_enabled() and STOP_MARKER.exists()

    def launch_cycle(self, cycle_id: str) -> subprocess.Popen[str]:
        env = os.environ.copy()
        env["AUTOMATH_RUN_ID"] = self.run_id
        env["AUTOMATH_CYCLE_ID"] = cycle_id
        env["AUTOMATH_RUNTIME_ROLE"] = "main_publication"
        cmd = configured_child_command(self.child_args)
        self._last_verbose_key = None
        self._last_verbose_emit_monotonic = 0.0
        self.verbose_print("launching child: " + shlex.join(cmd), cycle_id=cycle_id)
        proc = subprocess.Popen(
            cmd,
            cwd=ROOT,
            env=env,
            text=True,
            start_new_session=True,
        )
        heartbeat = {
            "run_id": self.run_id,
            "cycle_id": cycle_id,
            "state": "cycle_launching",
            "stage": "startup",
            "active_slug": None,
            "manager_pid": proc.pid,
            "manager_pgid": pr.process_group_id(proc.pid),
            "stage_child_pid": None,
            "stage_child_pgid": None,
            "stdout_log": None,
            "last_heartbeat_at": pr.now_iso(),
            "last_stdout_mtime": None,
            "active_workers": [],
        }
        pr.write_json_atomic(pr.HEARTBEAT_PATH, heartbeat)
        self.refresh_lease(cycle_id=cycle_id, last_heartbeat_at=heartbeat["last_heartbeat_at"])
        pr.emit_event(
            "cycle_started",
            run_id=self.run_id,
            cycle_id=cycle_id,
            pid=proc.pid,
            pgid=heartbeat["manager_pgid"],
            mode=self.mode,
        )
        append_cycle_log(f"publication cycle started at {now_str()}.", run_id=self.run_id, cycle_id=cycle_id)
        return proc

    def _load_cycle_heartbeat(self, cycle_id: str) -> dict[str, object]:
        heartbeat = pr.load_heartbeat()
        if heartbeat.get("run_id") != self.run_id or heartbeat.get("cycle_id") != cycle_id:
            return {}
        return heartbeat

    def _write_stall_salvage(self, *, cycle_id: str, heartbeat: dict[str, object], heartbeat_age: float, proc: subprocess.Popen[str]) -> pathlib.Path:
        payload = {
            "run_id": self.run_id,
            "cycle_id": cycle_id,
            "mode": self.mode,
            "detected_at": pr.now_iso(),
            "heartbeat_age_secs": heartbeat_age,
            "supervisor_pid": self.pid,
            "supervisor_pgid": self.pgid,
            "manager_pid": heartbeat.get("manager_pid") or proc.pid,
            "manager_pgid": heartbeat.get("manager_pgid") or pr.process_group_id(proc.pid),
            "stage": heartbeat.get("stage"),
            "active_slug": heartbeat.get("active_slug"),
            "stage_child_pid": heartbeat.get("stage_child_pid"),
            "stage_child_pgid": heartbeat.get("stage_child_pgid"),
            "stdout_log": heartbeat.get("stdout_log"),
            "heartbeat": heartbeat,
        }
        stamp = pr.utc_stamp()
        path = pr.STALLS_DIR / f"{stamp}_{self.run_id}_{cycle_id}.json"
        pr.write_json_atomic(path, payload)
        return path

    def _record_runner_stall_failures(self, heartbeat: dict[str, object], salvage_path: pathlib.Path) -> None:
        slugs = active_slugs_from_heartbeat(heartbeat)
        if not slugs:
            return
        os.environ["AUTOMATH_RUN_ID"] = self.run_id
        os.environ["AUTOMATH_CYCLE_ID"] = heartbeat.get("cycle_id") if isinstance(heartbeat.get("cycle_id"), str) else ""
        os.environ["AUTOMATH_RUNTIME_ROLE"] = "main_publication"
        import automath_cycle as cycle_mod

        cycle_mod.ensure_state()
        for slug in slugs:
            entry = cycle_mod.find_queue_entry_by_slug(slug) or {"slug": slug, "title": slug}
            status_path = cycle_mod.candidate_status_path(slug)
            stdout_log = ROOT / heartbeat["stdout_log"] if isinstance(heartbeat.get("stdout_log"), str) else pr.LOGS / f"{slug}_runner_stall.stdout.log"
            last_message = pr.STALLS_DIR / f"{slug}_{heartbeat.get('cycle_id', 'unknown')}_runner_stall.last.txt"
            if not last_message.exists():
                last_message.write_text(
                    f"Runner stall salvage recorded at {pr.relative_display(salvage_path)}.\n",
                    encoding="utf-8",
                )
            result = cycle_mod.StageRunResult(
                stage_name=str(heartbeat.get("stage") or "runner_stall"),
                returncode=124,
                stdout_log=stdout_log,
                last_message=last_message,
                timed_out=False,
                timeout_secs=self.stall_secs,
                child_pid=heartbeat.get("stage_child_pid") if isinstance(heartbeat.get("stage_child_pid"), int) else None,
                child_pgid=heartbeat.get("stage_child_pgid") if isinstance(heartbeat.get("stage_child_pgid"), int) else None,
            )
            cycle_mod.record_candidate_infra_failure(
                entry,
                status_path,
                result,
                failure_reason="runner_stall",
                rotate_queue=True,
            )
            cycle_mod.update_runtime_candidate_state(
                slug,
                last_runner_stall_salvage=pr.relative_display(salvage_path),
            )

    def _handle_stall(self, cycle_id: str, proc: subprocess.Popen[str], heartbeat: dict[str, object], heartbeat_age: float) -> pathlib.Path:
        salvage_path = self._write_stall_salvage(cycle_id=cycle_id, heartbeat=heartbeat, heartbeat_age=heartbeat_age, proc=proc)
        manager_pgid = heartbeat.get("manager_pgid") if isinstance(heartbeat.get("manager_pgid"), int) else pr.process_group_id(proc.pid)
        stage_child_pgid = heartbeat.get("stage_child_pgid") if isinstance(heartbeat.get("stage_child_pgid"), int) else None
        stage = heartbeat.get("stage") if isinstance(heartbeat.get("stage"), str) else None
        slugs = active_slugs_from_heartbeat(heartbeat)

        signal_process_group(manager_pgid, signal.SIGTERM)
        if stage_child_pgid and stage_child_pgid != manager_pgid:
            signal_process_group(stage_child_pgid, signal.SIGTERM)

        pr.emit_event(
            "cycle_stalled",
            run_id=self.run_id,
            cycle_id=cycle_id,
            stage=stage,
            slug=", ".join(slugs) if slugs else None,
            pid=heartbeat.get("manager_pid") or proc.pid,
            pgid=manager_pgid,
            heartbeat_age_secs=heartbeat_age,
            salvage_path=salvage_path,
        )
        if stage:
            pr.emit_event(
                "stage_killed",
                run_id=self.run_id,
                cycle_id=cycle_id,
                stage=stage,
                slug=", ".join(slugs) if slugs else None,
                pid=heartbeat.get("stage_child_pid"),
                pgid=stage_child_pgid,
                reason="runner_stall_watchdog",
                timeout_secs=self.stall_secs,
                stdout_log=heartbeat.get("stdout_log"),
            )

        deadline = time.monotonic() + self.kill_grace_secs
        while time.monotonic() < deadline:
            if proc.poll() is not None and not pgid_alive(stage_child_pgid):
                break
            time.sleep(0.2)

        if proc.poll() is None and manager_pgid is not None:
            signal_process_group(manager_pgid, signal.SIGKILL)
        if stage_child_pgid and stage_child_pgid != manager_pgid:
            signal_process_group(stage_child_pgid, signal.SIGKILL)
        try:
            proc.wait(timeout=2)
        except subprocess.TimeoutExpired:
            pass

        self._record_runner_stall_failures(heartbeat, salvage_path)
        self.refresh_lease(cycle_id=cycle_id, last_heartbeat_at=pr.now_iso())
        append_cycle_log(
            f"publication cycle stalled at stage {stage or 'unknown'} and was killed by the watchdog; salvage at {pr.relative_display(salvage_path)}.",
            run_id=self.run_id,
            cycle_id=cycle_id,
        )
        return salvage_path

    def supervise_cycle(self, cycle_id: str) -> CycleOutcome:
        proc = self.launch_cycle(cycle_id)
        launched_at = pr.now_iso()
        while True:
            heartbeat = self._load_cycle_heartbeat(cycle_id)
            heartbeat_ts = heartbeat.get("last_heartbeat_at") if isinstance(heartbeat.get("last_heartbeat_at"), str) else launched_at
            self.refresh_lease(cycle_id=cycle_id, last_heartbeat_at=heartbeat_ts)

            returncode = proc.poll()
            if returncode is not None:
                event_name = "cycle_finished" if returncode == 0 else "cycle_errored"
                pr.emit_event(
                    event_name,
                    run_id=self.run_id,
                    cycle_id=cycle_id,
                    returncode=returncode,
                    stage=heartbeat.get("stage") if isinstance(heartbeat.get("stage"), str) else None,
                    slug=", ".join(active_slugs_from_heartbeat(heartbeat)) or None,
                    pid=proc.pid,
                    pgid=pr.process_group_id(proc.pid),
                )
                if returncode == 0:
                    append_cycle_log(f"publication cycle finished at {now_str()}.", run_id=self.run_id, cycle_id=cycle_id)
                else:
                    append_cycle_log(
                        f"publication cycle ended with an error at {now_str()} (returncode {returncode}).",
                        run_id=self.run_id,
                        cycle_id=cycle_id,
                    )
                return CycleOutcome(cycle_id=cycle_id, status="finished" if returncode == 0 else "errored", returncode=returncode)

            heartbeat_age = pr.iso_age_seconds(heartbeat_ts, default=None)
            if heartbeat_age is None:
                heartbeat_age = self.stall_secs + 1
            self.maybe_emit_verbose_progress(
                cycle_id=cycle_id,
                proc=proc,
                heartbeat=heartbeat,
                heartbeat_age=heartbeat_age,
            )
            if heartbeat_age > self.stall_secs:
                salvage_path = self._handle_stall(cycle_id, proc, heartbeat, heartbeat_age)
                return CycleOutcome(cycle_id=cycle_id, status="stalled", returncode=1, salvage_path=salvage_path)

            time.sleep(self.heartbeat_secs)

    def maybe_sleep_between_cycles(self) -> None:
        if self.mode == "once":
            return
        self.refresh_lease(cycle_id=None, last_heartbeat_at=pr.now_iso())
        append_cycle_log(f"publication cycle sleeping for {self.sleep_seconds} seconds.", run_id=self.run_id)
        time.sleep(self.sleep_seconds)

    def run(self) -> int:
        self.acquire_lease()
        deferred_stop_marker = False
        completed = 0
        try:
            target_cycles = 1 if self.mode == "once" else self.cycles
            while True:
                if self.mode == "continuous" and self.should_stop_before_cycle():
                    append_cycle_log("stop marker detected before starting a new cycle; stopping the continuous runner.", run_id=self.run_id)
                    break

                if self.mode == "n-cycles" and STOP_MARKER.exists():
                    STOP_MARKER.unlink()
                    deferred_stop_marker = True
                    append_cycle_log(
                        f"bounded publication run deferred an existing stop marker before cycle {completed + 1}/{target_cycles} so the requested run could continue.",
                        run_id=self.run_id,
                    )

                cycle_id = pr.make_cycle_id(completed + 1)
                outcome = self.supervise_cycle(cycle_id)
                completed += 1

                if self.mode == "once":
                    return outcome.returncode

                if self.mode == "n-cycles" and STOP_MARKER.exists():
                    STOP_MARKER.unlink()
                    deferred_stop_marker = True
                    append_cycle_log(
                        f"bounded publication run deferred a stop marker raised during cycle {completed}/{target_cycles} until the requested run completes.",
                        run_id=self.run_id,
                    )

                if self.mode == "continuous" and stop_harness_enabled() and STOP_MARKER.exists():
                    append_cycle_log("stop marker detected after the publication cycle; stopping the continuous runner.", run_id=self.run_id)
                    break

                if self.mode == "n-cycles" and target_cycles is not None and completed >= target_cycles:
                    append_cycle_log(
                        f"bounded publication run completed {completed}/{target_cycles} requested cycle(s).",
                        run_id=self.run_id,
                    )
                    break

                self.maybe_sleep_between_cycles()

            if self.mode == "n-cycles" and deferred_stop_marker:
                STOP_MARKER.write_text("", encoding="utf-8")
                append_cycle_log(
                    f"bounded publication run restored the deferred stop marker after completing {completed}/{self.cycles} requested cycle(s).",
                    run_id=self.run_id,
                )
            return 0
        finally:
            self.release_lease()


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="AutoMath publication supervisor")
    parser.add_argument("--mode", choices=["once", "continuous", "n-cycles"], required=True)
    parser.add_argument("--cycles", type=int, default=None)
    parser.add_argument("-v", "--verbose", action="store_true", help="print live heartbeat progress to the terminal")
    parser.add_argument("child_args", nargs=argparse.REMAINDER)
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    child_args = list(args.child_args)
    if child_args[:1] == ["--"]:
        child_args = child_args[1:]
    if args.mode == "n-cycles":
        if args.cycles is None or args.cycles <= 0:
            print("--cycles must be a positive integer when --mode n-cycles is used.", file=sys.stderr)
            return 2
    try:
        supervisor = PublicationSupervisor(args.mode, cycles=args.cycles, child_args=child_args, verbose=args.verbose)
        return supervisor.run()
    except LeaseError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("publication supervisor interrupted; releasing lease.", file=sys.stderr)
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
