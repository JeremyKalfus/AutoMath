# Working Packet: The First Residual Weight-36 Circulant Weighing Matrix Case

- slug: `circulant-weighing-matrix-105-36`
- title: circulant-weighing-matrix-105-36
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `False`
- paper leverage score: `72`
- single-solve-to-paper fraction: `0.74`

## statement
Determine whether there exists a circulant weighing matrix of order 105 and weight 36.

## novelty_notes
- frontier basis: Arasu-Gordon-Zhang isolate a short remaining weight-36 list after their eliminations, and the current Gordon repository still tracks CW(105,36) as part of that residual frontier.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If CW(105,36) is settled, the source literature already supplies the finite residual table, the multiplier framework, and the exact narrative for why this case matters. The note would mainly present the decisive construction or nonexistence certificate and explain how it closes the first remaining weight-36 slot.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: True
- certificate compactness: moderate
- exact gap from source: tiny
- assessment: Strong paper shape if solved, but not lane-eligible for the strict micro-paper objective because the most plausible route remains computationally narrow rather than a clearly compact one-pass argument.

## likely_paper_shape
- note title: The First Residual Weight-36 Circulant Weighing Matrix Case
- hypothetical title: On the Existence of CW(105,36)
- paper shape: A one-theorem note settling the first remaining weight-36 circulant weighing-matrix case in the Strassler/Gordon frontier.
- publication if solved: A construction or nonexistence proof for CW(105,36) would plausibly support a short note settling the first surviving weight-36 case from the current Strassler/Gordon circulant weighing-matrix frontier.
- minimal artifact requirements: Either an explicit first row for a CW(105,36), or a compact nonexistence proof or orbit-exhaust certificate strong enough to exclude all multiplier-compatible possibilities.

## hypothetical_abstract
We determine the existence status of the circulant weighing matrix CW(105,36). The current Strassler/Gordon frontier leaves this parameter as the first surviving weight-36 case after the nonexistence results of Arasu, Gordon, and Zhang. A resolution therefore yields a self-contained residual-case note with only light frontier recap beyond the decisive argument.

## single_solve_explanation
Because the literature already compresses the weight-36 frontier into a short residual list, an exact resolution of CW(105,36) would immediately give the title theorem of a short paper. The remaining work would mostly restate the frontier, document the multiplier-orbit setup, and present the final certificate. The main reason this stays out of the strict lane is that the likeliest proof route still looks computation-heavy.

## broader_theorem_nonimplication
The Arasu-Gordon-Zhang paper explicitly leaves CW(105,36) in its residual open list after applying its available multiplier and contracted-multiplier machinery, and the current Gordon repository continues to treat it as unresolved rather than absorbed by a later general theorem.

## literature_gap
After the 2019/2021 eliminations, the residual weight-36 frontier still includes CW(105,36), and the current Gordon repository does not record a later resolution.

## transfer_kit
- lemma: Theorem 2.1 in Arasu-Gordon-Zhang gives the self-conjugacy obstruction that forces trivial folded intersection numbers in favorable modulus settings.
- lemma: Theorem 2.2 supplies multiplier orbits for prime-power weights relatively prime to the order, reducing supports to unions of multiplier orbits.
- lemma: Lemma 1 gives the folded intersection-number equations that every candidate CW(n,36) must satisfy before any search begins.
- lemma: Theorem 4.1 provides contracted multipliers for residual open cases and is exactly the tool the source uses to keep the weight-36 residue small.
- toy example: The paper's Proposition 1 and its surrounding orbit table provide a model hand-checkable elimination of a smaller open circulant weighing-matrix case by multiplier-orbit bookkeeping.
- known obstruction: Current multiplier and contracted-multiplier reductions have not yet forced a contradiction for CW(105,36), so any successful proof must either finish a narrowed exhaustive orbit search or add a sharper arithmetic obstruction.
- prior-work stop sentence: The source literature still leaves CW(105,36) inside the residual weight-36 open list after the currently published eliminations.
- recommended first attack: Exploit the contracted-multiplier setup already available for the weight-36 residue and try to finish the orbit table with a bounded exhaustive elimination that can be written up as a short certificate rather than a broad search campaign.
- paper if solved: If solved exactly, the paper would be a one-theorem note closing the first residual weight-36 circulant weighing-matrix case.

## bounded_source_list
- Daniel M. Gordon, Circulant Weighing Matrices (La Jolla Combinatorics Repository / Jupyter Book, 2022; GitHub dataset release visible as May 16, 2025), together with K.T. Arasu, Daniel M. Gordon, and Yiran Zhang, "New Nonexistence Results on Circulant Weighing Matrices" (arXiv:1908.08447, consulted via arXiv/ar5iv on 2026-04-15), especially the introduction stating that 34 Strassler-table cases remained before that paper's eliminations and Section 5 / Table 10 listing the surviving open weight-36 cases including CW(105,36).
- Strassler's circulant weighing-matrix table as updated by Tan, the Arasu-Gordon-Zhang 2019/2021 elimination paper, and Gordon's 2022/2025 repository snapshot.
- artifacts/circulant-weighing-matrix-105-36/record.md
- artifacts/circulant-weighing-matrix-105-36/status.json
