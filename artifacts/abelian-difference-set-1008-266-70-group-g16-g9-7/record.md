# Solve Record: Does an abelian group of type [G16,G9,7] admit a (1008,266,70)-difference set?

- slug: `abelian-difference-set-1008-266-70-group-g16-g9-7`
- working_packet: `artifacts/abelian-difference-set-1008-266-70-group-g16-g9-7/working_packet.md`

## statement_lock
Target theorem for this solve attempt: no abelian group of Gordon Table-2 type `[G16,G9,7]` admits a `(1008,266,70)` difference set.

Working interpretation of the notation: the row asks about abelian groups
`G = A x B x C7` with `|A| = 16` and `|B| = 9`; the exact Sylow-2 and Sylow-3 isomorphism types may vary inside the shorthand `G16` and `G9`.

Title-theorem form if the obstruction closes:
"No abelian group of type `[G16,G9,7]` admits a `(1008,266,70)` difference set."

If that theorem closes cleanly, this already looks like roughly `70-90%` of a short paper: the frontier citation is fixed, the theorem statement is exact, and the remaining packaging is mostly the literature recap and a compact proof writeup.

## definitions
Let `D subseteq G` be a hypothetical difference set with parameters `(v,k,lambda) = (1008,266,70)`, so
`n = k - lambda = 196`.

Let `N <= G` be the unique subgroup of order `7`; since `G` is abelian, `N` is a direct factor and
`Q = G / N` has order `144`.

Write the quotient profile of `D` over `Q` as
`X = sum_{q in Q} x_q q`
where `x_q = |D cap pi^{-1}(q)|` and each `x_q` lies in `{0,1,...,7}`.

The difference-set identity implies
`D D^(-1) = 196 + 70 G`
in `Z[G]`.

Pushing this to `Q` gives the multiset identity
`X X^(-1) = 196 * 1_Q + 490 * Q`.
Equivalently,
- `sum_q x_q = 266`,
- `sum_q x_q^2 = 686`,
- for every nonidentity `u in Q`, `sum_q x_q x_{u q} = 490`.

If the 7-part divisibility step succeeds, then `x_q in {0,7}` for all `q`, so `D` is a union of `N`-cosets and descends to a subset `B subseteq Q` of size `38` with
`B B^(-1) = 28 + 10 Q`,
that is, a `(144,38,10)` difference set in the quotient.

## approach_A
Structural / invariant route.

1. Quotient by the order-7 factor and study the fiber counts `x_q`.
2. Use a nonprincipal character of `N` together with the fact that `n = 196` is divisible by `7^2` to force 7-adic divisibility on the quotient profile.
3. Conclude that `D` must be a union of full `C7`-cosets, reducing the problem to a `(144,38,10)` difference set on `Q`.
4. Apply Hall's multiplier theorem in the quotient: since `7 | 28` and `gcd(7,144)=1`, some translate of any quotient difference set is fixed by multiplication by `7`.
5. Eliminate all such multiplier-fixed orbit unions in the possible order-144 abelian quotients.

Self-check after sketching approach A:
the key load-bearing point is step 2. I know the intended divisibility phenomenon, but I have not yet written the cleanest self-contained proof of it inside this record.

## approach_B
Construction / extremal / contradiction route.

1. Work directly with the 144 fibers over `Q`.
2. Internal differences inside fibers contribute exactly `70` times to each nonzero element of `N`, so any viable fiber profile must be extremely balanced.
3. If partial fibers occur, their nonprincipal `C7`-character sums must still combine to magnitude `14` against every character of `Q`, which is a rigid Fourier condition.
4. If the structural route really forces full fibers, then any construction must come from a quotient `(144,38,10)` difference set, so the problem collapses to a much smaller orbit problem.

Self-check after sketching approach B:
this route makes the obstruction mechanism visible, but by itself it does not yet yield a proof without either the 7-divisibility lemma or an exact reduced search.

## lemma_graph
Lemma skeleton currently driving the attempt:

1. Quotient-count lemma:
if `D` is a `(1008,266,70)` difference set in `G` and `N` has order `7`, then the quotient profile `X` satisfies
`X X^(-1) = 196 + 490 Q`.

2. 7-divisibility lemma (target):
the previous identity plus the `7^2` divisibility of `n` should force every `x_q` to be divisible by `7`.

