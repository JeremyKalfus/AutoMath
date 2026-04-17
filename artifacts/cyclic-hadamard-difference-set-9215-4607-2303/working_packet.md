# Working Packet: On the Cyclic Hadamard Difference-Set Case (9215,4607,2303)

- slug: `cyclic-hadamard-difference-set-9215-4607-2303`
- title: Does the cyclic group C_9215 admit a (9215,4607,2303)-difference set?
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `79`
- single-solve-to-paper fraction: `0.78`

## statement
Determine whether the cyclic group C_9215 admits a (9215,4607,2303)-difference set.

## novelty_notes
- frontier basis: Baumert-Gordon 2004 Table 5 isolates (9215,4607,2303) as open, Gordon's 2019 La Jolla Repository slides still list 9215 among the seven small open cyclic Hadamard cases, and a 2026 status slide repeats the same seven values.
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
- assessment: This remains lane-eligible because the exact case is source-anchored and theorem-stable, and one clean solve would still look like the title theorem of a short note. It ranks below the top three only because the publication packet feels slightly less crisp at current audit depth.

## likely_paper_shape
- note title: On the Cyclic Hadamard Difference-Set Case (9215,4607,2303)
- hypothetical title: The cyclic Hadamard difference-set case (9215,4607,2303).
- paper shape: A short note eliminating or constructing the cyclic Hadamard case (9215,4607,2303).
- publication if solved: Settling the cyclic Hadamard case v = 9215 would plausibly yield a focused note removing another named survivor from the sub-10000 open list.
- minimal artifact requirements: A proof or disproof for the cyclic group of order 9215, the decisive multiplier or character-sum obstruction exploiting 5-, 19-, and 97-quotients together with n = 2^8 * 3^2, and a short literature note explaining why 9215 remains outside the current eliminations.

## hypothetical_abstract
We determine whether the cyclic group C_9215 admits a (9215,4607,2303)-difference set. Baumert and Gordon list this exact parameter set as open in their 2004 table of cyclic Hadamard survivors, Gordon's 2019 La Jolla Repository slides still retain 9215 among the seven small unresolved cases below 10000, and a 2026 status slide repeats the same seven values. A resolution would therefore support a short note whose title theorem is exactly this residual cyclic Hadamard case.

## single_solve_explanation
The literature already packages the frontier as a named residual table entry, so solving the exact case would supply the paper's core mathematical contribution immediately. What remains is a bounded writeup and the final literature note. Because the theorem slice is exact and family-labeled, the result would already look like the title theorem of a short note.

## broader_theorem_nonimplication
The canonical 2004 table and the 2019 and 2026 status sources still leave 9215 unresolved while nearby cyclic Hadamard cases are marked as eliminated. The surfaced literature therefore does not already imply the exact 9215 statement via a broader theorem.

## literature_gap
Baumert-Gordon 2004 Table 5 and Gordon's 2019 cyclic-Hadamard slide both leave (9215,4607,2303) unresolved, and bounded 2026 status checks still present 9215 among the same seven sub-10000 survivors without a later exact settlement.

## transfer_kit
- lemma: Baumert-Gordon 2004 Table 5 isolates (9215,4607,2303) as an open cyclic Hadamard case.
- lemma: The same table shows nearby cyclic Hadamard cases already eliminated by Lander theorems, clarifying the residual frontier.
- lemma: Gordon's 2019 slides still list 9215 among the seven small open cyclic Hadamard cases below 10000, and a 2026 status slide repeats the same seven values.
- lemma: Any cyclic difference set must satisfy the standard group-ring and character equations D D^(-1) = n + lambda G and |chi(D)|^2 = n for nontrivial characters.
- toy example: Compare 9215 with the nearby excluded case 8463 from the same 2004 table to see where the standard eliminators stop and the unresolved residue begins.
- known obstruction: Existing cyclic Hadamard restrictions already eliminate several nearby values, so any proof for 9215 must use finer arithmetic than the standard textbook filters.
- prior-work stop sentence: The literature surface used here stops at listing (9215,4607,2303) as an exact open cyclic Hadamard case and does not provide a later case-specific resolution.
- recommended first attack: Exploit 5-, 19-, and 97-quotient profile constraints together with n = 2^8 * 3^2 and multiplier or character-sum conditions in the cyclic group of order 9215.
- paper if solved: If solved exactly, the paper would be a short note removing the cyclic Hadamard case (9215,4607,2303) from the small-open-case list.

## bounded_source_list
- Leonard D. Baumert and Daniel M. Gordon, "On the existence of cyclic difference sets with small parameters" (Fields Institute Communications 41, 2004), Table 5 listing (9215,4607,2303) as open among the cyclic Hadamard cases up to v = 10000; status rechecked against Daniel M. Gordon, "The La Jolla Difference Set Repository" talk slides (ArasuFest, August 3, 2019), cyclic-Hadamard slide listing 9215 among the seven small open cases.
- Baumert-Gordon 2004 Table 5, Gordon's 2019 La Jolla Difference Set Repository slides on cyclic Hadamard cases, Hong-Yeop Song's 2026 status slide repeating the same seven v < 10000 cases, the local attempt/source/paper/search memory, and bounded exact-tuple web searches that did not surface a later exact settlement.
- artifacts/cyclic-hadamard-difference-set-9215-4607-2303/record.md
- artifacts/cyclic-hadamard-difference-set-9215-4607-2303/status.json
