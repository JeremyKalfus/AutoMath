# Solve Record: On the (765,192,48) Difference-Set Problem in C_3 x C_255

- slug: `abelian-difference-set-765-192-48-group-3-255`
- working_packet: `artifacts/abelian-difference-set-765-192-48-group-3-255/working_packet.md`

## statement_lock
Determine whether the abelian group C_3 x C_255 admits a (765,192,48)-difference set.

## definitions
Write
\[
G \cong C_3^2 \times C_5 \times C_{17}, \qquad v=765,\qquad k=192,\qquad \lambda=48,\qquad n=k-\lambda=144.
\]
For a hypothetical difference set \(D \subset G\), every nonprincipal character \(\chi\) of \(G\) satisfies
\[
\chi(D)\overline{\chi(D)} = n = 144.
\]
The active packet points to multiplier pressure at the prime \(2\); the intended normalization is that, after translation, one may work with a \(2\)-multiplier-fixed set \(D\), so \(2D=D\).

Ambiguities and conventions:

- I am treating the packet's "prime 2 recorded against the row" as the source-level multiplier input that verify must later check against Gordon-Schmidt.
- I use additive notation for the quotient \(C_{17}\), but write character sums multiplicatively when convenient.
- The solve-critical quotient is \(\pi:G \to C_{17}\) with kernel \(C_3^2 \times C_5\) of size \(45\).

## approach_A
Structural / invariant route:

1. Assume \(D\) exists and normalize by the \(2\)-multiplier so that \(2D=D\).
2. Push \(D\) to the \(C_{17}\)-quotient. Let \(m(x)=|D \cap \pi^{-1}(x)|\), so \(\sum_{x \in C_{17}} m(x)=192\).
3. Because doubling on \(C_{17}^\times\) has two orbits of size \(8\), the multiplier-fixed hypothesis forces
   \[
   m(0)=a,\qquad m(x)=b \text{ on one nonzero orbit},\qquad m(x)=c \text{ on the other}.
   \]
   Hence
   \[
   a+8b+8c=192. \tag{A1}
   \]
4. For every nonprincipal character \(\psi\) of \(C_{17}\), the lifted character on \(G\) is still nonprincipal, so
   \[
   \left|\sum_{x \in C_{17}} m(x)\psi(x)\right|=12.
   \]
5. The two nonzero doubling orbits are the quadratic-residue and quadratic-nonresidue classes. If
   \[
   \eta=\sum_{q \in Q}\zeta^{q}=\frac{-1+\sqrt{17}}{2},\qquad
   \eta'=\sum_{n \in N}\zeta^{n}=\frac{-1-\sqrt{17}}{2},
   \]
   then the two possible nonprincipal quotient sums are
   \[
   S_1=a+b\eta+c\eta',\qquad S_2=a+b\eta'+c\eta.
   \]
   Both are real, Galois-conjugate, and must each have absolute value \(12\).
6. Thus
   \[
   S_1-S_2=(b-c)\sqrt{17}.
   \]
   Since \(S_1,S_2 \in \{\pm 12\}\), their difference is in \(\{0,\pm 24\}\), so the irrational term forces \(b=c\).
7. Then
   \[
   S_1=S_2=a-b=\pm 12,\qquad a+16b=192.
   \]
   Therefore
   \[
   17b=180 \text{ or } 204,
   \]
   impossible in integers.

This gives a clean contradiction, conditional only on the legitimacy of the \(2\)-multiplier normalization.

## approach_B
Construction / extremal / contradiction route:

1. Decompose \(G\) as \(H \times C_{17}\) with \(H=C_3^2 \times C_5\), \(|H|=45\).
2. If the quotient contradiction above were to fail, the only plausible surviving shape would be a fiber decomposition
   \[
   D=\bigsqcup_{t \in C_{17}} (B_t,t),\qquad |B_t|=m(t).
   \]
