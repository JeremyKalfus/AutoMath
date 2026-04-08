Read `AGENTS.md`, `selected_problem.md`, `artifacts/<slug>/record.md`, and `artifacts/<slug>/status.json` first.

This is the VERIFY stage.
Use LIMITED web only for PASS 1.
Do NOT browse after PASS 1 unless absolutely required to confirm rediscovery status within budget.

You are a skeptical verifier.
Your job is not to improve the solution except for tiny conservative repairs.

Run 4 passes in this exact order:

PASS 1: REDISCOVERY / prior-art audit
- This pass is allowed LIMITED web search.
- Budget:
  - max 8 searches
  - max 6 minutes
  - stop early if rediscovery is clearly established
- Search patterns must include:
  1. exact instance notation / parameter tuple
  2. alternative notation / reordered parameters / family notation
  3. the canonical source itself
  4. theorem / proposition / example / observation / corollary checks inside the same source
  5. one recent citation / status / discussion check if needed
- Decide whether the exact intended statement is already solved, directly implied, or explicitly exhibited in existing literature.
- Treat "correct proof of a known result" and "novel solve of an open problem" as different outcomes.
- If rediscovery is found, set:
  - `verify_verdict = "REDISCOVERY"`
  - `classification = "REDISCOVERY"`
  - `lean_ready = false`
  - `next_action = "archive_as_rediscovery"`
- If rediscovery is found, still add a short note on whether the current proof seems correct, but do NOT classify as `EXACT`.

PASS 2: Faithfulness
- Does the claimed result match the intended statement exactly?
- Look for:
  - wrong-theorem drift
  - quantifier drift
  - changed definitions
  - weaker or stronger proxy statements
  - mismatch between the natural-language claim and the actual solved claim

PASS 3: Proof correctness
- Find the first incorrect step, or say none found.
- Look for:
  - hidden assumptions
  - missing cases
  - unjustified leaps
  - handwaving where rigor is needed

PASS 4: Adversarial check
- If code or a checker exists, rerun it.
- If there is a candidate construction or counterexample, try to break it.
- Check that any computation actually supports the mathematical claim being made.

Then update `artifacts/<slug>/record.md` with these sections:
- `verify_rediscovery`
- `verify_faithfulness`
- `verify_proof`
- `verify_adversarial`
- `verify_verdict`
- `minimal_repair_if_any`

Update `artifacts/<slug>/status.json` with:
- `stage = "verify"`
- `verify_verdict` = `REDISCOVERY` | `VERIFIED` | `MINOR_FIX` | `WRONG_STATEMENT` | `CRITICAL_FLAW` | `UNVERIFIED`
- `classification`
- `confidence`
- `lean_ready`
- `next_action`

Rules:
- If PASS 1 establishes rediscovery, the verifier must not leave the run labeled `EXACT`.
- If the exact intended statement now looks right and frontier-novel, leave the run as `CANDIDATE` pending Lean, not `EXACT`.
- If the solver proved a nearby but different statement, classification must be `VARIANT`, not `EXACT`.
- If only a tiny repair is needed, you may patch it conservatively.
- If the candidate still looks real after checking and is not a rediscovery, set `lean_ready` to `true`.
- If it is not good enough, or if it is a rediscovery, set `lean_ready` to `false` and say exactly why.
