# Solve Record: On the (909,228,57) Difference-Set Problem in C_3 x C_303

- slug: `abelian-difference-set-909-228-57-group-3-303`
- working_packet: `artifacts/abelian-difference-set-909-228-57-group-3-303/working_packet.md`

## statement_lock
Determine whether the abelian group C_3 x C_303 admits a (909,228,57)-difference set.

## definitions
Write the group additively as
\[
G \cong C_3 \times C_{303} \cong C_3^2 \times C_{101}=:N\times K,
\]
with \(|N|=9\), \(|K|=101\), \(v=909\), \(k=228\), \(\lambda=57\), and order
\[
n=k-\lambda=171=3^2\cdot 19.
\]
If \(D\subseteq G\) is a \((909,228,57)\)-difference set, then in the group ring
\[
DD^{(-1)}=171\cdot 1_G+57\cdot G.
\]
The source packet records the standard multiplier input for this row: \(19\) is the relevant numerical multiplier. I use this as the external lemma imported from the Gordon-Schmidt lane. Thus there exists \(g\in G\) such that
\[
D^{(19)}=g+D.
\]
Equivalently, \(D\) is a union of orbits of the affine permutation
\[
F(x)=19x-g.
\]
Self-check: the solve turns entirely on the source-level multiplier premise; verify must confirm that premise exactly for this row.

## approach_A
Structural / invariant route.

1. Decompose \(G=N\times K\) with \(N\cong C_3^2\) and \(K\cong C_{101}\).
2. Study the affine action \(F(x)=19x-g\).
   On \(N\), multiplication by \(19\) is the identity because \(19\equiv 1\pmod 3\), so the \(N\)-part of \(F\) is translation by a fixed \(a\in N\).
   On \(K\), \(F\) is \(q\mapsto 19q-b\), an affine map conjugate to multiplication by \(19\).
3. Since \(19^5\equiv 84\not\equiv 1\pmod{101}\) and \(19^{25}\equiv 1\pmod{101}\), the order of \(19\) in \((\mathbf Z/101\mathbf Z)^\times\) is \(25\).
   Hence on \(K\), \(F\) has exactly one fixed point and four cycles of length \(25\).
4. Project \(D\) to the quotient \(G/K\cong N\) and use the group-ring identity to force
\[
\sum_{n\in N} c_n=228,\qquad \sum_{n\in N} c_n^2=171+57\cdot 101=5928,
\]
where \(c_n:=|D\cap (n+K)|\).
5. Combine the orbit-shape constraints from \(F\) with the quadratic identity above. This gives a short Diophantine contradiction in both cases \(a=0\) and \(a\neq 0\).

Self-check: this route is theorem-facing and does not require search; the only imported ingredient is the multiplier premise.

## approach_B
Construction / contradiction route.

1. Project instead to \(G/N\cong C_{101}\). Let \(a_q:=|D\cap (N+q)|\).
2. The affine \(19\)-action on \(C_{101}\) has one fixed coset and four \(25\)-cycles, so
\[
228=\sum_q a_q = x+25(y_1+y_2+y_3+y_4),
\]
forcing \(x=3\) for the distinguished coset.
3. The quotient identity
\[
\sum_q a_q^2 = 171+57\cdot 9 = 684
\]
then gives
\[
3^2+25(y_1^2+y_2^2+y_3^2+y_4^2)=684,
\]
so \(y_1^2+\cdots + y_4^2=27\) and \(y_1+\cdots + y_4=9\). This forces the multiset \(\{y_i\}=\{3,3,3,0\}\).
4. This heavily restricts the shape of \(D\) across the \(101\)-quotient, but I do not yet see a contradiction from these data alone without reintroducing the \(N\)-projection.

Self-check: approach B gives a sharp occupancy profile and is useful as a cross-check, but by itself it does not yet close the row.

## lemma_graph
Lemma skeleton.

1. Source multiplier lemma:
   \(19\) acts as a numerical multiplier for the row \((909,228,57)\) in \(C_3\times C_{303}\).
