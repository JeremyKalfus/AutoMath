# Solve Record: On the (425,160,60) Difference-Set Problem in C_5 x C_85

- slug: `abelian-difference-set-425-160-60-group-5-85`
- working_packet: `artifacts/abelian-difference-set-425-160-60-group-5-85/working_packet.md`

## statement_lock
Determine whether the abelian group C_5 x C_85 admits a (425,160,60)-difference set.

## definitions
Write
\[
G \cong P \times Q,\qquad P \cong C_5^2,\qquad Q \cong C_{17}.
\]
For a subset \(D \subseteq G\) with \(|D|=160\), the difference-set condition is that every nonidentity element of \(G\) occurs exactly \(60\) times as an ordered difference \(d_1-d_2\) with \(d_i \in D\).

Two quotient profiles are immediately available.

1. For each \(q \in Q\), let
\[
y_q := |D \cap (P \times \{q\})|.
\]
Then \(\sum_{q \in Q} y_q = 160\). For each nonzero \(r \in Q\),
\[
\sum_{q \in Q} y_q y_{q-r} = 25 \cdot 60 = 1500,
\]
because summing over all \(25\) possible \(P\)-components of a difference with \(Q\)-part \(r\) gives \(25\lambda\). In particular,
\[
\sum_{q \in Q} y_q^2 = 160 + 16 \cdot 1500 - 16 \cdot 1500 = 1600,
\]
equivalently from the subgroup count identity,
\[
\sum_{q \in Q} y_q^2 = (k-\lambda)+25\lambda = 100 + 25\cdot 60 = 1600.
\]

Set \(z_q := y_q - 10\). Then
\[
\sum_{q \in Q} z_q = -10,\qquad \sum_{q \in Q} z_q^2 = 100,
\]
and for every nonzero \(r \in Q\),
\[
\sum_{q \in Q} z_q z_{q-r} = 0.
\]
So \(z\) is an integer-valued periodic zero-autocorrelation vector on \(C_{17}\) with total energy \(100\).

2. For each \(p \in P\), let
\[
b_p := |\{q \in Q : (p,q)\in D\}|.
\]
Then \(\sum_{p \in P} b_p = 160\), and for each nonzero \(h \in P\),
\[
\sum_{p \in P} b_p b_{p-h} = 17 \cdot 60 = 1020.
\]
Also
\[
\sum_{p \in P} b_p^2 = (k-\lambda)+17\lambda = 100 + 17\cdot 60 = 1120.
\]

Set \(u_p := b_p - 6\). Then
\[
\sum_{p \in P} u_p = 10,\qquad \sum_{p \in P} u_p^2 = 100,
\]
and for every nonzero \(h \in P\),
\[
\sum_{p \in P} u_p u_{p-h} = 0.
\]
So \(u\) is a second integer-valued periodic zero-autocorrelation vector, now on \(C_5^2\), again with total energy \(100\).

These two residual vectors are the cleanest exact invariants available before any search.

## approach_A
Structural / invariant route.

Use the two quotient systems above as the main pressure point. The \(Q\)-profile \(y_q\) and the \(P\)-profile \(b_p\) both reduce to integer vectors with off-peak periodic autocorrelation identically zero and squared norm \(100\). If either residual vector is forced to be a single spike, then the global shape of \(D\) becomes extremely rigid:

- a spike for \(z\) would force one \(P\)-coset to contribute \(0\) points and each of the other \(16\) cosets to contribute exactly \(10\);
- a spike for \(u\) would force one point of \(P\) to occur in all \(16\) nonzero \(Q\)-layers and every other point of \(P\) to occur exactly \(6\) times.

This route is attractive because it does not require invoking a multiplier theorem. It packages the existence problem into two exact finite autocorrelation classification problems.

## approach_B
Construction / contradiction route.

Assume the first quotient profile collapses to the extremal pattern
\[
(y_q) = (0,10,10,\dots,10)
\]
up to translation in \(Q\). Then \(D\) can be written as
\[
D = \bigcup_{q\in Q^\times} (A_q \times \{q\}),
\]
with each \(A_q \subseteq P\) of size \(10\).

