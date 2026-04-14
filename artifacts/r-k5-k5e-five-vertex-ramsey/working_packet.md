# Working Packet: The Exact Value of R(K5, K5-e)

- slug: `r-k5-k5e-five-vertex-ramsey`
- title: Determine the exact value of R(K5, K5-e)
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `83`
- single-solve-to-paper fraction: `0.78`

## statement
Determine the least n such that every red-blue coloring of K_n contains a red K5 or a blue K5-e.

## novelty_notes
- frontier basis: Current public survey data still leaves the pair in the interval 30 <= R(K5, K5-e) <= 33. It is explicitly highlighted as one of the remaining unsolved five-vertex graph cases, so an exact closure has an immediate paper frame.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the exact value is found, the decisive argument or extremal coloring is already the paper. What remains is a short literature paragraph, a compact verification artifact, and a comparison with the already solved neighboring five-vertex pairs.
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
- certificate compactness: moderate
- exact gap from source: small
- assessment: Pass. This is a stable, still-open exact theorem slice with a strong family anchor and low editorial overhead.

## likely_paper_shape
- note title: The Exact Value of R(K5, K5-e)
- hypothetical title: The Exact Value of R(K5, K5-e)
- paper shape: A one-theorem note closing one of the last unresolved five-vertex graph Ramsey pairs.
- publication if solved: An exact determination of R(K5, K5-e) would already read like the title theorem of a short note on one of the last unresolved five-vertex graph Ramsey pairs.
- minimal artifact requirements: Either a forcing proof at the correct threshold or one explicit extremal coloring on n-1 vertices together with a small verification certificate.

## hypothetical_abstract
We determine the two-color Ramsey number R(K5, K5-e). The current survey literature leaves this parameter in the interval 30 <= R(K5, K5-e) <= 33 and identifies it as one of the remaining unresolved five-vertex graph cases. Our result closes that gap and completes another exact entry in the five-vertex Ramsey table.

## single_solve_explanation
One exact solve would already be the honest main theorem of the note. The family anchor is strong because this is not an isolated curiosity but one of the small residual five-vertex cases tracked by the survey literature. After the solve, very little remains beyond the proof or witness and a short contextual discussion.

## broader_theorem_nonimplication
General Ramsey recurrences and monotonicity only recover the interval and do not force a specific value. The survey still records a true multi-value gap rather than a case implicitly settled by a broader theorem.

## literature_gap
Current public sources stop at 30 <= R(K5, K5-e) <= 33.

## transfer_kit
- lemma: DS1.17 records the current lower bound 30 <= R(K5, K5-e).
- lemma: DS1.17 records the current upper bound R(K5, K5-e) <= 33.
- lemma: The same survey isolates K5 versus K5-e as one of the remaining open five-vertex graph Ramsey pairs, so the surrounding family narrative is already in place.
- toy example: The solved neighboring five-vertex case R(K5, W5) = 27 shows how a single exact closure in this table naturally supports a short standalone note.
- known obstruction: Any proof of the upper endpoint must rule out all colorings at one threshold, while any lower-bound improvement needs an explicit extremal coloring suppressing a red K5 and a blue K5-e simultaneously.
- prior-work stop sentence: Current sources stop at 30 <= R(K5, K5-e) <= 33.
- recommended first attack: Start from the known lower-bound constructions cited by the survey and perform a tightly controlled extension analysis before allowing any broader computational campaign.
- paper if solved: The paper would be a concise exact-value note on one of the last unresolved five-vertex Ramsey pairs.

## bounded_source_list
- Stanislaw P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, 2024), Section 5.11, especially the summary at page 40 stating 30 <= R(K5, K5-e) <= 33; together with bounded 2026-04-14 web checks against the survey page and historical five-vertex-graph summaries that did not reveal a later exact closure.
- DS1.17 Section 5.11 plus bounded 2026-04-14 survey-page and five-vertex-summary web checks.
- artifacts/r-k5-k5e-five-vertex-ramsey/record.md
- artifacts/r-k5-k5e-five-vertex-ramsey/status.json