2. Orbit lemma on \(K\):
   the affine map \(q\mapsto 19q-b\) on \(C_{101}\) has one fixed point and four \(25\)-cycles.
3. Orbit lemma on \(N\):
   the \(N\)-part of \(F\) is translation by \(a\in C_3^2\), so its orbits have size \(1\) if \(a=0\), otherwise size \(3\).
4. Quotient energy lemma:
   for \(c_n=|D\cap (n+K)|\),
   \[
   \sum c_n=228,\qquad \sum c_n^2=5928.
   \]
5. Case split.
   If \(a=0\), each \(c_n\) has the form \(25u_n+\varepsilon_n\) with \(\sum u_n=9\), \(\sum \varepsilon_n=3\), contradicting the energy lemma.
   If \(a\neq 0\), the three translation orbits on \(N\) force a coarser form \(25m_i+\delta_{i,j}\), again contradicting the energy lemma.
6. Conclude nonexistence.

Self-check: every node after Lemma 1 is elementary.

## chosen_plan
Choose approach A.

Reason:
- it produces a direct nonexistence proof using only the imported multiplier fact plus elementary orbit counting;
- it naturally yields a paper-shaped title theorem;
- it keeps code off.

Planned title theorem:

“The abelian group \(C_3\times C_{303}\cong C_3^2\times C_{101}\) admits no \((909,228,57)\)-difference set.”

If this proof is sound, a successful solve would already be about 80-90% of a short paper. The remaining packaging is just: cite the precise multiplier theorem used for \(19\), explain why the row survived the published filters, and polish the two-case orbit count.

Self-check: the plan remains inside the exact row and does not drift into a broader campaign.

## self_checks
- Statement lock check:
  the intended theorem remains the exact [3,303] row and not a broader family claim.
- Imported-input check:
  the proof uses only one external mathematical input beyond routine difference-set identities: the source-level assertion that \(19\) is a numerical multiplier here.
- Orbit check:
  the order computation on \(C_{101}\) is explicit: \(19^5\equiv 84\neq 1\) and \(19^{25}\equiv 1\pmod{101}\), so the nontrivial orbit length is \(25\).
- Quotient check:
  the coefficient-of-identity formula after quotienting by \(K\) is \(171+57|K|=171+5757=5928\).
- Conservatism check:
  until verify confirms the multiplier premise and audits the affine-action formalism, this should be treated as a strong solver-stage disproof candidate, not yet a final exact closure.

## code_used
No code used. The attempt stayed reasoning-first and did not need search or a checker.

## result
Provisional theorem claim.

Assuming the source packet’s multiplier input is correct, there is no \((909,228,57)\)-difference set in \(C_3\times C_{303}\).

Proof attempt.