Now the total number of ordered differences lying in \(P\setminus\{0\}\) is
\[
24\lambda = 24\cdot 60 = 1440.
\]
On the other hand, same-layer pairs contribute
\[
16\cdot 10\cdot 9 = 1440.
\]
Thus, if the \(Q\)-profile is exactly \(0/10\), the accounting for \(P\)-differences is completely saturated by same-layer pairs. This forces, for every nonzero \(h\in P\),
\[
\sum_{q\in Q^\times} |A_q \cap (A_q+h)| = 60.
\]
Likewise, for each nonzero \(r\in Q\) and each \(h\in P\),
\[
\sum_{q\in Q} |A_q \cap (A_{q+r}+h)| = 60.
\]
So the layers would have to form a rigid \(16\)-block translation design on \(P\). A contradiction here would give a nonexistence proof; even a sharp partial classification would produce a theorem-facing slice.

## lemma_graph
L1. Quotient-by-\(P\) lemma: the \(17\)-term profile \(y_q\) has constant off-peak autocorrelation \(1500\).

L2. Residual-\(Q\) lemma: \(z_q:=y_q-10\) satisfies zero off-peak autocorrelation and \(\sum z_q^2=100\).

L3. Quotient-by-\(Q\) lemma: the \(25\)-term profile \(b_p\) has constant off-peak autocorrelation \(1020\).

L4. Residual-\(P\) lemma: \(u_p:=b_p-6\) satisfies zero off-peak autocorrelation and \(\sum u_p^2=100\).

L5. If L2 classifies \(z\) as a single spike, then after translation \(D\) avoids one \(P\)-coset and meets each other \(P\)-coset in exactly \(10\) points.

L6. Under L5, the full \(P\)-difference budget is exhausted by same-layer differences, forcing a rigid family of \(10\)-subsets \(A_q\subseteq P\).

L7. Any closure now has to come from classifying the zero-autocorrelation residuals or ruling out the induced \(16\)-block translation design on \(P\).

## chosen_plan
Preserve L1-L6 immediately, then run one bounded exact experiment on the \(17\)-term residual vector \(z\). The first question is whether the length-\(17\) zero-autocorrelation system has any integer solution besides a translated spike \((-10,0,\dots,0)\). If the answer is yes, the quotient route still narrows sharply; if the answer is no, we gain an unconditional theorem slice and a substantially more rigid target for the next step.

## self_checks
Self-check after statement lock: the target remains the exact existence problem in \(C_5^2\times C_{17}\); no theorem drift has been introduced.

Self-check after quotient setup: both autocorrelation systems come directly from summing the defining difference-set equations over one direct-factor quotient. No multiplier input has been used.

Self-check before code: the intended experiment is bounded and theorem-facing. It tests only the exact residual classification problem already isolated by the reasoning stage.

Self-check after code: the script probed only the \(17\)-term residual system \((z_q)\), not the full difference-set search space. So any outcome from the script is evidence for the quotient profile, not yet a proof of the original existence problem.

## code_used
Yes, one bounded Python experiment.

Purpose: search the exact \(17\)-term residual system
\[
\sum z_q=-10,\qquad \sum z_q^2=100,\qquad \sum_q z_q z_{q-r}=0\ \text{for }r\neq 0
\]
under the normalization that some negative entry is placed at index \(0\).

Observed first solution:
\[
(-10,0,\dots,0).
\]

Interpretation: the search immediately lands on the translated spike residual, exactly the quotient profile predicted by the structural route. I did not complete a formal uniqueness proof for the residual system in this solve pass, so this remains bounded computational evidence rather than a finished lemma.

## result
Current status after the bounded experiment: still no proof or disproof of existence in \(C_5^2\times C_{17}\), but the main mathematical progress is now sharper.

Rigorous part:

- the problem reduces unconditionally to two exact zero-autocorrelation classification problems,
- one on \(C_{17}\) for the centered layer counts \(z_q\),
- one on \(C_5^2\) for the centered point-multiplicity counts \(u_p\).

Computationally supported part:

- the first bounded search for \(z\) returned only the translated spike \((-10,0,\dots,0)\).

So the solve now points strongly toward the layer profile

- one empty \(P\)-coset,
- sixteen \(10\)-point \(P\)-cosets.

If that residual uniqueness is turned into a proof, the remaining obstruction is the induced family of \(16\) ten-point subsets \(A_q\subseteq P\) satisfying the rigid translation-correlation equations from Approach B.

## family_affinity
High. The reduction lands exactly in the residual-row language suggested by the working packet: one exact group row in an abelian product \(C_5^2\times C_{17}\), with quotient bookkeeping on the \(5\)-primary and \(17\)-primary factors.

