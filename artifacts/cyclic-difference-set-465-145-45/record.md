# Solve Record: The Cyclic (465,145,45) Difference-Set Problem

- slug: `cyclic-difference-set-465-145-45`
- working_packet: `artifacts/cyclic-difference-set-465-145-45/working_packet.md`

## statement_lock
Determine whether the cyclic group C_465 admits a (465,145,45)-difference set.

## definitions
Conventions fixed for this solve:

- Work in the additive group `G = Z/465Z`.
- A `(465,145,45)` difference set means a subset `D ⊂ G` of size `145` such that every nonzero `g ∈ G` has exactly `45` ordered representations `g = d_1 - d_2` with `d_i ∈ D`.
- The parameter identity is locked: `(v-1)λ = k(k-1)` gives `464·45 = 145·144 = 20880`, so the tuple is internally consistent.
- Set `n = k - λ = 100`.
- For a divisor `w | 465`, write the contracted coefficient vector `b^{(w)} = (b_0, ..., b_{w-1})`, where `b_i` counts elements of `D` in the residue class `i mod w`.
- Then `∑ b_i = 145`, each `b_i` is an integer in `[0, 465/w]`, and Fourier inversion gives
  `∑ b_i^2 = n + λ(465/w)` and `∑_i b_i b_{i-s} = λ(465/w)` for every nonzero `s mod w`.

Ambiguities and scope notes:

- The exact numerical-multiplier route is not manager-provided here, so if a contradiction uses multiplier invariance I must state clearly where the solve depends on that standard ingredient.
- No broader family claim is assumed. The active target is only the exact cyclic case `(465,145,45)`.
- Lean stays off unless a fully convincing exact proof or explicit counterexample package emerges.

## approach_A
Structural / invariant route:

1. Try to force a useful numerical multiplier from the prime divisors of `n = 100`.
2. Contract modulo `31` because `465 = 15·31`, the fibers over `Z/31Z` have size `15`, and `2` has small orbit structure modulo `31`:
   `ord_31(2) = 5`, so the nonzero residues split into six `2`-orbits of size `5`.
3. If `2` acts as a multiplier, the contracted vector modulo `31` must be constant on those six orbits. Writing the orbit-values as `x_1, ..., x_6` and `a = b_0`, we get
   `a + 5∑ x_j = 145` and `a^2 + 5∑ x_j^2 = 775`.
4. Add the full contracted correlation equations modulo `31`. If that orbit-constant integer system has no solution, the cyclic difference set is impossible.

Why this path is attractive:

- It matches the transfer-kit recommendation.
- It aims directly at a paper-shaped nonexistence theorem.
- The bounded search is on a tiny orbit-compressed system, not on subsets of `C_465`.

## approach_B
Construction / contradiction route without assuming a new multiplier:

1. Work simultaneously with contractions modulo `31` and modulo `15`.
2. Use the exact correlation identities
   `∑ (b_i^{(31)})^2 = 775`, `∑ (b_j^{(15)})^2 = 1495`,
   together with row/column compatibility for a hypothetical `31 × 15` `0/1` incidence matrix of `D`.
3. Try to prove that every admissible pair of marginal vectors forces a forbidden local obstruction, such as too much concentration in some fiber or an impossible residue-distribution parity pattern.

Why this is weaker:

- It avoids multiplier dependence, but the feasible region is much larger.
- It looks more likely to produce only partial obstructions than a clean title theorem.

## lemma_graph
Proof skeleton currently targeted:

1. Parameter lock: `n = 100`.
2. Mod-`31` contraction identities:
   `∑ b_i = 145`,
   `∑ b_i^2 = 100 + 45·15 = 775`,
   `∑_i b_i b_{i-s} = 45·15 = 675` for `s ≠ 0`.
3. Orbit compression under a candidate multiplier `2`:
   `b_i = b_{2i}` on `Z/31Z`.
