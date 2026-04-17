# Working Packet: On the Cyclic Hadamard Difference-Set Case (3439,1719,859)

- slug: `cyclic-hadamard-difference-set-3439-1719-859`
- title: Does the cyclic group C_3439 admit a (3439,1719,859)-difference set?
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `88`
- single-solve-to-paper fraction: `0.84`

## statement
Determine whether the cyclic group C_3439 admits a (3439,1719,859)-difference set.

## novelty_notes
- frontier basis: Baumert-Gordon 2004 Table 5 isolates (3439,1719,859) as open, and Gordon's 2019 La Jolla Repository slides still list 3439 among the seven small open cyclic Hadamard cases.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: One exact solve would already remove a named residual case from a standard open-case table in a classical family. The remaining work is mostly exposition, literature placement, and a compact arithmetic certificate.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: low
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: tiny
- assessment: This is a clean micro-paper lane target: exact, source-anchored, theorem-stable, and already framed by the literature as a residual case whose direct resolution would look like a short paper. The main remaining risk is ordinary novelty checking rather than paper shape.

## likely_paper_shape
- note title: On the Cyclic Hadamard Difference-Set Case (3439,1719,859)
- hypothetical title: The cyclic Hadamard difference-set case (3439,1719,859).
- paper shape: A short note eliminating or constructing the smallest surviving cyclic Hadamard case below 10000.
- publication if solved: Settling the smallest surviving cyclic Hadamard case v = 3439 would plausibly yield a focused note removing one of the seven residual cases below 10000.
- minimal artifact requirements: A proof or disproof for the cyclic group of order 3439, the decisive character-sum or multiplier obstruction on n = 860, and a short literature note explaining why 3439 remains outside the already eliminated neighboring cases.

## hypothetical_abstract
We determine whether the cyclic group C_3439 admits a (3439,1719,859)-difference set. Baumert and Gordon list this exact parameter set as open in their 2004 table of cyclic Hadamard survivors, and Gordon's 2019 La Jolla Repository slides still retain 3439 among the seven small unresolved cases below 10000. A resolution would therefore stand as the title theorem of a short note removing one explicit residual case from the cyclic Hadamard landscape.

## single_solve_explanation
The literature already packages the frontier as a named residual table entry, so solving the exact case would supply the core mathematical contribution immediately. Little beyond a careful writeup, a bounded prior-art note, and the proof certificate would remain. Because the group is uniquely cyclic and the family label is already canonical, the honest paper title does not need to drift after the solve.

## broader_theorem_nonimplication
The canonical 2004 table explicitly leaves 3439 open while marking six nearby cases as already eliminated by Lander's theorems, and the 2019 slides still list 3439 as unresolved. The surfaced literature therefore does not already collapse this case into a broader published theorem.

## literature_gap
Baumert-Gordon 2004 Table 5 leaves the exact cyclic Hadamard parameter set (3439,1719,859) open, and Gordon's 2019 slides continue to list 3439 among the small surviving cases without a later exact settlement.

## transfer_kit
- lemma: Baumert-Gordon 2004 Table 5 isolates (3439,1719,859) as an open cyclic Hadamard case.
- lemma: The same table shows six nearby cyclic Hadamard cases already eliminated by specific theorems from Lander's book, so the remaining case sits just beyond current off-the-shelf eliminations.
- lemma: Gordon's 2019 slides still list 3439 among the seven small open cyclic Hadamard cases below 10000.
- lemma: Any cyclic difference set must satisfy the standard group-ring and character equations D D^(-1) = n + lambda G and |chi(D)|^2 = n for nontrivial characters.
- toy example: Compare 3439 with the neighboring excluded case 4623 from the same 2004 table to see exactly where existing Lander-type eliminations stop.
- known obstruction: The standard cyclic Hadamard restrictions already kill several nearby cases, so any proof for 3439 must exploit a finer arithmetic obstruction rather than replaying the textbook eliminations.
- prior-work stop sentence: The literature surface used here stops at listing (3439,1719,859) as an exact open cyclic Hadamard case and does not provide a later case-specific resolution.
- recommended first attack: Exploit the factorization n = 860 = 2^2 * 5 * 43 together with multiplier and character-sum constraints in the cyclic group of order 3439.
- paper if solved: If solved exactly, the paper would be a short note removing the cyclic Hadamard case (3439,1719,859) from the small-open-case list.

## bounded_source_list
- Leonard D. Baumert and Daniel M. Gordon, "On the existence of cyclic difference sets with small parameters" (Fields Institute Communications 41, 2004), Table 5 listing (3439,1719,859) as open among the cyclic Hadamard cases up to v = 10000; status rechecked against Daniel M. Gordon, "The La Jolla Difference Set Repository" slides (2019), cyclic-Hadamard slide listing 3439 among the seven small open cases.
- Baumert-Gordon 2004 Table 5, Gordon's 2019 La Jolla Difference Set Repository slides on cyclic Hadamard cases, the local attempt/source/paper/search memory, and bounded exact-tuple status searches that did not surface a later settlement.
- artifacts/cyclic-hadamard-difference-set-3439-1719-859/record.md
- artifacts/cyclic-hadamard-difference-set-3439-1719-859/status.json