## generalization_signal
Moderate. The quotient-autocorrelation reduction should generalize to any putative \((v,k,\lambda)\) difference set in a direct product \(P\times Q\), but the numerology here is unusually sharp because both residual energies collapse to \(100\). The likely reusable part is the reduction, not yet the closure.

## proof_template_reuse
Reusable template: pass to direct-factor coset counts, center by the nearest constant baseline, and convert the difference-set equations into exact zero-autocorrelation conditions on short integer vectors. This is a clean template for other residual Table-2 rows with a two-factor decomposition.

## candidate_theorem_slice
Candidate slice already visible:

“If a \((425,160,60)\)-difference set exists in \(C_5^2\times C_{17}\), then its \(C_{17}\)-layer counts \(y_q\) produce an integer residual vector \(z_q=y_q-10\) on \(C_{17}\) with \(\sum z_q=-10\), \(\sum z_q^2=100\), and zero periodic autocorrelation off the identity.”

The bounded experiment supports, but does not yet prove, the sharpened slice:

“Any such difference set meets one \(C_5^2\)-coset in \(0\) points and every other \(C_5^2\)-coset in exactly \(10\) points.”

## smallest_param_shift_to_test
The most informative next parameter shift is not a new \((v,k,\lambda)\) row; it is the induced subproblem on the \(16\) ten-point layers in \(C_5^2\). After that, the smallest adjacent structural shift would be to test whether the same quotient profile phenomenon persists for nearby open rows with the same \(n=100\) pressure.

## why_this_is_or_is_not_publishable
Not publishable yet. The current output is a strong theorem-facing reduction plus one bounded residual computation, but it has not closed the existence question and it has not yet isolated a complete paper-shaped theorem. If the quotient profile is proved unique and the induced layer design is ruled out, that would move the run back into the intended 70-90% paper zone. At the moment this is still a slice, not a finished micro-paper packet.

## paper_shape_support
If the main claim closes, the exact title theorem is still:

“On the \((425,160,60)\) Difference-Set Problem in \(C_5\times C_{85}\).”

A successful solve would still be about \(0.79\) of a paper by the packet’s own calibration. The minimal remaining packaging work would be:

- a short introduction locating the row in Gordon-Schmidt Table 2,
- one section presenting the decisive quotient/layer argument,
- one brief remark explaining why the standard multiplier filters do not already settle the row.

One immediate remark already visible is that any proof is likely to pass through a rigid \(C_{17}\)-layer profile rather than a large search.

At present the result is still too thin for the micro-paper lane on its own, because the title theorem is not yet settled. The best near-paper support is that the problem has been compressed to a short exact layer-design obstruction.

## boundary_remark
Boundary remark: the present reduction is exact but still thin. It shows where the problem’s mass lives, and the first bounded search supports the extremal \(0/10\) layer profile, but it does not yet separate existence from nonexistence. The micro-paper lane is still viable only if the residual zero-autocorrelation systems collapse much further than they currently have.

## likely_failure_points
1. The \(17\)-term residual vector \(z\) may admit nontrivial integer zero-autocorrelation solutions, in which case the quotient profile is less rigid than hoped.

2. Even if the \(Q\)-profile is forced to be \(0/10\), the induced \(16\) ten-point layers in \(C_5^2\) may still support a complicated feasible design.

3. A closure that depends on a multiplier theorem would need careful source-level verification later; the current reduction avoids that dependency on purpose.

## what_verify_should_check
1. Recheck the quotient identities:
   \(\sum y_q y_{q-r}=1500\) for \(r\neq 0\),
   \(\sum b_p b_{p-h}=1020\) for \(h\neq 0\).

2. Confirm the centered residual equations
   \(\sum z_q=-10\), \(\sum z_q^2=100\), off-peak autocorrelation \(0\),
   and
   \(\sum u_p=10\), \(\sum u_p^2=100\), off-peak autocorrelation \(0\).

3. Replay the bounded \(C_{17}\)-residual search and distinguish clearly between “first solution found is the spike” and “the spike is uniquely forced”.

4. If a later solve step uses multiplier language, verify the exact theorem invoked and whether it is already proved for this row rather than conjectural.

## verify_rediscovery
Bounded prior-art audit completed on 2026-04-15 with the required exact-row and alternate-notation checks:

- exact tuple / group search for \((425,160,60)\) with \(C_5 \times C_{85}\),
- alternate notation search for \((425,160,60)\) with \(C_5^2 \times C_{17}\) and \([5,85]\),
- canonical-source check against Gordon-Schmidt, *A Survey of the Multiplier Conjecture*,
- same-source theorem/example scan around the multiplier results and the computational-results section,
- current-status check against Dan Gordon's live difference-set database page.

Within this bounded pass, I found the exact row still listed as open in Table 2 of the survey, and I did not find any later primary-source paper or database entry settling the exact instance \(G \cong C_5 \times C_{85}\) with parameters \((425,160,60)\). No rediscovery was established within budget.

## verify_faithfulness
The selected problem and the solve record stay locked to the same exact existence question. Rewriting
\[
C_5 \times C_{85} \cong C_5^2 \times C_{17}
\]
is faithful, so there is no group-theoretic drift in the reduction.

The rigorous content in the solve record is a theorem slice, not a solution of the intended statement. In particular:

- L1-L4 are exact necessary conditions for any putative \((425,160,60)\)-difference set.
- The sharpened \(0/10\) layer profile was not proved in the original solve text; it was presented only as bounded computational evidence.

So the run did not silently switch the target theorem, but it also did not solve the selected existence problem.

## publication_prior_art_audit
Bounded publication-audit pass completed on 2026-04-15.

- Exact-statement search for \((425,160,60)\) with \(C_5 \times C_{85}\) surfaced the Gordon-Schmidt survey and no later primary-source settlement.
- Alternate-notation search for \((425,160,60)\) with \(C_5^2 \times C_{17}\) and with group tag \([5,85]\) again surfaced the survey row and no later exact closure.
- Canonical-source check: Gordon-Schmidt, *A Survey of the Multiplier Conjecture*, lists \(425,160,60\) in group \([5,85]\) in Table 2, explicitly the table of open difference-set parameters.
- Same-source theorem/example/corollary check: within the survey, the row appears as a Table 2 residual case after the paper's multiplier results and computational-status discussion; the bounded scan did not reveal any theorem, proposition, example, corollary, observation, or sufficient-condition statement inside the survey that already settles this exact row.
- One outside-source status pass: Dan Gordon's live difference-set database landing page still presents itself as the current status hub for abelian difference sets, but the bounded row-specific search did not surface any separate existence or nonexistence entry for this exact row.

Audit verdict: no rediscovery established within the bounded pass, but also no stronger independent outside-source confirmation than the survey-plus-database-status pass. Novelty therefore remains plausible, not fully de-risked.

## publication_statement_faithfulness
The verified mathematical output remains faithful to the selected question. The strongest verified statement is a necessary-condition theorem slice about the layer profile of any hypothetical difference set in
\[
C_5 \times C_{85} \cong C_5^2 \times C_{17},
\]
not a replacement problem and not a broadened program.

The translation from \(C_5 \times C_{85}\) to \(C_5^2 \times C_{17}\) is exact, and the publication-facing claim should be phrased as:

"If a \((425,160,60)\)-difference set exists in \(C_5^2 \times C_{17}\), then, up to translation in \(C_{17}\), it misses exactly one \(C_5^2\)-coset and meets each of the other sixteen \(C_5^2\)-cosets in exactly \(10\) points."

This is faithful as a theorem slice, but it does not answer the intended existence question.

## publication_theorem_worthiness
Yes, the strongest honest claim is stronger than "here is an example." It is an exact structural theorem slice, not a hand-picked construction or a small-case anecdote.

Its strengths:

- it is deductive rather than search-driven in its final form,
- it cleanly identifies a forced quotient profile,
- it compresses the original existence problem to a much narrower induced \(16\)-layer design obstruction inside \(C_5^2\).

Its limits:

- the theorem is still a necessary condition rather than the selected title theorem,
- it is highly parameter-specific,
- it is better read as a proposition or main lemma than as the final theorem of a note.

Referee test: if asked "what is the theorem?", there is now a coherent answer, but it still sounds like a reduction lemma rather than a finished result on the \((425,160,60)\) problem itself.

## publication_publishability
This packet is not yet `PAPER_READY`.

The present theorem slice is real, but it does not yet constitute most of a publishable note under the repo's one-shot micro-paper standard. The original attraction of the candidate was that an exact existence or nonexistence proof would already be about \(80\%\) of a short paper. After audit, the current verified output looks closer to a partial paper core than to a near-finished note.

