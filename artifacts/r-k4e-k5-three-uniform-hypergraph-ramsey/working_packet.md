# Working Packet: The Exact Value of R(K4-e, K5; 3)

- slug: `r-k4e-k5-three-uniform-hypergraph-ramsey`
- title: Determine the exact value of R(K4-e, K5; 3)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `69`
- single-solve-to-paper fraction: `0.72`

## statement
Determine the least n such that every red-blue coloring of the triples of an n-element set contains either a red 3-uniform K4-e or a blue 3-uniform K5.

## novelty_notes
- frontier basis: Current public sources leave this 3-uniform Ramsey number at 14 <= R(K4-e, K5; 3) <= 16. The 2021 paper introduced the first published upper bound and left only a small exact gap.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: A precise endpoint would already give the note its title theorem and core content. The remaining work would be to package the exact forcing or extremal construction cleanly and relate it to the neighboring exact 3-uniform cases.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: moderate
- publication narrative strength: moderate
- editorial overhead: moderate
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: small
- assessment: Borderline pass. The gap is wider and the proof could sprawl, but the family anchor is still good enough that one exact solve could plausibly support a short note.

## likely_paper_shape
- note title: The Exact Value of R(K4-e, K5; 3)
- hypothetical title: The Exact Value of R(K4-e, K5; 3)
- paper shape: A short exact-value note in a small 3-uniform missing-edge-versus-clique family.
- publication if solved: An exact determination of R(K4-e, K5; 3) would likely support a compact note because the family is standard and the interval is already only three values wide.
- minimal artifact requirements: Either a 15-vertex extremal coloring of triples avoiding red K4-e and blue K5, or a forcing proof that every 16-vertex coloring already contains one.

## hypothetical_abstract
We determine the 3-uniform hypergraph Ramsey number R(K4-e, K5; 3). Previous work gave 14 <= R(K4-e, K5; 3) <= 16 and did not settle the finite endpoint. Our result closes this remaining gap for the smallest missing-edge-versus-clique case still left open in the bounded audit.

## single_solve_explanation
This is still paper-shaped because the main theorem is already clear and narrowly scoped. After an exact solve, most of the remaining work is presenting the witness or forcing proof and positioning it beside the neighboring exact hypergraph values. The wider interval makes it weaker than the top one-step candidate.

## broader_theorem_nonimplication
The bounded audit did not locate a broader published theorem that forces the exact endpoint here. The 2021 result narrows the finite search space but does not collapse the value to 14, 15, or 16 automatically.

## literature_gap
Current public sources stop at 14 <= R(K4-e, K5; 3) <= 16.

## transfer_kit
- lemma: Lidicky-Pfender (2021), Theorem 9, gives the upper bound R(K4-e, K5; 3) <= 16.
- lemma: The same theorem records the known lower bound 14 <= R(K4-e, K5; 3).
- lemma: The exact result R(K4-e, K5-e; 3) = 12 from the same paper gives a nearby calibration point for proof scale.
- lemma: The 2021 paper explicitly notes that no previous upper bound was known, so the finite interval is a recent frontier slice rather than a classical rediscovery trap.
- toy example: The exact neighboring case R(K4-e, K5-e; 3) = 12 from the same source is the closest worked exact benchmark.
- known obstruction: Blue K5 avoidance still allows many dense local triple systems, while red K4-e avoidance constrains link graphs only indirectly, so an exact proof can expand quickly.
- prior-work stop sentence: Current sources stop at 14 <= R(K4-e, K5; 3) <= 16.
- recommended first attack: Start from the 2021 SDP obstruction patterns and try to classify feasible link graphs on a hypothetical 15-vertex extremal coloring before any brute-force search.
- paper if solved: The paper would be a compact exact-value note for a small 3-uniform missing-edge-versus-clique Ramsey number.

## bounded_source_list
- Bernard Lidicky and Florian Pfender, "Semidefinite Programming and Ramsey Numbers" (SIAM J. Discrete Math. 35(4) (2021)), Theorem 9, which gives 14 <= R(K4-e, K5; 3) <= 16; together with bounded 2026-04-14 survey and recent-status web checks during curation that did not reveal a later exact determination.
- 2021 Lidicky-Pfender Theorem 9 and surrounding hypergraph discussion, plus bounded 2026-04-14 recent-status web checks.
- artifacts/r-k4e-k5-three-uniform-hypergraph-ramsey/record.md
- artifacts/r-k4e-k5-three-uniform-hypergraph-ramsey/status.json