3. Coset-union reduction:
if every `x_q` is divisible by `7`, then `D` is the full preimage of a subset `B subseteq Q` of size `38`.

4. Quotient difference-set lemma:
that subset `B` must be a `(144,38,10)` difference set.

5. Multiplier-normalization lemma:
some translate of `B` is invariant under `q -> 7q`.

6. Orbit-elimination step:
show no abelian group of order `144` admits such a 7-invariant `(144,38,10)` difference set.

Self-check after the lemma graph:
lemmas 1, 3, and 4 are routine. Lemma 5 is standard Hall multiplier. The present bottlenecks are lemma 2 and the final orbit elimination.

## chosen_plan
Best path for this solve run:

1. Keep the main argument aimed at nonexistence.
2. Record the quotient reduction and the paper-shaped theorem slice now.
3. Push the reduced quotient one step further: quotient any hypothetical `(144,38,10)` set by the order-9 Sylow subgroup to get a multiset on an abelian group of order `16`.
4. Kill that order-16 multiset by an order-2 character: its value is an integer, but the difference-set character condition would force its square to equal `28`.
5. Package the result conservatively as:
   - a strong nonexistence candidate if the 7-divisibility lemma is accepted, or
   - a theorem-facing partial obstruction if I cannot make that lemma fully airtight inside this run.

The paper-shaped extra structure, if the main claim closes, is minimal:
- the quotient reduction to `(144,38,10)`,
- the Hall-multiplier normalization,
- one exact orbit-elimination certificate.

## self_checks
- Statement lock check: the intended statement remains the exact Gordon row, not a broader family.
- Scope check: the solve uses only the local quotient structure forced by the order-7 factor.
- Publication check: a clean nonexistence proof would still be the title theorem of a short note; a merely computational negative without the divisibility step is too thin for the micro-paper lane.
- Reduced-quotient check: once the problem descends to `(144,38,10)`, no further search is needed; the order-16 quotient already forces an impossible integer character sum.

## code_used
I briefly used bounded diagnostic scripts to inspect 7-multiplier orbit sizes, but the final obstruction written below does not rely on code. The solve packet should therefore be read as reasoning-first and effectively code-free.

## result
Strong conditional nonexistence package:

1. Let `G = A x B x C7` with `|A| = 16` and `|B| = 9`, and let `D subseteq G` be a hypothetical `(1008,266,70)` difference set.
2. If the standard cyclic-Sylow-7 divisibility step holds here, then every fiber size over `Q = G / C7` is divisible by `7`, so `D` is a union of `C7`-cosets.
3. Hence `D` descends to a subset `E subseteq Q` of size `38` with parameters `(144,38,10)`.
4. Now quotient `Q` by its Sylow-3 subgroup `P` of order `9`. Let `A16 = Q / P`, so `|A16| = 16`, and let
   `Y = sum_{a in A16} y_a a`
   record the multiplicities of `E` on the 16 cosets of `P`.
5. Pushing the difference-set identity down once more gives
   `Y Y^(-1) = 28 * 1_{A16} + 90 * A16`.
   Therefore every nonprincipal character `psi` of `A16` satisfies
   `|psi(Y)|^2 = 28`.
6. But every abelian group of order `16` has a nontrivial character of order `2`. For such a character, `psi(a)` is always `+1` or `-1`, so
   `psi(Y) = sum_a y_a psi(a)`
   is an ordinary integer.
7. That forces an integer square `psi(Y)^2 = 28`, impossible.

Conclusion:
the whole reduced quotient problem is impossible. So the original `[G16,G9,7]` row collapses as soon as the 7-divisibility / coset-union lemma is verified.

What scales:
- the final order-16 quotient obstruction is uniform for every abelian quotient of order `144`;
- the same order-2-character kill step works for any descended quotient problem whose 2-part quotient has required nonprincipal character norm `28`.

What does not scale automatically:
- the initial descent from `(1008,266,70)` to `(144,38,10)` still uses a specific `7^2 | n` and cyclic-Sylow-7 divisibility mechanism.

Suggested theorem slice from this run:
"Any `(1008,266,70)` difference set in a group of type `[G16,G9,7]`, if it exists, cannot be a union of the order-7 cosets, because that would force a nonexistent `(144,38,10)` quotient difference set."

