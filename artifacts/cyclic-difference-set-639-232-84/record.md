# Solve Record: The Cyclic (639,232,84) Difference-Set Problem

- slug: `cyclic-difference-set-639-232-84`
- working_packet: `artifacts/cyclic-difference-set-639-232-84/working_packet.md`

## statement_lock
The exact intended statement is:

> Determine whether the cyclic group \(C_{639}\) admits a \((639,232,84)\)-difference set.

Solve-stage title theorem if the obstruction path closes:

> The cyclic group \(C_{639}\) admits no \((639,232,84)\)-difference set.

This would already be most of a micro-paper: the active packet rates the solve-to-paper fraction at about `0.73`, and the remaining packaging would be limited to literature positioning against the surviving cyclic/noncyclic table rows and a clean presentation of the contracted argument.

## definitions
Work in additive notation on \(G=C_{639}\).

A \((v,k,\lambda)\)-difference set in \(G\) is a subset \(D \subseteq G\) with \(|D|=k\) such that every nonzero group element has exactly \(\lambda\) representations as \(d_1-d_2\) with \(d_1,d_2 \in D\).

Here

- \(v=639=9\cdot 71\),
- \(k=232\),
- \(\lambda=84\),
- \(n=k-\lambda=148=4\cdot 37\),
- \(\gcd(v,n)=1\).

For any quotient \(G \twoheadrightarrow C_w\) with kernel size \(m=v/w\), the contracted image
\[
X=\sum_{i=0}^{w-1} a_i x^i
\]
has coefficients \(a_i \in \{0,\dots,m\}\) satisfying
\[
\sum_i a_i = k,\qquad
\sum_i a_i^2 = n+\lambda m,\qquad
\sum_i a_i a_{i-t} = \lambda m \ \text{for every } t\not\equiv 0 \pmod w.
\]

Ambiguities/conventions to fix:

- I treat "admits" as existence in the cyclic group only, not in arbitrary abelian groups of order \(639\).
- The noncyclic \([3,213]\) row is context only; it is not part of the solve target.
- All quotient arguments below are necessary conditions only unless they yield an outright inconsistency.

## approach_A
Structural / invariant route: contract to small quotients of \(C_{639}\), starting with \(C_3\) and then \(C_9\).

For the quotient \(C_{639}\twoheadrightarrow C_3\), let the three contracted coefficients be \((u_0,u_1,u_2)\). Since the kernel has size \(213\),
\[
u_0+u_1+u_2=232,\qquad
u_0^2+u_1^2+u_2^2 = 148+84\cdot 213 = 18040.
\]
Solving these Diophantine constraints gives a unique multiset:
\[
\{u_0,u_1,u_2\}=\{84,78,70\}.
\]

Derivation: writing \((u_0,u_1,u_2)=(77+a,77+b,78-a-b)\), the square equation becomes
\[
a^2+b^2+ab-a-b=49,
\]
whose integer solutions only produce permutations of \((84,78,70)\).

This is already a rigid theorem slice: any cyclic \((639,232,84)\)-difference set must project to \(C_3\) with occupancies exactly \(84,78,70\) up to permutation.

For the quotient \(C_{639}\twoheadrightarrow C_9\), with coefficients \(c_0,\dots,c_8\in\{0,\dots,71\}\), we get
\[
\sum_{i=0}^8 c_i = 232,\qquad
\sum_{i=0}^8 c_i^2 = 148+84\cdot 71 = 6112,
\]
and for each nonzero shift \(t\pmod 9\),
\[
\sum_{i=0}^8 c_i c_{i-t} = 84\cdot 71 = 5964.
\]
Moreover the three block sums
\[
c_0+c_3+c_6,\quad c_1+c_4+c_7,\quad c_2+c_5+c_8
\]
must be a permutation of \(84,78,70\).

This turns the existence problem into a finite exact consistency problem on nine bounded integers.

## approach_B
Construction / extremal / contradiction route: contract to \(C_{71}\), where each coefficient lies in \(\{0,\dots,9\}\).