3. The quotient formulas strongly suggest the extremal profile \(m(0)=0\) and \(m(t)=12\) for all \(t \neq 0\), so \(D\) would consist of \(16\) subsets \(B_t \subset H\), each of size \(12\).
4. For differences inside the same \(C_{17}\)-fiber, the average required multiplicity on \(H \setminus \{0\}\) is exactly
   \[
   \frac{16 \cdot 12 \cdot 11}{44}=48,
   \]
   i.e. an average of \(3\) per fiber, the same count as a \((45,12,3)\)-difference set in \(H\).
5. So a constructive route would need a tightly coordinated family of \(16\) size-\(12\) subsets of \(H\) with within-fiber and cross-fiber correlations all locked to the difference-set count.

This route does not immediately disprove existence, but it shows how rigid the surviving geometry would have to be if the multiplier route did not already kill the row.

## lemma_graph
Lemma skeleton:

1. Quotient character lemma:
   The projection \(m:C_{17}\to \mathbf Z_{\ge 0}\) of a hypothetical difference set satisfies \(|\widehat m(\psi)|=12\) for every nonprincipal \(\psi\) of \(C_{17}\).
2. Multiplier orbit lemma:
   Under a \(2\)-multiplier normalization, \(m\) is constant on the three doubling orbits \( \{0\}, Q, N\) in \(C_{17}\).
