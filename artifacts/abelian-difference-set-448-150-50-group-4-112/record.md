# Solve Record: Does the abelian group C_4 x C_112 admit a (448,150,50)-difference set?

- slug: `abelian-difference-set-448-150-50-group-4-112`
- working_packet: `artifacts/abelian-difference-set-448-150-50-group-4-112/working_packet.md`

## statement_lock
Determine whether the abelian group C_4 x C_112 admits a (448,150,50)-difference set.

## definitions
Write
\[
G \cong C_4 \times C_{16} \times C_7 = P \times C_7,
\]
with \(P := C_4 \times C_{16}\) of order \(64\). A \((448,150,50)\)-difference set \(D \subseteq G\) would satisfy
\[
DD^{(-1)} = 100 \cdot 1_G + 50 G
\]
in the integral group ring, where \(n = k-\lambda = 100\).

Let \(z\) generate the \(C_7\) factor and decompose
\[
D = \sum_{j=0}^{6} z^j A_j,
\]
with \(A_j \subseteq P\). Then \(|A_0|+\cdots+|A_6| = 150\).

Conventions used below:
- \(A_0\) denotes the fiber over the identity of \(C_7\).
- \(\alpha_r\) denotes the number of points of \(A_0\) in residue class \(r \bmod 4\) of the \(C_{16}\)-coordinate.
- \(\beta_r\) denotes the corresponding count in any nonzero \(C_7\)-fiber after the 5-multiplier normalization.
- \(F := C_4 \times 4C_{16} \le P\) has order \(16\), and \(P/F \cong C_4\).

Ambiguities / conventions to keep explicit:
- I am using additive notation for the abelian group, but group-ring formulas are written multiplicatively.
- I am treating the standard multiplier consequence "5 acts as a numerical multiplier because \(5 \mid n\) and \((5,448)=1\)" as available from the packet's recommended attack. The solve below only uses the orbit consequences that follow from that normalization.
- The exact point where a translation is used is the normalization making the 5-action fix one \(C_7\)-fiber and permute the six nonzero fibers transitively.

## approach_A
Structural / invariant route.

Step A1. Quotient by the Sylow-2 subgroup \(P\), so only the \(C_7\)-fiber counts remain. If \(a_j := |A_j|\), then the projected group-ring identity on \(C_7\) gives
\[
\sum_{j=0}^{6} a_j = 150,\qquad \sum_{j=0}^{6} a_j^2 = 100 + 50 \cdot 64 = 3300.
\]

Step A2. Under the 5-multiplier normalization, multiplication by 5 is transitive on the six nonzero elements of \(C_7\), so
\[
(a_0,a_1,\dots,a_6) = (a,b,b,b,b,b,b).
\]
Then
\[
a+6b=150,\qquad a^2+6b^2=3300,
\]
which forces \((a,b)=(30,20)\). So any such \(D\) must have one heavy fiber of size 30 and six equal fibers of size 20.

Step A3. Quotient the 2-part further by \(F=C_4\times 4C_{16}\), giving \(P/F \cong C_4\). This creates residue-count vectors
\[
\alpha=(\alpha_0,\alpha_1,\alpha_2,\alpha_3),\qquad \beta=(\beta_0,\beta_1,\beta_2,\beta_3),
\]
with \(\sum \alpha_r=30\), \(\sum \beta_r=20\), and \(A_0\) 5-invariant implying \(\alpha_1,\alpha_2,\alpha_3\) are multiples of 4.

Step A4. Two Fourier packages arise on \(C_4\):
- \(\delta := \alpha-\beta\), coming from characters nontrivial on \(C_7\),
- \(\varepsilon := \alpha+6\beta\), coming from characters trivial on \(C_7\).

Each package has all nonprincipal \(C_4\)-character values of absolute value 10, so both satisfy short autocorrelation systems. This reduces the whole problem to a tiny integral consistency check.

