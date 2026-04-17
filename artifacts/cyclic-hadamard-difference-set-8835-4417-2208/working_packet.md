# Working Packet: On the Cyclic Hadamard Difference-Set Case (8835,4417,2208)

- slug: `cyclic-hadamard-difference-set-8835-4417-2208`
- title: Does the cyclic group C_8835 admit a (8835,4417,2208)-difference set?
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `85`
- single-solve-to-paper fraction: `0.82`

## statement
Determine whether the cyclic group C_8835 admits a (8835,4417,2208)-difference set.

## novelty_notes
- frontier basis: Baumert-Gordon 2004 Table 5 isolates (8835,4417,2208) as open, Gordon's 2019 La Jolla Repository slides still list 8835 among the seven small open cyclic Hadamard cases, and a 2026 status slide repeats the same seven values.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: One exact solve would already remove a named survivor from a canonical residual list in a classical family. The remaining work is mostly exposition, literature placement, and the final arithmetic certificate.
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
- assessment: This is a viable micro-paper lane target with strong family anchor and stable theorem slice. It is especially attractive because n = 47^2 suggests a comparatively compact arithmetic certificate without changing the paper shape.

## likely_paper_shape
- note title: On the Cyclic Hadamard Difference-Set Case (8835,4417,2208)
- hypothetical title: The cyclic Hadamard difference-set case (8835,4417,2208).
- paper shape: A short note eliminating or constructing the cyclic Hadamard case (8835,4417,2208).
- publication if solved: Settling the cyclic Hadamard case v = 8835 would plausibly yield a focused note removing another named survivor from the sub-10000 open list.
- minimal artifact requirements: A proof or disproof for the cyclic group of order 8835, the decisive multiplier or character-sum obstruction exploiting 3-, 5-, 19-, and 31-quotients together with n = 47^2, and a short literature note explaining why 8835 remains outside the current eliminations.

## hypothetical_abstract
We determine whether the cyclic group C_8835 admits a (8835,4417,2208)-difference set. Baumert and Gordon list this exact parameter set as open in their 2004 table of cyclic Hadamard survivors, Gordon's 2019 La Jolla Repository slides still retain 8835 among the seven small unresolved cases below 10000, and a 2026 status slide repeats the same seven values. A resolution would therefore support a short paper whose title theorem is exactly this residual cyclic Hadamard case.

## single_solve_explanation
The mathematical contribution is already packaged by the literature as a single residual case, so one exact solve would do almost all of the paper's substantive work. What remains is a bounded writeup, the final novelty note, and the certificate details. Because the cyclic case is exact and family-labeled, the proof does not need feeder lemmas from a broader campaign to become paper-shaped.

## broader_theorem_nonimplication
The canonical 2004 table and the 2019 and 2026 status sources still leave 8835 unresolved while adjacent cyclic Hadamard cases are marked as eliminated. The surfaced literature therefore does not already imply the exact 8835 statement via a broader theorem.

## literature_gap
Baumert-Gordon 2004 Table 5 and Gordon's 2019 cyclic-Hadamard slide both leave (8835,4417,2208) unresolved, and bounded 2026 status checks still present 8835 among the same seven sub-10000 survivors without a later exact settlement.

## transfer_kit
- lemma: Baumert-Gordon 2004 Table 5 isolates (8835,4417,2208) as an open cyclic Hadamard case.
- lemma: The same table shows neighboring cyclic Hadamard cases already eliminated by Lander theorems, clarifying the residual frontier.
- lemma: Gordon's 2019 slides still list 8835 among the seven small open cyclic Hadamard cases below 10000, and a 2026 status slide repeats the same seven values.
- lemma: Any cyclic difference set must satisfy the standard group-ring and character equations D D^(-1) = n + lambda G and |chi(D)|^2 = n for nontrivial characters.
- toy example: Compare 8835 with the nearby excluded case 8463 from the same 2004 table to see how the open residue sits just beyond the currently available eliminators.
- known obstruction: Existing cyclic Hadamard restrictions already remove several nearby values, so any proof for 8835 must exploit finer arithmetic data than the standard Lander-type exclusions.
- prior-work stop sentence: The literature surface used here stops at listing (8835,4417,2208) as an exact open cyclic Hadamard case and does not provide a later case-specific resolution.
- recommended first attack: Exploit 3-, 5-, 19-, and 31-quotient profile constraints together with the square order n = 47^2 and multiplier or character-sum conditions in the cyclic group of order 8835.
- paper if solved: If solved exactly, the paper would be a short note removing the cyclic Hadamard case (8835,4417,2208) from the small-open-case list.

## bounded_source_list
- Leonard D. Baumert and Daniel M. Gordon, "On the existence of cyclic difference sets with small parameters" (Fields Institute Communications 41, 2004), Table 5 listing (8835,4417,2208) as open among the cyclic Hadamard cases up to v = 10000; status rechecked against Daniel M. Gordon, "The La Jolla Difference Set Repository" talk slides (ArasuFest, August 3, 2019), cyclic-Hadamard slide listing 8835 among the seven small open cases.
- Baumert-Gordon 2004 Table 5, Gordon's 2019 La Jolla Difference Set Repository slides on cyclic Hadamard cases, Hong-Yeop Song's 2026 status slide repeating the same seven v < 10000 cases, the local attempt/source/paper/search memory, and bounded exact-tuple web searches that did not surface a later exact settlement.
- artifacts/cyclic-hadamard-difference-set-8835-4417-2208/record.md
- artifacts/cyclic-hadamard-difference-set-8835-4417-2208/status.json