If \(b_0,\dots,b_{70}\) are the \(71\) contracted coefficients, then
\[
\sum_{i=0}^{70} b_i = 232,\qquad
\sum_{i=0}^{70} b_i^2 = 148+84\cdot 9 = 904,
\]
and every nonzero cyclic autocorrelation equals \(756\).

This is compatible with a low-variance occupancy model, so the \(71\)-quotient alone does not immediately contradict existence. Its use would be secondary:

- either as a multiplier-orbit compression target if the \(9\)-quotient obstruction stalls,
- or as a consistency check after any \(9\)-quotient candidate survives.

Reason for not choosing it first: the variable count is much larger, and without a clean multiplier lock in hand it is not the shortest route to a paper-shaped exact theorem.

## lemma_graph
Lemma skeleton currently targeted:

1. If \(D\subset C_{639}\) is a \((639,232,84)\)-difference set, then every quotient contraction satisfies the standard constant-correlation equations.
2. In the quotient \(C_3\), those equations force the coefficient multiset to be exactly \(\{84,78,70\}\).
3. Therefore any quotient to \(C_9\) must refine one of the three \(C_3\)-block patterns with block sums \(84,78,70\).
4. If no \(9\)-tuple \((c_0,\dots,c_8)\) satisfies the exact \(C_9\) equations together with those block sums, then no cyclic \((639,232,84)\)-difference set exists.
5. If such a \(9\)-tuple does exist, the obstruction attempt weakens to a genuine structural slice rather than a full disproof, and the next theorem-facing task is to lift the contradiction to \(C_{71}\) or to character values in \(Q(\zeta_9)\).

## chosen_plan
The solve began with the \(C_9\) obstruction because it was the smallest exact quotient. A bounded checker then found an explicit feasible \(9\)-contraction:
\[
[16,26,28,24,26,28,30,26,28],
\]
whose block sums are \(70,78,84\) and whose nonzero cyclic autocorrelations all equal \(5964\).

So the raw \(C_9\) obstruction does not close the theorem.

Best current path is therefore the multiplier-orbit route on the \(71\)-quotient:

1. use the standard cyclic multiplier input at the prime \(2\mid n\),
2. normalize by translation so that a putative difference set is \(2\)-invariant,
3. contract to \(C_{71}\),
4. use the \(2\)-orbit structure on \(C_{71}\) to force the total size \(232\) into an impossible congruence class.

What extra structure makes the result paper-shaped if this closes?

- a short lemma isolating the forced \(C_3\) occupancy pattern \((84,78,70)\),
- one proposition recording that the \(C_9\) contraction is not itself contradictory,
- the main \(71\)-quotient multiplier-orbit contradiction,
- one sentence separating the cyclic \([639]\) case from the noncyclic \([3,213]\) row.

Minimal remaining packaging work if the disproof survives verification:

- cite the exact cyclic multiplier theorem and the translation-normalization step in the precise form needed,
- state that the \(C_9\) system is nonempty so the \(71\)-quotient orbit argument is the real closing step,
- add a brief literature paragraph around the surviving table row.

## self_checks
- Self-check after statement lock: the target remains the cyclic case only, with no scope drift toward all abelian groups of order \(639\).
- Self-check after Approach A: the \(C_3\) contraction really is forced up to permutation; this is a rigorous slice, not a heuristic.
- Self-check after Approach B: the \(71\)-quotient is kept as a backup structural lane, not as an uncontrolled search.
- Self-check after the \(C_9\) checker: the experiment found a real feasible contraction, so that route must be recorded as a boundary result rather than overstated as a contradiction.
- Self-check after the multiplier pivot: the only load-bearing extra input is the standard cyclic multiplier theorem plus the usual translation normalization.
- Self-check after the \(71\)-orbit count: the contradiction is purely arithmetic and uses only the orbit sizes and the coset-size bound \(b_i\le 9\).

## code_used
Minimal code only.

Used one-off Python checks for two bounded tasks:

- verify that the \(C_9\) contracted system is nonempty by finding an explicit feasible tuple
  \([16,26,28,24,26,28,30,26,28]\),
