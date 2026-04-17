# Solve Record: Does the abelian group C_7 x C_49 admit a (343,171,85)-difference set?

- slug: `abelian-difference-set-343-171-85-group-7-49`
- working_packet: `artifacts/abelian-difference-set-343-171-85-group-7-49/working_packet.md`

## statement_lock
Determine whether the abelian group C_7 x C_49 admits a (343,171,85)-difference set.

## definitions
Write
\[
G=\langle x\rangle \times \langle y\rangle \cong C_7\times C_{49},
\]
with \(|x|=7\) and \(|y|=49\). A \((343,171,85)\)-difference set is a subset \(D\subseteq G\) of size \(171\) such that in the group ring
\[
DD^{(-1)}=171+85(G-1).
\]
Equivalently, every nonprincipal character \(\chi\) of \(G\) satisfies
\[
|\chi(D)|^2 = k-\lambda = 86.
\]
For the quotient map \(\pi_H:G\to G/H\), the fiber-count function is
\[
f_H(gH)=|D\cap gH|.
\]
Two quotient choices matter immediately:

1. \(H=\langle y\rangle\cong C_{49}\), giving a 7-term coset-count vector \(a_i\).
2. \(N=\langle y^7\rangle\cong C_7\), giving a 49-term fiber-count function on \(G/N\cong C_7\times C_7\).

The exact title theorem, if closed, would be:
"The abelian group \(C_7\times C_{49}\) does not admit a \((343,171,85)\)-difference set"
or
"The abelian group \(C_7\times C_{49}\) admits a \((343,171,85)\)-difference set."

## approach_A
Structural / invariant route through the quotient \(G/\langle y\rangle\cong C_7\).

Let \(a_i = |D\cap x^i\langle y\rangle|\), \(i\in \mathbf Z/7\mathbf Z\). Summing the group-ring identity over each coset of \(\langle y\rangle\) gives
\[
\sum_i a_i = 171,
\]
\[
\sum_i a_i^2 = 171 + 48\cdot 85 = 4251,
\]
and for each nonzero \(t\in \mathbf Z/7\mathbf Z\),
\[
\sum_i a_i a_{i+t} = 49\cdot 85 = 4165.
\]
After centering at the average scale \(24\), with \(b_i=a_i-24\), this becomes
\[
\sum_i b_i = 3,\qquad \sum_i b_i^2=75,\qquad \sum_i b_i b_{i+t}=-11\ \ (t\neq 0).
\]
Equivalently, every nonprincipal character \(\psi\) of \(C_7\) satisfies
\[
\left|\sum_i b_i\psi(i)\right|^2 = 86.
\]
This compresses the full difference-set problem to an integral 7-variable periodic-autocorrelation problem. If that 7-term system has no solution, the original difference set cannot exist.

Self-check: this route is legitimate because quotienting preserves the summed correlation equations exactly; no hidden search assumption enters yet.

## approach_B
Construction / contradiction route through the quotient \(G/N\cong C_7\times C_7\), where \(N=\langle y^7\rangle\).

Let \(c_q=|D\cap \pi_N^{-1}(q)|\) for \(q\in C_7\times C_7\). Then each fiber has size at most 7, and
\[
\sum_q c_q = 171.
\]
Summing coefficients of \(DD^{(-1)}\) over \(N\)-cosets gives
\[
\sum_q c_q^2 = 171+6\cdot 85 = 681,
\]
and for each nonzero \(t\in C_7\times C_7\),
\[
\sum_q c_q c_{q+t} = 7\cdot 85 = 595.
\]
With \(z_q=c_q-3\), this becomes
\[
\sum_q z_q = 24,\qquad \sum_q z_q^2 = 96,\qquad \sum_q z_q z_{q+t}=10\ \ (t\neq 0),
\]
with each \(z_q\in\{-3,-2,-1,0,1,2,3,4\}\).

This is a sharper but larger obstruction package. It encodes the "Paley shadow" on the elementary-abelian quotient and may expose an incompatibility between 7-bounded fibers and the constant nontrivial autocorrelation \(10\).

Self-check: this route is stronger than Approach A but costlier; it should be used only after the 7-term quotient has been squeezed first.

## lemma_graph
Lemma skeleton currently visible:

1. If \(D\subseteq C_7\times C_{49}\) is a \((343,171,85)\)-difference set, then every nonprincipal character has modulus squared \(86\).
2. Pushing \(D\) to the quotient by \(\langle y\rangle\) yields a 7-term integer vector \(a=(a_0,\dots,a_6)\) with
\[
\sum a_i=171,\quad \sum a_i^2=4251,\quad \sum a_i a_{i+t}=4165\ (t\neq 0).
\]
3. Centering by \(a_i=24+b_i\) yields a 7-term integer vector \(b\) with
\[
\sum b_i=3,\quad \sum b_i^2=75,\quad \sum b_i b_{i+t}=-11\ (t\neq 0).
\]
4. Therefore any existence proof or nonexistence proof must pass through a highly constrained length-7 periodic-autocorrelation instance.
5. If the 7-term system is soluble, then the 49-term quotient system on \(G/N\) is the next obstruction layer.

The small theorem slice already visible is:
"Any \((343,171,85)\)-difference set in \(C_7\times C_{49}\) induces a 7-term centered coset-count vector with constant nontrivial periodic autocorrelation \(-11\)."

## chosen_plan
Best path: squeeze the \(C_7\)-quotient first.

Reason:

1. It is the cheapest exact obstruction layer.
2. It already yields a paper-facing theorem slice even if the full group case remains open.
3. A tiny bounded experiment on the resulting 7-variable system is justified after the structural reductions are recorded.

If the 7-term system is impossible, we get a clean nonexistence theorem. If it has only a few integer solutions, those become the interface data for the \(C_7\times C_7\) quotient.

## self_checks
1. The active slug is `abelian-difference-set-343-171-85-group-7-49`, and the active title is the exact group-existence question for \(C_7\times C_{49}\).
2. No handoff memo path was present in the active selection file, so the canonical artifact files remain in scope.
3. The current reasoning stays inside the exact group row and does not drift into parameter-only claims.
4. A bounded 7-variable search was used only after the quotient equations were derived on paper.
5. The search output was checked against the exact equations \(\sum b_i=3\), \(\sum b_i^2=75\), and \(\sum b_i b_{i+t}=-11\).

## code_used
A tiny bounded integer search on the 7-term quotient system was used.

Scope only:

1. enumerate all integer 7-tuples \(b_i\) with \(\sum b_i=3\) and \(\sum b_i^2=75\);
2. retain only those with periodic autocorrelation \(-11\) for each nonzero shift;
3. quotient the survivors by cyclic shift and reversal.

Outcome:

- 112 oriented solutions,
- 8 orbits up to shift and reversal.

Orbit representatives for \(b\), with the corresponding coset counts \(a=b+24\), are:

1. \(b=(-6,-2,3,0,3,1,4)\), \(a=(18,22,27,24,27,25,28)\)
2. \(b=(-6,-1,5,0,3,0,2)\), \(a=(18,23,29,24,27,24,26)\)
3. \(b=(-6,0,0,-1,2,3,5)\), \(a=(18,24,24,23,26,27,29)\)
4. \(b=(-6,0,2,5,0,-1,3)\), \(a=(18,24,26,29,24,23,27)\)
5. \(b=(-6,0,4,3,1,-2,3)\), \(a=(18,24,28,27,25,22,27)\)
6. \(b=(-6,1,0,-2,4,3,3)\), \(a=(18,25,24,22,28,27,27)\)
7. \(b=(-3,-3,0,4,4,-3,4)\), \(a=(21,21,24,28,28,21,28)\)
8. \(b=(-3,-3,2,-3,2,2,6)\), \(a=(21,21,26,21,26,26,30)\)

## result
Best current result: the first quotient obstruction has been completely classified.

For any subgroup \(H\le G\) of order \(49\), if \(a_0,\dots,a_6\) are the intersection counts of a hypothetical \((343,171,85)\)-difference set with the seven cosets of \(H\), then after centering \(b_i=a_i-24\) one has
\[
\sum b_i=3,\qquad \sum b_i^2=75,\qquad \sum b_i b_{i+t}=-11\ \ (t\neq 0)
\]
and, up to cyclic shift and reversal, exactly eight such 7-tuples exist.

So the \(C_7\)-quotient does not by itself prove nonexistence. It does, however, shrink the row-profile possibilities to a finite explicit list.

Self-check: this is a real finite obstruction theorem, not merely an informal heuristic. It still falls short of the exact existence/nonexistence statement.

## family_affinity
High. This sits exactly on the group-sensitive Paley-parameter lane: the parameters already occur in the Paley group \(C_7^3\), so any proof here must isolate what changes when one \(C_7\) factor thickens to \(C_{49}\).

## generalization_signal
Moderate. What scales is the reduction from a difference-set identity to explicit line-sum autocorrelation constraints in low-order quotients. What does not yet scale is the final closure step: the eight surviving line-profile orbits are specific to the exact constants \(171,85\) and still need a second obstruction layer.

