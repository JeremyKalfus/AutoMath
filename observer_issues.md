# Observer Issues

Historical note:
This file is a harness-debug log, not a live operating spec. Read it as historical infrastructure context, not as the current publication-selection policy.

## 2026-04-08

- Confirmed issue: a curation worker can finish writing `queue.json` close to the timeout boundary, but `run_once.sh` may check for a usable queue too quickly and incorrectly end the cycle as if no queue was produced.
- Change made: added a short post-curation retry window in [`run_once.sh`](/Users/jeremykalfus/CodingProjects/AutoMath/run_once.sh) so the harness rechecks for a usable queue a few times before declaring curation unsuccessful.
- Confirmed issue: once the queue drained to a single Lean-incomplete candidate (`abelian-difference-set-4761-120-3`), the bounded run began replaying that same slug every cycle instead of refilling the queue. This starves the curation step and prevents meaningful multi-cycle exploration.
- Change made: updated [`run_once.sh`](/Users/jeremykalfus/CodingProjects/AutoMath/run_once.sh) so that if Lean is reached but still does not finish an exact checked result, the slug is moved aside via `failed_problems.json` instead of being rotated back into the queue indefinitely. This preserves the artifact but prevents one unresolved Lean candidate from starving fresh curation.
- Confirmed issue: on curation timeout, the worker could keep running in descendant processes after the harness had already given up on the cycle. That produced late `queue.json` / `selected_problem.md` writes and ledger lines after the cycle had already been classified as having no usable queue.
- Change made: updated the `run_stage` process launcher inside [`run_once.sh`](/Users/jeremykalfus/CodingProjects/AutoMath/run_once.sh) to start each stage in its own process group and kill the whole group on timeout or forced early termination. This makes stage timeouts deterministic and prevents late descendant writes from racing the harness.