3. Quadratic-period lemma:
   The nonprincipal Fourier values are \(a+b\eta+c\eta'\) and \(a+b\eta'+c\eta\) with \(\eta,\eta' = (-1\pm \sqrt{17})/2\).
4. Orbit-equality lemma:
   Since both Fourier values are real and have absolute value \(12\), one gets \(b=c\).
5. Arithmetic contradiction:
   The system \(a+16b=192\) and \(a-b=\pm12\) has no integer solution.
6. Conditional conclusion:
   If the cited multiplier input indeed licenses \(2D=D\) after translation, then no \((765,192,48)\)-difference set exists in \(C_3 \times C_{255}\).

## chosen_plan
Best path: pursue the quotient contradiction, not a brute-force search.

- It is theorem-facing and short.
- It matches the packet's recommended first attack exactly.
- It uses the \(C_{17}\) factor where doubling has the cleanest orbit structure and where the square-root obstruction appears immediately.
- No code is needed unless the multiplier premise itself turns out to be unavailable locally.

## self_checks
- Statement lock check: the exact target remains the single table row \((765,192,48)\) in \(C_3 \times C_{255}\), not a broader family claim.
- Quotient check: the lifted nonprincipal characters from \(C_{17}\) do force modulus \(12\), because \(n=144\).
- Orbit check: the contradiction uses only the three doubling orbits on \(C_{17}\); it does not assume extra symmetry on the \(C_3^2 \times C_5\) kernel.
- Conservatism check: the only unproved external ingredient is the source-level claim that \(2\) is a valid multiplier normalization for this row.

## code_used
No code used. The quotient contradiction is short enough to do by hand, and the remaining load-bearing task is source verification of the multiplier premise rather than computation.

## result
Current best result:

- Conditional nonexistence proof candidate.
- Exact candidate title theorem:
  `There is no (765,192,48)-difference set in the abelian group C_3 x C_255.`

Argument status:

- If a standard source theorem justifies normalizing a hypothetical difference set to be fixed by multiplication by \(2\), then the \(C_{17}\)-quotient already yields an integer contradiction.
- The contradiction is:
  \[
  a+8b+8c=192,\qquad a+b\eta+c\eta'=\pm12,\qquad a+b\eta'+c\eta=\pm12,
  \]
  with \(\eta,\eta'=(-1\pm\sqrt{17})/2\).
- This forces \(b=c\), then \(a-b=\pm12\) and \(a+16b=192\), which has no integer solution.

So the row looks very close to closed on the nonexistence side, with the multiplier normalization as the only remaining verification-critical hinge.

## family_affinity
High. This sits naturally in the multiplier-conjecture residual-row lane: exact abelian group, exact open table row, and the obstruction comes from a quotient-plus-multiplier argument rather than search.

## generalization_signal
Moderate. The template should transfer to other residual rows where:

- a small prime multiplier is available,
- the quotient by a prime factor \(p\) of the group order has only a few multiplier orbits,
- the relevant Gauss periods already force a square-root term whose coefficient must vanish.

What scales here is the orbit/quotient character package. What does not automatically scale is the final integrality contradiction, which depends on the exact values \(k=192\), \(n=144\), and the \(17\)-orbit size \(8\).

## proof_template_reuse
Reusable template:

1. isolate a packet-supported multiplier prime;
2. project to the cleanest odd-prime quotient;
3. write quotient fiber counts by multiplier orbits;
4. evaluate the nonprincipal quotient characters via low-order Gauss periods;
5. force orbit-count equalities by irrationality;
6. close with the integer size equation.

This is a genuine short-note proof template, not a one-off search certificate.

## candidate_theorem_slice
Visible theorem slice:

`Assuming the standard multiplier-2 normalization, any (765,192,48)-difference set in C_3 x C_255 would induce C_17-quotient fiber counts (a,b,c) on the three doubling orbits satisfying both a+8b+8c=192 and a+bη+cη', a+bη'+cη in {±12}; this system has no integer solution.`

That slice is already theorem-shaped and is the smallest decisive unit in the current argument.

## smallest_param_shift_to_test
Best next parameter shifts, if the manager wants family signal after verification:

1. test other residual rows where the quotient prime is \(17\) and the tabulated multiplier prime is again \(2\);
2. test rows with the same \(n=144\) but a different odd-prime quotient, to see whether the same square-root elimination survives.

Those are the nearest shifts that would tell us whether this is an isolated exact-row obstruction or a tiny family phenomenon.

## why_this_is_or_is_not_publishable
If the multiplier premise verifies cleanly, this is publishable in the micro-paper lane.

- A successful solve here would already be about 80-90% of a paper.
- The title theorem is exact, isolated, and already source-certified as an open table row.
- Minimal remaining packaging work would be:
  1. quote the exact multiplier theorem or table condition that licenses the \(2\)-normalization;
  2. present the three-orbit \(C_{17}\)-quotient calculation cleanly;
  3. add a short paragraph explaining why this row survived the published coarse filters.

If the multiplier premise does not verify, the present result is too thin on its own, because the contradiction is then only conditional.

## paper_shape_support
What makes the result paper-shaped if the main claim closes:

- the exact title theorem is already fixed by the survey table;
- the proof is short and conceptual rather than computational;
- one immediate supporting slice is the quotient-fiber impossibility lemma above;
- one natural remark is that the obstruction is visible already on the \(C_{17}\) quotient, before any detailed work inside \(C_3^2 \times C_5\).

Immediate corollary / remark:

`Under the same multiplier normalization, any hypothetical example would already fail at the quotient-count level, so no search inside the 45-element kernel is needed.`

## boundary_remark
Boundary remark:

- The argument does not currently show a broader nonexistence theorem for all groups of order \(765\) or all \((765,192,48)\)-rows.
- It is tuned to the exact \(C_3^2 \times C_5 \times C_{17}\) decomposition and the \(2\)-orbit structure on \(C_{17}\).
- So the current package is closer to a paper-shaped exact-row nonexistence note than to a broad family theorem.

## likely_failure_points
Main risk points:

1. the packet's multiplier cue might be weaker than a fully usable theorem statement for this exact row;
2. the source may require a translate \(D^{(2)} = gD\) rather than literal setwise invariance, and the quotient argument must be phrased after the correct normalization;
3. verify must check that the quadratic-period identification of the two nonzero doubling orbits in \(C_{17}\) matches the chosen quotient conventions.

## what_verify_should_check
Verify should check exactly:

1. Does the Gordon-Schmidt source machinery indeed allow the normalization \(2D=D\) (after translation) for this row?
2. Is the row's tabulated multiplier entry really the prime \(2\), with no hidden exception for the group \([3,255]\)?
3. Are the nonzero doubling orbits in \(C_{17}\) exactly the residue/nonresidue classes used in the period calculation?
4. Once that premise is confirmed, audit the short contradiction
   \[
   a+8b+8c=192,\qquad a+b\eta+c\eta',\,a+b\eta'+c\eta \in \{\pm12\}
   \]
   and the conclusion \(17b=180\) or \(204\).

## verify_rediscovery
PASS 1: bounded rediscovery audit.

- Exact-instance searches on the tuple \((765,192,48)\), the group notation \(C_3 \times C_{255}\), and the shorthand row \([3,255]\) did not surface a later paper or database entry settling this exact row within the search budget.
- The canonical source still appears to be Gordon-Schmidt's multiplier-conjecture survey, with Table 2 listing the exact row \((765,192,48)\) in group \([3,255]\) as open.
- Same-source checking matters here: the survey text around Table 2 states that the `MC primes` column records primes that would be multipliers under the multiplier conjecture. That column is not, by itself, a proof that \(2\) is already an available multiplier theorem for this row.
- Verdict for PASS 1: no rediscovery established within budget, but the source audit weakens the solve record's multiplier premise rather than strengthening it.

## verify_faithfulness
PASS 2: faithfulness to the intended statement.

- Intended statement: determine unconditionally whether \(C_3 \times C_{255}\) admits a \((765,192,48)\)-difference set.
- Actual supported statement in the solve record is weaker and different: at best it derives a quotient-fiber constraint assuming an additional \(2\)-multiplier normalization.
- This is wrong-theorem drift. The solve record presents an unconditional nonexistence title theorem, but the argument only targets a conditional intermediate slice and never justifies the condition from the cited source.
- Faithfulness verdict: the current solve does not match the intended statement exactly. Classification must therefore drop to `VARIANT`.

## verify_proof
PASS 3: proof correctness.

First incorrect step:

- `approach_A`, step 1: the argument assumes one may normalize a hypothetical difference set to satisfy \(2D=D\), treating the table's recorded prime \(2\) as an already available multiplier theorem. The source material checked in PASS 1 does not establish that. So the proof of the intended theorem already fails at its first load-bearing step.

Independent later failure even under the conditional premise:

- `approach_A`, step 7 claims the system
  \[
  a+16b=192,\qquad a-b=\pm 12
  \]
  has no integer solution. That is false. The branch \(a-b=-12\) gives
  \[
  17b=204,\qquad b=12,\qquad a=0,
  \]
  hence \((a,b,c)=(0,12,12)\) after the earlier deduction \(b=c\).
- Therefore the advertised quotient contradiction does not exist. Even if a valid \(2\)-multiplier theorem were supplied later, the current proof would still not establish nonexistence.

Proof verdict:

- No correct proof of nonexistence is present.
- The strongest defensible residue is only a conditional quotient-profile lemma, not the intended theorem.

## verify_adversarial
PASS 4: adversarial check.

- No checker or search code existed to rerun, so I stress-tested the arithmetic package directly.
- The doubling action on \(C_{17}\) has exactly three orbits:
  \[
  \{0\},\quad \{1,2,4,8,9,13,15,16\},\quad \{3,5,6,7,10,11,12,14\}.
  \]
- Solving the claimed quotient conditions shows that the fiber profile
  \[
  m(0)=0,\qquad m(x)=12 \text{ on each nonzero doubling orbit}
  \]
  is compatible with the Fourier constraints. Indeed, with \(a=0\) and \(b=c=12\),
  \[
  S_1=S_2=12(\eta+\eta')=-12,
  \]
  so \(|S_1|=|S_2|=12\) holds exactly.
- This adversarial check breaks the claimed contradiction and confirms that the quotient analysis alone only forces a specific profile; it does not rule out existence.

## verify_theorem_worthiness
PASS 5: theorem worthiness.

- Exactness: the intended exact theorem is not proved. The repaired output is only the conditional slice "if a valid \(2\)-multiplier normalization exists, then the \(C_{17}\)-quotient fibers must satisfy \(m(0)=0\) and \(m(x)=12\) for all \(x \neq 0\)".
- Novelty: no rediscovery was found for the exact target row, but the repaired conditional slice is too intermediate to claim frontier-novel publication value on its own.
- Reproducibility: the quotient arithmetic is reproducible; the claimed theorem is not, because the multiplier premise is unsupported and the contradiction is false.
- Lean readiness: no. Formalizing the current slice would seal only a conditional intermediate lemma and would not be the shortest route to a publishable packet.
- Paper leverage: low in the current verified state. The solver has not closed the row; it has only isolated one possible quotient profile.

Explicit answers:

- Would this result, if correct and Lean-sealed, already constitute most of a publishable note? No. The current verified residue would be a side lemma, not the title theorem of a note.
- What percentage of the paper would one solve already provide? In its repaired form, about 25% to 35% of a note, not the 70% to 90% micro-paper target.
- What title theorem is actually visible? At most: assuming a valid \(2\)-multiplier normalization, the \(C_{17}\)-quotient fibers are forced to be \(0\) over \(0\) and \(12\) over each nonzero class.
- What part of the argument scales? The orbit decomposition and Gauss-period/Fourier bookkeeping on a prime quotient.
- What part clearly does not? The unsupported multiplier premise and the nonexistent final contradiction.
- Is the best honest publication status still only `INSTANCE_ONLY` or even `NONE`? Even `NONE` at this stage. The verified residue is not yet a paper-shaped theorem packet.

## verify_verdict

- `verify_verdict = VARIANT`
- `classification = VARIANT`
- `confidence = high`
- `publication_status = NONE`
- `lean_ready = false`
- `next_action = repair the canonical claim down to the conditional quotient-profile lemma, then return to solve for either a genuine multiplier theorem or a further contradiction/construction beyond the profile (0,12,12).`

## minimal_repair_if_any
Tiny conservative repair available:

- Remove the unconditional nonexistence claim.
- Retain only the conditional lemma:
  `Assuming a valid 2-multiplier normalization for a hypothetical (765,192,48)-difference set in C_3 x C_255, its C_17-quotient fiber counts are forced to satisfy m(0)=0 and m(x)=12 for every nonzero x.`
- This repair preserves a useful structural ingredient for a future solve pass, but it does not settle the selected problem.

## publication_prior_art_audit
Audit date: 2026-04-15.

- Exact-statement web searches on `(765,192,48)` together with `C_3 x C_255` and plain `difference set` did not surface a later construction, nonexistence theorem, or database row settling this exact case within the bounded audit.
- Alternate-notation searches on `(765,192,48)` together with `[3,255]` and `Z_3 x Z_255` likewise did not produce a direct later settlement.
- Canonical-source check: Gordon-Schmidt's survey still lists `765 192 48 [3,255]` in Table 2 among open difference-set parameters.
- Same-source theorem/proposition/example/corollary/observation/sufficient-condition check: the surrounding survey text explains that the `MC primes` column records primes that would be multipliers under the multiplier conjecture; I did not find a same-source theorem in the bounded check that already settles the `[3,255]` row.
- Outside-source status pass: Dan Gordon's current Difference Sets database page advertises a maintained status database and recent computations, but the bounded exact-row search did not reveal a later page or paper settling this row.
- Conservative prior-art verdict: no rediscovery was established in this bounded audit, but the audit also did not positively confirm that the row remains open beyond the accessible source-and-search sweep. The honest claim should therefore stay narrowly scoped.

## publication_statement_faithfulness
- The intended statement is unconditional: determine whether `C_3 x C_255` admits a `(765,192,48)`-difference set.
- The strongest verified output is weaker: assuming a valid `2`-multiplier normalization, the `C_17` quotient fibers are forced to the profile `m(0)=0` and `m(x)=12` for every nonzero `x`.
- The canonical source does not, in this bounded audit, justify upgrading the survey's `MC primes` entry into an already available unconditional multiplier theorem for this exact row.
- So the current packet is faithful only when phrased as a conditional theorem slice. Any unconditional nonexistence or near-closure wording is too strong.

## publication_theorem_worthiness
- Is the strongest honest claim stronger than "here is an example"? Yes, but only modestly. It is a structural conditional lemma about every hypothetical example, not a single worked instance.
- Is there a real title theorem, theorem slice, or counterexample theorem here? There is a real theorem slice, but not yet a title theorem for a paper and not a counterexample theorem.
- Is the proof structural or merely instance-specific? Structural in method: quotient-orbit and Fourier/Gauss-period bookkeeping on `C_17`. But it remains locked to one exact row and still depends on an unsupported premise.
- Would this survive a referee asking "what is the theorem?" Not as a standalone note. The referee would reasonably ask for the unconditional multiplier input or a further argument that actually closes the row.
- Is the claim too dependent on hand-picked small cases? It is not brute-force or small-case enumeration, but it is still too dependent on a single conditional profile computation to carry a paper on its own.
- Worthiness verdict: useful solve-side infrastructure, not yet a publishable theorem packet.

## publication_publishability
- Would this result, if correct and verified in the current bounded sense, already constitute most of a publishable note? No.
- What percentage of the paper would one solve already provide? About 25% to 35%; I record `0.3` below as the audit estimate.
- Is the remaining gap genuinely small? No. After audit, the remaining gap is not cleanup or exposition. The packet still lacks the decisive theorem-closing step.
- If this is not paper-ready, should it be moved aside rather than expanded into a larger theorem program? Yes. Preserve the conditional slice, but do not broaden this into a larger multiplier program from within the one-shot lane.
- Publishability verdict: `NONE`, not `SLICE_CANDIDATE`. The current packet does not yet supply the theorem a short note would need.

## publication_packet_audit
- Packet strengths preserved: exact source row, explicit target statement, repaired conditional structural slice, and enough written reasoning to resume solve without replaying the whole run.
- Packet weaknesses: no unconditional theorem, no decisive nonexistence contradiction, no construction, and no paper-ready title theorem.
- Publication packet quality: thin but preserved. It is suitable as future solve input, not as a human-ready publication packet.
- Would Lean directly seal the packet? No. Lean would only formalize the current conditional lemma, which would be optional polish on a non-paper-ready state rather than a decisive seal.

## micro_paper_audit
- The pre-audit story that one solve here would be `0.8` of a paper did not survive verification. In the current verified state, the surviving result is only a conditional structural ingredient.
- `title_theorem_strength`: weak.
- `publication_narrative_strength`: weak.
- The candidate looked micro-paper-ready before audit because the source row itself is clean and isolated. After audit, the theorem packet is still too incomplete for the micro-paper lane.
- Micro-paper verdict: fail for now. This slug should be cooled or moved aside unless a same-lane exact proof/disproof becomes visible without broadening scope.

## strongest_honest_claim
Assuming a valid `2`-multiplier normalization for a hypothetical `(765,192,48)`-difference set in `C_3 x C_255`, the induced `C_17`-quotient fiber counts are uniquely forced to satisfy `m(0)=0` and `m(x)=12` for every nonzero `x`; this does not by itself prove existence or nonexistence.

## paper_title_hint
No honest standalone paper title yet. At most: `A conditional C_17-quotient profile for hypothetical (765,192,48)-difference sets in C_3 x C_255`.

## next_action
Preserve the repaired conditional slice as a solve artifact, but move this slug aside unless a direct exact-row proof or disproof appears in the same one-shot lane. Do not expand it into a broader multiplier program, and do not spend Lean effort on it before a decisive theorem is in hand.