Assume \(D\subseteq G=N\times K\) is a \((909,228,57)\)-difference set, with \(N\cong C_3^2\) and \(K\cong C_{101}\). Import the source-level multiplier fact: \(19\) is a numerical multiplier for this row, so \(D^{(19)}=g+D\) for some \(g=(a,b)\in N\times K\). Therefore \(D\) is a union of orbits of
\[
F(n,q)=(n+a,\ 19q+b')
\]
for a suitable \(b'\in K\) after changing sign convention.

On \(K\), the affine map \(q\mapsto 19q+b'\) has exactly one fixed point \(q_*\), because \(1-19\) is invertible mod \(101\). Since \(19\) has multiplicative order \(25\) modulo \(101\), every other orbit on \(K\) has length \(25\).

Now project to \(N\). For each \(n\in N\), let
\[
c_n := |D\cap (n+K)|.
\]
Applying the quotient map \(G\to N\) to
\[
DD^{(-1)}=171\cdot 1_G+57\cdot G
\]
gives
\[
\left(\sum_{n\in N} c_n n\right)\left(\sum_{n\in N} c_n n\right)^{(-1)}
=171\cdot 1_N +57\cdot 101\,N.
\]
Hence
\[
\sum_{n\in N} c_n=228,\qquad \sum_{n\in N} c_n^2 =171+57\cdot 101=5928.
\]

Case 1: \(a=0\).

Then \(F\) fixes each \(n\in N\), so above the unique fixed point \(q_*\in K\) there are \(9\) fixed points of \(F\), one in each \(K\)-coset, and away from \(q_*\) all orbits have length \(25\). Because \(|D|=228\equiv 3\pmod{25}\), \(D\) contains exactly \(3\) fixed points and \(9\) orbits of length \(25\). Therefore for each \(n\in N\),
\[
c_n = 25u_n+\varepsilon_n,
\]
with \(u_n\in\{0,1,2,3,4\}\), \(\varepsilon_n\in\{0,1\}\), and
\[
\sum u_n=9,\qquad \sum \varepsilon_n=3.
\]
Using \(\sum c_n^2=5928\),
\[
5928=\sum (25u_n+\varepsilon_n)^2
=625\sum u_n^2 +50\sum u_n\varepsilon_n +\sum \varepsilon_n.
\]
Write \(q=\sum u_n^2\) and \(s=\sum u_n\varepsilon_n\). Since \(\sum \varepsilon_n=3\),
\[
625q+50s =5925,
\qquad\text{so}\qquad
25q+2s=237.
\]
But \(\sum u_n=9\) with nine nonnegative integers implies \(q\ge 9\), with equality only when every \(u_n=1\). Since \(2s\le 18\), the last equation forces \(q=9\) and \(s=6\). Equality \(q=9\) gives \(u_n=1\) for all \(n\), hence \(s=\sum \varepsilon_n=3\), contradiction.

Case 2: \(a\neq 0\).

Translation by \(a\) on \(N\cong C_3^2\) has exactly three orbits, each of size \(3\). Over the fixed point \(q_*\in K\), the affine map \(F\) therefore has three \(3\)-cycles. Over each \(25\)-cycle in \(K\), it has orbits of size \(\mathrm{lcm}(3,25)=75\). Since \(228\equiv 3\pmod{75}\), \(D\) must be the union of exactly one \(3\)-cycle and exactly three \(75\)-cycles.

Let the three translation orbits on \(N\) be \(O_1,O_2,O_3\). For each \(i\), let \(m_i\) be the number of chosen \(75\)-cycles supported on \(O_i\); then
\[
m_1+m_2+m_3=3.
\]
Exactly one of the three \(O_i\) also contributes the chosen \(3\)-cycle. So there is an index \(j\) such that
\[
c_n = 25m_i+\delta_{i,j}\qquad (n\in O_i).
\]
Therefore
\[
5928=\sum_{n\in N} c_n^2
=3\sum_{i=1}^3 (25m_i+\delta_{i,j})^2
=3\left(625\sum m_i^2 +50m_j +1\right).
\]
Hence
\[
625\sum m_i^2 +50m_j +1 =1976,
\qquad\text{so}\qquad
25\sum m_i^2 +2m_j =79.
\]
Because \(m_1+m_2+m_3=3\), we have \(\sum m_i^2\ge 3\), with equality only for \((m_1,m_2,m_3)=(1,1,1)\). The displayed equation forces \(\sum m_i^2=3\) and \(m_j=2\), but equality \(\sum m_i^2=3\) implies \(m_j=1\). Contradiction.

Both cases contradict the difference-set equations. Therefore no such \(D\) exists.

Conclusion:
the active best attempt is a rigorous nonexistence proof modulo one source-dependent checkpoint, namely confirmation that \(19\) is indeed a numerical multiplier for this exact row.

## family_affinity
High affinity with “residual-row nonexistence by multiplier orbit compression” problems in abelian difference-set tables, especially groups of the form \(p^2\times q\) where the multiplier acts trivially on the small \(p\)-part and with moderate order on the large prime quotient.

## generalization_signal
The part that scales is the template:

1. isolate a source-certified multiplier \(t\),
2. split \(G\) as “small part fixed by \(t\)” times “large part with long \(t\)-orbits,”
3. project to the fixed small quotient,
4. combine orbit-congruence information with the quotient square-sum identity.

The part that does not automatically scale is the final Diophantine contradiction: here it works because the \(9\)-point quotient and the \(25\)-orbit length force an unusually rigid decomposition.

## proof_template_reuse
Reusable template:

- use an affine-multiplier action rather than insisting on a literally fixed set;
- classify orbit sizes on each direct factor separately;
- push the difference-set equation through a quotient to get \(\sum c_i\) and \(\sum c_i^2\);
- encode orbit membership as \(c_i=Lu_i+\varepsilon_i\) with \(L\) the long orbit length;
- force an impossible Diophantine identity.

This is a realistic proof template for other exact survey rows with the same “one short orbit plus long cycles” geometry.

## candidate_theorem_slice
Candidate theorem slice visible from this solve:

If the Gordon-Schmidt multiplier input gives a numerical multiplier \(t\) for an abelian \((v,k,\lambda)\)-difference set in \(G=N\times K\), where \(t\) acts trivially on \(N\cong C_3^2\) and with order \(25\) on \(K\cong C_{101}\), then the quotient-square identities on \(N\) can obstruct existence. The present row is the cleanest exact instance of that slice.

## smallest_param_shift_to_test
Most informative next shifts:

1. another exact \(C_3^2\times C_p\) residual row where the certified multiplier has one fixed point and \(25\)-cycles on the \(p\)-part;
2. the same orbit template with a nearby small fixed quotient size, to see whether the contradiction survives when \(|N|\neq 9\).

These would test whether the current proof is an isolated arithmetic coincidence or the first member of a small theorem family.

## why_this_is_or_is_not_publishable
If verify confirms the multiplier premise, this is close to publishable in the strict micro-paper lane.

- Exact title theorem:
  “\(C_3\times C_{303}\) admits no \((909,228,57)\)-difference set.”
- Solve-to-paper fraction:
  about 0.85. The mathematics is already the title theorem of a short note.
- Minimal remaining packaging:
  cite the precise multiplier theorem or table entry that certifies \(19\), add 1-2 paragraphs explaining why the row survived prior filters, and polish the two-case affine-orbit proof.
- Immediate natural remark:
  the obstruction comes from the mismatch between the \(25\)-orbit geometry on the \(101\)-part and the \(9\)-point quotient energy identity on the \(3^2\)-part.

If the multiplier premise turns out to be weaker than assumed, the current package becomes too thin for publication, because the whole contradiction rests on that orbit structure.

## publication_prior_art_audit
Bounded prior-art pass completed on 2026-04-15.

- Exact-statement search: web searches for `(909,228,57)` together with `C_3 x C_303` or `difference set` surfaced the Gordon-Schmidt survey, but no later paper or note directly settling this exact row.
- Alternate-notation search: bounded searches using `[3,303]` and `Z_3 x Z_303` likewise surfaced no direct later settlement of the exact group case.
- Canonical source check: in Gordon-Schmidt, *A Survey of the Multiplier Conjecture*, Table 2 lists `909 228 57 [3,303]` among the open difference-set parameters, with `19` shown in the `MC primes` column. The table legend explains that this column tracks prime divisors of `n` relative to multiplier status, with special marking when the multiplier obligation is unknown or impossible.
- Canonical-source theorem/proposition/example/corollary/observation check: in the bounded read of the survey, I found the exact row only as a Table 2 residue. I did not find a separate theorem, proposition, corollary, observation, or worked example in the survey already settling `[3,303]`.
- Outside-source status pass: the La Jolla Difference Set Repository presents itself as a maintained database of possible/open/existence results for difference sets and points to multiplier-conjecture computations, but the bounded exact-row search surfaced no direct repository page or later publication resolving `(909,228,57)` in `[3,303]`.

Audit verdict: no rediscovery surfaced in the bounded pass. This is still an inference from a narrow exact-row search and should not be overstated as a full literature guarantee.

Source anchors used in this audit:
- Daniel M. Gordon and Bernhard Schmidt, *A Survey of the Multiplier Conjecture*, Table 2 and the table legend.
- La Jolla Difference Set Repository, status/search landing page.

## publication_statement_faithfulness
The solver packet stays locked to the intended exact statement and does not drift into a broader family claim. The argument targets the precise row `(909,228,57)` in `C_3 x C_303`, using the decomposition `C_3^2 x C_101` and an orbit/quotient obstruction.

The main faithfulness issue is not theorem drift but premise anchoring. The proof imports the claim that `19` is a certified multiplier for this exact row from the Gordon-Schmidt lane. The canonical source materially supports that import via Table 2 plus the `MC primes` legend, but the packet still does not pin a theorem number or explicit local derivation of that multiplier fact. Because this stage is publication audit rather than re-verify, the strongest honest claim remains conditional on that source anchor being accepted exactly as cited.

## publication_theorem_worthiness
This is stronger than “here is an example.” Even at current bounded confidence, the packet presents a conditional exact-row nonexistence theorem, not a construction anecdote or a hand-picked small-case observation.

There is a real title theorem here:

`C_3 x C_303` admits no `(909,228,57)`-difference set.

The proof idea is structural rather than brute-force instance checking. It uses affine multiplier orbits on `C_3^2 x C_101` and quotient square-sum identities, so the obstruction has recognizable theorem content. It is still arithmetic-specific to one row, but it is not merely a computation on tiny cases.

A referee asking “what is the theorem?” would get a clean answer if the multiplier premise is pinned cleanly. Without that citation anchor, the referee’s first objection would be immediate: is the theorem unconditional, or only conditional on a table convention? That objection is small but load-bearing.

## publication_publishability
If the multiplier premise is pinned as an unconditional source input, this result would already constitute most of a publishable note. The exact survey row already supplies the title-theorem slot, the literature gap sentence, and the short-note narrative. On mathematical content, one solve would provide roughly 70-80% of the paper.

At current audit resolution, the packet is not yet `PAPER_READY`. The remaining gap is genuinely small, but it is not cosmetic: the packet still hinges on a citation-sensitive multiplier premise that should be closed in verify before the result is treated as a human-ready publication packet.

This candidate did not merely look attractive before audit. The audit still sees a legitimate micro-paper target with a real theorem slice and low editorial overhead. The correct next move is to close the citation hinge and rerun the exact theorem audit, not to grow the target into a broader theorem program.

If the source anchor for the multiplier cannot be made explicit, this row should be moved aside as a conditional variant rather than expanded.

## publication_packet_audit
Proof artifacts are preserved well enough for continued work. The record contains the full two-case structural contradiction, the intended title theorem, the packaging notes, and the explicit point of dependence.

Current packet quality: strong conditional theorem packet with a small citation gap.

Lean would not directly seal the intended theorem today. At present it would only formalize a citation-conditional statement, so Lean remains optional later polish rather than an immediate stop condition.

Human-ready verdict: not yet. This should remain below `PAPER_READY` until the multiplier input is pinned in a way that verify is willing to treat as unconditional.

## micro_paper_audit
MICRO-PAPER verdict: still viable.

- Is the strongest honest claim stronger than an example? Yes.
- Would one correct solve already constitute most of a publishable note? Yes, provided the multiplier premise is made unconditional.
- What percentage of the paper would one solve already provide? About `0.72` at current packet quality.
- Is there a real theorem slice? Yes: an exact-row nonexistence theorem driven by multiplier-orbit compression.
- Is the claim too dependent on hand-picked small cases? No; it is exact-row specific, but the proof method is structural.
- If not yet paper-ready, is the gap genuinely small? Yes.
- Should it be moved aside rather than expanded if that gap cannot be closed? Yes.
- Would Lean directly seal the packet? Not yet; Lean is secondary after the citation hinge is closed.

## strongest_honest_claim
Conditional exact-row theorem: assuming the Gordon-Schmidt Table 2 / `MC primes` convention indeed certifies `19` as a known multiplier for the `[3,303]` row, the affine-orbit and quotient-energy argument rules out a `(909,228,57)`-difference set in `C_3 x C_303`.

## paper_title_hint
On the Nonexistence of a `(909,228,57)` Difference Set in `C_3 x C_303`

## next_action
Pin the multiplier input to an explicit Gordon-Schmidt source anchor that verify will accept as unconditional, then rerun verify/publication audit on the exact nonexistence theorem. If that anchor cannot be made explicit, freeze this packet as a conditional variant and move on rather than enlarging the theorem program.

## verify_rediscovery
Limited PASS 1 web audit found the canonical Gordon-Schmidt survey row and Gordon's live difference-set repository entry for the exact parameter set, but no later source that settles the exact row in \(C_3\times C_{303}\). I therefore do not mark this as a rediscovery.

The audit also did not produce a source-level confirmation, within budget, of the stronger local premise used in the solve record: namely that \(19\) is already a certified numerical multiplier for this exact row rather than merely the prime recorded in the survey's multiplier-conjecture metadata. That is a citation-risk issue, not a rediscovery.

## verify_faithfulness
The intended statement is the exact row:

\[
\text{``\(C_3\times C_{303}\) admits no \((909,228,57)\)-difference set.''}
\]

The solver's argument is faithful to that target only after importing the unpinned premise

\[
D^{(19)}=g+D.
\]

Because the current packet does not cite the exact source theorem, proposition, or table convention that makes this implication valid for the active row, the strongest honest locally verified claim is weaker:

\[
\text{If \(19\) is a certified numerical multiplier for this exact row, then no such difference set exists.}
\]

So the run does not presently verify the intended statement itself; it verifies a nearby conditional variant.

## verify_proof
Granting the multiplier premise, I do not find an internal mathematical error in the orbit-count proof.

- The decomposition \(G\cong C_3^2\times C_{101}\) and the quotient identities
  \[
  \sum c_n=228,\qquad \sum c_n^2=171+57\cdot 101=5928
  \]
  are correct.
- On \(C_{101}\), the affine action induced by multiplication by \(19\) has one fixed point and four \(25\)-cycles because \(19\) has order \(25\) modulo \(101\).
- In the case \(a=0\), the Diophantine contradiction is valid.
- In the case \(a\neq 0\), the \(3\)-cycle/\(75\)-cycle bookkeeping and final contradiction are also valid.

The first blocking step is therefore the uncited import of the multiplier lemma. I do not find a later internal mistake before that dependency becomes decisive.

## verify_adversarial
No checker or solver code existed, so PASS 4 reduced to skeptical recomputation.

- Recomputed the quotient-square identity: \(\sum c_n^2=5928\).
- Rechecked the modular-order claim: \(19^{25}\equiv 1\pmod{101}\) and the order is \(25\).
- Rechecked the case \(a=0\) contradiction: the constraints force \(q=9\) and then \(s=3\), giving \(25q+2s=231\neq 237\).
- Rechecked the case \(a\neq 0\) contradiction directly: there is no triple \((m_1,m_2,m_3)\) with \(m_1+m_2+m_3=3\) satisfying \(25\sum m_i^2+2m_j=79\).

I was not able to break the proof after assuming the multiplier input. The adversarial failure mode is still the same one: the packet never pins down the exact source mechanism that licenses the affine \(19\)-action in the first place.

## verify_theorem_worthiness
Exactness:
Not yet exact as a verified artifact. The current record supports only a conditional row-specific nonexistence theorem.

Novelty:
The bounded rediscovery audit did not locate a prior settlement of the exact row.

Reproducibility:
Moderate. Once the multiplier premise is cited exactly, the rest of the argument is short and reproducible.

Lean readiness:
No. Lean would currently formalize a conditional argument, not the intended exact theorem.

Paper leverage:
Potentially high if the multiplier citation is locked; currently below publication threshold because the load-bearing premise is still documentary rather than verified.

Explicit answers:

- Would this result, if correct and Lean-sealed, already constitute most of a publishable note?
  Yes, but only after the multiplier premise is source-locked. In that repaired state it would likely supply about 75-85% of a short note.
- What percentage of the paper would one solve already provide?
  In the repaired state, about \(0.8\). In the current verified state, materially less, because the main theorem is still conditional.
- What title theorem is actually visible?
  The visible theorem is conditional: if \(19\) is a certified numerical multiplier for the exact \((909,228,57)\) row in \(C_3\times C_{303}\), then the group admits no such difference set.
- What part of the argument scales?
  The affine-multiplier plus quotient-energy template plausibly scales to nearby residual rows with the same \(C_3^2\times C_p\) orbit geometry.
- What part clearly does not?
  The row-specific multiplier certification and the final rigid Diophantine numerology do not automatically scale.
- Is the best honest publication status still only `INSTANCE_ONLY` or even `NONE`?
  Even `NONE` for the current verified packet, because the exact intended theorem is not yet source-anchored.

## verify_verdict
`VARIANT`

Reason:
the solver produced a strong conditional nonexistence argument, but the packet does not yet verify the exact intended theorem because the source-dependent \(19\)-multiplier premise is not pinned to an exact citation.

## minimal_repair_if_any
No mathematical repair was applied.

The minimal conservative repair is documentary:

1. cite the exact source theorem / proposition / table convention showing that \(19\) is a valid numerical multiplier for this exact row in \(C_3\times C_{303}\), or
2. rewrite the theorem claim honestly as the conditional variant above and send it back to solve rather than treating the row as settled.

## paper_shape_support
This solve attempt does produce paper shape if it survives verification.

- The exact row already reads like a title theorem.
- The proof is short, self-contained after the multiplier citation, and not search-heavy.
- One clean supporting slice is immediate:
  a quotient-energy lemma for affine multiplier orbits in \(C_3^2\times C_{101}\).
- One boundary remark is immediate:
  the published multiplier machinery does not itself kill the row; the extra obstruction comes from combining that machinery with quotient occupancy identities.

On present evidence the result is not “just some witness”; it is an exact nonexistence theorem candidate.

## boundary_remark
Boundary remark.

The contradiction is not a generic no-go theorem for all \((909,228,57)\) groups or all \(p^2\times q\) groups. It specifically exploits:

- the imported \(19\)-multiplier input,
- the fact that \(19\equiv 1\pmod 3\),
- the fact that \(19\) has order \(25\) modulo \(101\),
- the tiny quotient size \(|C_3^2|=9\).

So the argument currently lands as a strong exact-row closure with a plausible small family extension, not yet as a broad theorem.

## likely_failure_points
Likely failure points for verification:

1. confirm from the cited source that \(19\) is indeed a valid numerical multiplier for this exact row and exact group;
2. check the sign convention in passing from \(D^{(19)}=g+D\) to an affine-invariant orbit decomposition;
3. audit the quotient group-ring identity carefully, especially the coefficient \(57\cdot 101\);
4. ensure that the orbit decomposition in the \(a\neq 0\) case really gives only one \(3\)-cycle and three \(75\)-cycles, with no hidden shorter affine orbits.

## what_verify_should_check
Verify should check, in order:

1. the exact source theorem / table mechanism that certifies \(19\) as a multiplier here;
2. the modular order computation \(\mathrm{ord}_{101}(19)=25\);
3. the affine orbit classification on \(C_{101}\) and on \(C_3^2\);
4. the quotient-to-\(N\) square-sum identity \(\sum c_n^2=5928\);
5. the two Diophantine contradictions:
   \(25q+2s=237\) in the \(a=0\) case and
   \(25\sum m_i^2+2m_j=79\) in the \(a\neq 0\) case;
6. whether this already merits `publication_status = PAPER_READY` after novelty audit, since the row-specific note looks short and self-contained if the multiplier citation is solid.
