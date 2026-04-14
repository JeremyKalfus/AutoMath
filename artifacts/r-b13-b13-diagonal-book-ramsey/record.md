# statement_lock

- Active slug: `r-b13-b13-diagonal-book-ramsey`.
- Active title: `Determine the exact value of R(B13, B13)`.
- Locked interpretation: `B13` is the book graph consisting of 13 triangles sharing one common edge.
- Exact intended theorem for this solve attempt: `R(B13, B13) = 54`.
- Why this would be paper-shaped if correct: the packet already supplies the one-step upper bound `R(B13, B13) <= 54`, so a 53-vertex obstruction immediately closes the frontier and would already read like the title theorem of a short note.
- 70-90% paper test: if the Paley-53 obstruction is valid and the packet upper bound is confirmed in verification, the solve is already about 85-90% of a micro-paper. The only residue is writing the construction cleanly, checking novelty, and optionally formalizing the finite-field count.

# definitions

- For a graph `H`, write `bk(H) = max_{uv in E(H)} |N_H(u) ∩ N_H(v)|`. Then `H` contains `B13` iff `bk(H) >= 13`.
- In a red-blue coloring of `K_n`, let `R` be the red graph and `B = \overline{R}` the blue graph. A monochromatic `B13` appears iff `bk(R) >= 13` or `bk(B) >= 13`.
- On `F_53`, let `χ` denote the quadratic character, with `χ(a) = 1` for nonzero squares, `χ(a) = -1` for nonsquares, and `χ(0) = 0`.

# approach_A

Structural / invariant route:

- Assume a coloring of `K_53` avoids monochromatic `B13`. Then every monochromatic edge lies in at most 12 monochromatic triangles.
- Let `M` be the number of monochromatic triangles. Double-counting triangle-edge incidences gives
  `3M <= 12 * binom(53, 2)`,
  so `M <= 5512`.
- Goodman-type lower bounds are then nearly tight at `n = 53`, which means this route does not immediately force a contradiction. Instead it suggests that any extremal coloring must sit very close to an equality configuration with highly balanced degrees and nearly constant same-color codegrees.
- Equality heuristics point toward a self-complementary strongly regular object on 53 vertices with degree 26 and monochromatic edge codegree 12.
- Self-check: this route does not prove `R(B13, B13) = 53`; it instead isolates the likely extremal shape and therefore supports looking for an explicit 53-vertex construction.

# approach_B

Construction / extremal route:

- Try to realize the extremal equality pattern directly.
- Consider the Paley coloring on `F_53`: color edge `{x,y}` red when `x-y` is a nonzero quadratic residue mod 53, and blue otherwise.
- Because `53 ≡ 1 (mod 4)`, `-1` is a square, so this is an undirected coloring.
- Standard Paley facts predict:
  `deg_red(x) = 26` for every vertex,
  every red edge has exactly `(53-5)/4 = 12` red common neighbors,
  the blue graph is isomorphic to the red graph by multiplication with a nonsquare, so every blue edge also has 12 blue common neighbors.
- If those facts hold, then both colors have book size exactly 12, hence the coloring of `K_53` avoids monochromatic `B13`.
- Combined with the packet upper bound `R(B13, B13) <= 54`, this yields the exact value `R(B13, B13) = 54`.
- Self-check: unlike Approach A, this route gives a concrete closure path and matches the extremal shape suggested by the near-equality triangle count.

# lemma_graph

- Lemma 1: A 53-vertex coloring with same-color common-neighborhood size at most 12 on every monochromatic edge implies `R(B13, B13) >= 54`.
- Lemma 2: The Paley graph `P(53)` is self-complementary and 26-regular.
- Lemma 3: Every edge of `P(53)` lies in exactly 12 triangles of `P(53)`.
- Lemma 4: By self-complementarity, every blue edge in the complementary coloring also lies in exactly 12 blue triangles.
- Lemma 5: Therefore the Paley coloring of `K_53` contains no monochromatic `B13`.
- Lemma 6: The packet's cited upper bound gives `R(B13, B13) <= 54`.
- Conclusion: `R(B13, B13) = 54`.

# chosen_plan

- Best path: use the explicit Paley-53 construction as the lower-bound witness and combine it with the packet upper bound.
- Proof skeleton:
  1. Define the Paley coloring on `F_53`.
  2. Show each color class has book size 12.
  3. Deduce a 53-vertex obstruction to monochromatic `B13`.
  4. Invoke the packet upper bound `54`.
  5. Record the resulting exact title theorem `R(B13, B13) = 54`.
