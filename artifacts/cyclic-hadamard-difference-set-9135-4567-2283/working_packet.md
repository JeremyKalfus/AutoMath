# Working Packet: On the Cyclic Hadamard Difference-Set Case (9135,4567,2283)

- slug: `cyclic-hadamard-difference-set-9135-4567-2283`
- title: Does the cyclic group C_9135 admit a (9135,4567,2283)-difference set?
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `82`
- single-solve-to-paper fraction: `0.8`

## statement
Determine whether the cyclic group C_9135 admits a (9135,4567,2283)-difference set.

## novelty_notes
- frontier basis: Baumert-Gordon 2004 Table 5 isolates (9135,4567,2283) as open, Gordon's 2019 La Jolla Repository slides still list 9135 among the seven small open cyclic Hadamard cases, and a 2026 status slide repeats the same seven values.
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
- assessment: This is a clean micro-paper lane target: exact, source-anchored, theorem-stable, and still explicitly present in the modern small-open-case list. It ranks slightly below 8591 and 8835 only because the arithmetic certificate looks a bit less compact.

## likely_paper_shape
- note title: On the Cyclic Hadamard Difference-Set Case (9135,4567,2283)
- hypothetical title: The cyclic Hadamard difference-set case (9135,4567,2283).
- paper shape: A short note eliminating or constructing the cyclic Hadamard case (9135,4567,2283).
- publication if solved: Settling the cyclic Hadamard case v = 9135 would plausibly yield a focused note removing another named survivor from the sub-10000 open list.
- minimal artifact requirements: A proof or disproof for the cyclic group of order 9135, the decisive multiplier or character-sum obstruction exploiting 3-, 5-, 7-, and 29-quotients together with n = 2^2 * 571, and a short literature note explaining why 9135 remains outside the current eliminations.

## hypothetical_abstract
We determine whether the cyclic group C_9135 admits a (9135,4567,2283)-difference set. Baumert and Gordon list this exact parameter set as open in their 2004 table of cyclic Hadamard survivors, Gordon's 2019 La Jolla Repository slides still retain 9135 among the seven small unresolved cases below 10000, and a 2026 status slide repeats the same seven values. A resolution would therefore stand as the title theorem of a short note removing one explicit residual case from the cyclic Hadamard landscape.

## single_solve_explanation
The literature already packages the frontier as a named residual table entry, so solving the exact case would supply the core mathematical contribution immediately. Little beyond a careful writeup, a bounded prior-art note, and the proof certificate would remain. Because the group is uniquely cyclic and the family label is already canonical, the honest paper title does not need to drift after the solve.

## broader_theorem_nonimplication
The canonical 2004 table explicitly leaves 9135 open while nearby cases are already eliminated, and the 2019 and 2026 status sources still list 9135 as unresolved. The surfaced literature therefore does not already collapse this case into a broader published theorem.

## literature_gap
Baumert-Gordon 2004 Table 5 and Gordon's 2019 cyclic-Hadamard slide both leave (9135,4567,2283) unresolved, and bounded 2026 status checks still present 9135 among the same seven sub-10000 survivors without a later exact settlement.

## transfer_kit
- lemma: Baumert-Gordon 2004 Table 5 isolates (9135,4567,2283) as an open cyclic Hadamard case.
- lemma: The same table shows nearby cyclic Hadamard cases already eliminated by Lander theorems, clarifying the residual frontier.
- lemma: Gordon's 2019 slides still list 9135 among the seven small open cyclic Hadamard cases below 10000, and a 2026 status slide repeats the same seven values.
- lemma: Any cyclic difference set must satisfy the standard group-ring and character equations D D^(-1) = n + lambda G and |chi(D)|^2 = n for nontrivial characters.
- toy example: Compare 9135 with the nearby excluded case 8463 from the same 2004 table to see where the standard eliminators stop and the unresolved residue begins.
- known obstruction: Existing cyclic Hadamard restrictions already kill several nearby values, so any proof for 9135 must exploit finer arithmetic than the standard eliminators.
- prior-work stop sentence: The literature surface used here stops at listing (9135,4567,2283) as an exact open cyclic Hadamard case and does not provide a later case-specific resolution.
- recommended first attack: Exploit 3-, 5-, 7-, and 29-quotient profile constraints together with n = 2^2 * 571 and multiplier or character-sum conditions in the cyclic group of order 9135.
- paper if solved: If solved exactly, the paper would be a short note removing the cyclic Hadamard case (9135,4567,2283) from the small-open-case list.

## bounded_source_list
- Leonard D. Baumert and Daniel M. Gordon, "On the existence of cyclic difference sets with small parameters" (Fields Institute Communications 41, 2004), Table 5 listing (9135,4567,2283) as open among the cyclic Hadamard cases up to v = 10000; status rechecked against Daniel M. Gordon, "The La Jolla Difference Set Repository" talk slides (ArasuFest, August 3, 2019), cyclic-Hadamard slide listing 9135 among the seven small open cases.
- Baumert-Gordon 2004 Table 5, Gordon's 2019 La Jolla Difference Set Repository slides on cyclic Hadamard cases, Hong-Yeop Song's 2026 status slide repeating the same seven v < 10000 cases, the local attempt/source/paper/search memory, and bounded exact-tuple web searches that did not surface a later exact settlement.
- artifacts/cyclic-hadamard-difference-set-9135-4567-2283/record.md
- artifacts/cyclic-hadamard-difference-set-9135-4567-2283/status.json
