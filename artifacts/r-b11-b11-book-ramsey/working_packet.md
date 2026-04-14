# Working Packet: The Exact Value of R(B11, B11)

- slug: `r-b11-b11-book-ramsey`
- title: Determine the exact value of R(B11, B11)
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `74`
- single-solve-to-paper fraction: `0.73`

## statement
Determine the least n such that every graph on n vertices contains a copy of B11 or its complement contains a copy of B11.

## novelty_notes
- frontier basis: Current checked public sources support only 45 <= R(B11, B11) <= 46.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the gap is closed, the paper packet is nearly complete because the diagonal family framing and the one-gap corridor are already established. After the solve, the work left is mainly the witness or forcing proof, one brief comparison with the prime-power exact cases, and routine verification.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: tiny
- assessment: Lane-eligible. The exact theorem slice is stable, the broader-family nonimplication is specific and clean, and one exact solve would already carry most of a genuine short note.

## likely_paper_shape
- note title: The Exact Value of R(B11, B11)
- hypothetical title: The Exact Value of R(B11, B11)
- paper shape: A one-theorem exact-value note on a diagonal book Ramsey one-gap residue.
- publication if solved: Closing the one-gap case R(B11, B11) would already support a short diagonal-book note rather than a feeder step.
- minimal artifact requirements: Either a 45-vertex self-complementary-style witness avoiding B11 in both colors, or a proof that every 45-vertex graph contains a B11 or its complement contains a B11.

## hypothetical_abstract
We determine the diagonal book Ramsey number R(B11, B11). Existing checked sources leave this value in the one-gap interval 45 <= R(B11, B11) <= 46, while the currently available infinite exact family covers only prime-power cases and does not include n = 11. Our result closes a compact unresolved diagonal case in the small-book regime.

## single_solve_explanation
This candidate passes the 70-90% paper test because an exact solve would itself be the honest title theorem and the surrounding narrative is already in place. What remains after the solve is mostly a concise comparison with known prime-power exact diagonal cases and a short certificate-verification section. The target is not merely a curiosity because it probes the boundary of the known diagonal family at the first unresolved non-prime-power one-gap case in the checked range.

## broader_theorem_nonimplication
The checked 2022 diagonal theorem gives exact values only when 4n + 1 is a prime power, and that mechanism does not apply at n = 11 because 45 is not a prime power. The 2025 source gives only the one-gap corridor 45-46 and no broader theorem or example settles the exact value.

## literature_gap
Publicly checked sources stop at 45 <= R(B11, B11) <= 46.

## transfer_kit
- lemma: Theorem 1 of the 2025 source gives 45 <= R(B11, B11) <= 46.
- lemma: The 2022 source states that diagonal book numbers are exact at 4n + 2 when 4n + 1 is a prime power, which explains nearby solved cases but excludes n = 11.
- lemma: The same 2025 theorem gives neighboring diagonal one-gap cases and exact almost-diagonal values, providing local family structure for comparisons.
- toy example: The prime-power diagonal case n = 12 gives a nearby exact benchmark R(B12, B12) = 50 in the checked family literature.
- known obstruction: A 45-vertex extremal witness must globally cap the common-neighbor count on every candidate spine edge in both colors, so any proof may need a rigid extremal partition rather than a local edge-count argument alone.
- prior-work stop sentence: Current checked sources stop at the one-gap window 45 <= R(B11, B11) <= 46.
- recommended first attack: Exploit the diagonal symmetry first: analyze a hypothetical 45-vertex critical graph via common-neighbor bounds around each edge and compare the extremal shape with the nearby prime-power exact constructions.
- paper if solved: The paper would be a short exact-value note on an unresolved diagonal book Ramsey one-gap case.

## bounded_source_list
- Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Theorem 1, which gives 45 <= R(B11, B11) <= 46; and Shyam Narayanan and Tian Zhang, "Ramsey numbers of fans and large books" (Electronic Journal of Combinatorics 29(1), 2022), which records the prime-power exactness mechanism for diagonal book numbers but does not settle n = 11 because 4n + 1 = 45 is not a prime power; together with bounded exact-statement, alternate-notation, source-internal, outside-source, and recent-status web checks on 2026-04-14 that did not reveal a later exact closure.
- Lidicky-McKinley-Pfender-Van Overberghe 2025 Theorem 1, Narayanan-Zhang 2022 for the prime-power diagonal exactness mechanism, and bounded 2026-04-14 exact-term, alternate-notation, source-internal, outside-source, and recent-status web checks.
- artifacts/r-b11-b11-book-ramsey/record.md
- artifacts/r-b11-b11-book-ramsey/status.json
