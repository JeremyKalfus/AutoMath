# Working Packet: The Exact Value of GR(3, K6, 2)

- slug: `gr3-k6-at-most-two-colors`
- title: Determine the exact value of GR(3, K6, 2)
- publication status: `NONE`
- packet quality: `weak`
- micro-paper eligible: `False`
- paper leverage score: `34`
- single-solve-to-paper fraction: `0.38`

## statement
Determine the least n such that every 3-edge-coloring of K_n contains a copy of K6 using at most 2 colors.

## novelty_notes
- frontier basis: Current public sources support only 32 <= GR(3, K6, 2) <= 54.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: A future exact solution would indeed headline a paper, but the current corridor is far too wide for a one-shot micro-paper target. Too much of the eventual paper would still be hidden inside a large search and certification campaign.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: moderate
- publication narrative strength: weak
- editorial overhead: high
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: True
- certificate compactness: low
- exact gap from source: broad
- assessment: Fails the micro-paper lane decisively. It remains in the queue only as an honestly labeled low-priority fallback candidate.

## likely_paper_shape
- note title: The Exact Value of GR(3, K6, 2)
- hypothetical title: The Exact Value of GR(3, K6, 2)
- paper shape: A broad computational exact-value project rather than a clean micro-note.
- publication if solved: An exact determination of GR(3, K6, 2) would be publishable in principle, but it is far outside the current micro-paper lane.
- minimal artifact requirements: A large-scale extremal-coloring search or a major new structural forcing argument, plus substantial machine-checkable certification.

## hypothetical_abstract
We determine GR(3, K6, 2), the least n such that every 3-edge-coloring of K_n contains a K6 using at most two colors. The presently checked literature leaves this parameter between 32 and 54. Our result closes a large open interval in the generalized small Ramsey program.

## single_solve_explanation
A successful exact solve would still yield a legitimate title theorem. But the current gap is too broad, the likely certificate is too large, and the packaging cost after the solve is still substantial. This is therefore a genuine frontier target but not a micro-paper target.

## broader_theorem_nonimplication
The 2025 paper gives only a wide corridor and does not indicate any theorem reducing the K6 case to the exact smaller cases. The bounded 2026 audit found no later closure.

## literature_gap
Publicly checked sources stop at 32 <= GR(3, K6, 2) <= 54.

## transfer_kit
- lemma: Table 1 of the 2025 paper gives 32 <= GR(3, K6, 2) <= 54.
- lemma: The same source proves exact smaller generalized cases such as GR(3, K4, 2) = 10.
- lemma: Section 3 explains the computational toolkit currently available for this family.
- toy example: The exact benchmark GR(3, K4, 2) = 10 illustrates the family definition, though it is much smaller than the target.
- known obstruction: The present gap is so wide that neither a compact certificate nor a single local structural lemma is visible from the current literature.
- prior-work stop sentence: Current checked sources stop at 32 <= GR(3, K6, 2) <= 54.
- recommended first attack: Do not prioritize this in the strict micro-paper lane; only revisit if the smaller generalized cases are exhausted and a new structural reduction appears.
- paper if solved: The paper would be a substantial computational exact-value article, not a short micro-note.

## bounded_source_list
- Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Table 1 and Section 3, which give 32 <= GR(3, K6, 2) <= 54; together with the 2024 arXiv preprint version and the authors' project page, plus bounded exact-statement and recent-status web checks on 2026-04-14 that did not reveal a later exact determination.
- Lidicky-McKinley-Pfender-Van Overberghe 2025 Table 1 and Section 3, the 2024 preprint version, the project page, and bounded 2026-04-14 exact-term and recent-status web checks.
- artifacts/gr3-k6-at-most-two-colors/record.md
- artifacts/gr3-k6-at-most-two-colors/status.json