## approach_B
Construction / contradiction route.

Work directly with 5-orbits in \(G\). Since \(5 \equiv 1 \pmod 4\), has order 4 on \(C_{16}\), and order 6 on \(C_7^\times\), the 5-orbits in \(G\) have sizes 1, 4, 6, or 12:
- 16 singleton orbits from \(C_4 \times 4C_{16} \times \{0\}\),
- 12 orbits of size 4 from the remaining points of \(P \times \{0\}\),
- 16 orbits of size 6 from \(C_4 \times 4C_{16} \times C_7^\times\),
- 24 orbits of size 12 from the remaining points with nonzero \(C_7\)-coordinate.

Thus a 5-invariant \(D\) would have to be a union of these orbits with
\[
30 = c + 4d,\qquad 120 = 6u + 12v,
\]
for suitable orbit counts. This alone is far too weak, but it gives a contradiction template: once the quotient identities determine the residue profile on \(P/F \cong C_4\), any orbit decomposition that violates those residue counts dies immediately. So this route is useful as a back-end consistency check, not as the lead proof.

## lemma_graph
Lemma skeleton.

1. If a \((448,150,50)\)-difference set \(D\subseteq G\) exists, then after the 5-multiplier normalization the six nonzero \(C_7\)-fibers have equal cardinality.
2. The projected \(C_7\)-moment identities then force the exact fiber profile \((30,20,20,20,20,20,20)\).
3. Passing from \(P\) to \(P/F \cong C_4\) produces residue-count vectors \(\alpha,\beta\) with \(\sum \alpha_r=30\), \(\sum \beta_r=20\), and \(\alpha_1,\alpha_2,\alpha_3 \equiv 0 \pmod 4\).
4. The vector \(\delta=\alpha-\beta\) has \(C_4\)-Fourier magnitudes all equal to 10, hence
   - either \((\delta_0+\delta_2,\delta_1+\delta_3)=(10,0)\) or \((0,10)\),
   - and the centered parameters satisfy a radius-5 sum-of-squares equation.
5. The vector \(\varepsilon=\alpha+6\beta\) has principal sum 150 and nonprincipal \(C_4\)-Fourier magnitudes 10, hence
   - either \((\varepsilon_0+\varepsilon_2,\varepsilon_1+\varepsilon_3)=(80,70)\) or \((70,80)\),
   - and its centered parameters also satisfy a radius-5 sum-of-squares equation.
6. Solve the resulting tiny integral system
\[
\alpha = (\varepsilon+6\delta)/7,\qquad \beta = (\varepsilon-\delta)/7,
\]
with the nonnegativity and divisibility constraints.

If that system has no solution, the difference set does not exist.

## chosen_plan
Best path: complete the quotient-consistency contradiction from Approach A.

Reason:
- it uses the exact group structure \(C_4 \times C_{16} \times C_7\),
- it stays theorem-facing rather than search-heavy,
- and it only needs a tiny bounded integer check after the main algebra is written down.

The intended title theorem, if this closes, is:
"There is no \((448,150,50)\)-difference set in \(C_4 \times C_{112}\)."

If the contradiction lands cleanly, that theorem would already be about 70-90% of a paper. The remaining packaging would be light: one short introduction positioning the residual [4,112] row among the other order-448 group types, plus a brief remark on the quotient/multiplier mechanism.

Current status of that plan:
- the \(C_7\)-quotient step closed completely;
- the \(P/F \cong C_4\) step reduced the search to one residue profile up to symmetry;
- the final contradiction did not appear at this quotient level alone.

## self_checks
Self-check after statement lock:
- The target is still the exact group-specific row [4,112], not a broader family claim.

Self-check after Approach A:
- The \(C_7\)-quotient identity uses only the standard projection formula \(n\cdot 1 + \lambda |H| K\), so the second moment 3300 is correct.
- Solving \(a+6b=150\), \(a^2+6b^2=3300\) gives the unique integer solution \((30,20)\).

