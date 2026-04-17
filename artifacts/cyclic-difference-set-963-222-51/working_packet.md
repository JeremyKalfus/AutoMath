# Working Packet: The cyclic (963,222,51) difference-set case

- slug: `cyclic-difference-set-963-222-51`
- title: Does the cyclic group C_963 admit a (963,222,51)-difference set?
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `84`
- single-solve-to-paper fraction: `0.78`

## statement
Determine whether the cyclic group C_963 admits a (963,222,51)-difference set.

## novelty_notes
- frontier basis: Gordon's 2019 La Jolla slides still isolate (963,222,51) as a small open cyclic case and as the exact [9,107] residue, and bounded 2026-04-15 status checks surfaced no later exact closure.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the exact cyclic row is settled, the title theorem, literature gap, and family anchor are already fixed by the source. What remains is mainly exposition and the bounded novelty-audit record, not a feeder ladder or a second mathematical campaign.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: low
- immediate corollary headroom: moderate
- isolated exact-case risk: low
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: high
- exact gap from source: tiny
- assessment: This is the only strict lane survivor in the current five-slot shortlist. The theorem slice is stable, the family anchor is strong, the solve-to-publication distance is short, and the bounded status audit did not surface either a local attempt conflict or a later exact closure. If solved exactly, this would honestly read like the title theorem of a short note rather than a feeder instance.

## likely_paper_shape
- note title: The cyclic (963,222,51) difference-set case
- hypothetical title: The cyclic (963,222,51) difference-set case
- paper shape: Exact one-row closure note for a named small cyclic Ryser/Lander residue.
- publication if solved: Closing the exact cyclic (963,222,51) / [9,107] row would already yield a paper-shaped note because the case is explicitly isolated in the La Jolla open-case slides and bounded 2026-04-15 status checks surfaced no later exact closure.
- minimal artifact requirements: Either a cyclic construction in C_963 or a compact nonexistence proof using multiplier, quotient, or character constraints, together with a short note recording the bounded no-closure status audit.

## hypothetical_abstract
We study the exact cyclic difference-set case (963,222,51), listed by Gordon among the small open residues for Ryser-type and Lander-type cyclic difference-set questions. We determine the existence question by combining multiplier restrictions with contraction data forced on the 9- and 107-quotients. This closes one of the smallest named cyclic residues in the La Jolla open-case tables.

## single_solve_explanation
The row is already isolated by a canonical source and already carries a recognizable family anchor. If the exact cyclic case is settled, most of the paper is present immediately: statement, motivation, literature stop line, and main theorem. What remains is mainly exposition and the bounded novelty-audit record.

## broader_theorem_nonimplication
The surfaced literature did not reveal a broader theorem eliminating all remaining small cyclic Ryser/Lander residues, and the exact order-963 row is still singled out rather than absorbed by a generic closed family.

## literature_gap
Prior work surfaced in this curation run stops at listing the exact cyclic row (963,222,51) / [9,107] as open; the bounded 2026-04-15 search did not surface a later exact resolution.

## transfer_kit
- lemma: Counting gives n = k - lambda = 171 and the group-ring identity D D^(-1) = n + lambda G.
- lemma: Cyclic difference sets admit strong numerical multiplier restrictions, as emphasized in the La Jolla repository sources and the multiplier literature cited there.
- lemma: Contractions to quotients such as C_9 and C_107 preserve rigid character-value constraints that can be checked without a broad search campaign.
- lemma: The row has already survived the standard easy filters in the canonical open-case tables, so any proof starts beyond the basic BRC and Schutzenberger tests.
- toy example: The order factorization 963 = 9 * 107 gives the smallest nontrivial quotient pattern to test first; a hypothetical cyclic set would have tightly constrained images in C_9 and C_107.
- known obstruction: Multiplier and quotient-profile constraints appear rigid enough that one bad contraction profile could force immediate nonexistence.
- prior-work stop sentence: Gordon's 2019 La Jolla slides still list (963,222,51) / [9,107] as an exact open cyclic residue, and bounded 2026-04-15 status searches surfaced no later exact closure.
- recommended first attack: Push the multiplier group and quotient contractions to C_9 and C_107 far enough to force an impossible orbit or coefficient profile.
- paper if solved: If solved, the paper is a short exact closure note for one of the named small cyclic residues in the La Jolla open-case tables.

## bounded_source_list
- Daniel M. Gordon, "The La Jolla Difference Set Repository" (ArasuFest talk slides, August 3, 2019), especially the Ryser-conjecture slide listing the cyclic row (963,222,51,171) among the small open cases and the Lander-conjecture slide listing the exact group [9,107] as a smallest open case with p = 3.
- Gordon's 2019 La Jolla repository slides for the exact frontier statement, together with bounded 2026-04-15 exact-tuple and status searches to confirm that no later exact closure surfaced.
- artifacts/cyclic-difference-set-963-222-51/record.md
- artifacts/cyclic-difference-set-963-222-51/status.json