4. Reduced integer system on seven variables `(a, x_1, ..., x_6)`.
5. If that reduced system is inconsistent, conclude nonexistence of a cyclic `(465,145,45)` difference set.

Small lemma slice visible already:

- Any multiplier-invariant mod-`31` contraction must satisfy a rigid seven-variable correlation system. Even if the full nonexistence proof stalls, that compressed system is a reusable theorem-facing artifact.

## chosen_plan
Best path: pursue approach A.

Reason:

- This case is only publishable in the micro-paper lane if the solve closes the exact cyclic tuple, and the multiplier-plus-contraction route is the only local path that plausibly gets all the way there without drifting into a broader campaign.
- The bounded computation, if needed, is justified only after the structural equations are on record.

Exact title theorem if this closes:

- `The cyclic group C_465 admits no (465,145,45) difference set.`

Publication framing if that theorem closes:

- This would already be about `84%` of a short paper.
- Minimal remaining packaging work would be: restate the residual-status provenance, isolate the multiplier input being used, and present the reduced orbit-equation contradiction cleanly.
- An immediate boundary remark would be that the obstruction is tied to the `31`-component and the `2`-orbit decomposition modulo `31`, not to a generic elimination of nearby cyclic tuples.

## self_checks
Self-check after statement lock:

- The tuple is fixed and internally consistent.
- The target remains the exact cyclic case, not a family claim.

Self-check after choosing the route:

- The intended experiment is theorem-facing and tiny.
- I am not starting with generic search on subsets of `C_465`.
- The main risk is dependence on a multiplier theorem that is not fully rederived inside this packet.

Self-check after the mod-`31` test:

- The first contraction did not force a contradiction; two orbit-constant mod-`31` solutions exist.
- That failure is informative rather than fatal: it shows mod `31` alone is too coarse.

Self-check after the finer contraction test:

- Modulo `93` and modulo `155`, the `2`-orbit-compressed contraction systems both have zero solutions.
- The computation stayed inside the promised narrow lane: orbit-compressed exact checks, not subset search in `C_465`.
- The only serious remaining gap is to treat the `2`-multiplier input as a cited theorem in the final writeup rather than as an unproved local fact.

## code_used
Yes. Candidate-local helper:

- `artifacts/cyclic-difference-set-465-145-45/orbit_contraction_check.py`

What it checks:

- Assume a translated difference set is fixed by multiplication by `2`.
- Contract modulo `93` and modulo `155`.
- Impose exact sum, square-sum, and nonzero-correlation equations on the resulting orbit-constant coefficient vectors.
- Exhaustively enumerate the orbit-compressed systems.

Observed output:

- mod `93`: orbit sizes `[1,10,5,10,10,5,10,5,10,5,10,2,5,5]`, solutions `0`
- mod `155`: orbit sizes `[1,20,20,5,20,20,20,5,20,5,4,5,5,5]`, solutions `0`

## result
Current strongest result:

- Candidate nonexistence proof: assuming the standard numerical-multiplier input that `2` is a multiplier for this cyclic difference-set parameter set, `C_465` admits no `(465,145,45)` difference set.

Reasoning chain:

1. `n = k - λ = 100`, and the standard multiplier theorem should force `2` to be a numerical multiplier because `2 | n` and `gcd(2,465)=1`.
2. After translation, a hypothetical difference set may therefore be taken `2`-invariant.
3. A `2`-invariant set yields orbit-constant contracted coefficient vectors modulo `93` and modulo `155`.
4. For modulus `93`, the contraction identities require
   `∑ c_i = 145`, `∑ c_i^2 = 325`, and every nonzero shift-correlation equals `225`.
   The `2`-orbit structure consists of one orbit of size `1`, one of size `2`, six of size `5`, and six of size `10`.
   Exhaustive orbit-compressed search finds no solution.