Self-check after Approach B:
- Orbit sizes \(1,4,6,12\) match the orders of the 5-action on \(C_4\), \(C_{16}\), and \(C_7^\times\).
- This route is not yet decisive; it remains subordinate to the quotient contradiction.

Self-check after the bounded quotient check:
- The \(C_4\)-Fourier systems for \(\delta=\alpha-\beta\) and \(\varepsilon=\alpha+6\beta\) were solved by a tiny bounded integer enumeration, not by search over subsets of \(G\).
- The surviving outputs are exactly
  \[
  (\alpha,\beta)=((2,12,8,8),(6,4,4,6))
  \]
  and its \(1 \leftrightarrow 3\) swap
  \[
  (\alpha,\beta)=((2,8,8,12),(6,6,4,4)).
  \]
- These two are equivalent under inversion on the quotient \(C_4\), so there is only one profile up to quotient symmetry.

## code_used
Yes, but minimally and only after the reasoning scaffold was written.

Used:
- a tiny Python enumeration of the radius-5 parameterizations for the \(C_4\)-quotient vectors \(\delta=\alpha-\beta\) and \(\varepsilon=\alpha+6\beta\),
- filtered by integrality, nonnegativity, and the 5-orbit divisibility \(\alpha_1,\alpha_2,\alpha_3 \equiv 0 \pmod 4\).

Not used:
- no SAT / ILP / CP-SAT,
- no brute-force search over subsets of \(G\),
- no construction search in the full group.

## result
Partial structural result, not a full solve.

Assuming the standard 5-multiplier normalization, any \((448,150,50)\)-difference set in
\[
G \cong C_4 \times C_{16} \times C_7
\]
must satisfy:

1. Exact \(C_7\)-fiber profile:
\[
(|A_0|,|A_1|,\dots,|A_6|)=(30,20,20,20,20,20,20).
\]

2. If \(F=C_4\times 4C_{16}\) and \(\alpha_r,\beta_r\) record the counts in the quotient \(P/F\cong C_4\) for the heavy fiber and any nonzero fiber respectively, then up to the involution \(r\mapsto -r\) on \(C_4\),
\[
\alpha=(2,12,8,8),\qquad \beta=(6,4,4,6).
\]

Equivalently, the heavy fiber has only 2 points in the multiplier-fixed residue class and distributes the remaining 28 points as \(12,8,8\) across the three nonfixed residue classes, while each nonzero fiber distributes as \(6,4,4,6\).

This is a genuine theorem-facing slice, but it does not yet prove nonexistence.

## family_affinity
High. This argument sits exactly in the residual-case multiplier lane for abelian difference sets of order \(448\), and it uses the specific \(2\)-primary decomposition that earlier eliminations did not cover.

## generalization_signal
Moderate. The \(C_{2^a}\times C_{2^b}\times C_p\) quotient package looks reusable whenever a prime multiplier is transitive on the nonzero \(C_p\)-fibers and the remaining 2-part has a small fixed-subgroup quotient. What is not yet clear is how often the second \(C_4\)-level consistency system stays this rigid.

## proof_template_reuse
Reusable template:
1. normalize by a prime multiplier,
2. force equal nonzero \(p\)-fibers,
3. project the 2-part by the multiplier-fixed subgroup,
4. translate the existence problem into a tiny Fourier/autocorrelation system on a quotient such as \(C_4\),
5. finish by integrality and divisibility.

## candidate_theorem_slice
Candidate theorem slice visible now:
"Under the 5-multiplier normalization, any \((448,150,50)\)-difference set in \(C_4\times C_{112}\) has \(C_7\)-fiber profile \((30,20,20,20,20,20,20)\), and, after quotienting the 2-part by \(C_4\times 4C_{16}\), its residue counts are forced to the unique profile \((2,12,8,8)\) for the heavy fiber and \((6,4,4,6)\) for each nonzero fiber, up to inversion of the quotient \(C_4\)."