- verify the multiplier arithmetic on the \(71\)-quotient, namely \(\operatorname{ord}_{71}(2)=35\), so the nonzero indices split into two \(2\)-orbits of size \(35\).

No SAT, ILP, CP-SAT, construction search, or broad brute force over subsets of \(C_{639}\) was used.

## result
Provisional disproof, contingent on the standard cyclic multiplier theorem in the exact form used below.

Claim:

> Assuming the standard cyclic multiplier fact that every prime divisor of \(n\) coprime to \(v\) is a numerical multiplier, the cyclic group \(C_{639}\) admits no \((639,232,84)\)-difference set.

Proof attempt:

Let \(D\subset C_{639}\) be a putative \((639,232,84)\)-difference set. Then
\[
n=k-\lambda=148,
\]
so \(2\mid n\) and \(\gcd(2,639)=1\).

By the standard cyclic multiplier theorem, \(2\) is a numerical multiplier. Thus
\[
2D=D+s
\]
for some \(s\in C_{639}\). Since \(\gcd(2-1,639)=1\), the usual translation-normalization step lets us replace \(D\) by a translate and assume
\[
2D=D.
\]

Now contract to the quotient \(C_{639}\twoheadrightarrow C_{71}\) with kernel of size \(9\). Let \(b_i\) be the number of elements of \(D\) in the \(i\)-th coset of the order-\(9\) subgroup. Then each \(b_i\) lies in \(\{0,\dots,9\}\), and
\[
\sum_{i=0}^{70} b_i = 232.
\]

Because \(2D=D\), the contracted coefficient vector is \(2\)-invariant:
\[
b_{2i}=b_i \qquad (i\in C_{71}).
\]

The multiplicative order of \(2\) modulo \(71\) is \(35\). Hence the action \(i\mapsto 2i\) on \(C_{71}\) has exactly three orbits:

- \(\{0\}\),
- one nonzero orbit of size \(35\),
- a second nonzero orbit of size \(35\).

Therefore the \(71\)-quotient coefficients have the form
\[
b_0=c,\qquad b_i=a \text{ on one nonzero orbit},\qquad b_i=b \text{ on the other},
\]
with \(0\le a,b,c\le 9\). Summing coefficients gives
\[
232 = c + 35a + 35b.
\]
Reducing modulo \(35\), we get
\[
c \equiv 22 \pmod{35}.
\]
But \(c\in\{0,1,\dots,9\}\), impossible.

This contradiction rules out \(D\).

What the argument scales to:

- the multiplier-orbit compression on quotient groups,
- the use of a small kernel bound to turn orbit sizes into a size congruence obstruction.

What does not obviously scale:

- the specific congruence \(232\equiv 22\pmod{35}\),
- the choice of the quotient \(C_{71}\), which is tailored to this factorization \(639=9\cdot 71\).

Suggested theorem slice if verification wants the smallest unconditional part:

- the exact \(C_3\) occupancy lemma \(\{84,78,70\}\),
- plus the statement that the \(C_9\) contracted system is nonempty, so any final disproof must use more than the first contraction layer.

Most useful next parameter shifts:

- another cyclic survivor with a prime factor \(p\) such that a multiplier has one or two large nonzero orbits mod \(p\),
- or a nearby case with the same \(9\cdot p\) structure where the quotient-\(p\) orbit sum immediately clashes with \(k\).

Package assessment:

- if the multiplier theorem validates exactly as used, this is close to a paper-shaped exact-case disproof;
- without that citation, the package is still only a strong solve-stage counterexample attempt rather than a finished micro-paper.

## family_affinity
Strong. The final route stays inside the classical cyclic elimination program: numerical multipliers, quotient contractions, and orbit-size contradictions on a prime quotient.

## generalization_signal
Moderate. The \(C_3\) forcing lemma generalizes cleanly, and the orbit-compression method is reusable whenever a multiplier has few large orbits on a prime quotient. The exact contradiction here is still instance-tuned.

## proof_template_reuse
Reusable template:

1. contract to the smallest prime-power quotient dividing \(v\),
2. solve the resulting low-dimensional moment equations exactly,
3. record whether that small quotient is genuinely obstructive or merely feasible,
4. invoke a verified multiplier on a complementary quotient,
5. convert multiplier invariance into orbit-compressed quotient coefficients,
6. finish with a size or congruence obstruction.

That template should transfer to nearby cyclic survivor rows with a small prime-power factor and a complementary prime quotient carrying large multiplier orbits.

## candidate_theorem_slice
Candidate theorem slice:

> If a cyclic \((639,232,84)\)-difference set exists, then its image in \(C_3\) has coefficient multiset \(\{84,78,70\}\); equivalently, every such set meets the three cosets of the index-\(3\) subgroup in exactly \(84\), \(78\), and \(70\) points.

Secondary slice now visible:

> The exact \(C_9\) contracted system refining those block sums is nonempty, so the first nontrivial contraction does not itself rule out the cyclic case.

This matters because it identifies where the real obstruction begins: at the multiplier-compressed \(71\)-quotient, not at the \(9\)-quotient.

## smallest_param_shift_to_test
Two parameter shifts would be most informative after the active case:

- keep the same quotient architecture and test another cyclic survivor with \(9\mid v\) but a complementary prime quotient on which a small multiplier has one or two large nonzero orbits,
- in the present family, test whether replacing \(71\) by another prime factor in a nearby table row yields the same immediate congruence obstruction \(k=b_0+\#\mathcal{O}\cdot m\).

## why_this_is_or_is_not_publishable
If the multiplier theorem validates exactly as used, the result is close to publishable and is plausibly 70-90% of a short paper.

Why:

- the exact title theorem is already clear,
- the proof body is short and uses one sharp orbit-congruence contradiction,
- the remaining packaging work is light.

Minimal remaining packaging work:

- give the multiplier theorem in the precise cyclic form needed,
- state the translation-normalization step explicitly,
- note that the \(C_9\) quotient is feasible and therefore not the closing contradiction,
- separate the cyclic \([639]\) case from the noncyclic \([3,213]\) row.

Why I am still conservative:

- the load-bearing theorem is cited from standard lore rather than rederived here,
- the proof is exact-case and still instance-shaped,
- publication readiness depends on verification confirming the multiplier input rather than downgrading it.

## paper_shape_support
If the main claim closes negatively, the smallest natural supporting structure is now:

- main theorem: nonexistence in \(C_{639}\),
- support lemma: the \(C_3\) contraction is forced to be \((84,78,70)\),
- boundary remark: the \(C_9\) contraction is feasible, so the decisive step is the multiplier-compressed \(71\)-quotient,
- final boundary remark: the argument does not settle the noncyclic \([3,213]\) case.

One immediate remark that would naturally fall out:

- any future cyclic proof in this family must look beyond the first contraction layer; the \(9\)-quotient alone leaves room for exact contracted data.

## boundary_remark
Boundary remark:

- the \(C_9\) quotient does not obstruct existence by itself;
- the part that scales is the multiplier-orbit compression on a complementary quotient;
- the part that does not obviously scale is the exact congruence clash \(232=c+35m\) with \(c\le 9\).

So the current package is no longer "just an instance witness," but it is still an exact-case cyclic note rather than a broad family theorem.

## likely_failure_points
- The load-bearing risk is the multiplier input: verification must confirm that \(2\mid n\) and \(\gcd(2,639)=1\) really suffice for the exact cyclic multiplier statement used here.
- The translation-normalization step from \(2D=D+s\) to a translate with \(2D=D\) must be checked explicitly.
- The quotient-orbit passage must preserve the bound \(0\le b_i\le 9\) exactly as used.

## what_verify_should_check
- Check the \(C_3\) derivation carefully: the only integer solutions to the moment equations are permutations of \((84,78,70)\).
- Check that the displayed \(C_9\) witness really satisfies the exact contracted equations with kernel size \(71\).
- Check the cyclic multiplier theorem in the precise form needed for \(2\mid n=148\) and \(v=639\).
- Check the translation-normalization step from numerical multiplier to setwise invariance.
- Check that multiplication by \(2\) on \(C_{71}\) has exactly two nonzero orbits of size \(35\).
- In publication audit, check that the final note cleanly separates the cyclic \([639]\) case from the noncyclic \([3,213]\) row.

## verify_rediscovery
Bounded prior-art audit run on 2026-04-15.

- Query patterns checked within budget: the exact tuple \((639,232,84)\), alternate cyclic notation \([639]\), the canonical Baumert-Gordon 2004 source, same-source / same-family theorem-proposition-example coverage, and one recent-status-style check.
- No rediscovery was established in that pass.
- The canonical source chain still supports frontier status inside the bounded audit: Baumert-Gordon 2004 keeps \((639,232,84)\) in the surviving cyclic table, and Gordon-Schmidt 2015 Table 2 still lists the cyclic \([639]\) row as open.
- The 2015 survey entry is especially important here because it records `MC primes = 2,37` for this exact row, meaning those primes are still only multiplier-conjecture candidates in that source, not already settled numerical multipliers.
- No later exact existence or nonexistence theorem for cyclic \(C_{639}\) surfaced within the capped search pass.

Conclusion: no rediscovery found within budget, but the literature recheck weakens the solve-stage proof because its load-bearing multiplier input is not already present in the cited source chain.

## verify_faithfulness
The artifact is not faithful to the intended statement.

- Intended statement: determine unconditionally whether the cyclic group \(C_{639}\) admits a \((639,232,84)\)-difference set.
- Actual proved content after skeptical checking: the record gives a conditional obstruction, namely that if \(2\) is available as a numerical multiplier for a putative cyclic \((639,232,84)\)-difference set, then the quotient-\(71\) orbit count yields a contradiction.
- That is a nearby but different theorem. The solve-stage prose repeatedly presents the conclusion as a provisional disproof and labels the load-bearing multiplier step as "standard," but the bounded source audit does not support that description for this exact row.

Faithfulness verdict: `VARIANT`, not an exact resolution of the selected problem.

## verify_proof
First incorrect / unjustified step found:

> "By the standard cyclic multiplier theorem, \(2\) is a numerical multiplier."

Why this fails:

- The bounded source audit rechecked Gordon-Schmidt 2015 precisely because it is the packet's own status anchor. For the exact \((639,232,84)\) cyclic row, that survey still lists `MC primes = 2,37`.
- In that source, `MC primes` are multiplier-conjecture primes, not automatically established multipliers for the exact case. So the record cannot treat \(2\) as already available by a standard theorem without a separate derivation.
- The artifact does not verify the extra hypotheses needed to derive \(2\) from a proved multiplier theorem, nor does it cite a later source settling that input for this row.

Downstream status:

- Once one inserts the extra assumption " \(2\) is a numerical multiplier," the remaining arithmetic appears coherent: the translation-normalization step is standard because \(\gcd(2-1,639)=1\), the action of multiplication by \(2\) on \(C_{71}\) has two nonzero orbits of size \(35\), and the equation \(232=c+35a+35b\) with \(0\le c\le 9\) is impossible.
- So the failure is not in the quotient-\(71\) arithmetic; it is at the theorem-input boundary. The intended unconditional nonexistence theorem is not proved.

## verify_adversarial
Adversarial reruns were arithmetic rather than exploratory.

- Recomputed the \(C_3\) contraction equations directly: the unique coefficient multiset is \(\{70,78,84\}\).
- Rechecked the displayed \(C_9\) witness \([16,26,28,24,26,28,30,26,28]\): total \(232\), square-sum \(6112\), every nonzero cyclic autocorrelation \(5964\), and block sums \(70,78,84\).
- Recomputed \(\operatorname{ord}_{71}(2)=35\).
- Exhaustively checked the orbit-sum equation \(232=c+35a+35b\) for \(0\le a,b,c\le 9\): no solutions.

These reruns support the unconditional helper slices and the conditional quotient-\(71\) contradiction. The adversarial break is source-level: the multiplier step is not available as an established theorem in the bounded source chain.

## verify_theorem_worthiness
Assessment after skeptical checking:

- Exactness: fails for the intended statement. The verified content is a conditional obstruction plus exact low-quotient structural slices.
- Novelty: no rediscovery was established, but there is also no verified frontier resolution of the selected problem.
- Reproducibility: good for the arithmetic slices; poor as a publication packet because the decisive input is still an unproved external assumption for this row.
- Lean readiness: no. Lean would only formalize a conditional variant or partial lemmas, not the missing unconditional theorem.
- Would this result, if correct and Lean-sealed, already constitute most of a publishable note? No. The missing step is still the main theorem-sized content.
- Best estimate of solve-to-paper fraction for the honest verified content: about `0.20`.
- Title theorem actually visible: "If \(2\) is a numerical multiplier for a cyclic \((639,232,84)\) difference set, then no such set exists," together with the exact \(C_3\) occupancy lemma and the fact that the \(C_9\) contracted system is nonempty.
- What scales: the \(C_3\) forcing lemma, the nonempty \(C_9\) contracted system, and the quotient-orbit compression template on prime quotients.
- What clearly does not: the unsupported multiplier input and the instance-specific congruence clash on the \(71\)-quotient.
- Best honest publication status now: `NONE`. This is true-but-publication-distant helper structure, not a one-solve-away paper packet.

## verify_verdict
- `verify_verdict = VARIANT`
- `classification = VARIANT`
- `confidence = high`

Reason: the exact case does not appear rediscovered within the bounded audit, but the solve-stage artifact does not prove the intended unconditional theorem. What survives is a narrower conditional variant and two reusable contraction lemmas.

## minimal_repair_if_any
Tiny conservative repair only:

- Relabel the main claim as conditional on \(2\) being a valid numerical multiplier for this exact cyclic row.
- Preserve the exact \(C_3\) occupancy lemma \(\{70,78,84\}\) and the explicit feasible \(C_9\) contraction as verified helper artifacts.
- Do not send this packet to Lean or publication in its current state; the shortest honest next step is an unconditional justification of the multiplier input or a different nonconjectural obstruction route.

## publication_prior_art_audit
Bounded publication audit run on 2026-04-15.

- Exact statement search and alternate-notation search did not surface a later paper proving existence or nonexistence for cyclic \((639,232,84)\) beyond the packet's canonical source chain.
- In Baumert-Gordon 2004, the exact row appears in Table 3 as an open cyclic survivor with \(v=639\), \(k=232\), \(\lambda=84\), \(n=148\); the paper's case-by-case theorem section does not single out this row for a theorem, proposition, example, corollary, or observation-level resolution.
- In Gordon-Schmidt 2015, Table 2 still lists both \([639]\) and the distinct noncyclic \([3,213]\) realization for \((639,232,84)\) among the open parameters, with `MC primes = 2,37`; in that source this means multiplier-conjecture primes, not proved numerical multipliers.
- Follow-up check: Gordon 2022 on small-\(\lambda\) difference sets does not mention this tuple in the bounded pass, so it does not change the status of the exact cyclic row.

Publication-audit prior-art verdict: no rediscovery found within the capped pass, but also no later exact resolution located. The source chain still supports "open exact row" rather than "already settled theorem."

## publication_statement_faithfulness
The strongest honest current packet is not faithful to the intended statement.

- Intended statement: determine unconditionally whether \(C_{639}\) admits a \((639,232,84)\)-difference set.
- What the artifacts actually support: an exact \(C_3\) occupancy lemma, a nonempty \(C_9\) contraction witness, and a conditional \(C_{71}\)-orbit contradiction assuming \(2\) is a numerical multiplier for this exact cyclic row.
- The decisive gap is theorem-sized, not editorial: the proof does not currently justify the multiplier input needed to convert the conditional obstruction into the intended unconditional theorem.

Faithfulness judgment: `VARIANT`.

## publication_theorem_worthiness
The current packet does contain real mathematics, but not yet a referee-stable title theorem.

- Strongest honest claim stronger than "here is an example": yes, but only modestly. The \(C_3\) rigidity lemma and the conditional orbit obstruction are genuine structural statements, not a single instance witness.
- Real title theorem or theorem slice visible now: only a helper slice such as "any cyclic \((639,232,84)\)-difference set has \(C_3\)-occupancies \(\{70,78,84\}\)" or the conditional nonexistence theorem under a multiplier assumption.
- Structural versus instance-specific: mixed. The \(C_3\) lemma is structural, but the packet's main contradiction is still highly instance-tuned and contingent on an unproved input for this row.
- Would this survive "what is the theorem?": not in its current form. The honest answer would still sound like helper structure around an unsolved exact case.
- Dependence on hand-picked small cases: still too high. The \(C_9\) witness is useful boundary data, but it highlights that the first contraction layer does not close the problem.

Theorem-worthiness verdict: below `SLICE_CANDIDATE` as a publication packet, even though some individual lemmas are worth preserving.

## publication_publishability
This is not yet close enough to a publishable note.

- Would the present verified content already constitute most of a publishable note? No.
- Best estimate of paper fraction already supplied by the current honest packet: about `0.20`.
- Remaining gap small or only apparently small before audit? It only looked small before audit. The missing multiplier justification is the title-theorem-sized bridge, not light cleanup.
- Should this be moved aside rather than expanded into a broader theorem program? Yes. The correct response is to cool the candidate, preserve the verified slices, and avoid campaign drift.
- Would Lean directly seal the packet? No. Lean would only formalize helper lemmas or the conditional variant; it would not supply the missing unconditional theorem input.

Publication-status verdict: `NONE`.

## publication_packet_audit
Packet-quality judgment after bounded audit:

- Prior-art position is still frontier-facing in the narrow sense: the exact cyclic row remains open in the canonical source chain checked.
- Proof artifacts are preserved well enough for reuse: the \(C_3\) occupancy lemma, explicit feasible \(C_9\) tuple, and conditional \(C_{71}\)-orbit contradiction remain valuable side results.
- The packet is not HUMAN_READY because the strongest honest claim is not yet paper-shaped enough to leave the discovery queue as a publishable theorem note.
- The narrative is weaker than it first appeared because the packet cannot honestly claim more than "first quotient rigid, second quotient feasible, final contradiction conditional on a not-yet-justified multiplier."

Overall packet quality: `low` as a publication packet, despite usable internal artifacts.

## micro_paper_audit
Micro-paper lane judgment:

- The current packet fails the micro-paper lane in its present form.
- It is not just an example, but it is still not enough theorem for a micro-paper because the central exact-case resolution is missing.
- The strongest honest note one could presently write would be a helper-lemma note, not the intended exact-case title theorem.
- The family anchor remains good, but the theorem leverage collapses once the multiplier step is downgraded from theorem input to unresolved assumption.

Micro-paper verdict: cool this slug unless an unconditional multiplier citation or different nonconjectural obstruction appears quickly.

## strongest_honest_claim
The strongest honest claim currently supported is:

> Any cyclic \((639,232,84)\)-difference set has \(C_3\)-occupancy multiset \(\{70,78,84\}\); the corresponding \(C_9\) contracted system is nonempty; and if \(2\) is a numerical multiplier for this exact cyclic row, then the quotient-\(71\) orbit count gives a contradiction and rules out existence.

This is stronger than a mere example, but weaker than a publishable exact-case theorem.

## paper_title_hint
If one had to title the honest surviving packet today, the least misleading option would be:

> First-Quotient Constraints for the Cyclic \((639,232,84)\) Difference-Set Problem

That title is still helper-note shaped, not title-theorem shaped.

## next_action
Next action:

- Leave `publication_status = NONE`.
- Preserve the verified helper artifacts exactly as reusable input to a later solve pass.
- Move this candidate aside rather than broadening scope.
- Reopen only if a source-backed unconditional multiplier theorem for this exact row, or a different nonconjectural obstruction route, is found.