## proof_template_reuse
Reusable template:

1. choose the largest cyclic \(p^2\)-factor;
2. push to the \(p\)-quotient and the maximal elementary-abelian quotient;
3. convert the difference-set identity into exact fiber autocorrelation equations;
4. isolate short integral sequences whose existence is necessary for the full group case;
5. classify those sequences exactly before spending effort on the larger quotient.

## candidate_theorem_slice
Current best slice:
"If \(D\subseteq C_7\times C_{49}\) is a \((343,171,85)\)-difference set and \(H\le G\) has order \(49\), then the seven coset intersection counts of \(D\) with respect to \(H\) lie, up to cyclic shift and reversal, in one of exactly eight explicit patterns."

This is a theorem-shaped supporting slice, not yet the title theorem.

## smallest_param_shift_to_test
The best next shift is still group-shape, not parameter-shape:

1. keep \((343,171,85)\) fixed and compare the eight allowed line profiles against the known Paley realization in \(C_7^3\);
2. then test compatibility of those same profiles with the \(49\)-fiber quotient \(G/\langle y^7\rangle\cong C_7^2\).

Those two checks should reveal what is genuinely exponent-\(49\)-specific.

## why_this_is_or_is_not_publishable
If the main claim closes, yes: this is already roughly 80% of a paper. The exact title theorem is the group-specific existence or nonexistence statement for \(C_7\times C_{49}\). Minimal remaining packaging would be a short literature positioning paragraph, the explicit quotient/character argument, and one comparison remark against the known Paley realization in \(C_7^3\).

At the current stage the package is closer to paper-shaped than a vague partial attempt, because the first obstruction layer is now finitely classified. But it is still too thin for the micro-paper lane: the current result is a supporting theorem slice, not the title theorem.

## paper_shape_support
If the nonexistence route works, the natural paper shape is:

1. derive the 7-term quotient obstruction;
2. show the obstruction has no integral realization (or no realization compatible with the 49-fiber quotient);
3. conclude nonexistence in \(C_7\times C_{49}\);
4. contrast with the Paley realization in \(C_7^3\).

One immediate corollary / remark, if the nonexistence route closes, would be that the same parameter set \((343,171,85)\) is group-sensitive inside the abelian category, with \(C_7^3\) admissible but \(C_7\times C_{49}\) excluded.

At the present partial stage, the natural boundary remark is weaker: every order-49 quotient of a hypothetical solution must exhibit one of eight explicit line profiles, so any final contradiction now has to come from compatibility between line directions, not from a single quotient alone.

## boundary_remark
The current argument does not yet rule out existence. What scales is the quotient-fiber rigidity: every index-7 quotient sees one of eight explicit profiles. What does not yet scale is the global compatibility problem across the full \(C_7\times C_7\) quotient. So the current package is still an instance-level structural slice, though materially closer to a paper-shaped claim than an unstructured partial.

## likely_failure_points
1. The 7-term quotient system may actually have integral solutions, so the first obstruction might stop short of contradiction.
2. Even with only eight orbit types surviving, lifting line profiles to a full \(49\)-fiber configuration may still be nontrivial.
3. Because the parameters already exist in \(C_7^3\), any successful contradiction must use exponent-\(49\) structure somewhere, not just parameter arithmetic.

## what_verify_should_check
1. Recheck the quotient-correlation derivations from the group-ring identity.
2. Confirm that the centered 7-term system is stated with the correct constants \(24, 75, -11\).
3. Confirm independently that the bounded search really yields 112 oriented solutions and 8 shift/reversal orbits.
4. If a contradiction is later claimed, verify that it genuinely uses \(C_7\times C_{49}\) and not only the parameters \((343,171,85)\).
5. If a later bounded search is used on the \(49\)-fiber quotient, verify that it enforces only genuine consequences of the group-ring equations.

## verify_rediscovery
Bounded prior-art audit outcome: rediscovery established.

Evidence checked:

1. Gordon-Schmidt's survey table records the exact row \((343,171,85)\) in group \([7,49]\) as open.
2. Gordon's 2019 La Jolla repository slides still list `343 171 85 [7,49]` among open existence cases.
3. A later primary-source preprint, Yinan Huang, "Forbidden multipliers in abelian difference sets" (arXiv:2511.10231, posted November 13, 2025), explicitly states in its Table 1 that \((343,171,85)\) in \(C_7\times C_{49}\) is ruled out by Theorems 1 and 7.

Conservative verifier reading: the exact intended statement for this packet is no longer frontier-open. The exact group row appears to have been settled in prior art after the 2019 status check used by curation. Under the verify rules this forces:

- `verify_verdict = REDISCOVERY`
- `classification = REDISCOVERY`
- `publication_status = REDISCOVERY`
- `lean_ready = false`
- `next_action = archive_as_rediscovery`

## verify_faithfulness
The local solve artifact is faithful about its own scope.

Findings:

1. The intended statement is the exact existence question for \((343,171,85)\) in \(C_7\times C_{49}\).
2. The solve record does not falsely claim to settle that title statement.
3. The actual proved slice is narrower: a necessary quotient-profile classification for hypothetical solutions.
4. The record repeatedly marks the output as partial and says explicitly that the argument does not yet prove existence or nonexistence.

So there is no wrong-theorem drift inside the local proof notes. The correction required by verification is classification drift against the literature, not theorem-statement drift inside the artifact.

## verify_proof
No incorrect step was found in the local quotient-slice argument.

Checks:

1. The quotient by an order-49 subgroup gives seven coset counts \(a_i\) with
\[
\sum_i a_i = 171,\qquad \sum_i a_i^2 = 171 + 48\cdot 85 = 4251,
\]
and, for each nonzero shift \(t\),
\[
\sum_i a_i a_{i+t} = 49\cdot 85 = 4165.
\]
These are the standard coefficient-summing consequences of \(DD^{(-1)} = 171 + 85(G-1)\).
2. Centering by \(a_i = 24 + b_i\) is correct because \(171 = 7\cdot 24 + 3\), giving
\[
\sum_i b_i = 3,\qquad \sum_i b_i^2 = 75,\qquad \sum_i b_i b_{i+t} = -11 \ \ (t\neq 0).
\]
3. No hidden step was found between the quotient identities and the centered autocorrelation system.

The main limitation is not correctness but scope: this proof only yields a necessary condition for any hypothetical difference set.

## verify_adversarial
Independent rerun confirms the stated finite classification.

Adversarial checks performed:

1. Re-enumerated all integer 7-tuples satisfying
\[
\sum b_i = 3,\qquad \sum b_i^2 = 75,\qquad \sum_i b_i b_{i+t} = -11 \ \ (t=1,\dots,6),
\]
using a fresh backtracking script.
2. Verified the solver's counts exactly:
   - `112` oriented solutions
   - `8` dihedral orbits up to cyclic shift and reversal
3. Verified that the eight orbit representatives listed in the record are correct.

No persistent checker file existed in the artifact directory, so there was no saved program to rerun verbatim. The independent rerun still supports the local slice.

## verify_theorem_worthiness
Assessment after skeptical checking:

1. Exactness: the local slice is exact as a necessary-condition theorem, but it is not the title theorem.
2. Novelty: the title problem is no longer novel because the exact \([7,49]\) row appears already ruled out in 2025 prior art.
3. Reproducibility: good for the local slice; the quotient derivation is short and the finite classification reruns cleanly.
4. Lean readiness: no. Lean is not the shortest remaining path because the frontier claim is already settled in the literature.
5. Paper leverage: the local slice now has low frontier leverage. By itself it is a supporting lemma, not a publishable micro-paper packet.

Explicit answers:

- Would this result, if correct and Lean-sealed, already constitute most of a publishable note? No. After the rediscovery finding, the local slice is supporting material rather than the title theorem of a fresh note.
- What percentage of the paper would one solve already provide? About 10-20% at most for the surviving local slice; effectively 0% toward a new frontier note on the original exact row because that note has already been claimed in prior art.
- What title theorem is actually visible? "Any hypothetical \((343,171,85)\)-difference set in \(C_7\times C_{49}\) has, along every order-49 quotient, one of exactly eight explicit coset-count profiles."
- What part of the argument scales? The quotient-fiber reduction from the group-ring identity to short periodic-autocorrelation constraints.
- What part clearly does not? The closure step from explicit line profiles to a full group nonexistence theorem.
- Is the best honest publication status still only `INSTANCE_ONLY` or even `NONE`? For the original packet it is `REDISCOVERY`; for the surviving local slice alone the honest standalone paper status is at best `NONE`.

## verify_verdict
`REDISCOVERY`

Reason: the exact intended statement appears already settled by prior art, while the local artifact only proves a narrower supporting quotient-profile classification.

## minimal_repair_if_any
No mathematical repair was needed for the local quotient slice.

The minimal conservative repair is archival:

1. reclassify the packet from `PARTIAL` to `REDISCOVERY`;
2. set publication status to `REDISCOVERY`;
3. preserve the quotient-profile classification as a supporting artifact only;
4. route the slug to `archive_as_rediscovery`.