5. For modulus `155`, the contraction identities require
   `∑ d_i = 145`, `∑ d_i^2 = 235`, and every nonzero shift-correlation equals `135`.
   The `2`-orbit structure consists of one orbit of size `1`, one of size `4`, six of size `5`, and six of size `20`.
   Exhaustive orbit-compressed search again finds no solution.

So the current packet points to:

- `Candidate theorem:` The cyclic group `C_465` admits no `(465,145,45)` difference set.

What extra structure makes this paper-shaped if the main claim closes?

- A short lemma statement of the multiplier input.
- A compact human presentation of one of the two orbit-compressed contradictions, with the second modulus retained as an independent check or appendix remark.

## family_affinity
Strong family affinity: this is one of the canonical residual cyclic difference-set cases with small `k`, so any exact resolution plugs directly into the classical cyclic necessary-condition program.

## generalization_signal
Moderate generalization signal: the reusable part is the template “force a multiplier from `n`, then contract at divisors of `v` where the multiplier has sparse orbit structure.” What scales is the orbit-compressed contraction method; what does not automatically scale is the exact choice of modulus (`93` or `155`) and the numerical infeasibility check, which are tuned to this tuple.

## proof_template_reuse
Reusable template: multiplier invariance plus contracted correlation equations at a divisor of `v`, followed by orbit compression and an exact infeasibility check on the contracted coefficients.

## candidate_theorem_slice
Candidate theorem slice:

- Assuming `2` is a numerical multiplier, no `2`-invariant contracted coefficient vector modulo `93` satisfies the exact difference-set equations.
- Independently, assuming the same multiplier input, no `2`-invariant contracted coefficient vector modulo `155` satisfies the exact difference-set equations.
- Either slice is already theorem-facing; together they give a robust candidate obstruction.

## smallest_param_shift_to_test
Most informative nearby shifts:

- Test the same multiplier-contraction template on the sibling residual cyclic case from the same source table.
- Inside this instance, test whether the mod-`93` obstruction alone can be rewritten into a shorter hand proof without the second modulus.

## why_this_is_or_is_not_publishable
If the multiplier input is accepted as standard and the orbit-compressed contradiction is written cleanly, this is already in the `70–90%` paper band: the title theorem is the exact residual-case nonexistence statement, and the remaining work is short exposition plus a careful theorem/citation boundary. In its current state the package is stronger than a loose theorem slice but still slightly too thin for the micro-paper lane because the key multiplier lemma is referenced rather than fully integrated into the prose proof.

## paper_shape_support
Paper-shaped support visible if the main claim closes:

- title theorem: nonexistence in `C_465`;
- strongest supporting slice: empty `2`-orbit-contracted systems modulo `93` and `155`;
- immediate corollary / remark: any proof of existence would have to break the standard `2`-multiplier route, since every `2`-invariant contraction at these moduli is impossible;
- packaging burden: low, because the literature already isolates the tuple as residual.

## boundary_remark
Boundary remark candidate:

- The obstruction looks local to the interaction of `n = 100` with the `×2` orbit structures on divisors `93` and `155` of `465`; it is not yet evidence for a broad family theorem beyond this residual case.

## likely_failure_points
Likely failure points:

- The multiplier input must be stated exactly correctly; if my remembered multiplier theorem is too coarse, the route weakens immediately.
- The exhaustive orbit-compressed contradiction is exact, but the paper version still needs a reader-friendly presentation rather than “trust the script.”
- Verify should rerun the helper script independently and inspect the contraction formulas carefully.

## what_verify_should_check
If solve reaches a strong obstruction, verify should check:

- the exact multiplier input used to force invariance under `2`;
- the translation step from numerical multiplier to an actually `2`-fixed difference set in `Z/465Z`;
- the derivation of the contracted correlation identities modulo `93` and modulo `155`;
- an independent rerun of `artifacts/cyclic-difference-set-465-145-45/orbit_contraction_check.py`;
- whether the argument is already latent in Baumert-Gordon style tables or is genuinely new theorem closure.

