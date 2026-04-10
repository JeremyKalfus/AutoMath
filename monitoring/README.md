# AutoMath Publication Monitoring

Use this repo-side setup if you want Codex app automation without running the manager on the main checkout.

## Files

- Prompt file: [monitoring/publication_monitor.prompt.md](/Users/jeremykalfus/CodingProjects/AutoMath/monitoring/publication_monitor.prompt.md)
- Runner: [scripts/run_publication_monitor.sh](/Users/jeremykalfus/CodingProjects/AutoMath/scripts/run_publication_monitor.sh)
- Continuous manager: [run_continuous.sh](/Users/jeremykalfus/CodingProjects/AutoMath/run_continuous.sh)
- Cycle summary: [artifacts/families/summary.md](/Users/jeremykalfus/CodingProjects/AutoMath/artifacts/families/summary.md)

## Manual Codex App Setup

1. Create a new automation in the Codex app.
2. Name it `AutoMath Publication Monitor`.
3. Set the workspace to `/Users/jeremykalfus/CodingProjects/AutoMath`.
4. Schedule it hourly.
5. Paste the prompt from [monitoring/publication_monitor.prompt.md](/Users/jeremykalfus/CodingProjects/AutoMath/monitoring/publication_monitor.prompt.md).
6. Leave the automation in active status.

## What The Runner Does

- creates or reuses a dedicated git worktree under `.worktrees/publication-monitor`
- seeds that worktree with the current publication-control surface, campaigns, family artifacts, and seed-instance evidence
- runs one publication cycle there
- syncs stable campaign and monitoring outputs back to the main checkout

## Default Long-Horizon Mode

- The repo-local default long-horizon manager is [run_continuous.sh](/Users/jeremykalfus/CodingProjects/AutoMath/run_continuous.sh).
- It keeps cycling in publication mode until `.stop_harness` exists or a campaign honestly reaches `publication_status = PAPER_READY`.
- Use the monitor runner only when you want a one-cycle worktree pass or a Codex app automation, not as the primary manager loop.

## What To Watch

- [artifacts/families/summary.md](/Users/jeremykalfus/CodingProjects/AutoMath/artifacts/families/summary.md)
- [ledger.md](/Users/jeremykalfus/CodingProjects/AutoMath/ledger.md)
- [artifacts/families/zero_divisor_prime_labelings/status.json](/Users/jeremykalfus/CodingProjects/AutoMath/artifacts/families/zero_divisor_prime_labelings/status.json)
- [artifacts/families/cnbc_quintic_nonexistence/status.json](/Users/jeremykalfus/CodingProjects/AutoMath/artifacts/families/cnbc_quintic_nonexistence/status.json)