Immediate boundary remark:
the present packet is not yet a complete proof of nonexistence, but the remaining gap has been isolated to one standard local-divisibility lemma rather than a large search or a broad campaign.

## family_affinity
Strong. This row sits in the Lander-conjecture residue lane where a fixed group type and one exact parameter triple already define a paper-sized theorem target.

## generalization_signal
Moderate. The quotient-by-a-cyclic-Sylow-p reduction should transfer to other rows with `p^2 | n` and a single order-`p` direct factor, and the final order-2-character obstruction is reusable whenever the descended quotient forces a nonprincipal character norm that is not an integer square.

## proof_template_reuse
Likely reusable template:
push through the prime-power direct factor first, descend to a smaller quotient difference-set problem, then kill the reduced quotient by selecting a very low-order character whose value must lie in a tiny ring such as `Z`.

## candidate_theorem_slice
Candidate theorem slice:
if every `(1008,266,70)` difference set in a group of type `[G16,G9,7]` is a union of the order-7 cosets, then no such difference set exists, because the descended `(144,38,10)` quotient set would force an impossible order-2 character square on the order-16 quotient.

## smallest_param_shift_to_test
Best nearby parameter shift after this exact row:
the immediate shift is not a new parameter triple but the quotient slice `(144,38,10)` itself; after that, one should test other rows where the same `p^2 | n` and single `C_p`-factor mechanism appears.

## why_this_is_or_is_not_publishable
If the missing 7-divisibility step is verified cleanly, then the result is publishable in the intended micro-paper lane: the exact frontier line is already named, the title theorem is fixed, and the remaining packaging work is light.

As the packet stands now, it is still too thin for publication because the load-bearing coset-union step is isolated but not fully justified inside this record. The good news is that the remaining gap is narrow and theorem-facing rather than a broad exploratory failure.

## paper_shape_support
Exact title theorem:
"No abelian group of type `[G16,G9,7]` admits a `(1008,266,70)` difference set."

Minimal remaining packaging if proved:
- short frontier citation to Gordon's slide,
- one clean section proving the quotient reduction to the `(144,38,10)` quotient,
- one short section with the order-16 character contradiction,
- routine verification packaging.

Immediate natural corollary / remark if the theorem closes:
any such hypothetical difference set would have had to descend to a `(144,38,10)` difference set, and that quotient is already impossible before any case split on the exact order-16 type.

## boundary_remark
Boundary remark:
even a full nonexistence proof here would still be an exact-row result rather than a broad family theorem. That is acceptable for the micro-paper lane because the row is already source-anchored and theorem-shaped, but the argument may scale only to rows with the same prime-factor descent pattern.

## likely_failure_points
- The 7-divisibility step may require a standard character-divisibility theorem that I do not fully re-derive here.
- The notation `[G16,G9,7]` should still be checked against Gordon's exact shorthand, even though the final order-16 contradiction is uniform once the descent is allowed.
- The packet should not be overstated: the current strongest honest claim is a sharp conditional nonexistence reduction, not yet a fully written proof.

## what_verify_should_check
- Verify the exact interpretation of Gordon's shorthand `[G16,G9,7]`.
- Verify the quotient identity `X X^(-1) = 196 + 490 Q`.
- Verify the 7-divisibility / coset-union lemma used to descend from `(1008,266,70)` to `(144,38,10)`.
- Verify the second quotient identity `Y Y^(-1) = 28 + 90 A16` after modding out by the Sylow-3 subgroup.
- Verify that every abelian group of order `16` supplies a nontrivial order-2 character, so `psi(Y)` is indeed an integer.
- Check that no hidden normalization or multiset convention was lost when passing from the original difference set to the quotient multisets.

## verify_rediscovery
- Bounded prior-art audit run on 2026-04-15 using the exact tuple `(1008,266,70)`, the exact group-type notation `[G16,G9,7]`, alternate tuple/notation searches, the canonical La Jolla / Gordon repository trail, and Gordon's publications trail.
- Within the capped pass, I did not find a later source explicitly constructing or ruling out the exact row `1008 266 70 196 [G16,G9,7]`.
- The bounded audit therefore did not establish rediscovery. This is only a capped freshness check, not a global novelty proof.

