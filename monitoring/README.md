# AutoMath Publication Monitoring

Use this repo-side setup if you want Codex app automation without running the manager on the main checkout.

## Files

- Prompt file: [monitoring/publication_monitor.prompt.md](/Users/jeremykalfus/CodingProjects/AutoMath/monitoring/publication_monitor.prompt.md)
- Runner: [scripts/run_publication_monitor.sh](/Users/jeremykalfus/CodingProjects/AutoMath/scripts/run_publication_monitor.sh)
- Continuous manager: [run_continuous.sh](/Users/jeremykalfus/CodingProjects/AutoMath/run_continuous.sh)
- Cycle summary: [artifacts/summary.md](/Users/jeremykalfus/CodingProjects/AutoMath/artifacts/summary.md)

## Manual Codex App Setup

1. Create a new automation in the Codex app.
2. Name it `AutoMath Publication Monitor`.
3. Set the workspace to `/Users/jeremykalfus/CodingProjects/AutoMath`.
4. Schedule it hourly.
5. Paste the prompt from [monitoring/publication_monitor.prompt.md](/Users/jeremykalfus/CodingProjects/AutoMath/monitoring/publication_monitor.prompt.md).
6. Leave the automation in active status.

## What The Runner Does

- creates or reuses a dedicated git worktree under `.worktrees/publication-monitor`
- seeds that worktree with the current publication-control surface and the active one-shot packet queue
- runs one publication cycle there
- syncs stable monitoring and dossier outputs back to the main checkout

## Default Long-Horizon Mode

- The repo-local default long-horizon manager is [run_continuous.sh](/Users/jeremykalfus/CodingProjects/AutoMath/run_continuous.sh).
- It keeps cycling in one-shot publication mode until `.stop_harness` exists or the strongest honest claim reaches `publication_status = PAPER_READY`.
- In the default lane, it should keep curating for `paper_candidate` entries whose solve would already be basically a paper.
- In the live manager, solve may run on up to 2 queued candidates concurrently, while verify, publication audit, and Lean remain serial.
- Use the monitor runner only when you want a one-cycle worktree pass or a Codex app automation, not as the primary manager loop.

## What To Watch

- [selected_problem.md](/Users/jeremykalfus/CodingProjects/AutoMath/selected_problem.md)
- [queue.json](/Users/jeremykalfus/CodingProjects/AutoMath/queue.json)
- [artifacts/summary.md](/Users/jeremykalfus/CodingProjects/AutoMath/artifacts/summary.md)
- [ledger.md](/Users/jeremykalfus/CodingProjects/AutoMath/ledger.md)

The summary file lives at `artifacts/summary.md` and should be read as the current micro-paper control surface.
