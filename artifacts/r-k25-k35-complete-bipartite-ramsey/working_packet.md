# Working Packet: The Exact Value of R(K2,5, K3,5)

- slug: `r-k25-k35-complete-bipartite-ramsey`
- title: Determine the exact value of R(K2,5, K3,5)
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `84`
- single-solve-to-paper fraction: `0.84`

## statement
Determine the least n such that every red-blue coloring of K_n contains either a red K2,5 or a blue K3,5.

## novelty_notes
- frontier basis: Current public sources leave this mixed complete-bipartite Ramsey number at 22 <= R(K2,5, K3,5) <= 23. That is already a one-step finite frontier after the 2025 lower-bound improvement and the 2021 SDP upper bound.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the endpoint 22 versus 23 is settled, the note already has its title theorem, main comparison with prior work, and exact frontier claim. What remains is mainly a compact critical coloring or a short forcing argument, plus a brief placement beside the nearby exact bipartite cases.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: low
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: high
- exact gap from source: tiny
- assessment: Pass. This is the cleanest untouched one-step graph Ramsey gap found in the bounded curation pass, and one exact solve would already account for most of a short publishable note.

## likely_paper_shape
- note title: The Exact Value of R(K2,5, K3,5)
- hypothetical title: The Exact Value of R(K2,5, K3,5)
- paper shape: A one-theorem exact-value note closing a one-step mixed bipartite Ramsey gap.
- publication if solved: An exact determination of R(K2,5, K3,5) would read as the title theorem of a short note because the public frontier is already a one-step mixed complete-bipartite Ramsey gap.
- minimal artifact requirements: Either an explicit 22-vertex coloring avoiding red K2,5 and blue K3,5, or a compact proof that every 23-vertex coloring forces one of them.

## hypothetical_abstract
We determine the two-color Ramsey number R(K2,5, K3,5). Previous work left this number in the interval 22 <= R(K2,5, K3,5) <= 23. Our result closes the remaining one-step gap for this mixed complete-bipartite pair.

## single_solve_explanation
This target cleanly passes the 70-90% paper test because the public frontier is already one endpoint wide. Once the exact value is known, the note is mostly a short extremal construction or forcing proof together with a minimal literature comparison. There is no feeder ladder between the solve and the paper-shaped claim.

## broader_theorem_nonimplication
Known exact results for neighboring bipartite pairs such as R(K3,4, K3,4) and R(K3,5, K3,5) do not force the mixed pair R(K2,5, K3,5). The bounded audit did not uncover a broader theorem that collapses the 22 versus 23 endpoint automatically.

## literature_gap
Current public sources stop at 22 <= R(K2,5, K3,5) <= 23.

## transfer_kit
- lemma: Ghebleh et al. (2025) provide the current lower bound R(K2,5, K3,5) >= 22.
- lemma: By symmetry of two-color Ramsey numbers, Lidicky-Pfender (2021), Theorem 7, gives the upper bound R(K2,5, K3,5) = R(K3,5, K2,5) <= 23.
- lemma: The 2022 small-Ramsey bounds paper records the exact neighboring value R(K3,4, K3,4) = 25, giving a nearby solved model in the same complete-bipartite corridor.
- lemma: The same 2022 paper records the exact neighboring value R(K3,5, K3,5) = 33, showing the family is publication-legible through exact finite endpoint papers.
- toy example: The exact case R(K3,4, K3,4) = 25 is the nearest solved mixed-bipartite benchmark for how a finite exact-value note in this family can look.
- known obstruction: A lower-bound coloring can stay dense while suppressing K2,5 in one color and K3,5 in the other, so any upper-bound proof must rule out the last 22-vertex critical configuration family without drifting into a broad census.
- prior-work stop sentence: Current sources stop at 22 <= R(K2,5, K3,5) <= 23.
- recommended first attack: Start from the 2025 lower-bound construction and test whether every extension by one new vertex forces either a red K2,5 or a blue K3,5, while tracking degree-pattern restrictions suggested by the 2021 SDP upper bound.
- paper if solved: The paper would be a short exact-value note closing a one-step mixed complete-bipartite Ramsey gap.

## bounded_source_list
- Mohammad Ghebleh, Salem Al-Yakoob, Ali Kanso, and Dragan Stevanovic, "Reinforcement learning for graph theory, II. Small Ramsey numbers" (The Art of Discrete and Applied Mathematics 8(1) (2025)), abstract giving R(K_{2,5}, K_{3,5}) >= 22; together with Bernard Lidicky and Florian Pfender, "Semidefinite Programming and Ramsey Numbers" (SIAM J. Discrete Math. 35(4) (2021)), Theorem 7, giving R(K3,5, K2,5) <= 23; and bounded 2026-04-14 recent-status web checks that did not reveal a later exact determination.
- 2025 Ghebleh-Al-Yakoob-Kanso-Stevanovic abstract-level lower-bound source, 2021 Lidicky-Pfender Theorem 7 for the upper bound, nearby exact bipartite Ramsey values from the 2022 bounds paper, and bounded 2026-04-14 recent-status web checks.
- artifacts/r-k25-k35-complete-bipartite-ramsey/record.md
- artifacts/r-k25-k35-complete-bipartite-ramsey/status.json
