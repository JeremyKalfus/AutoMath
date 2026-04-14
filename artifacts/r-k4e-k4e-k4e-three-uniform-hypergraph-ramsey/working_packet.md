# Working Packet: The Exact Value of R(K4-e, K4-e, K4-e; 3)

- slug: `r-k4e-k4e-k4e-three-uniform-hypergraph-ramsey`
- title: Determine the exact value of R(K4-e, K4-e, K4-e; 3)
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `81`
- single-solve-to-paper fraction: `0.81`

## statement
Determine the least n such that every 3-coloring of the triples of an n-element set contains a monochromatic 3-uniform K4-e in one of the three colors.

## novelty_notes
- frontier basis: Current public sources leave this 3-color 3-uniform Ramsey number at 13 <= R(K4-e, K4-e, K4-e; 3) <= 14. The gap is already one step after the 2021 SDP improvement.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the endpoint 13 versus 14 is settled, the main theorem, motivation, and frontier comparison are already in place. The remaining work is mainly a compact extremal coloring or forcing proof, plus a short explanation of how it fits next to the nearby exact 3-uniform cases.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: moderate
- publication narrative strength: strong
- editorial overhead: moderate
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: tiny
- assessment: Pass. This is the cleanest untouched one-step gap found after the exclusion sweep, and one exact solve would already account for most of a publishable note.

## likely_paper_shape
- note title: The Exact Value of R(K4-e, K4-e, K4-e; 3)
- hypothetical title: The Exact Value of R(K4-e, K4-e, K4-e; 3)
- paper shape: A one-theorem exact-value note closing a one-step 3-uniform missing-edge Ramsey gap.
- publication if solved: An exact determination of R(K4-e, K4-e, K4-e; 3) would read as the title theorem of a short note because the public frontier is already a one-step 3-uniform hypergraph gap.
- minimal artifact requirements: Either an explicit 13-vertex 3-coloring of triples avoiding monochromatic K4-e in all colors, or a compact proof that every 3-coloring on 14 vertices forces one.

## hypothetical_abstract
We determine the 3-uniform hypergraph Ramsey number R(K4-e, K4-e, K4-e; 3). Previous work placed this number in the interval 13 <= R(K4-e, K4-e, K4-e; 3) <= 14. Our result closes the remaining one-step gap for the three-color missing-edge K4 family.

## single_solve_explanation
This already has the shape of a short paper because the frontier is a single endpoint. Once the exact value is established, the note mostly writes itself around one extremal construction or one forcing argument. The surrounding context is already small and sharply localized.

## broader_theorem_nonimplication
The 2021 paper improves the upper bound but does not subsume this exact endpoint into a broader published theorem. No stronger general theorem surfaced in the bounded audit that would force 13 or 14 automatically.

## literature_gap
Current public sources stop at 13 <= R(K4-e, K4-e, K4-e; 3) <= 14.

## transfer_kit
- lemma: Lidicky-Pfender (2021), Theorem 9, gives the upper bound R(K4-e, K4-e, K4-e; 3) <= 14.
- lemma: The same theorem records the lower bound 13 <= R(K4-e, K4-e, K4-e; 3) from earlier literature.
- lemma: Lidicky-Pfender (2021), Theorem 10, shows the neighboring exact value R(K4-e, K5; 3) = 12 and provides a local-model template for turning a sharp SDP certificate into an exact finite proof.
- lemma: The 2021 paper explicitly frames these as fixed-size hypergraph Ramsey questions accessible to exact finite analysis rather than asymptotic machinery.
- toy example: The exact neighboring case R(K4-e, K5; 3) = 12 from the same paper is the closest worked example of the intended proof style.
- known obstruction: Any lower-bound construction must coordinate three colors on triples while suppressing every monochromatic K4-e, and any upper-bound proof must rule out the last 13-vertex critical configuration family.
- prior-work stop sentence: Current sources stop at 13 <= R(K4-e, K4-e, K4-e; 3) <= 14.
- recommended first attack: Interrogate the sharp 2021 SDP profile for forbidden 6- and 7-vertex traces, then attempt a constrained completion or uniqueness argument on the putative 13-vertex extremals.
- paper if solved: The paper would be a short exact-value note closing the remaining one-step gap for the three-color 3-uniform K4-e Ramsey number.

## bounded_source_list
- Bernard Lidicky and Florian Pfender, "Semidefinite Programming and Ramsey Numbers" (SIAM J. Discrete Math. 35(4) (2021)), Theorem 9, which gives 13 <= R(K4-e, K4-e, K4-e; 3) <= 14; together with bounded 2026-04-14 survey and recent-status web checks during curation that did not reveal a later exact determination.
- 2021 Lidicky-Pfender Theorem 9 for the current bounds, nearby 2021 Theorem 10 as local-method context, and bounded 2026-04-14 survey/recent-status web checks.
- artifacts/r-k4e-k4e-k4e-three-uniform-hypergraph-ramsey/record.md
- artifacts/r-k4e-k4e-k4e-three-uniform-hypergraph-ramsey/status.json
