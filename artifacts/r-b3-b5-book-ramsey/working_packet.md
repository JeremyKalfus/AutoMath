# Working Packet: The Exact Value of R(B3, B5)

- slug: `r-b3-b5-book-ramsey`
- title: Determine the exact value of R(B3, B5)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `55`
- single-solve-to-paper fraction: `0.64`

## statement
Determine the least n such that every graph on n vertices contains a copy of B3 or its complement contains a copy of B5.

## novelty_notes
- frontier basis: Current checked sources support only 17 <= R(B3, B5) <= 18, but the exact-status audit is not strong enough to certify low rediscovery risk.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the gap is genuinely open and then closed, the note would still be nearly complete immediately. It misses the lane because the novelty audit is not strong enough and the very small case risks collapsing into an already-known remark.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: moderate
- publication narrative strength: moderate
- editorial overhead: moderate
- immediate corollary headroom: low
- isolated exact-case risk: high
- broader-theorem implication risk: unresolved
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: high
- exact gap from source: tiny
- assessment: Not lane-eligible. The theorem slice is still paper-shaped if open, but unresolved rediscovery risk is too high for strict one-shot publication mode.

## likely_paper_shape
- note title: The Exact Value of R(B3, B5)
- hypothetical title: The Exact Value of R(B3, B5)
- paper shape: A very short exact-value note on a tiny almost-diagonal book case, if novelty survives.
- publication if solved: An exact closure of R(B3, B5) could still support a short note, but the small-case rediscovery surface is too exposed for the strict lane under the present audit budget.
- minimal artifact requirements: Either a 17-vertex graph avoiding B3 whose complement avoids B5, or a forcing proof that every 17-vertex graph contains B3 or its complement contains B5.

## hypothetical_abstract
We determine the two-color Ramsey number R(B3, B5). Existing checked sources leave this almost-diagonal case in the corridor 17 <= R(B3, B5) <= 18. If genuinely open, closing this gap would produce a very short note on a tiny book Ramsey residue, but the rediscovery surface for so small a case remains exposed.

## single_solve_explanation
If the case is genuinely open, one solve would still carry most of the final note because the title theorem and basic family framing are already visible. What remains after the solve would mainly be the decisive proof or witness and a very short comparison paragraph. It fails the strict micro-paper lane because small-case rediscovery risk is too high under the present bounded audit.

## broader_theorem_nonimplication
The checked 2025 source gives only the lower bound and DS1.17 gives only the generic upper bound 18. The problem is not obvious from the broader family bounds, but the small size raises unresolved risk that an older exact observation already settles it.

## literature_gap
Current checked public sources support only 17 <= R(B3, B5) <= 18, but the exact-status audit remains incomplete for a low-parameter case.

## transfer_kit
- lemma: Lemma 1 of the 2025 source gives 17 <= R(B3, B5).
- lemma: DS1.17 Section 5.3(g) gives the generic upper bound R(B3, B5) <= 18.
- lemma: The 2025 source records exact nearby values on the same family line for larger pairs, showing the surrounding notation and paper shell.
- toy example: The exact solved neighbor R(B5, B6) = 23 shows how a short book-Ramsey exact-value note is packaged, although it lies slightly above the target.
- known obstruction: For such a small case, the main obstruction may be rediscovery rather than proof size: a tiny exact theorem can already have appeared as a proposition, example, or remark in older literature.
- prior-work stop sentence: Current checked sources support only the corridor 17 <= R(B3, B5) <= 18, but the bounded audit does not yet certify low rediscovery risk.
- recommended first attack: Before any solve effort, run a stricter exact-statement and old-source sweep dedicated to this specific pair; if it survives, then test whether a 16-vertex lower-bound construction can be extended to 17 vertices.
- paper if solved: If the case survives the novelty audit, the paper would be a very short exact-value note on a tiny almost-diagonal book Ramsey case.

## bounded_source_list
- Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Lemma 1, which gives 4n - 3 <= R(B_{n-2}, B_n) for 4 <= n <= 21 and therefore 17 <= R(B3, B5); together with Stanislaw P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, 2024), Section 5.3(g), which gives the generic book upper bound R(Bm, Bn) <= 2(m + n + 1) and therefore R(B3, B5) <= 18; plus bounded family-level web checks on 2026-04-14 that did not surface a later exact closure but did not completely discharge rediscovery risk for this very small case.
- Lidicky-McKinley-Pfender-Van Overberghe 2025 Lemma 1, DS1.17 Section 5.3(g), and bounded 2026-04-14 family-level web checks.
- artifacts/r-b3-b5-book-ramsey/record.md
- artifacts/r-b3-b5-book-ramsey/status.json
