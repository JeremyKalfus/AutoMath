# Solve Record: Does the cyclic group C_3439 admit a (3439,1719,859)-difference set?

- slug: `cyclic-hadamard-difference-set-3439-1719-859`
- working_packet: `artifacts/cyclic-hadamard-difference-set-3439-1719-859/working_packet.md`

## statement_lock
Locked target: determine whether there exists a subset \(D \subset C_{3439}\) of size \(1719\) such that every nonzero group element has exactly \(859\) representations as \(d_1-d_2\) with \(d_i \in D\).

Equivalently, for \(v=3439\), \(k=1719\), \(\lambda=859\), and \(n=k-\lambda=860\), decide whether a cyclic Hadamard difference set with these exact parameters exists.

If this closes cleanly, the honest title theorem is: "The cyclic group \(C_{3439}\) does not admit a \((3439,1719,859)\)-difference set" or its constructive negation if existence is proved.

## definitions
- Write the group additively as \(G=C_{3439}\cong \mathbb Z/3439\mathbb Z\).
- A \((v,k,\lambda)\)-difference set is a \(k\)-subset \(D\subset G\) such that every nonzero \(g\in G\) has exactly \(\lambda\) ordered representations \(g=d_1-d_2\) with \(d_i\in D\).
- The order of the difference set is \(n=k-\lambda=860=2^2\cdot 5\cdot 43\).
- Factorization correction: \(3439=19\cdot 181\), so \(G\) is cyclic but not of prime order.
- For any nontrivial character \(\chi\) of \(G\), a difference set still satisfies \(|\chi(D)|^2=n=860\).
- The subgroup structure now matters. Let \(H_{181}\) be the subgroup of order \(181\), and \(H_{19}\) the subgroup of order \(19\).
- If \(x_0,\dots,x_{18}\) are the coset intersection counts of \(D\) modulo \(H_{181}\), then \(\sum x_i=1719\) and the projected group-ring equation on \(G/H_{181}\cong C_{19}\) gives
  - \(\sum_i x_i^2 = 860 + 859\cdot 181 = 156339\),
  - \(\sum_i x_i x_{i-t} = 859\cdot 181 = 155479\) for every nonzero \(t \in C_{19}\).
- Writing \(x_i=90+y_i\), these become
  - \(\sum_i y_i = 9\),
  - \(\sum_i y_i^2 = 819\),
  - \(\sum_i y_i y_{i-t} = -41\) for every nonzero \(t \in C_{19}\).
- If \(z_0,\dots,z_{180}\) are the coset intersection counts of \(D\) modulo \(H_{19}\), then \(\sum z_j=1719\) and similarly
  - \(\sum_j z_j^2 = 860 + 859\cdot 19 = 17181\),
  - \(\sum_j z_j z_{j-s} = 859\cdot 19 = 16321\) for every nonzero \(s \in C_{181}\).
- Writing \(z_j=9+w_j\), these become
  - \(\sum_j w_j = 90\),
  - \(\sum_j w_j^2 = 900\),
  - \(\sum_j w_j w_{j-s} = 40\) for every nonzero \(s \in C_{181}\).
- Ambiguities to keep fixed:
  - No noncyclic group is under consideration; the group is uniquely \(C_{3439}\).
  - Solve should distinguish exact nonexistence from mere failure of a specific construction.
  - "Paper-shaped" here means an exact elimination or construction of this residual case, plus one minimal structural remark showing why this case matters inside the small-open cyclic Hadamard list.

## approach_A
Structural / invariant route:

Use the character equation \(|\chi(D)|^2=860\) on the order-\(19\) and order-\(181\) quotient characters. The relevant arithmetic data are the residue orders of \(2,5,43\) modulo \(19\) and modulo \(181\). If an odd-exponent prime divisor of \(860\) becomes self-conjugate in either quotient cyclotomic field, the corresponding character value could be impossible.

Computation shows:

- modulo \(19\): \(\operatorname{ord}(2)=18\), \(\operatorname{ord}(5)=\operatorname{ord}(43)=9\);
- modulo \(181\): \(\operatorname{ord}(2)=180\), \(\operatorname{ord}(5)=15\), \(\operatorname{ord}(43)=9\).

So the odd-exponent primes \(5\) and \(43\) are not self-conjugate in either quotient field. The clean parity obstruction does not close.

Self-check: the structural route produced a valid reduction and ruled out the easiest contradiction, but not the case itself.

## approach_B
Construction / extremal / contradiction route:

Exploit the subgroup quotients rather than the full group at once. The projected count vectors \(x\) on \(C_{19}\) and \(z\) on \(C_{181}\) satisfy exact constant-autocorrelation equations. A contradiction here would be stronger than a raw search: it would show that no quotient intersection pattern compatible with a difference set exists.

The length-\(19\) system is especially attractive:

- integers \(y_i\) with \(\sum y_i=9\),
- \(\sum y_i^2=819\),
- \(\sum y_i y_{i-t}=-41\) for all nonzero \(t\).

