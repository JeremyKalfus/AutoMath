Read `AGENTS.md` first.

This is the CURATION stage.
Use web search.

Goal:
Create a queue of exactly 5 VERY NICHE, SIMPLE, still-open math problems that GPT-5.4 could plausibly solve in one dedicated no-web run.

Hard limits:
- max 20 searches total
- maximum 8 minutes of curation effort
- stop early as soon as 5 acceptable problems are found
- do not keep browsing after a valid queue has been found
- at or before the budget boundary, stop browsing and immediately write `queue.json` and `selected_problem.md` before any closing prose

Skip any problem whose slug already appears in `failed_problems.json` or is clearly a duplicate / near-duplicate of a failed problem.

Strong preferences:
- crisp exact statements
- low prerequisite depth
- verifier-friendly problems
- reasoning-friendly problems
- no huge brute-force-first path
- diversity across the 5 queued problems; downrank batches that collapse into one narrow recent literature vein unless that vein is overwhelmingly stronger

What "GPT-5.4-capable" means for this harness:
- intended statement fits in at most about 120 words
- at most 6 basic definitions or conventions are needed
- finite or small-parameter problem
- one of these shapes:
  - exact value
  - minimum / maximum size
  - existence / nonexistence
  - explicit counterexample
  - exact small-parameter bound
- plausible short structural attack via symmetry, invariant, extremal reasoning, construction, or contradiction
- cheap verifier or witness-checker exists
- low literature dependence
- plausible Lean statement formalization
- if code is needed at all, it should mainly be a short checker or tiny bounded experiment

Hard reject if any of these hold:
- broad asymptotic conjecture
- heavy analysis / probability / algebraic geometry / large machinery
- stale or unclear open status
- likely already solved
- only realistic path is huge brute force / generic SAT / ILP / optimization
- no clear verifier
- intended statement is ambiguous

Prefer canonical or near-canonical sources:
- problem repositories
- parameter tables
- benchmark pages
- official problem pages
- recent status-confirming discussions
- Prefer canonical open-problem repositories, parameter tables, and gap pages over paper-conclusion "open directions".
- If a candidate comes from a recent paper conjecture or open-problems section, downrank it unless there is independent evidence that the exact instance still appears open.

Every final queued candidate must pass a bounded rediscovery audit before it enters the queue.
Every final queued candidate must also pass a deeper open-status audit, not just a quick source-local check.
For each final candidate, explicitly do all of these checks:
- exact instance search using the exact notation / tuple / title
- alternate notation / reordered tuple / synonym search
- canonical-source search
- theorem / proposition / example / observation / corollary search inside the canonical source
- one independent search outside the canonical source for status evidence
- one recent status / citation / discussion search if the source is a paper or discussion rather than a repository or table

Hard rediscovery rule:
- If a specific instance is extracted from a broader open family, you MUST check whether the same source already contains an earlier theorem, proposition, example, observation, corollary, or sufficient condition that settles that exact instance.
- Do not trust a conclusion or open-question section by itself.
- Reject or strongly downrank candidates when:
  - the exact instance already appears in an example or theorem
  - the status is family-open but instance-specific status is unclear
  - the only apparent evidence of openness is a vague concluding question
  - the instance is likely already implied by a general sufficient condition

For each chosen problem, collect:
- `title`
- `slug`
- `question`
- `canonical_source`
- `open_status_checked_on`
- `canonical_statement`
- `intended_statement`
- `definitions`
- `why_reasoning_friendly`
- `why_low_token`
- `verifier_hint`
- `lean_hint`
- `red_flags`
- `attack_style`
- `rediscovery_risk`
- `why_still_appears_open`
- `curation_confidence`

Rules for the queue:
- `queue.json` must be a valid JSON array of exactly 5 dossiers
- use at most 2 queued problems from the same paper, source family, or very narrow recent literature vein unless the evidence is overwhelmingly stronger than the alternatives
- keep the queue best-first by:
  1. reasoning_friendliness
  2. verifier_feasibility
  3. freshness / open-status confidence
  4. low prerequisite depth
  5. low token cost
- preferred outcome: 5 solid dossiers
- if fewer than 5 high-confidence problems are found within the budget, fill the remaining slots with the best available candidates and set `"curation_confidence": "low"` on those weaker entries rather than hanging forever
- when weaker candidates are used, include clear `rediscovery_risk` notes rather than silently treating them as frontier-clean
- otherwise use `"curation_confidence": "high"`

Write guarantee:
- before exiting, ALWAYS write `queue.json`
- before exiting, ALWAYS write `selected_problem.md`
- the first queue entry must be copied into `selected_problem.md`
- append exactly one short line to `ledger.md` in plain English saying which 5 slugs were queued

Do not solve anything during curation.
Do not write a long essay.
Preserve the reasoning-first bias and downrank search-heavy or giant-bruteforce-first tasks.
