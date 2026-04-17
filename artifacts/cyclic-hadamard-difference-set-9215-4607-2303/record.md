# Solve Record: Does the cyclic group C_9215 admit a (9215,4607,2303)-difference set?

- slug: `cyclic-hadamard-difference-set-9215-4607-2303`
- working_packet: `artifacts/cyclic-hadamard-difference-set-9215-4607-2303/working_packet.md`

## statement_lock
Let \(G=\mathbb Z/9215\mathbb Z\). The intended claim is:

There does not exist a subset \(D \subset G\) of size \(4607\) such that every nonzero element of \(G\) has exactly \(2303\) representations as \(d_1-d_2\) with \(d_1,d_2 \in D\).

Equivalently, determine whether a cyclic \((9215,4607,2303)\)-difference set exists. Here
\[
v=9215=5\cdot 19\cdot 97,\qquad
k=4607,\qquad
\lambda=2303,\qquad
n=k-\lambda=2304=48^2.
\]

If the answer is negative, the exact title theorem would be:

`The cyclic group C_9215 admits no (9215,4607,2303)-difference set.`

A successful solve would already be about 70-90% of a short paper, because the literature already isolates this exact tuple as a named open cyclic Hadamard survivor and the remaining packaging is mostly exposition plus literature positioning.

## definitions
- Difference-set equation in the group ring:
  \[
  D D^{(-1)} = n + \lambda G.
  \]
  For every nontrivial additive character \(\chi\) of \(G\), this gives
  \[
  |\chi(D)|^2 = n = 2304.
  \]
- Since \(\gcd(n,v)=1\) and \(2,3 \mid n\), the standard numerical multiplier theorem makes \(2\) and \(3\) multipliers.
- Because \(\gcd(2-1,9215)=1\), any translate of a \(2\)-multiplier image can be absorbed. So after translation one may assume \(D\) is fixed by \(x\mapsto 2x\).
- For a quotient \(G \twoheadrightarrow Q\), let \(b_q\) be the number of points of \(D\) in the coset indexed by \(q\in Q\). Then
  \[
  \sum_{q\in Q} b_q = k,\qquad
  \sum_{q\in Q} b_q \psi(q)
  \]
  has squared modulus \(2304\) for every nontrivial character \(\psi\) of \(Q\).
- The \(2\)-fixed normalization means the quotient count vector is constant on \(2\)-orbits in every quotient used below.

## approach_A
Structural / invariant route.

1. Normalize by the multiplier \(2\), so \(D\) is a union of \(2\)-orbits.
2. Push \(D\) to prime quotients \(C_5\), \(C_{19}\), and \(C_{97}\).
3. Use the quotient character condition \(|\psi(B)|=48\) to force the quotient count profiles.
4. Lift to product quotients \(C_{95}=C_5\times C_{19}\) and \(C_{485}=C_5\times C_{97}\).
5. Use marginal compatibility plus sum-of-squares constraints to collapse the remaining orbit variables.

This route is attractive because \(n=48^2\) is a perfect square and \(v\) has only three prime factors, so the prime and semiprime quotients are unusually rigid.

## approach_B
Construction / extremal / contradiction route.

Assume a \(2\)-fixed difference set exists and ask how concentrated it can be on cosets of the prime-index subgroups.

1. The \(C_5\) quotient has one distinguished class and four equal nonzero classes.
2. The \(C_{19}\) quotient has one distinguished class and eighteen equal nonzero classes.
3. The \(C_{97}\) quotient has one distinguished class and, a priori, two nonzero classes corresponding to quadratic residues and nonresidues mod \(97\).
4. The mixed quotient \(C_{485}\) then behaves like a compatibility test: the \(C_5\) and \(C_{97}\) marginals must fit into the same \(2\)-orbit decomposition.
5. If the resulting row/column counts or square-sum budget have no integral realization, we get a contradiction without any global search.

This is the best contradiction lane because it stays theorem-facing and avoids generic brute force.

## lemma_graph
Lemma skeleton currently in hand:

1. Multiplier normalization:
   Any cyclic \((9215,4607,2303)\)-difference set can be translated to be fixed by multiplication by \(2\).
2. Prime-quotient forcing:
   In \(C_5\), the quotient counts must be \((883,931,931,931,931)\).
3. Prime-quotient forcing:
   In \(C_{19}\), the quotient counts must be \((197,245,\dots,245)\).
4. Prime-quotient forcing with quadratic split:
   In \(C_{97}\), the quotient counts are forced to be \((95,47,\dots,47)\), where the two nonzero \(2\)-orbits are the quadratic residues and nonresidues modulo \(97\).
5. Product-quotient compatibility:
   In \(C_{95}\), the count vector is forced into exactly two \(2\)-orbit patterns:
   - Case I: \(x_0=73,\ y=45,\ z=31,\ (u,w)=(49,51)\) up to swapping \(u,w\).
   - Case II: \(x_0=1,\ y=49,\ z=49,\ u=w=49\).
6. Product-quotient compatibility:
   In \(C_{485}\), the unique prime-quotient profile on \(C_{97}\) is \((95,47,\dots,47)\); there is no second admissible \(C_{97}\) branch.
7. \(C_{485}\) square-budget collapse:
   Writing the \(2\)-orbit variables as
   \[
   x_0,\ y_R,\ y_N,\ z,\ u_0,\dots,u_3,\ v_0,\dots,v_3,
   \]
   the marginals force \(x_0=z=19\) and \(y_R+y_N=18\). A convexity check kills the alternative \(x_0=67,\ z=7\), which would correspond to \(y_R+y_N=17\).

The next unresolved edge is the full mixed-character check on \(C_{485}\) or the analogous \(C_{1843}\) quotient.

## chosen_plan
Use approach A as the main line.

Immediate target:

1. lock the multiplier-normalized quotient profiles;
2. preserve them in the record and status;
3. run one bounded exact computation only if needed, on the quotient \(C_{485}\), to see whether the remaining orbit variables admit any full character-compatible realization.

This keeps the work inside the micro-paper lane. If the \(C_{485}\) mixed-character check already contradicts existence, that is very close to a title theorem. If it does not, the surviving quotient package is still a legitimate theorem-facing slice.

## self_checks
- Check 1: the normalization by the multiplier \(2\) is legitimate because \(\gcd(2-1,9215)=1\).
- Check 2: the forced \(C_5\) profile is consistent with both the sum and the square-sum:
  \(883+4\cdot 931=4607\) and \(883^2+4\cdot 931^2=2304+2303\cdot 1843\).
- Check 3: the forced \(C_{19}\) profile is consistent with both the sum and the square-sum:
  \(197+18\cdot 245=4607\) and \(197^2+18\cdot 245^2=2304+2303\cdot 485\).
- Check 4: the \(C_{95}\) two-case classification satisfies the mixed-character norm equation
  \[
  \left(x_0-y-z+\frac{u+w}{2}\right)^2 + 95\left(\frac{u-w}{2}\right)^2 = 48^2.
  \]
- Check 5: the \(C_{97}\) prime-quotient system has the unique orbit-constant solution \((95,47,\dots,47)\); the previously listed \((0,48,\dots,48)\) pattern is impossible because it sums to \(4608\), not \(4607\).
- Check 6: the bounded \(C_{485}\) enumeration was over all ordered \(2\)-orbit assignments compatible with the derived marginals and square budget; it found \(32\) surviving orbit-count solutions, so there is no false contradiction there.
- Check 7: the bounded \(C_{1843}\) enumeration was over all ordered \(2\)-orbit assignments compatible with the exact marginals
  \(x_0=z=5\), \(y_R=y_N=2\), \(\sum u_i=\sum v_i=15\), and total square budget \(90\);
  it found exactly \(3\) surviving orbit-count solutions.

## code_used
Used two bounded Python checks only after the reasoning package was written:

1. exhaustive orbit-count search on the quotient \(C_{485}=C_5\times C_{97}\);
2. exhaustive orbit-count search on the quotient \(C_{1843}=C_{19}\times C_{97}\).