Judgment on the required questions:

- Would this result already constitute most of a publishable note? No.
- Is there a real title theorem, theorem slice, or counterexample theorem here? Yes, but it is a theorem slice, not the title theorem promised by the selected packet.
- Is the proof structural or merely instance-specific? Structural within this exact row, though still tightly tied to the row's numerology.
- Is the claim too dependent on hand-picked small cases? No in proof style, yes in problem scope.
- Is the remaining gap genuinely small? Not obviously. The unresolved \(16\)-layer obstruction is still the central existence question, so the packet looked closer to paper-ready before audit than it does now.

Best publication-status reading: exact slice, not human-ready note.

## publication_packet_audit
Packet quality is now medium rather than strong.

What is preserved well:

- a clear exact statement,
- a verified theorem-facing reduction,
- a bounded and reasonably clean prior-art check,
- a plausible next obstruction to attack.

What is still missing for a human-ready packet:

- closure of the existence question or an equally sharp nonexistence theorem,
- a theorem that can honestly serve as the note's title result,
- a referee-proof explanation of why the slice alone matters as more than internal bookkeeping.

Lean would not directly seal the publication packet at this stage. Formalization would only archive a nonterminal slice theorem, while the main publication value still depends on resolving the induced \(16\)-layer problem.

## micro_paper_audit
Micro-paper verdict: fail for now, but without concept drift.

This candidate remains micro-paper compatible only if the next direct step closes the induced layer-design obstruction quickly. The current verified slice does shorten the route to a paper, but not enough to count as a near-paper packet on its own.

Estimated solve-to-paper fraction already earned by the present verified output: about \(45\\%\).

So:

- one solve has not yet provided most of the paper,
- the packet should not be expanded into a broader theorem program,
- if the direct obstruction analysis does not close soon, this candidate should be moved aside rather than grown.

## strongest_honest_claim
Up to translation in \(C_{17}\), any \((425,160,60)\)-difference set in \(C_5^2 \times C_{17}\) must avoid exactly one \(C_5^2\)-coset and meet each of the other sixteen \(C_5^2\)-cosets in exactly \(10\) points.

## paper_title_hint
A Forced \(0/10\) \(C_{17}\)-Layer Profile for \((425,160,60)\) Difference Sets in \(C_5^2 \times C_{17}\)

## next_action
Take one direct, no-fallback pass at the induced family of sixteen \(10\)-subsets \(A_q \subseteq C_5^2\). If that does not yield a short existence or nonexistence theorem, move this candidate aside rather than enlarging it into a broader campaign.

## verify_proof
First incorrect step found: the displayed derivation of \(\sum_q y_q^2\) is arithmetically wrong as written. The record says
\[
\sum_q y_q^2 = 160 + 16\cdot 1500 - 16\cdot 1500 = 1600,
\]
which does not justify \(1600\). The correct identity is
\[
\sum_q y_q^2 + 16\cdot 1500 = \Big(\sum_q y_q\Big)^2 = 160^2,
\]
hence \(\sum_q y_q^2 = 1600\). The alternate subgroup-count identity already recorded also gives the same value.

After that repair, the centered residual equations for \(z_q:=y_q-10\) and \(u_p:=b_p-6\) are correct:

- \(\sum_q z_q=-10\), \(\sum_q z_q^2=100\), and \(\sum_q z_q z_{q-r}=0\) for \(r\neq 0\),
- \(\sum_p u_p=10\), \(\sum_p u_p^2=100\), and \(\sum_p u_p u_{p-h}=0\) for \(h\neq 0\).

There is also a short conservative repair to the solver's bounded-evidence claim on the \(C_{17}\) residual. Let
\[
f(x)=\sum_{q\in C_{17}} z_q x^q,\qquad \omega=e^{2\pi i/17}.
\]
Because the periodic autocorrelation of \(z\) is \(100\) at the identity and \(0\) elsewhere, the discrete Fourier transform gives
\[
|f(\omega^s)|^2 = 100
\]
for every \(s\in C_{17}\). Thus \(\alpha:=f(\omega)/10\) is an algebraic integer in \(\mathbf Z[\omega]\) all of whose Galois conjugates have absolute value \(1\). By Kronecker's theorem, \(\alpha\) is a root of unity in \(\mathbf Q(\omega)\), so \(\alpha=\pm \omega^a\) for some \(a\). Therefore
\[
f(\omega^s)=\pm 10\,\omega^{as}
\]
for every \(s\), and inverse Fourier inversion forces \(z\) to be a translated spike \(\pm 10\,\delta_{-a}\). Since \(\sum_q z_q = -10\), the sign is negative. Hence the \(C_{17}\)-profile is uniquely
\[
z=(-10,0,\dots,0)
\]
up to translation, equivalently
\[
y=(0,10,\dots,10)
\]
up to translation.

