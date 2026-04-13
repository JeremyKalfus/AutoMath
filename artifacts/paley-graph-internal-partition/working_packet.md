# Working Packet: Internal Partitions in Paley Graphs

- slug: `paley-graph-internal-partition`
- title: Does every Paley graph have an internal partition?
- publication status: `SLICE_CANDIDATE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `74`
- single-solve-to-paper fraction: `0.78`

## statement
Settle the Paley-family problem outright, either by proving all Paley graphs admit internal partitions or by finding a minimal counterexample within the residue-graph family.

## novelty_notes
- frontier basis: The 2024 internal-partitions paper lists the Paley-family problem explicitly as Problem 7.
- why still open: The 2024 paper lists the Paley statement explicitly as Problem 7, and the bounded outside-status search did not turn up any later resolution.
- attempted conflict check: The repo exclusion sweep found no prior attempt, active campaign, or archived near-duplicate around Paley internal partitions.
- rediscovery risk: low

## proof_sketch
- attack style: quadratic-residue symmetry plus cohesive-set and near-bisection arguments specialized to Paley graphs
- likely route: Any family-wide solution or first counterexample would already be a referee-facing theorem on a famous graph class.
- verifier focus: A positive witness is a partition with local neighbour-count checks; a negative solution needs a rigorous structural obstruction, not a heuristic search trace.

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: moderate
- immediate corollary headroom: moderate
- isolated exact-case risk: low
- broader-theorem implication risk: low
- search-heavy: False
- certificate compactness: high
- exact gap from source: broad
- assessment: Pass, but lower priority: the paper shape is excellent, yet the target is a full family theorem rather than a tiny exact residue.

## likely_paper_shape
- note title: Internal Partitions in Paley Graphs
- hypothetical title: Internal Partitions in Paley Graphs
- paper shape: A family theorem on a canonical pseudorandom graph class, with either a universal construction or a first counterexample and structural explanation.
- publication if solved: A complete Paley-family theorem is immediately paper-ready because the family is classical and the statement is already singled out as a named open problem.
- minimal artifact requirements: Either a constructive partition rule across the family or a rigorous first counterexample with local neighbour-count verification.

## hypothetical_abstract
We settle the Paley internal-partition problem posed in the 2024 internal-partitions note. Using the additive and multiplicative symmetries of Paley graphs, we either construct internal partitions uniformly across the family or isolate a first counterexample together with the structural obstruction that forces it. Because the family is classical and the theorem statement is already singled out in the literature, the solve itself supplies most of a finished note.

## single_solve_explanation
The source already frames this as a standalone open problem on a famous graph family, so a full solve immediately gives the paper title, statement, and motivation. After the solve, the remaining work is mainly a brief background paragraph on internal partitions, a polished proof, and one or two remarks comparing Paley graphs with the general regular-graph setting. The main caution is breadth, not packaging.

## broader_theorem_nonimplication
The 2024 paper poses the Paley-family statement as an open problem rather than deducing it from a broader theorem, and bounded status checks found no later family-wide implication closing it.

## literature_gap
The recent internal-partitions paper records the Paley-family statement as an explicit open problem and does not advance beyond posing it.

## transfer_kit
- lemma: Paley graphs are regular self-complementary Cayley graphs on F_q, so additive and multiplicative symmetries are available from the start.
- lemma: Internal partitions are verified purely by local neighbour counts across the chosen bipartition, giving a tiny checker once a candidate partition is proposed.
- lemma: The 2024 paper already isolates the Paley-family statement as a named open problem, so any structural Paley-specific lemma feeds directly into the final theorem narrative.
- toy example: P(5) = C_5 is the smallest sanity-check model for the partition condition and keeps the neighbour-count verification completely explicit.
- known obstruction: Paley graphs are pseudo-random enough that naive bisection or switching heuristics may not preserve the internal condition.
- prior-work stop sentence: The recent internal-partitions paper states the Paley-family theorem as an explicit open problem and stops there.
- recommended first attack: Search for a residue-class based partition or a canonical near-bisection stabilized by the Paley automorphism group.
- paper if solved: The paper would be a single family-theorem note on a classical algebraic graph family, with one proof section and a short comparison to the general internal-partition literature.

## bounded_source_list
- Pál Bärnkopf, Zoltán Lóránt Nagy, and Zoltán Paulovics, "A Note on Internal Partitions: The 5-Regular Case and Beyond" (Graphs and Combinatorics, 2024), Problem 7.
- The 2024 internal-partitions note, standard Paley graph background, and one bounded later-status search.
- artifacts/paley-graph-internal-partition/record.md
- artifacts/paley-graph-internal-partition/status.json