- Why this path dominates: it closes the frontier with a compact exact construction and does not require a heavy search or a family-wide forcing argument.

# self_checks

- After statement lock: the micro-paper target remains valid because exact closure here is already the title theorem of a short note.
- After structural route: no contradiction is forced at 53, so switching to an extremal construction is not concept drift.
- After choosing the Paley route: the key risk is an indexing error in the common-neighbor count, not a broad strategic gap.
- Before code: only a tiny witness verification is justified; broad search is not.
- After code: the local check confirms the intended extremal pattern exactly, so the remaining uncertainty is literature-side, not combinatorial.

# code_used

- Tiny local witness verification executed.
- Check performed: build the Paley coloring on `F_53`, then compute all red degrees, all red-edge red codegrees, and all blue-edge blue codegrees.
- Output summary:
  - red degree set = `{26}`,
  - red-edge red-codegree set = `{12}`,
  - blue-edge blue-codegree set = `{12}`.
- Interpretation: the explicit 53-vertex witness behaves exactly as the proof sketch requires.

# result

Provisional exact closure:

- Define a red-blue coloring of `K_53` on vertex set `F_53` by declaring `{x,y}` red iff `x-y` is a nonzero quadratic residue modulo 53, and blue otherwise.
- Since `53 ≡ 1 (mod 4)`, `-1` is a square, so the rule is symmetric in `x,y`.
- Red common-neighbor count:
  for a red edge `{x,y}`, the difference `r = y-x` is a square. Translating by `-x` and then scaling by `r^{-1}` reduces the count of common red neighbors of `{x,y}` to the number
  `N = #{z in F_53 : χ(z) = χ(z-1) = 1}`.
- Let
  `S = sum_{z in F_53} (1 + χ(z))(1 + χ(z-1))`.
  The terms `z = 0,1` contribute `2` each, and every other term contributes `4` exactly when both `z` and `z-1` are nonzero squares and `0` otherwise. Hence `S = 4N + 4`.
- Expanding gives
  `S = 53 + sum_z χ(z(z-1))`,
  because `sum_z χ(z) = sum_z χ(z-1) = 0`.
- By the standard quadratic-character identity `sum_z χ(z(z-1)) = -1`, we get `S = 52`, so `N = 12`.
- Therefore every red edge lies in exactly 12 red triangles. Thus the red graph contains no `B13`.
- The blue graph is obtained from the red graph by multiplying all vertices by any fixed nonsquare in `F_53`, so it is isomorphic to the red graph. Hence every blue edge also lies in exactly 12 blue triangles, and the blue graph also contains no `B13`.
- Therefore this coloring of `K_53` has no monochromatic `B13`, so `R(B13, B13) >= 54`.
- The active packet supplies the matching upper bound `R(B13, B13) <= 54`.
- Hence the exact value is
  `R(B13, B13) = 54`.
- Local computational self-check: a direct exhaustive scan of the Paley coloring on `F_53` confirms that every red and blue edge has exactly 12 same-color common neighbors, so the witness is not merely heuristic.

Supporting paper-shape extraction:

- Smallest supporting theorem slice: the Paley graph `P(53)` is a 53-vertex self-complementary coloring with monochromatic book size exactly 12.
- Immediate corollary / remark: the unresolved one-step interval `53 <= R(B13, B13) <= 54` collapses on the lower-bound side by a finite-field construction, so no 54-vertex forcing argument is needed for closure.
- Why the instance matters: it is an exact closure of a diagonal one-step frontier in a standard Ramsey family, with a compact extremal certificate rather than a large search artifact.
- Minimal remaining packaging work if this survives verification: write the Paley construction cleanly, cite the upper-bound lemma exactly, and check whether this Paley-based exact closure has already been explicitly recorded in the literature.

# family_affinity

- Very strong affinity with diagonal book Ramsey numbers and with self-complementary finite-field extremal constructions.
- The proof is not an isolated ad hoc witness; it sits in the standard Paley / strongly-regular corridor and interacts naturally with the family upper bound `4n + 2`.

# generalization_signal

- What clearly scales: for any prime power `q ≡ 1 (mod 4)`, the Paley graph `P(q)` gives a self-complementary coloring in which each monochromatic edge lies in exactly `(q-5)/4` monochromatic triangles.
- For `q = 4n + 1`, this yields a lower bound
  `R(B_n, B_n) >= q + 1 = 4n + 2`
  whenever `q` exists as a prime power.
