# Working Packet: On the Cyclic Hadamard Difference-Set Case (4355,2177,1088)

- slug: `cyclic-hadamard-difference-set-4355-2177-1088`
- title: Does the cyclic group C_4355 admit a (4355,2177,1088)-difference set?
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `84`
- single-solve-to-paper fraction: `0.81`

## statement
Determine whether the cyclic group C_4355 admits a (4355,2177,1088)-difference set.

## novelty_notes
- frontier basis: Baumert-Gordon 2004 Table 5 isolates (4355,2177,1088) as open, and Gordon's 2019 La Jolla Repository slides still retain 4355 among the seven small open cyclic Hadamard cases.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: A direct resolution would immediately close one of the canonical residual cases in a classical open family. Beyond the solve, only bounded exposition and literature positioning remain.
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
- assessment: This is a viable micro-paper lane target with strong family anchor and stable theorem slice. It is slightly less attractive than 3439 only because it is the second-smallest surviving cyclic Hadamard case rather than the smallest.

## likely_paper_shape
- note title: On the Cyclic Hadamard Difference-Set Case (4355,2177,1088)
- hypothetical title: The cyclic Hadamard difference-set case (4355,2177,1088).
- paper shape: A short note eliminating or constructing the cyclic Hadamard case (4355,2177,1088).
- publication if solved: Settling the cyclic Hadamard case v = 4355 would plausibly yield a focused note removing another named survivor from the sub-10000 open list.
- minimal artifact requirements: A proof or disproof for the cyclic group of order 4355, the decisive character-sum or multiplier obstruction on n = 1089, and a short literature note explaining why the case remains outside existing Lander-type eliminations.

## hypothetical_abstract
We determine whether the cyclic group C_4355 admits a (4355,2177,1088)-difference set. Baumert and Gordon list this exact parameter set as open in their 2004 table of cyclic Hadamard survivors, and Gordon's 2019 La Jolla Repository slides still retain 4355 among the seven small unresolved cases below 10000. A resolution would therefore support a short paper whose title theorem is exactly this residual cyclic Hadamard case.

## single_solve_explanation
The mathematical contribution is already packaged by the literature as a single residual case, so one exact solve would do almost all of the paper's substantive work. What remains is a bounded writeup and the final novelty note. Because the cyclic case is exact and family-labeled, the proof does not need feeder lemmas from a broader campaign to become paper-shaped.

## broader_theorem_nonimplication
The canonical 2004 open-case table and Gordon's 2019 slides both still leave 4355 unresolved while adjacent cyclic Hadamard cases are marked as eliminated. The surfaced literature therefore does not already imply the exact 4355 statement via a broader theorem.

## literature_gap
Baumert-Gordon 2004 Table 5 leaves the exact cyclic Hadamard parameter set (4355,2177,1088) open, and Gordon's 2019 slides continue to list 4355 among the small surviving cases without a later case-specific resolution.

## transfer_kit
- lemma: Baumert-Gordon 2004 Table 5 isolates (4355,2177,1088) as an open cyclic Hadamard case.
- lemma: The same table marks several neighboring cyclic Hadamard cases as already excluded by Lander theorems, clarifying the exact residual frontier.
- lemma: Gordon's 2019 slides still list 4355 among the seven small open cyclic Hadamard cases below 10000.
- lemma: Any cyclic difference set must satisfy the standard group-ring and character equations D D^(-1) = n + lambda G and |chi(D)|^2 = n for nontrivial characters.
- toy example: Compare 4355 with the neighboring excluded case 5775 from the same 2004 table to see how the exact residual case sits beyond the current theorem surface.
- known obstruction: Existing cyclic Hadamard restrictions already dispose of many nearby values, so any proof for 4355 must exploit arithmetic information finer than the standard eliminators.
- prior-work stop sentence: The literature surface used here stops at listing (4355,2177,1088) as an exact open cyclic Hadamard case and does not provide a later case-specific resolution.
- recommended first attack: Exploit the square order n = 1089 = 3^2 * 11^2 together with multiplier and character-sum constraints in the cyclic group of order 4355.
- paper if solved: If solved exactly, the paper would be a short note removing the cyclic Hadamard case (4355,2177,1088) from the small-open-case list.

## bounded_source_list
- Leonard D. Baumert and Daniel M. Gordon, "On the existence of cyclic difference sets with small parameters" (Fields Institute Communications 41, 2004), Table 5 listing (4355,2177,1088) as open among the cyclic Hadamard cases up to v = 10000; status rechecked against Daniel M. Gordon, "The La Jolla Difference Set Repository" slides (2019), cyclic-Hadamard slide listing 4355 among the seven small open cases.
- Baumert-Gordon 2004 Table 5, Gordon's 2019 La Jolla Difference Set Repository slides on cyclic Hadamard cases, the local attempt/source/paper/search memory, and bounded exact-tuple status searches that did not surface a later settlement.
- artifacts/cyclic-hadamard-difference-set-4355-2177-1088/record.md
- artifacts/cyclic-hadamard-difference-set-4355-2177-1088/status.json