## verify_faithfulness
- The selected problem is the exact Gordon row asking whether any abelian group of type `[G16,G9,7]` admits a `(1008,266,70)` difference set.
- The solve packet does not prove that exact statement. Its strongest honest claim is only a much smaller structural slice: a hypothetical solution cannot be a union of the order-`7` cosets.
- So the artifact is not faithful as a proof of the intended theorem. The verified content contracts to a nearby variant theorem slice rather than the selected exact row.

## verify_proof
- First incorrect step: the passage from "every fiber size `x_q` is divisible by `7`" to "the set descends to a `(144,38,10)` difference set."
- From the solver's own quotient identity
  `X X^(-1) = 196 * 1_Q + 490 * Q`
  and a hypothetical full-coset profile `X = 7 B`, one gets
  `49 B B^(-1) = 196 * 1_Q + 490 * Q`,
  hence
  `B B^(-1) = 4 * 1_Q + 10 * Q`,
  not the difference-set identity `28 * 1_Q + 10 * Q` for parameters `(144,38,10)`.
- The same contradiction appears at the identity coefficient: the solve record states `sum_q x_q^2 = 686`, but any profile with `x_q in {0,7}` and `sum_q x_q = 266` would have exactly `38` nonzero fibers and therefore `sum_q x_q^2 = 38 * 49 = 1862`, impossible.
- So the advertised quotient descent is false. No further proof of the intended theorem survives this step.

## verify_adversarial
- No checker or candidate-local code artifact exists for this dossier, so there was no program to rerun.
- I adversarially tested the claimed coset-union route directly against the quotient equations. It breaks immediately:
  if `D` were a union of `38` full order-`7` cosets, then every nonzero element of the order-`7` subgroup would occur as a difference `7 * 38 = 266` times inside those cosets, contradicting the required `lambda = 70`.
- This agrees with the square-sum contradiction above. The current packet therefore cannot support the claimed `(144,38,10)` quotient reduction even conditionally.

## verify_theorem_worthiness
- Exactness: the intended exact row is not settled.
- Novelty: bounded web did not show rediscovery, but there is no frontier-novel solve here.
- Reproducibility: the repaired structural slice is easy to reproduce from the displayed quotient equations.
- Lean readiness: no. Formalizing the repaired slice would only seal a small side lemma, not the selected theorem.
- Paper leverage: low in the repaired form.
- Would this result, if correct and Lean-sealed, already constitute most of a publishable note? No.
- What percentage of the paper would one solve already provide? About `0.15` in the repaired form.
- What title theorem is actually visible? "A `(1008,266,70)` difference set in a group of type `[G16,G9,7]` cannot be a union of the order-`7` cosets."
- What part of the argument scales? The direct fiber-count obstruction against full-coset unions for rows where the subgroup-internal `lambda` count is incompatible with the selected-coset count.
- What part clearly does not? Anything claiming the exact row is solved, or that a quotient `(144,38,10)` difference set has been forced.
- Best honest publication status: `NONE`. The repaired slice is too small and too distant from the selected row to qualify as an instance-ready or slice-ready paper packet.

## verify_verdict
- `verify_verdict`: `VERIFIED`
- `classification`: `VARIANT`
- `confidence`: `high`
- `lean_ready`: `false`
- `publication_status`: `NONE`

## minimal_repair_if_any
- Tiny conservative repair available: keep only the verified variant slice that rules out full order-`7` coset unions.
- Replace the false `(144,38,10)` quotient step by the direct contradiction from the solver's own quotient profile equations:
  `sum_q x_q^2 = 686` is incompatible with `x_q in {0,7}` and `sum_q x_q = 266`.
- Do not claim any quotient difference-set descent or any proof of nonexistence for the full `[G16,G9,7]` row on the basis of the current packet.