- What does not automatically scale: exact closure still also needs the matching upper bound for that same `n`, plus a novelty check that the Paley closure has not already been recorded explicitly.
- Suggested theorem slice if the current result is real: a short lemma isolating the Paley lower-bound mechanism for diagonal books when `4n + 1` is a prime power, then applying it to `n = 13`.

# proof_template_reuse

- Reusable template:
  1. encode the coloring by quadratic residues over `F_q`,
  2. compute monochromatic edge codegrees by a character-sum or standard Paley parameter count,
  3. exploit self-complementarity to transfer the same codegree bound to the opposite color,
  4. combine with a family upper bound.
- This is reusable for nearby diagonal book cases exactly when a suitable prime-power order aligns with the page count.

# candidate_theorem_slice

- Candidate slice: `The Paley graph on 53 vertices gives a red-blue coloring of K_53 with monochromatic book size exactly 12 in each color.`
- Candidate title theorem: `The Exact Value of R(B13, B13)`.
- Current package assessment: if the packet upper bound is confirmed, this is closer to a paper-shaped claim than a mere instance witness because the finite-field construction directly closes the exact frontier.

# smallest_param_shift_to_test

- First shift: test `n` with `4n + 1` prime or prime power and compare against the same upper-bound corridor.
- Most relevant immediate checks: `n = 12` (`4n + 1 = 49`) and `n = 15` (`4n + 1 = 61`).
- Why these help: they show whether the Paley template only explains the `n = 13` case or systematically closes neighboring diagonal cases in the same interval family.

# why_this_is_or_is_not_publishable

- If verification confirms both the packet upper bound and the absence of a prior published exact closure, this is publishable in the micro-paper lane.
- Reason: the exact title theorem is already identified, the proof artifact is compact, and the remaining packaging work is low.
- Current caution: solve-stage confidence is high but not final because the packet citation and novelty status still need verification, and the Paley observation may conceivably already be known implicitly or explicitly.
- Bottom line: this is not too thin for the micro-paper lane if the exact closure survives verification; without verification it remains a strong candidate rather than a finished paper packet.

# paper_shape_support

- Title theorem: `The Exact Value of R(B13, B13)`.
- One immediate remark: the lower-bound witness is algebraic and self-complementary, which makes the note cleaner than a computational extremal search.
- Minimal remaining packaging work:
  1. verify that the cited upper bound is exactly `54`,
  2. novelty-check whether the Paley-53 closure has already appeared,
  3. write the two-paragraph Paley proof and one short discussion paragraph against nearby cases.
- Current estimate: a successful solve here is already roughly 85-90% of a paper.

# boundary_remark

- The argument scales on the lower-bound side through Paley parameters and self-complementarity.
- It does not by itself create a family theorem for all `n`; it only closes cases where the finite-field order and the upper-bound corridor align.
- Natural corollary / boundary sentence: `The case n = 13 is not a search-heavy sporadic exception; it is exactly the Paley order q = 53 case inside the general diagonal-book interval 4n + 1 <= R(B_n, B_n) <= 4n + 2.`

# likely_failure_points

- The main technical risk is a convention mismatch in the definition of `B13`.
- The main literature risk is that the Paley-53 closure may already be an easy folklore observation or an uncited remark in the source paper.
- The main citation risk is that the active packet's `<= 54` upper bound must still be checked against the actual source text during verification.

# what_verify_should_check

- Confirm the exact book-graph convention matches the solve proof.
- Confirm the cited source really gives `R(B13, B13) <= 54`.
- Check whether the Paley-53 construction or an equivalent SRG(53,26,12,13) observation already appears in the cited paper or related book-Ramsey literature.
- If needed, verify the character-sum step or replace it with a direct citation of Paley graph parameters.
- Decide whether the strongest honest publication status is `PAPER_READY` or only `SLICE_EXACT` after novelty checking.

# verify_rediscovery

- PASS 1 used a bounded web audit only.
- Search patterns covered: exact-instance notation (`R(B13,B13)` and `R(B_{13},B_{13})`), alternate notation around book graphs and Paley-53 / SRG(53,26,12,13), the canonical 2025 EJC source, theorem-level checks inside that source corridor, and a recent-status check centered on Wesley (2026).
- Within budget, I did not find an explicit prior exact determination of `R(B13, B13)` or an explicit prior statement that the Paley-53 witness closes the diagonal case.
- The bounded audit is still only negative evidence. The notation is noisy, and I did not obtain a full source-level proof-chain inspection inside this verify pass.
- Rediscovery verdict for this pass: not established within budget.