No generic optimization, SAT, or broad brute force over subsets of \(C_{9215}\) was used.

## result
Current outcome: no full solution yet, but the quotient structure is now sharply constrained.

Established structural consequences of any putative cyclic \((9215,4607,2303)\)-difference set:

- \(D\) may be assumed \(2\)-invariant after translation.
- The \(C_5\) quotient profile is forced to be \((883,931,931,931,931)\).
- The \(C_{19}\) quotient profile is forced to be \((197,245,\dots,245)\).
- The \(C_{97}\) quotient profile is forced to be \((95,47,\dots,47)\).
- In the quotient \(C_{95}\), only two \(2\)-orbit count patterns survive.
- In the quotient \(C_{485}\), the row/column and square-sum constraints collapse the problem to a narrow residual family with \(x_0=z=19\) and \(y_R+y_N=18\); an exhaustive orbit-count check leaves exactly \(32\) ordered solutions.
- In the quotient \(C_{1843}\), the same method is much sharper: it forces
  \[
  x_0=z=5,\qquad y_R=y_N=2,\qquad \sum u_i=\sum v_i=15,
  \]
  with total secondary square budget
  \[
  \sum u_i^2 + \sum v_i^2 = 90,
  \]
  and the exhaustive orbit-count check leaves exactly \(3\) ordered solutions.

Representative surviving \(C_{1843}\) patterns are:

- \(u=(4,0,3,1,4,3)\), \(v=(3,3,3,2,2,2)\);
- \(u=(2,3,4,3,3,0)\), \(v=(2,3,2,3,1,4)\);
- \(u=(3,3,2,2,2,3)\), \(v=(4,0,1,4,3,3)\).

This is a real theorem-facing obstruction slice, but it is not yet the full nonexistence proof.

## family_affinity
High. This sits exactly in the cyclic Hadamard residual family with \(v=4n-1\), \(n\) a square, and \(v\) split into three odd prime factors. The quotient-and-multiplier method is tailored to that family, not just to this isolated tuple.

## generalization_signal
Moderate positive signal. The method should transfer to other residual cyclic Hadamard cases whose group order has a small number of prime factors and where a small multiplier such as \(2\) or \(3\) has long orbit lengths on the prime quotients.

What appears to scale:
- forcing prime-quotient profiles from \(|\psi(B)|=48\);
- collapsing semiprime quotients using orbit marginals and square budgets.

What does not yet scale automatically:
- the final mixed-character elimination on larger product quotients.

## proof_template_reuse
Reusable template:

1. normalize by a numerical multiplier;
2. classify prime-quotient profiles by orbit symmetry plus the \(48\)-norm condition;
3. combine prime quotients into one semiprime quotient;
4. use marginal compatibility and convexity to eliminate whole branches before any computation;
5. reserve code only for the final small residual orbit system.

## candidate_theorem_slice
Candidate slice:

`Any cyclic (9215,4607,2303)-difference set, after a suitable translation, is fixed by the multiplier 2. Its prime-quotient profiles are forced to be (883,931,931,931,931) on C_5, (197,245,…,245) on C_19, and (95,47,…,47) on C_97; moreover, its C_95 quotient has only two possible 2-orbit count patterns, and its C_485 quotient must satisfy x_0=z=19 and y_R+y_N=18.`

Stronger current version:

`... and its C_1843 quotient must satisfy x_0=z=5, y_R=y_N=2, \sum u_i=\sum v_i=15, with only three ordered orbit-count solutions.`

This is theorem-shaped enough to be worth preserving even though the final contradiction is not yet reached.

## smallest_param_shift_to_test
Inside this instance, the smallest useful shift is not a new global parameter set but the next compatibility layer:

1. intersect the surviving \(C_{485}\) and \(C_{1843}\) orbit families inside the full \(C_5\times C_{19}\times C_{97}\) quotient;
2. if that still survives, push one level deeper to a joint compatibility computation on the \(75\) full \(2\)-orbits of \(C_{9215}\).