## smallest_param_shift_to_test
Two next shifts would be most informative:
- stay in the same packet and refine one level further from \(P/F\cong C_4\) to \(P/4C_{16}\cong C_4\times C_4\), to see whether the unique coarse residue profile actually lifts;
- compare the same quotient package on the nearest sibling order-448 groups with different 2-primary decomposition to test whether the forced profile is special to \([4,112]\) or part of a broader nonexistence template.

## why_this_is_or_is_not_publishable
If the nonexistence proof closes from here, it is publishable in the intended micro-paper lane: the exact title theorem is already clear, the result closes a cited residual row, and the remaining packaging is light.

At the current stopping point, the packet is still too thin for publication by itself. The reduction to one coarse residue profile is mathematically real and useful, but it is still an instance-level structural lemma rather than the title theorem.

## paper_shape_support
What would make the result paper-shaped, beyond the main closure:
- one clean proposition recording the forced \((30,20,\dots,20)\) fiber profile,
- one proposition recording the now-forced coarse \(C_4\)-residue profile,
- one short concluding theorem or contradiction eliminating the remaining lift.

Natural immediate remark if the contradiction lands:
the proof explains why the [4,112] row survives coarse order-448 arguments but dies once the specific \(C_4 \times C_{16}\) quotient geometry is exposed.

## boundary_remark
Current boundary: the argument already sees genuinely group-specific structure, but the last step still needs either a finer quotient lift obstruction or a direct character/orbit contradiction. So the current package is closer to a paper-shaped claim than a random exact witness would be, but it is still not yet a micro-paper result.

## likely_failure_points
Most likely technical failure points:
- the 5-multiplier normalization may require a translation choice that has to be stated more carefully than I have yet written,
- the \(C_4\)-Fourier equations do admit one coarse residue profile up to symmetry, so this quotient is not enough on its own,
- the residue-count contradiction likely needs one more local constraint from the lift to \(P/4C_{16}\) or from a direct character argument inside \(P\).

## what_verify_should_check
If this reaches a strong contradiction, verification should check:
- the exact multiplier normalization statement for 5 in this parameter set,
- the projected group-ring identities on \(C_7\) and \(C_4\),
- the derivation of the radius-5 sum-of-squares parametrizations,
- the bounded enumeration yielding the unique coarse residue profile up to symmetry,
- and whether that profile can or cannot be lifted to a subset of \(P\).

## verify_rediscovery
PASS 1 was a bounded prior-art audit on 2026-04-15 using the required exact-tuple, alternate-notation, canonical-source, same-source, and recent-status search patterns. Within the search budget, it rechecked:

- exact instance notation: `"(448,150,50)" "C_4 x C_112" difference set`
- alternate notation: `"(448,150,50)" "[4,112]" difference set`
- canonical source / table anchor: `"A Survey of the Multiplier Conjecture" Table 2 448 150 50 4 112`
- same-source / nearby theorem check: `Arasu Proposition 4 448 150 50 C_4 C_112 difference set`
- recent / status-style sweeps for later settlement and repository-style status pages

Bounded conclusion:

- Gordon-Schmidt still serves as the canonical source anchor for this exact residual row and keeps the `[4,112]` case open in Table 2.
- The surfaced Arasu nonexistence result removes other order-448 group decompositions, not `C_4 x C_112`.
- The bounded later-status sweep did not surface a targeted post-2016 settlement of the exact row.

So PASS 1 did not establish rediscovery within budget. This is only a bounded non-rediscovery finding, not a proof of novelty.

## verify_faithfulness
The intended statement is the exact existence question:

> determine whether `C_4 x C_112` admits a `(448,150,50)` difference set.

The current artifact does not settle that statement. Its strongest honest output is only a conditional structural slice:

- assuming a usable `5`-multiplier normalization for this exact row,
- one gets the forced `C_7`-fiber profile `(30,20,20,20,20,20,20)`,
- and one gets one forced coarse `C_4`-quotient residue profile up to inversion.

That is a weaker proxy statement rather than the intended theorem. So the packet remains faithful to the exact target as a research direction, but the proved content is only a partial conditional reduction, not the intended existence/nonexistence result.

## verify_proof
First load-bearing gap:

- In `definitions` / `approach_A`, the solve takes as available the statement that `5` acts as a usable numerical multiplier because `5 | n` and `gcd(5,448)=1`.

That is not justified inside the artifact, and no cited theorem is provided there establishing that multiplier conclusion for this exact row. Since the whole reduction to equal nonzero `C_7`-fibers depends on that normalization, the main argument is not verified as an unconditional proof about the selected problem.

Bounded downstream check:

- conditional on the `5`-multiplier normalization,
- the projected `C_7` moment equations are correct,
- the solution `(30,20)` to `a + 6b = 150`, `a^2 + 6b^2 = 3300` is correct,
- and the stated `C_4`-quotient Fourier package is arithmetically consistent.

So no later arithmetic mistake was found in the reduced quotient calculation. The verification failure is the unsupported multiplier premise, not a downstream enumeration error.

## verify_adversarial
There is no candidate-local checker file to rerun, so the adversarial pass used an independent tiny enumeration from first principles of the displayed quotient constraints.

I independently enumerated all nonnegative pairs

\[
\alpha \in \mathbf{Z}_{\ge 0}^4,\qquad \beta \in \mathbf{Z}_{\ge 0}^4
\]

with

- `sum(alpha) = 30`,
- `sum(beta) = 20`,
- `alpha_1, alpha_2, alpha_3 \equiv 0 \pmod 4`,
- all nonprincipal `C_4`-Fourier magnitudes of `delta = alpha - beta` equal `10`,
- all nonprincipal `C_4`-Fourier magnitudes of `epsilon = alpha + 6 beta` equal `10`.

The rerun produced exactly two solutions:

\[
(\alpha,\beta)=((2,12,8,8),(6,4,4,6))
\]

and its inversion swap

\[
(\alpha,\beta)=((2,8,8,12),(6,6,4,4)).
\]

So the solver's coarse quotient profile survives adversarial recomputation conditional on the multiplier setup. What the rerun does *not* certify is:

- that the `5`-multiplier premise is legitimate for the exact row,
- or that the coarse quotient data lifts to an actual difference set / contradiction in `P`.

## verify_theorem_worthiness
Assessment by the required lenses:

- exactness: not exact; the current verified content is a conditional reduction, not the selected existence/nonexistence theorem
- novelty: bounded PASS 1 did not establish rediscovery of the target row, but the current conditional slice is not yet a strong standalone novelty claim
- reproducibility: moderate; the quotient arithmetic and tiny enumeration are reproducible
- Lean readiness: no; formalizing this conditional slice would not be the shortest path to a sealed packet
- paper leverage: the target still has strong leverage if solved, but the current verified output does not

Required explicit answers:

- Would this result, if correct and Lean-sealed, already constitute most of a publishable note?
  - No. A Lean-sealed conditional quotient lemma would still leave the multiplier justification and the actual existence/nonexistence theorem unresolved.
- What percentage of the paper would one solve already provide?
  - The current verified slice looks closer to about `35%` of a note than to the intended `70-90%` micro-paper lane.
- What title theorem is actually visible?
  - At best: under a valid `5`-multiplier normalization, any `(448,150,50)` difference set in `C_4 x C_112` has forced `C_7`-fiber sizes `(30,20,20,20,20,20,20)` and a unique coarse `C_4`-quotient residue profile up to inversion.
- What part of the argument scales?
  - The quotient / Fourier reduction template could plausibly scale to nearby `C_{2^a} x C_{2^b} x C_p` settings when a genuine multiplier theorem is available.