## verify_rediscovery
- PASS 1 stayed within the bounded web budget and checked the exact tuple notation `(465,145,45)`, alternate tuple phrasing `465 145 45`, the cyclic family wording, the canonical Baumert-Gordon source, same-source theorem/proposition/example/corollary coverage, and one recent status-style search.
- Within that budget I did not find a published existence proof, nonexistence theorem, or direct implication already settling the exact cyclic case.
- The strongest status signal found in-budget still treated this tuple as unresolved: Baumert-Gordon 2004 leaves it among the final small cyclic residual cases, Gordon-Schmidt 2015 still lists `[465]` as open, and a 2024 search result snippet for `New contractibility criteria for difference sets` still says the remaining open cyclic cases are `(465,145,45)` and `(469,208,92)`.
- Verdict for PASS 1: no rediscovery established within budget.

## verify_faithfulness
- The intended statement is exact and unconditional: determine whether `C_465` admits a `(465,145,45)` difference set.
- The solver's strongest honest output is different: *if* multiplication by `2` may be imposed as a genuine multiplier symmetry, then the `2`-orbit-contracted coefficient systems modulo `93` and `155` are infeasible.
- That is a nearby conditional obstruction, not the intended theorem. The packet therefore drifts at the theorem boundary: it substitutes an uncited multiplier premise for the exact cyclic existence question.
- The translation step from “numerical multiplier” to “after translation one may assume `D` is fixed by `x -> 2x`” is also not proved inside the artifact.
- Faithfulness verdict: `VARIANT`, not an exact solve of the selected problem.

## verify_proof
- First incorrect / unsupported step: the solve record asserts that `2` is a standard numerical multiplier merely because `2 | n = 100` and `gcd(2,465)=1`.
- That step is not justified by anything written in the packet, and the cited source family is exactly the multiplier-conjecture literature, so this implication cannot be treated as automatic without the precise theorem statement and hypotheses.
- The same-source easy salvage route also fails on direct arithmetic grounds. For the common `w`-multiplier criterion used in Baumert-Gordon style contraction arguments, one needs the prime divisors of `n` to generate the same residue class modulo the chosen divisor `w`. But for `w = 93`, `155`, and `465`, exhaustive residue checks give no solution to `5^j ≡ 2 (mod w)` and none to `2^j ≡ 5 (mod w)` over full unit-group periods. So the packet does not even have a quick local path to certify `2` as a valid common multiplier at these moduli.
- Conditional on the multiplier premise, I did not find a second arithmetic flaw in the orbit-contraction computation itself. The failure is earlier: the bridge from the intended theorem to the computed obstruction is not established.

## verify_adversarial
- I reran `artifacts/cyclic-difference-set-465-145-45/orbit_contraction_check.py`.
- The script reproduced the recorded outputs exactly:
  - mod `93` orbit sizes `[1, 10, 5, 10, 10, 5, 10, 5, 10, 5, 10, 2, 5, 5]`, solutions `0`
  - mod `155` orbit sizes `[1, 20, 20, 5, 20, 20, 20, 5, 20, 5, 4, 5, 5, 5]`, solutions `0`
- I also ran direct residue checks showing that the easiest common-multiplier rescue is unavailable locally:
  - no `j` with `5^j ≡ 2 (mod 93)`, `5^j ≡ 2 (mod 155)`, or `5^j ≡ 2 (mod 465)` over full unit-group periods;
  - no `j` with `2^j ≡ 5 (mod 93)`, `2^j ≡ 5 (mod 155)`, or `2^j ≡ 5 (mod 465)` over full unit-group periods.
- So the computation supports a real conditional obstruction, but it does not repair the theorem-faithfulness gap.