Across nearby cases, the template should next be tested on another cyclic Hadamard survivor with three prime factors and square \(n\), because that is the smallest family move that preserves the proof architecture.

## why_this_is_or_is_not_publishable
If the nonexistence proof closes from the current quotient package, the result is already paper-shaped: it would settle a named residual cyclic Hadamard case and would likely require only light packaging.

The current partial result alone is not yet publishable in the micro-paper lane. It is still a structural slice rather than a closure theorem. The missing ingredient is one decisive contradiction on the remaining \(C_{485}\) or \(C_{1843}\) orbit family.

At the moment the result is still too thin for the micro-paper lane by itself. It has theorem shape, but not title-theorem closure.

Minimal remaining packaging work after a successful closure:
- write the multiplier normalization cleanly;
- state the forced prime and semiprime quotient profiles as lemmas;
- present the final contradiction;
- add the short literature note explaining that this removes one survivor from the sub-10000 cyclic Hadamard list.

## paper_shape_support
What extra structure would make this paper-shaped if the main claim closes?

- one decisive obstruction lemma on the last residual semiprime quotient;
- one short corollary stating that the \(v=9215\) cyclic Hadamard case is eliminated;
- one boundary remark explaining why the argument uses the specific \(5\), \(19\), and \(97\) quotient geometry and does not yet settle the remaining survivors uniformly.

Immediate corollary if the contradiction closes:

`The sub-10000 cyclic Hadamard survivor v=9215 is removed from the Baumert-Gordon/Gordon residual list.`

## boundary_remark
Boundary remark:

The current obstruction package is already stronger than a generic “no witness found” statement: it shows that any putative solution must have a highly nonuniform but very rigid quotient profile, including the exact \(C_5\), \(C_{19}\), and \(C_{97}\) images and only a tiny residual family on \(C_{485}\). What is still missing is the final mixed-character contradiction that turns this rigidity into full nonexistence.

One natural corollary, if the final contradiction is obtained, is that the sub-10000 survivor \(v=9215\) drops out by a proof that is visibly arithmetic rather than search-heavy. What does not yet scale is the last compatibility step across both semiprime quotients simultaneously.

## likely_failure_points
- The \(C_{485}\) orbit labeling must be handled carefully; a bookkeeping error there could create fake contradictions.
- The derivation of the \(C_{97}\) profile should be recorded as a direct integer-uniqueness check; the previously written extra branch \((0,48,\dots,48)\) is not admissible because it already violates the sum constraint.
- The residual \(C_{485}\) and \(C_{1843}\) solutions may still be mutually incompatible in the full three-factor quotient, but that has not yet been checked here.
- Conversely, if the residual families are jointly compatible, then the final obstruction probably sits at the full-group orbit level rather than in a single semiprime quotient.

## what_verify_should_check
- Recheck the multiplier-normalization step and its translation argument.
- Recompute the forced prime-quotient profiles on \(C_5\), \(C_{19}\), and \(C_{97}\), noting that \(C_{97}\) has the unique orbit-constant profile \((95,47,\dots,47)\).
- Verify the \(C_{95}\) two-case classification, especially the mixed-character norm formula.
- Verify the \(C_{485}\) marginal equations:
  \(x_0+4z=95\),
  \(x_0+48(y_R+y_N)=883\),
  and the square-budget reduction leading to \(x_0=z=19\) and \(y_R+y_N=18\).
- Verify that the exhaustive \(C_{485}\) orbit search really leaves exactly \(32\) character-compatible assignments.
- Verify the \(C_{1843}\) deductions
  \(x_0=z=5\),
  \(y_R=y_N=2\),
  \(\sum u_i=\sum v_i=15\),
  \(\sum u_i^2+\sum v_i^2=90\),
  and that the exhaustive orbit search really leaves exactly \(3\) assignments.
- Check the next unresolved step: whether the surviving \(C_{485}\) and \(C_{1843}\) orbit packages can coexist inside a full \(C_{9215}\) \(2\)-orbit model.