- What part clearly does not?
  - The exact coarse profile, the publication claim, and the final obstruction do not currently scale; they still depend on a missing multiplier justification and on one more group-specific elimination step.
- Is the best honest publication status still only `INSTANCE_ONLY` or even `NONE`?
  - Still `NONE`. The verified artifact is too conditional and too incomplete even for an `INSTANCE_ONLY` publication claim.

## verify_verdict
Verdict: `verify_verdict = UNVERIFIED`, `classification = PARTIAL`, `publication_status = NONE`, `lean_ready = false`.

Reason:

- PASS 1 did not establish rediscovery within budget.
- The first load-bearing step of the proof assumes, rather than proves or cites, a usable `5`-multiplier theorem for this exact row.
- The downstream quotient arithmetic survives conditional recomputation, so the artifact preserves a real conditional structural slice, but not a verified solve of the selected problem.

## minimal_repair_if_any
No mathematical repair was applied to the main solve record.

Smallest conservative repair:

- restate every downstream claim explicitly as conditional on a proved `5`-multiplier theorem for this exact row,
- or remove the multiplier-based normalization and replace it with an unconditional argument before making any existence / nonexistence claim.

## publication_prior_art_audit
Bounded publication prior-art audit completed on `2026-04-15`.

- Exact-statement searches for `"(448,150,50)" "C_4 x C_112" difference set` and close variants surfaced Gordon-Schmidt `2016` as the canonical open-row anchor together with older order-448 papers, but no post-`2016` row-closing theorem for `C_4 x C_112`.
- Alternate-notation searches for `"(448,150,50)" "[4,112]" difference set` again surfaced the same survey-table trail, with no later targeted settlement in the bounded pass.
- Canonical-source check: Gordon-Schmidt `2016`, Table `2`, still lists `(448,150,50)` in group `[4,112]` among the residual cases, with `5` appearing in the `MC primes` column rather than as an already proved multiplier theorem.
- Theorem / proposition / example / corollary / observation / sufficient-condition check inside the canonical source found no local theorem closing `[4,112]`; the survey's quoted general multiplier theorem requires `p > lambda`, so it does not justify `p = 5` when `lambda = 50`.
- Outside-source status check: Lopez-Sanchez `1997` still lists `(448,150,50)` among the unresolved abelian tuples of order under `500`, and Arasu `2000`, Proposition `4`, removes several other order-448 group types but not `C_4 x C_112`.
- A recent follow-up check was warranted because the current artifact turns on the `5`-multiplier step. A bounded sweep of exact-tuple searches and Dan Gordon's publications page through `2025` surfaced no later paper explicitly settling the `[4,112]` row or making `5` unconditional for this exact case.

Conservative prior-art verdict: bounded audit did not establish rediscovery, but it also confirmed that the current solve artifact leans on the open multiplier-conjecture lane rather than on a cited theorem already present in the canonical source.

## publication_statement_faithfulness
The packet is not faithful to the selected statement at publication level.

- Selected statement: determine whether `C_4 x C_112` admits a `(448,150,50)` difference set.
- Strongest honest supported claim: assuming a valid `5`-multiplier normalization for this exact row, any such difference set has forced `C_7`-fiber sizes `(30,20,20,20,20,20,20)` and a unique coarse `C_4`-quotient residue profile up to inversion.
- This is stronger than "here is an example," because it gives a structural necessary-condition slice rather than a one-off witness.
- It is still not the selected theorem. The current artifact neither proves nonexistence nor constructs a difference set in `C_4 x C_112`.
- The main faithfulness problem is load-bearing: the argument assumes exactly the `5`-multiplier setup that the canonical survey treats as conjectural `MC-prime` data for this row, not as a theorem cited in the artifact.
- A referee asking "what is the theorem?" would not receive the advertised row-closing theorem; they would receive a conditional reduction.