# verify_faithfulness

- The solve claim is faithful to the intended statement provided one accepts the cited upper bound `R(B13, B13) <= 54`.
- The witness argument is aimed at the exact diagonal problem, not a nearby almost-diagonal proxy: it shows a coloring of `K_53` with no monochromatic `B13`, which is exactly the lower-bound side needed for the least-`n` Ramsey statement.
- No quantifier drift, definition drift, or theorem-swap was found in the local packet.
- The one external dependency is citation faithfulness: the proof as recorded still relies on the packet's statement that Lemma 1 in the 2025 source gives the matching upper bound.

# verify_proof

- I found no internal mathematical error in the local proof sketch.
- The Paley coloring definition is symmetric because `53 ≡ 1 (mod 4)`, so `-1` is a square.
- The reduction from an arbitrary red edge `{x,y}` to the count `#{z : χ(z)=χ(z-1)=1}` is standard affine normalization and is coherent.
- The character-sum calculation to obtain `12` common red neighbors is consistent with the Paley parameter set `(53,26,12,13)`.
- The blue-side transfer by multiplication with a nonsquare is also correct: it swaps squares and nonsquares, so the complement is isomorphic to the red graph.
- First incorrect step found: none in the local argument.
- Remaining proof risk is external rather than internal: the final exact closure still depends on the cited upper bound being accurately inherited from the source.

# verify_adversarial

- There was no saved checker file, so I reran the witness directly from the definition of quadratic residues modulo `53`.
- Independent scan result:
  - red degree set = `{26}`
  - blue degree set = `{26}`
  - red-edge red-codegree set = `{12}`
  - blue-edge blue-codegree set = `{12}`
  - maximum monochromatic book size in each color = `12`
- This adversarial rerun supports the claimed `53`-vertex obstruction and did not expose a broken edge case.
- I did not find a computational contradiction to the witness.

# verify_theorem_worthiness

- Exactness: the local solve packet supports a concrete exact-value claim, but under harness rules it must remain below `EXACT` because Lean is incomplete and publication audit is still pending.
- Novelty: bounded rediscovery checking did not find a prior exact closure, but novelty is not yet sealed strongly enough for a publication claim.
- Reproducibility: high on the lower-bound side; the witness is algebraic and the local rerun reproduced the codegree pattern exactly.
- Lean readiness: not yet. The theorem is formalizable, but Lean is not the shortest remaining path because source-faithfulness and publication-status audit still dominate the remaining uncertainty.
- Paper leverage: high if the source upper bound and novelty survive audit.
- Would this, if correct and Lean-sealed, already constitute most of a publishable note? Yes.
- Estimated paper fraction from one solved claim: about `0.82`.
- Title theorem actually visible: `R(B13, B13) = 54`, with the operational slice that the Paley graph on `53` vertices has monochromatic book size `12` in each color.
- What scales: the Paley lower-bound mechanism for diagonal books when `q = 4n + 1` is a prime power and the corresponding upper-bound corridor is already known.
- What clearly does not scale automatically: exact publication closure for other `n`; each case still needs its own matching upper bound and its own rediscovery audit.
- Best honest publication status now: `SLICE_CANDIDATE`, not `PAPER_READY`, and not merely `INSTANCE_ONLY` because the theorem packet is real if the citation chain holds.

# verify_verdict

- `CANDIDATE_SURVIVES_WITH_CITATION_RISK`
- The bounded rediscovery audit did not establish rediscovery.
- The local proof and rerun support the lower-bound witness.
- The run must stay `CANDIDATE` because the exact closure still depends on a cited upper bound not directly revalidated here and because publication audit has not yet sealed novelty.

# minimal_repair_if_any

- No mathematical repair was needed to the Paley witness.
- Conservative repair applied at the packet level: do not describe the result as finalized exact closure or publication-ready yet.
- Minimal next repair is documentary rather than mathematical:
  1. directly verify the exact upper-bound statement in the cited source text,
  2. perform the publication audit on whether the Paley-53 closure is already explicit or directly implied in prior art,
  3. only then decide whether Lean is the shortest remaining sealing step.

# publication_prior_art_audit