Any exact impossibility for this system already kills the full difference set.

Self-check: this remains theorem-facing because it is a quotient obstruction, not an unconstrained subset search.

## lemma_graph
1. Difference-set hypothesis \(\Rightarrow\) for every nontrivial character \(\chi\), \(|\chi(D)|^2=860\).
2. Because \(3439=19\cdot 181\), restrict first to quotient characters of orders \(19\) and \(181\).
3. Quotient to \(C_{19}\) and \(C_{181}\) to obtain exact integer autocorrelation systems for coset-count vectors \(x\) and \(z\).
4. Residue-order computation modulo \(19\) and \(181\) tests the easiest self-conjugacy obstruction; it fails for the odd-exponent primes \(5\) and \(43\).
5. Next, analyze the quotient autocorrelation systems directly; any impossibility there kills the full case.
6. If no contradiction appears even at quotient level, the attempt remains a structural package rather than a solve.

## chosen_plan
Best path now:

- keep the corrected factorization \(3439=19\cdot 181\) explicit;
- use the quotient systems as the main object;
- try to eliminate the length-\(19\) count vector \(y\) first, because it is the smallest exact reduction forced by the difference-set axioms;
- only if pure reasoning stalls, run a very small exact computation over quotient-count patterns, not over subsets of \(C_{3439}\).

This keeps the experiment bounded and structurally justified.

## self_checks
- Statement lock completed: exact group, exact parameter triple, and exact theorem target fixed.
- No concept drift so far: both approaches stay on the advertised character-sum / multiplier lane from the packet.
- Before code, the artifact now contains a theorem-facing proof skeleton and publication-aware framing.
- Major correction preserved: \(3439\) is composite, so the solve must proceed through quotient characters, not a prime-field shortcut.
- The first structural obstruction was tested honestly and failed for substantive arithmetic reasons, not from missing computation.
- After quotient reduction: the derived \(C_{19}\) and \(C_{181}\) count systems check internally against the total-sum and total-square identities.
- After parity reduction: the mod-2 arguments are exact field-norm calculations on \(C_{19}\) and \(C_{181}\), not heuristic parity guesses.
- After the reduced multiset check: the length-\(19\) reduced system is still feasible at the multiset level, so a contradiction cannot be claimed from sum and square data alone.

## code_used
Used so far:

- exact factor check showing \(3439=19\cdot 181\);
- exact residue-order computations for \(2,5,43\) modulo \(19\) and modulo \(181\).
- exact bounded multiset feasibility check for the reduced length-\(19\) system \(\sum t_i=-5\), \(\sum t_i^2=205\).
- exact residue-intersection check modulo \(181\), showing that the subgroups generated by \(5\) and \(43\) meet in a common order-\(3\) element.

No search over subsets has been used. A quotient-count search is justified only if the current direct reasoning on the reduced systems stalls.

## result
Current strongest result:

- the naive prime-order model is false because \(3439=19\cdot 181\);
- any putative difference set induces exact quotient-count systems on \(C_{19}\) and \(C_{181}\);
- the quickest self-conjugacy obstruction does not apply, since the odd-exponent primes \(5\) and \(43\) have odd orders modulo both \(19\) and \(181\).
- on the \(19\)-quotient, writing \(x_i=90+y_i\), the deviation vector satisfies
  - \(\sum y_i=9\),
  - \(\sum y_i^2=819\),
  - \(\sum y_i y_{i-t}=-41\) for all nonzero \(t\);
- reducing this system mod \(2\) shows every \(y_i\) is odd, so \(y_i=2t_i+1\) with
  - \(\sum t_i=-5\),
  - \(\sum t_i^2=205\),
  - \(\sum t_i t_{i-t}=-10\) for all nonzero \(t\);
- on the \(181\)-quotient, writing \(z_j=9+w_j\), the deviation vector satisfies
  - \(\sum w_j=90\),
  - \(\sum w_j^2=900\),
  - \(\sum w_j w_{j-s}=40\) for all nonzero \(s\),
  and the same mod-\(2\) norm argument forces every \(w_j\) to be even.

The reduced length-\(19\) system still has feasible multisets, so the current unconditional package is a real structural slice, not a nonexistence proof.

Conditional slice from the packeted multiplier lane:

- if Baumert-Gordon's contracted multiplier theorem truly applies at \(w=19\), then \(2,5,43\) can all be aligned to the common residue class \(5 \bmod 19\), whose nonzero orbits have sizes \(9\) and \(9\);
- then the \(19\)-quotient count vector must have the form
  - \(x_0=a\),
  - \(x_i=b\) on one nonzero \(5\)-orbit,
  - \(x_i=c\) on the other nonzero \(5\)-orbit,
  and the exact equations force only two possibilities:
  - \((a,b,c)=(63,93,91)\) up to swapping \(b,c\),
  - \((a,b,c)=(117,91,87)\) up to swapping \(b,c\).

This is the best theorem-facing output reached here. It narrows the case sharply but does not settle existence.

