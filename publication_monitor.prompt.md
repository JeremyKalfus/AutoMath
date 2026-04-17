Run the repo-local publication monitor in `/Users/jeremykalfus/CodingProjects/AutoMath` by executing `./scripts/run_publication_monitor.sh`.

After the run:

- read `artifacts/_logs/events.jsonl` as the authoritative timeline
- read `artifacts/summary.md`
- report only if one of these is true:
  - the strongest honest `publication_status` changed
  - the active `paper_candidate` changed
  - the next blocker changed materially
  - a worker infrastructure failure occurred
  - the current one-shot lane looks stalled and needs a different paper candidate

If none of those happened, give a very short status note using the current snapshot instead of a long replay of the cycle.