## publication_theorem_worthiness
The surviving result has some theorem content, but it is not title-theorem strength.

- Is the strongest honest claim stronger than "here is an example"? Yes. It is a structural necessary-condition theorem slice.
- Is there a real title theorem, theorem slice, or counterexample theorem here? There is a theorem slice, but not a title theorem and not a counterexample theorem.
- Is the proof structural or merely instance-specific? Structural in method, exact-row-specific in scope, and conditional on a multiplier premise that is not currently sourced as a theorem for this case.
- Would this survive a referee asking "what is the theorem?" No. The current answer is too premise-dependent and too far from the advertised closure.
- Is the claim still too dependent on hand-picked small cases? Not in the brute-force sense, but yes in the publication sense: the packet depends on one hand-picked quotient profile and an unresolved multiplier assumption.
- If this is not yet paper-ready, is the remaining gap genuinely small? No. After audit, the remaining gap is mathematical closure, not just writeup or Lean polish.

## publication_publishability
This is not publication-ready in the micro-paper sense.

- Would this result, if correct and verified in the current bounded sense, already constitute most of a publishable note? No.
- What percentage of a publishable note does the current boundedly supported result provide? About `25%`.
- Prospectively, an exact solve of the original `[4,112]` row would still likely supply around `80%` of a short note, but that prospective leverage is not the same as the current audited packet.
- Is there a real title theorem here? Not yet. There is only a conditional quotient theorem slice.
- If this is not yet paper-ready, should it be moved aside rather than expanded into a larger theorem program? Yes. Preserve the slice, but do not broaden this into a feeder-ladder project.
- Would Lean directly seal the packet? No. Lean would only formalize a conditional reduction and would act as later archival polish, not as the missing mathematical closure.

Publication status decision: `NONE`.

## publication_packet_audit
Packet-quality audit for the current strongest honest claim:

- `publication_status`: `NONE`
- `publication_confidence`: `high`
- `publication_packet_quality`: `thin`
- `proof_artifacts_preserved`: yes, for the conditional quotient slice and for the audit trail showing why it is not enough
- `lean_packet_seal`: no
- `human_ready`: no

Why not `SLICE_CANDIDATE`:

- the main surviving slice is conditional on the unresolved multiplier-conjecture lane for this row,
- the remaining gap is not genuinely small after skeptical checking,
- and the packet fails the referee test "what is the theorem?"

## micro_paper_audit
This run fails the strict micro-paper lane in its current audited form.

- The candidate still looks attractive as a target if solved exactly: closing the exact `[4,112]` row would be close to a paper on its own.
- After audit, the current packet is not close to that state. Its strongest honest output is only a conditional quotient slice.
- The surviving claim is stronger than an example, but it is not yet the title theorem of a short note.
- The packet therefore only looked close before audit. Once the multiplier premise is checked against the canonical source, the remaining gap is not light.

## strongest_honest_claim
Assuming a valid `5`-multiplier normalization for the exact row `[4,112]`, any `(448,150,50)` difference set in `C_4 x C_112` has `C_7`-fiber sizes `(30,20,20,20,20,20,20)` and, after quotienting the `2`-part by `C_4 x 4C_16`, a unique coarse residue profile up to inversion: heavy fiber `(2,12,8,8)` and nonzero fiber `(6,4,4,6)`.

## paper_title_hint
No current publication title is recommended. The least misleading fallback title would be:

`Conditional Fiber and Quotient-Residue Constraints for a Hypothetical (448,150,50) Difference Set in C_4 x C_112`

but this is not strong enough for the active micro-paper lane.

## next_action
- Preserve the conditional quotient slice as audited partial progress.
- Do not treat the current multiplier-based reduction as theorem-closing evidence.
- Move this candidate aside unless a same-lane argument either proves the `5`-multiplier step from cited theorems or replaces it with an unconditional obstruction / construction.
- Do not widen this into a broader multiplier-conjecture program from this packet.