## family_affinity
Very high. This instance still sits squarely inside the small residual cyclic Hadamard list, and the corrected quotient reduction remains in the standard character-sum / subgroup-analysis lane used for cyclic cases.

## generalization_signal
Moderate. The specific quotient-count reduction works whenever \(v\) has a small factor and the problem can be pushed onto low-length cyclic quotients. The exact arithmetic obstruction found here, if any, could transfer to other composite-order residual cyclic Hadamard cases.

## proof_template_reuse
Potential reusable template: first factor \(v\) correctly, then push the difference-set equations to the smallest nontrivial quotient(s), derive exact integer autocorrelation systems for coset counts, and only then decide whether a bounded exact computation is needed.

## candidate_theorem_slice
Two theorem-facing slices are now visible:

1. Unconditional slice: any cyclic \((3439,1719,859)\)-difference set forces a \(C_{19}\) quotient deviation vector of odd entries and a \(C_{181}\) quotient deviation vector of even entries, satisfying the exact reduced autocorrelation systems displayed above.
2. Conditional sharper slice: if the common \(w=19\) multiplier theorem from the Baumert-Gordon lane is verified for this row, then the \(19\)-quotient counts collapse to exactly two patterns, namely \((63,93,91)\) or \((117,91,87)\) up to swapping the two nonzero orbits.

## smallest_param_shift_to_test
If this exact case resists elimination, the first useful shift is another residual cyclic Hadamard case whose group order has a small factor, so the same quotient-count reduction can be tried. Within this case itself, the immediate next shift is not a new parameter row but the sharper \(w=19\) versus \(w=181\) interaction.

## why_this_is_or_is_not_publishable
If the exact case falls to a clean quotient obstruction, this is already close to paper-ready: the residual-case status is literature-packaged, and the remaining work would mostly be exposition, bounded novelty verification, and polishing the obstruction into a short note.

Current verdict: not yet publishable in the micro-paper lane.

- A successful exact solve here would still be about 70-90% of a paper, with the exact title theorem "The cyclic group \(C_{3439}\) does not admit a \((3439,1719,859)\)-difference set" if nonexistence lands.
- Minimal remaining packaging after a genuine solve would be: one precise multiplier/quotient theorem citation, the short residual-case literature note, and a compact proof certificate.
- The present output is still too thin because it stops at a structural quotient packet and one conditional two-pattern collapse; it does not yet close the exact row.

## paper_shape_support
Extra structure that would make the result paper-shaped if the main claim closes:

- one explicit proposition isolating the decisive quotient obstruction for the \(C_{19}\) or \(C_{181}\) coset-count system;
- one short remark explaining why the off-the-shelf Lander eliminations still leave this composite-order case alive;
- one minimal corollary or boundary remark placing 3439 among the residual cyclic Hadamard cases below \(10000\).

Because the selection packet already rates this as \(0.84\) solve-to-paper fraction, a successful nonexistence proof should already be roughly 70-90% of the paper.

Immediate corollary / remark naturally falling out of the current slice:

- any final proof is likely to need the interaction between the \(19\)- and \(181\)-quotient structures, because neither quotient alone collapses under the first arithmetic obstruction tested here.

## boundary_remark
Natural boundary remark: the obstruction, if it exists, is now visibly tied to the quotient-count arithmetic forced by the factorization \(3439=19\cdot 181\). So even a successful elimination here would likely be an exact residual-case result, not a general cyclic-Hadamard theorem.

What scales:

- the quotient-count reduction to proper divisors of \(v\);
- the mod-\(2\) norm argument forcing parity in the reduced quotient systems;
- the Gauss-period computation on a prime quotient once a two-orbit multiplier pattern is justified.

What does not yet scale:

- the precise jump from the packet's multiplier hints to an unconditional \(w=19\) or \(w=181\) multiplier theorem for this exact row;
- the final contradiction, since the quotient slices found so far are still feasible.

## likely_failure_points
- I may still need a sharper known theorem to convert the quotient-count system into a short contradiction.
- The length-\(19\) and length-\(181\) systems may admit integer solutions even if no full difference set exists.
- A bounded computation over quotient counts could produce only negative evidence rather than a theorem, which would still be too thin for the micro-paper lane.
- The strongest sharpened slice in this record is conditional on a contracted multiplier theorem that has not been reloaded verbatim inside this run.

## what_verify_should_check
- Confirm the factorization \(3439=19\cdot 181\) and the derived quotient-count equations exactly.
- Confirm that any final obstruction on the quotient counts is fully rigorous and not just computationally suggestive.
- Recheck all residue-order computations modulo \(19\) and \(181\).
- Reconfirm that the literature still treats this exact tuple as open and that no later case-specific elimination exists.
- If a nonexistence proof lands, verify whether the argument scales to a small theorem slice or remains strictly instance-only.
- Most importantly, if the conditional \(w=19\) two-pattern collapse is reused, verify the exact hypotheses and conclusion of the Baumert-Gordon contracted multiplier theorem before treating it as unconditional.