## verify_rediscovery
Bounded prior-art audit run on 2026-04-15 with limited web only.

- Exact-tuple and alternate-notation searches for `(9215,4607,2303)` and `9215 cyclic Hadamard difference set` did not surface a later exact construction or nonexistence theorem within budget.
- The canonical source still lists the exact tuple as open: Baumert-Gordon 2004, Table 5, line `9215 4607 2303 Open` ([cds.pdf](https://www.dmgordon.org/papers/cds.pdf)).
- Same-source theorem/example/corollary checking inside the canonical paper did not reveal a hidden elimination for `v=9215`; the nearby eliminated rows are different tuples.
- A current-status check of Gordon's site found the repository still live but frozen as of 2026-03-01, with no in-budget tuple-specific settlement surfaced from the current public pages ([dmgordon.org](https://www.dmgordon.org/), [difference-set repository landing page](https://www.dmgordon.org/diffset/)).

Verdict: bounded PASS 1 did not establish rediscovery. I therefore did not relabel this run as `REDISCOVERY`.

## verify_faithfulness
The solve artifact stays on the exact selected problem: a nonexistence attempt for a cyclic \((9215,4607,2303)\)-difference set in \(C_{9215}\). I did not find wrong-theorem drift or a change of definitions.

The first faithfulness issue is local rather than global: the record claimed an extra \(C_{97}\) prime-quotient option \((0,48,\dots,48)\). That is not a genuine branch of the intended argument, because it already violates the sum constraint \(a+48b+48c=4607\). After removing that impossible branch, the verified claim envelope remains a partial obstruction package for the exact intended statement.

## verify_proof
First incorrect step found: Lemma 4 / Check 5 as originally written allowed a second \(C_{97}\) orbit-constant profile \((0,48,\dots,48)\). A direct integer check shows that this pattern sums to \(4608\), so it cannot occur.

This is a tiny arithmetic defect, not a theorem-drift problem and not a rediscovery issue. After the repair, the multiplier normalization and the forced prime-quotient profiles on \(C_5\), \(C_{19}\), and \(C_{97}\) survive skeptical checking. I did not find a later contradiction in the verified portion because the artifact does not yet close the full nonexistence proof.

I did not independently replay the claimed `32` surviving \(C_{485}\) orbit assignments or the claimed `3` surviving \(C_{1843}\) assignments from durable local code, because no checker or enumeration script was preserved in the candidate-local artifact surface for this run.

## verify_adversarial
No candidate-local checker or enumeration script was preserved under `artifacts/cyclic-hadamard-difference-set-9215-4607-2303/`, so there was no full solver computation to rerun directly.

I did rerun independent arithmetic checks in plain Python:

- \(\operatorname{ord}_5(2)=4\), \(\operatorname{ord}_{19}(2)=18\), and \(\operatorname{ord}_{97}(2)=48\), matching the orbit geometry assumed in the record.
- The \(C_5\) quotient system has the unique orbit-constant solution \((883,931,931,931,931)\).
- The \(C_{19}\) quotient system has the unique orbit-constant solution \((197,245,\dots,245)\).
- The \(C_{97}\) quotient system has the unique orbit-constant solution \((95,47,\dots,47)\).

Adversarial outcome: the prime-quotient layer checks out, and the only concrete break I found is the now-repaired impossible extra \(C_{97}\) branch.

## verify_theorem_worthiness
Exactness: the current honest verified content is a structural slice, not the exact nonexistence theorem.

Novelty: bounded PASS 1 did not establish rediscovery, so the exact selected problem still appears frontier-novel within the limited audit budget.

Reproducibility: moderate at the prime-quotient layer, but weaker than desired for the semiprime residual-family claims because the local artifact does not preserve the enumeration code needed for a clean replay.

Lean readiness: no. Lean would currently formalize only a partial obstruction slice, while the shortest remaining path to a sealed packet is still mathematical closure of the residual \(C_{485}\) / \(C_{1843}\) compatibility step.

Paper leverage: the selected exact case still has good micro-paper leverage if closed. The currently verified slice alone does not yet look like most of a publishable note.

Direct answers:

- Would this result, if correct and Lean-sealed, already constitute most of a publishable note? The exact nonexistence theorem would, but the currently verified partial slice would not.
- What percentage of the paper would one solve already provide? For the exact case, still roughly \(75\\%-80\\%\). For the currently verified slice alone, closer to \(35\\%-45\\%\).
- What title theorem is actually visible now? A structural theorem forcing the prime-quotient profiles of any cyclic \((9215,4607,2303)\)-difference set.
- What part of the argument scales? Multiplier normalization and prime-quotient forcing should transfer to nearby three-prime cyclic Hadamard survivors.
- What part clearly does not? The final mixed-character elimination and semiprime/full-group compatibility step do not yet scale and are not yet closed here.
- Is the best honest publication status still only `INSTANCE_ONLY` or even `NONE`? For the current verified artifact, the best honest publication status is `NONE`; it is still publication-distant.

## verify_verdict
- verify verdict: `MINOR_FIX`
- classification: `PARTIAL`
- confidence: `medium`
- strongest honest verified claim: after translation, any putative cyclic \((9215,4607,2303)\)-difference set can be taken \(2\)-invariant, and its prime-quotient profiles on \(C_5\), \(C_{19}\), and \(C_{97}\) are forced to be \((883,931^4)\), \((197,245^{18})\), and \((95,47^{96})\), respectively.

## minimal_repair_if_any
Conservative repair applied:

- removed the impossible extra \(C_{97}\) branch \((0,48,\dots,48)\);
- restated the \(C_{97}\) prime-quotient profile as uniquely forced;
- left the semiprime residual-family claims in place as solve-stage leads rather than upgrading them to verified closure results.

## publication_prior_art_audit
Bounded publication audit run on 2026-04-15 with limited web only.

- Exact-statement and alternate-notation searches for `(9215,4607,2303)`, `9215 cyclic Hadamard difference set`, and nearby wording did not surface a later case-specific construction or nonexistence theorem within budget.
- Canonical-source check: Baumert-Gordon 2004, Table 5 still lists `9215 4607 2303 Open`. I also checked the surrounding Table 5 lines to make sure the nearby eliminated rows are different parameter sets and not a hidden sufficient-condition settlement for \(v=9215\).
- Follow-up status check: Gordon's 2019 La Jolla Repository talk still lists `9215` among the seven small open cyclic Hadamard cases below \(10000\).
- Outside-status pass: the current La Jolla Difference Set Repository landing page is still live and still exposes an `open` status surface, but I did not rely on its search form as a primary tuple-specific proof. A recent Song slide surfaced in search results repeating the same seven survivors; because the underlying PDF did not fetch cleanly in-budget, I treat that item only as corroborating status evidence.

Prior-art verdict: bounded audit did not establish rediscovery. The exact selected case still looks unresolved on the audited literature surface, but "still open in the sources" is not the same thing as "current packet is close to a paper."

## publication_statement_faithfulness
The artifact remains faithful to the exact selected problem: cyclic \((9215,4607,2303)\)-difference sets in \(C_{9215}\).

The faithfulness contraction is publication-facing rather than mathematical. The selected title theorem asks for full existence or nonexistence. The strongest honest audited claim is narrower:

`after translation, any putative cyclic (9215,4607,2303)-difference set is 2-invariant and has uniquely forced prime-quotient profiles on C_5, C_19, and C_97.`

That is still on-target, but it is only a slice of the intended theorem. The unresolved semiprime/full-group compatibility step remains load-bearing, and the candidate-local artifact surface does not preserve a durable checker for the quoted \(C_{485}\) and \(C_{1843}\) survivor counts.

## publication_theorem_worthiness
Direct answers.

- Is the strongest honest claim stronger than "here is an example"? Yes. It is a structural obstruction slice, not an example.
- Is there a real theorem here? Yes, but the real theorem currently visible is a forced-profile lemma/proposition, not the advertised closure theorem for the \(v=9215\) case.
- Is the proof structural or merely instance-specific? Structural in method, but still heavily instance-specific in payload. It uses the exact factorization \(9215=5\cdot 19\cdot 97\), the multiplier \(2\), and the exact square norm \(n=48^2\).
- Would this survive a referee asking "what is the theorem?" As an internal lemma inside a short elimination note, probably yes. As the title theorem of a standalone micro-paper, probably no.
- Is the claim too dependent on hand-picked small cases? It does not depend on a witness search over tiny cases, but it is still tied to one exact tuple and its quotient geometry. That makes it a credible obstruction lemma, not yet a compelling standalone paper claim.

Theorem-worthiness verdict: theorem-shaped and worth preserving, but too auxiliary to carry the one-shot publication objective by itself.

## publication_publishability
The current audited packet is not `PAPER_READY`.

Why not:

- the remaining gap is not just exposition or Lean polish; it is the decisive mathematical compatibility step that would turn the obstruction slice into a title theorem;
- the strongest honest claim is still a preparatory slice rather than a settlement of the canonical open case;
- the candidate-local proof surface does not preserve durable local code for the quoted semiprime residual-family counts, which weakens replay confidence exactly where the packet most needs closure.

Direct answers.

- Would this result, if correct and verified in the current bounded sense, already constitute most of a publishable note? No.
- What percentage of the current note would the present audited result already provide? About \(40\%\).
- What percentage would an exact closure of the selected \(v=9215\) case still provide? Roughly \(75\%-80\%\), because the literature already packages the case as a named residual open entry.
- If this is not yet paper-ready, is the remaining gap genuinely small? No. The gap may be narrow in description, but it is still mathematically decisive.
- If this is not yet paper-ready, should it be moved aside rather than expanded into a larger theorem program? Yes. Preserve the slice and cool the slug unless a tightly scoped final compatibility attack is ready. Do not widen this into a broader cyclic-Hadamard campaign.
- Would Lean directly seal the packet? No. Lean would currently formalize only the partial slice and would function as optional archival polish after closure, not as the thing that turns this into a publishable theorem packet.

## publication_packet_audit
Conservative publication classification:

- publication status: `SLICE_CANDIDATE`
- packet quality: `low`
- publication confidence: `medium`

Reason for `SLICE_CANDIDATE` rather than `NONE`: the strongest honest audited output is a genuine theorem slice stronger than an example. Reason for stopping below `SLICE_EXACT` and far below `PAPER_READY`: the slice is too auxiliary for the one-shot lane, and the decisive closure step remains unresolved and insufficiently preserved.

## micro_paper_audit
Micro-paper verdict:

- the selected target itself remains a valid micro-paper target if the exact \(v=9215\) case is settled;
- the current audited packet does not satisfy the micro-paper objective;
- the pre-audit attraction was real at selection time, but the present packet still sits on the wrong side of the title-theorem boundary.

This candidate therefore remains lane-eligible in principle but not lane-complete in its current solved state. The honest managerial move is to preserve the theorem slice, mark the packet as not human-ready, and avoid spending follow-on effort unless the final compatibility step can be attacked in a narrowly scoped way.

## strongest_honest_claim
After translation, any putative cyclic \((9215,4607,2303)\)-difference set can be taken \(2\)-invariant, and its prime-quotient profiles on \(C_5\), \(C_{19}\), and \(C_{97}\) are uniquely forced to be \((883,931,931,931,931)\), \((197,245,\dots,245)\), and \((95,47,\dots,47)\), respectively.

## paper_title_hint
Forced Prime-Quotient Profiles for Putative Cyclic \((9215,4607,2303)\)-Difference Sets

## next_action
Preserve the verified prime-quotient slice, cool this slug as not yet paper-ready, and only reopen it for a narrowly scoped final compatibility attack with durable candidate-local checker artifacts. Do not expand it into a broader theorem program or send the current packet to Lean as though formalization were the missing ingredient.
