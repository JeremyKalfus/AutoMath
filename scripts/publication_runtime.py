#!/usr/bin/env python3
from __future__ import annotations

import datetime as dt
import json
import os
import pathlib
import tempfile
import uuid
from typing import Any


ROOT = pathlib.Path(__file__).resolve().parents[1]
ARTIFACTS = pathlib.Path(os.environ.get("AUTOMATH_ARTIFACTS_ROOT", str(ROOT / "artifacts"))).resolve()
LOGS = pathlib.Path(os.environ.get("AUTOMATH_LOGS_ROOT", str(ARTIFACTS / "_logs"))).resolve()
RUNTIME_ROOT = pathlib.Path(
    os.environ.get("AUTOMATH_RUNTIME_ROOT", str(ARTIFACTS / "_runtime" / "main_publication"))
).resolve()
LEASE_PATH = pathlib.Path(os.environ.get("AUTOMATH_LEASE_PATH", str(RUNTIME_ROOT / "lease.json"))).resolve()
LEASE_LOCK_PATH = pathlib.Path(os.environ.get("AUTOMATH_LEASE_LOCK_PATH", str(RUNTIME_ROOT / "lease.lock"))).resolve()
HEARTBEAT_PATH = pathlib.Path(os.environ.get("AUTOMATH_HEARTBEAT_PATH", str(RUNTIME_ROOT / "heartbeat.json"))).resolve()
EVENTS_PATH = pathlib.Path(os.environ.get("AUTOMATH_EVENTS_PATH", str(LOGS / "events.jsonl"))).resolve()
STALLS_DIR = pathlib.Path(os.environ.get("AUTOMATH_STALLS_DIR", str(LOGS / "stalls"))).resolve()


def now_dt() -> dt.datetime:
    return dt.datetime.now().astimezone()


def now_iso() -> str:
    return now_dt().isoformat()


def now_str() -> str:
    return now_dt().strftime("%Y-%m-%d %H:%M:%S %Z")


def utc_stamp() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def ensure_runtime_layout() -> None:
    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    LOGS.mkdir(parents=True, exist_ok=True)
    RUNTIME_ROOT.mkdir(parents=True, exist_ok=True)
    STALLS_DIR.mkdir(parents=True, exist_ok=True)


def load_json(path: pathlib.Path, default: Any):
    try:
        with path.open("r", encoding="utf-8") as fh:
            return json.load(fh)
    except (FileNotFoundError, json.JSONDecodeError):
        return default


def atomic_write_text(path: pathlib.Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as tmp:
        tmp.write(text)
        tmp.flush()
        os.fsync(tmp.fileno())
        tmp_path = pathlib.Path(tmp.name)
    os.replace(tmp_path, path)


def write_json_atomic(path: pathlib.Path, data: Any) -> None:
    atomic_write_text(path, json.dumps(data, indent=2) + "\n")


def append_jsonl(path: pathlib.Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(payload, sort_keys=True) + "\n")


def parse_iso(value: str | None) -> dt.datetime | None:
    if not value:
        return None
    try:
        return dt.datetime.fromisoformat(value)
    except ValueError:
        return None


def process_is_alive(pid: int | None) -> bool:
    if pid is None or pid <= 0:
        return False
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    return True


def process_group_id(pid: int | None) -> int | None:
    if pid is None or pid <= 0:
        return None
    try:
        return os.getpgid(pid)
    except OSError:
        return None


def runtime_message_prefix(run_id: str | None = None, cycle_id: str | None = None) -> str:
    parts: list[str] = []
    if run_id:
        parts.append(f"run:{run_id}")
    if cycle_id:
        parts.append(f"cycle:{cycle_id}")
    if not parts:
        return ""
    return "[" + " ".join(parts) + "] "


def format_runtime_message(
    message: str,
    run_id: str | None = None,
    cycle_id: str | None = None,
) -> str:
    return runtime_message_prefix(run_id=run_id, cycle_id=cycle_id) + message


def load_lease() -> dict[str, Any]:
    data = load_json(LEASE_PATH, {})
    return data if isinstance(data, dict) else {}


def load_heartbeat() -> dict[str, Any]:
    data = load_json(HEARTBEAT_PATH, {})
    return data if isinstance(data, dict) else {}


def relative_display(path: pathlib.Path | str | None) -> str | None:
    if path is None:
        return None
    candidate = pathlib.Path(path)
    try:
        return str(candidate.resolve().relative_to(ROOT))
    except (ValueError, FileNotFoundError):
        try:
            return str(candidate.relative_to(ROOT))
        except ValueError:
            return str(candidate)


def current_run_id() -> str | None:
    value = os.environ.get("AUTOMATH_RUN_ID", "").strip()
    return value or None


def current_cycle_id() -> str | None:
    value = os.environ.get("AUTOMATH_CYCLE_ID", "").strip()
    return value or None


def make_run_id() -> str:
    return f"run-{utc_stamp().lower()}-{uuid.uuid4().hex[:8]}"


def make_cycle_id(index: int | None = None) -> str:
    suffix = uuid.uuid4().hex[:8]
    if index is None:
        return f"cycle-{utc_stamp().lower()}-{suffix}"
    return f"cycle-{index:04d}-{utc_stamp().lower()}-{suffix}"


def iso_age_seconds(value: str | None, *, default: float | None = None) -> float | None:
    parsed = parse_iso(value)
    if parsed is None:
        return default
    return max(0.0, (now_dt() - parsed).total_seconds())


def file_age_seconds(path: pathlib.Path) -> float | None:
    try:
        mtime = path.stat().st_mtime
    except FileNotFoundError:
        return None
    return max(0.0, now_dt().timestamp() - mtime)


def json_file_last_ts(path: pathlib.Path) -> str | None:
    data = load_json(path, {})
    if not isinstance(data, dict):
        return None
    value = data.get("last_heartbeat_at")
    return value if isinstance(value, str) else None


def _normalize_field(value: Any):
    if isinstance(value, pathlib.Path):
        return relative_display(value)
    if isinstance(value, dict):
        return {str(key): _normalize_field(item) for key, item in value.items() if item is not None}
    if isinstance(value, (list, tuple, set)):
        return [_normalize_field(item) for item in value]
    return value


def emit_event(event: str, *, run_id: str | None = None, cycle_id: str | None = None, **fields: Any) -> dict[str, Any]:
    ensure_runtime_layout()
    payload: dict[str, Any] = {
        "ts": now_iso(),
        "event": event,
    }
    effective_run_id = run_id or current_run_id()
    effective_cycle_id = cycle_id or current_cycle_id()
    if effective_run_id:
        payload["run_id"] = effective_run_id
    if effective_cycle_id:
        payload["cycle_id"] = effective_cycle_id
    for key, value in fields.items():
        if value is None:
            continue
        payload[key] = _normalize_field(value)
    append_jsonl(EVENTS_PATH, payload)
    return payload