## verify_theorem_worthiness
- Exactness: not exact for the selected problem. The packet currently proves at most a conditional orbit-symmetry obstruction.
- Novelty: no rediscovery was established within budget for the exact tuple, but novelty of the *conditional* obstruction is not enough because it does not settle the selected case.
- Reproducibility: the helper script is reproducible and the arithmetic reruns match the record.
- Lean readiness: `false`. Lean would formalize only a conditional slice whose bridge to the intended theorem is still missing.
- Paper leverage: low in the packet's current state.
- Would this result, if correct and Lean-sealed, already constitute most of a publishable note? No.
- What percentage of the paper would one solve already provide? About `0.32` for the current strongest honest claim, because the decisive step from the conditional slice to the exact cyclic nonexistence theorem is still absent.
- What title theorem is actually visible? At best: “No `2`-invariant contracted coefficient vector modulo `93` or `155` satisfies the exact difference-set equations for parameters `(465,145,45)`.”
- What part of the argument scales? The orbit-compressed contraction template itself: assume a justified multiplier, contract modulo a divisor with sparse orbit structure, and test the exact coefficient equations.
- What part clearly does not? The bridge from `n = 100` to the unconditional `×2` symmetry. That is the entire bottleneck, and without it the packet does not close the frontier claim.
- Best honest publication status: still `NONE`, not `INSTANCE_ONLY`, because the visible theorem slice is conditional and not yet a paper-shaped exact result.

## verify_verdict
- `verify_verdict = "WRONG_STATEMENT"`
- Final classification for this run: `VARIANT`
- Confidence: `high`
- `lean_ready = false`
- `lean_packet_seal = false`

## publication_prior_art_audit
- Exact-statement search and alternate-notation search stayed narrow: `(465,145,45)`, `465 145 45`, and cyclic-difference-set phrasing.
- Canonical-source check: Baumert-Gordon 2004, Table 1, still lists `465 145 45 100 Open`, and the surrounding text says the paper rules out four of the six open cyclic cases with `k <= 150`, which leaves `(465,145,45)` unresolved there rather than proved by some nearby theorem, proposition, corollary, example, or sufficient-condition remark.
- Later status check inside the cited source lane: Gordon-Schmidt 2015, Table 2, still lists `465 145 45 [465]` among the open difference-set parameters.
- One outside-source status pass: Buratti-Nakic 2024 (`Additivity of symmetric and subspace 2-designs`, Sect. 3 discussion after Theorem 3.1) explicitly says that, according to the cited repository/source, the existence of cyclic difference sets with parameters `(465,145,45)` is still open.
- Within this bounded audit I found no paper proving existence, proving nonexistence, or giving a directly cited earlier implication that already settles the exact cyclic case.
- Prior-art verdict: no rediscovery established in-budget, but also no new source-backed bridge that upgrades the current local obstruction to the intended theorem.

## publication_statement_faithfulness
- Intended statement: determine unconditionally whether `C_465` admits a `(465,145,45)` difference set.
- Strongest current packet output: if one may impose `x -> 2x` as a genuine multiplier symmetry, then the `2`-orbit-contracted coefficient systems modulo `93` and `155` are infeasible.
- That is not the same theorem. It is a conditional obstruction sitting one major bridge short of the selected frontier claim.
- The bounded audit does not supply that bridge. The 2015 survey records multiplier results and open cases, but nothing in the present packet cites a theorem that turns `2 | n = 100` into the unconditional multiplier conclusion actually needed here.
- The 2024 outside-source check is compatible with the verify concern: it gives an additive-design consequence from `2 | (k - lambda)` and `2` not dividing `v`, not the exact multiplier statement the solve packet used.
- Faithfulness verdict for publication purposes: the packet remains a `VARIANT`, not a faithful resolution of the selected problem.