- Bounded web pass on `2026-04-14` covered exact-statement searches (`R(B13,B13)`, `R(B_{13},B_{13})`), alternate-notation / construction searches (`book Ramsey 53 54 B13`, `Paley 53 book Ramsey`), the canonical 2025 EJC source, and one outside-source status pass via Wesley's 2026 paper / 2025 arXiv v2.
- The exact-statement search did not surface a later paper whose title is literally `R(B13,B13)=54`.
- That negative search result does not preserve novelty. The outside-source pass instead exposed a stronger issue: Wesley's 2026 paper reproduces Rousseau-Sheehan Theorem 1 and states that `R(B_n,B_n)=4n+2` whenever `q=4n+1` is a prime power.
- Since `53 = 4*13 + 1` is prime, this published family already gives `R(B13,B13)=54`.
- The 2025 EJC paper independently records the modern corridor `4n+1 <= R(B_n,B_n) <= 4n+2` for `4 <= n <= 21`, so the selected packet's quoted interval `53 <= R(B13,B13) <= 54` is consistent as a weaker modern restatement, not a live frontier gap.
- Prior-art verdict: `REDISCOVERY`. The current slug is not a new exact closure; it is a missed prime-power corollary of published literature.

# publication_statement_faithfulness

- The mathematical object is faithful: `B13` means a book of `13` triangles sharing one spine edge, and the local witness really addresses the diagonal Ramsey statement.
- The packet's open-status framing is not literature-faithful. After the bounded audit, the sentence "current sources stop at `53 <= R(B13,B13) <= 54`" is materially incomplete because published prior work already closes the case when `4n+1` is a prime power.
- The Paley-53 construction remains a faithful lower-bound ingredient, but it is not a new claim in this case.

# publication_theorem_worthiness

- There is a real theorem here: `R(B13,B13)=54`.
- It is stronger than "here is an example", and the lower-bound side is structural rather than hand-picked small-case search.
- But theorem-worthiness for a new paper fails because the exact theorem is already available as a published family corollary.
- A referee asking "what is the theorem?" would get a satisfactory answer mathematically, then immediately object that the theorem is already covered by the prime-power diagonal book result. That objection would be correct.

# publication_publishability

- This is not publishable in the frontier MICRO-PAPER lane.
- The remaining gap is not small editorial residue; the fatal problem is novelty, not proof polish.
- Lean-sealing the Paley witness would only formalize an already-implied result. It would not restore publication status.
- This slug should be moved aside rather than expanded into a larger theorem program.

# publication_packet_audit

- The strongest honest packet is now a documentation packet, not a publication packet: it cleanly instantiates the Paley-53 lower-bound mechanism and explains why the diagonal `n=13` case lands inside an already-published exact family.
- That packet is still useful as internal memory because it preserves a checked witness and the exact reason this target is dead for frontier work.
- Publication-packet quality for new work is therefore low even though the mathematical artifact itself is compact and correct.

# micro_paper_audit

- Is the strongest honest claim stronger than "here is an example"? Yes mathematically, because it identifies an exact value. No as a frontier contribution, because that exact value is already implied in print.
- Would this result, if correct and Lean-sealed, already constitute most of a publishable note? No in the one-shot micro-paper lane, because the novelty barrier has already failed.
- Estimated one-solve-to-paper fraction after audit: about `0.12`, reflecting that what remains is not paper packaging but the impossibility of claiming novelty.
- Is there a real title theorem, theorem slice, or counterexample theorem here? There is a real title theorem mathematically, but not one that remains available for a new frontier note.
- Is the proof structural or merely instance-specific? The lower-bound ingredient is structural / Paley-based; the exact `n=13` closure is a direct family corollary, not a fragile one-off computation.
- Would this survive a referee asking "what is the theorem?" Not as a new paper. The theorem exists, but the rediscovery objection lands first.
- Is the claim still too dependent on hand-picked small cases? No. The problem is prior art, not small-case dependence.
- If this is not yet paper-ready, is the remaining gap genuinely small or did the candidate only look attractive before audit? It only looked attractive before audit because the literature-gap assessment was wrong.
- If this is not yet paper-ready, should it be moved aside rather than expanded into a larger theorem program? Yes.
- Would Lean directly seal the packet, or would it only be optional polish / later archival formalization? Only optional archival formalization.

# strongest_honest_claim

- Published literature already implies `R(B13,B13)=54`. The Paley-53 construction is a correct instantiation of the known prime-power diagonal lower bound, and the exact value is not frontier-novel for `n=13`.

# paper_title_hint

- `No frontier title theorem remains; at best an expository note on the Paley-53 instantiation of a known prime-power diagonal book Ramsey result.`

# next_action

- Mark this slug as `REDISCOVERY`, preserve the checked Paley witness as an internal artifact, and replace the live candidate instead of sending this packet to Lean.