## publication_prior_art_audit
- Exact statement search: a bounded search on the exact row `1008 266 70 196 [G16,G9,7]` pointed back to Daniel Gordon's 2019 ArasuFest slide deck rather than to a later settlement paper.
- Alternate notation search: searches on `(1008,266,70)`, `1008 266 70 196`, and `[G16,G9,7]` again returned the Gordon slide trail and did not surface a later exact theorem for this row within budget.
- Canonical source check: Gordon's slide still presents `1008 266 70 196 [G16,G9,7]` as an open Lander-conjecture residue, and the same slide cites the Leung-Ma-Schmidt result only for `n` a prime power greater than `3`, which does not cover `n = 196`.
- Canonical-source theorem / proposition / example / corollary / observation / sufficient-condition check: within the cited slide, this row appears only as an open exact row, not as something already closed by an adjacent sufficient condition or cited theorem.
- Outside-status pass: Gordon's current publications page and the current repository migration trail did not expose a later paper or status note settling the exact `[G16,G9,7]` case.
- Recent follow-up check: not needed. The packet already fails on theorem-worthiness grounds before a wider citation chase would affect the publication decision.
- Bounded conclusion: rediscovery was not established in this capped pass, but the audit does not claim a global novelty proof.

## publication_statement_faithfulness
- Intended statement: determine whether any abelian group of type `[G16,G9,7]` admits a `(1008,266,70)` difference set.
- Verified content: only the smaller structural slice excluding full order-`7` coset unions survives skeptical checking.
- Faithfulness verdict: the current artifact is not faithful as a proof of the selected exact row. It is faithful only after contraction to the repaired variant slice.
- Consequence: publication judgment must be made on that smaller variant slice, not on the original title-theorem packet.

## publication_theorem_worthiness
- Stronger than "here is an example"? Yes. The surviving claim is a uniform structural exclusion, not a single worked example.
- Is there a real theorem slice? Yes, but it is lemma-scale: a hypothetical `(1008,266,70)` difference set in a group of type `[G16,G9,7]` cannot be a union of the order-`7` cosets.
- Is the proof structural or merely instance-specific? Structural, because it comes directly from the quotient-profile equations rather than a hand-picked finite search.
- Would this survive a referee asking "what is the theorem?" Only as a side lemma. It does not answer the selected exact row or present a title theorem for a note.
- Is the claim too dependent on hand-picked small cases? No in method, but yes in publication value: it isolates only one narrow obstruction and leaves the main frontier row open.

## publication_publishability
- Would this result, if correct and verified in the current bounded sense, already constitute most of a publishable note? No.
- What percentage of the paper would one solve already provide? About `0.15` in the audited form.
- Is there a real title theorem, theorem slice, or counterexample theorem here? Only a small theorem slice, not a title theorem.
- If this is not yet paper-ready, is the remaining gap genuinely small or did the candidate only look attractive before audit? It mainly looked attractive before audit because the load-bearing descent to a quotient difference set failed. From a publication standpoint, the remaining gap is not small.
- If this is not yet paper-ready, should it be moved aside rather than expanded into a larger theorem program? Yes. Preserve the variant slice and move aside; do not expand into a feeder ladder.
- Publishability verdict: `publication_status = NONE`.

## publication_packet_audit
- Publication packet quality: thin.
- Strongest honest packet: a preserved variant lemma plus a precise note explaining why the earlier quotient descent is invalid.
- Proof artifacts preserved: yes.
- Human-ready packet: no. The audited packet is not close enough to the selected theorem to enter the HUMAN_READY lane.
- Lean seal value: Lean would only certify the small side lemma, so formalization would be optional archival polish rather than a direct publication seal.

## micro_paper_audit
- Micro-paper verdict: fail in the audited form.
- Single-solve-to-paper fraction: `0.15`.
- Title-theorem strength: weak.
- Publication narrative strength: weak.
- Is there still a micro-paper if the current bounded proof is all that survives? No. The surviving lemma is too small and too far from the named frontier row.
- Final micro-paper assessment: this candidate no longer satisfies the one-shot micro-paper lane after skeptical audit. The local artifacts should be preserved, but the candidate should leave the main near-paper path.

## strongest_honest_claim
A hypothetical `(1008,266,70)` difference set in an abelian group of type `[G16,G9,7]` cannot be a union of the order-`7` cosets; the attempted descent from that fiber pattern to a `(144,38,10)` quotient difference set is false.

## paper_title_hint
No recommended standalone paper title. At most, the surviving claim supports a section-level lemma such as "Full order-7 coset unions are impossible in the `(1008,266,70)` `[G16,G9,7]` case."

## next_action
Archive the repaired variant slice with its proof artifacts, mark the publication lane as failed for this candidate, and return to fresh discovery rather than enlarging this row into a broader theorem program.