## publication_theorem_worthiness
- The visible mathematical content is stronger than “here is an example.” The helper script and contraction argument isolate a reproducible impossibility theorem for a specific `2`-orbit-constant contraction model.
- But the title-theorem question is still weak. A referee asking “what is the theorem?” would not yet get the residual cyclic-case resolution; they would get a conditional technical obstruction whose main premise is the unresolved bottleneck.
- The proof ingredients are partly structural: orbit compression plus exact contraction identities are reusable. The delivered claim, however, is still too dependent on one hand-picked symmetry assumption and two hand-picked moduli (`93` and `155`) to serve as the paper’s headline theorem.
- The best honest theorem slice is lemma-sized, not note-sized: no `2`-orbit-constant contraction modulo `93` or `155` satisfies the exact coefficient equations for a hypothetical cyclic `(465,145,45)` difference set.

## publication_publishability
- If the exact cyclic case were solved, this would indeed be close to a publishable micro-paper. That is why the candidate was curated.
- The current verified packet is not close in that sense. The missing step is not editorial polish, a short appendix, or Lean sealing; it is the decisive logical bridge from the conditional slice to the exact cyclic nonexistence claim.
- So the remaining gap is not genuinely small. The candidate looked attractive before audit because the residual-case narrative is strong, but the current artifact does not yet inherit that leverage.
- Publication verdict: not paper-ready, not slice-ready, and not a good target for “expand a bit and write it up.” The honest move is to preserve the obstruction and move the packet aside unless an exact source-backed multiplier route is found quickly.

## publication_packet_audit
- `publication_status`: `NONE`
- `publication_confidence`: `high`
- `publication_packet_quality`: `weak`
- The packet is not empty: it preserves a real conditional obstruction and a reproducible computation.
- But it is not most of a publishable note. The core frontier claim is still unproved, and the current slice would not survive referee scrutiny as the main theorem of a micro-paper.
- Lean would not directly seal the packet. Formalization would only fossilize the conditional obstruction; it would not solve the publication bottleneck.

## micro_paper_audit
- Stronger than “here is an example”?: yes, but only as a conditional obstruction lemma.
- Would this already constitute most of a publishable note?: no.
- Honest single-solve-to-paper fraction for the current packet: about `0.30`, not the pre-audit `0.84`.
- Is there a real title theorem, theorem slice, or counterexample theorem here?: there is a theorem slice, but not a title theorem for the selected problem.
- Is the proof structural or merely instance-specific?: the method is structural, the current deliverable is still instance-bound and premise-dependent.
- Would this survive “what is the theorem?” from a referee?: no, not as a paper in the one-shot lane.
- Is the claim still too dependent on hand-picked small cases?: yes; the packet leans on specific moduli and an unsupported symmetry bridge.
- If not paper-ready, is the remaining gap genuinely small?: no, the gap is central.
- If not paper-ready, should it be moved aside rather than expanded into a larger theorem program?: yes.
- Would Lean directly seal the packet, or only serve as later polish?: only later polish after an exact theorem exists; it is not the next bottleneck.

## strongest_honest_claim
If one additionally assumes that multiplication by `2` can be imposed as a genuine multiplier symmetry for a cyclic `(465,145,45)` difference set, then no `2`-orbit-constant contracted coefficient vector modulo `93` or `155` satisfies the exact sum, square-sum, and nonzero-correlation equations.

## paper_title_hint
Conditional Orbit-Contraction Obstructions to a Cyclic `(465,145,45)` Difference Set

## next_action
Preserve the current contraction artifact as a side obstruction, but move this packet aside in the micro-paper lane unless the exact multiplier bridge is repaired from a source-backed theorem or replaced by a multiplier-free argument that closes the unconditional cyclic case.
- Lean gate reason: Lean would only seal a conditional orbit-contraction slice, while the shortest remaining path to a real packet is to replace the unsupported `2`-multiplier bridge with a source-backed exact theorem or a multiplier-free obstruction.

## minimal_repair_if_any
- No tiny conservative repair upgrades this packet to the intended theorem.
- The smallest honest repair is classificatory: preserve the reproducible orbit-contraction computation as a conditional variant, remove the claim that `2 | n` automatically makes `2` a usable multiplier here, and restart solve from an exact source-backed multiplier theorem or from a multiplier-free obstruction route.