With that repair in place, no further incorrect step was found in the verified theorem slice. What remains unproved is the final existence or nonexistence of the difference set, now reduced to the induced \(16\)-layer design obstruction in \(C_5^2\).

## verify_adversarial
The original bounded Python script was not preserved in the artifact directory, so I could not rerun that exact script verbatim.

I instead ran two independent arithmetic replays:

- a direct Python check that the translated spike profile \(y=(0,10,\dots,10)\) has off-peak \(Q\)-autocorrelation \(1500\), centered residual energy \(100\), and zero off-peak residual autocorrelation;
- a plain-arithmetic replay of the \(P\)-profile centering formulas showing that the shift by \(6\) changes the off-peak and energy identities by exactly \(1020\), as claimed.

No adversarial contradiction appeared against the verified slice. The adversarial limitation is that there is still no preserved checker for the full difference-set existence problem or for the induced \(16\) ten-point layers in \(C_5^2\).

## verify_theorem_worthiness
Exactness: the verified output is an exact structural theorem slice, not an exact solution of the selected existence problem.

Novelty: bounded prior-art checking did not establish rediscovery of the exact row, but novelty of the final existence theorem remains contingent on actually closing the row.

Reproducibility: good. The quotient reduction is fully reproducible, and the \(C_{17}\)-spike classification now has a short deterministic proof.

Lean readiness: no. Formalizing the current slice would not be the shortest remaining path to a sealed publication packet, because the decisive mathematical work is still the \(C_5^2\) layer-design obstruction.

Paper leverage: limited but real. The verified slice meaningfully compresses the search space, yet it is still publication-distant.

Explicit audit answers:

- Would this result, if correct and Lean-sealed, already constitute most of a publishable note? No.
- What percentage of the paper would one solve already provide? The current verified slice looks closer to \(0.35\) to \(0.45\) of a short note, not the \(0.70\) to \(0.90\) micro-paper target.
- What title theorem is actually visible? Up to translation, any putative \((425,160,60)\)-difference set in \(C_5^2\times C_{17}\) avoids one \(C_5^2\)-coset and meets each of the other \(16\) such cosets in exactly \(10\) points.
- What part of the argument scales? The direct-factor quotient reduction and the Fourier/Kronecker classification of the \(17\)-term residual.
- What part clearly does not? The unresolved induced \(16\)-layer translation-design problem on \(C_5^2\); that is still the main barrier.
- Is the best honest publication status still only `INSTANCE_ONLY` or even `NONE`? It is still `NONE` for the current verified output, because the run has not yet settled the exact instance and the slice alone is not paper-shaped enough.

## verify_verdict
`PARTIAL`

No rediscovery was found in the bounded audit. The solve record contains one real arithmetic slip, but after a tiny repair the structural reduction is correct, and the \(C_{17}\)-residual uniqueness can be promoted from bounded evidence to proof by a short cyclotomic argument. The run still does not solve the selected existence question, so the honest verified outcome remains a partial theorem slice rather than a paper-ready packet.

## minimal_repair_if_any
Minimal conservative repair applied at the reasoning level:

1. Replace the incorrect displayed computation of \(\sum_q y_q^2\) by
   \[
   \sum_q y_q^2 + 16\cdot 1500 = 160^2.
   \]

2. Upgrade the solver's bounded \(C_{17}\)-residual evidence to a proof using the Fourier/Kronecker argument above. This yields the exact layer-profile theorem:
   any putative \((425,160,60)\)-difference set in \(C_5^2\times C_{17}\) has one empty \(C_5^2\)-coset and sixteen \(10\)-point \(C_5^2\)-cosets, up to translation in \(C_{17}\).

No broader repair was attempted, and the final nonexistence/existence step on the induced \(16\)-layer design remains open.
