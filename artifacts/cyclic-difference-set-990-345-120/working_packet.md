# Working Packet: The Cyclic (990,345,120) Difference-Set Case

- slug: `cyclic-difference-set-990-345-120`
- title: cyclic-difference-set-990-345-120
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `86`
- single-solve-to-paper fraction: `0.82`

## statement
Determine whether the cyclic group C_990 admits a (990,345,120)-difference set.

## novelty_notes
- frontier basis: Gordon's 2019 ArasuFest/LJDSR status slides still list (990,345,120,225) among the small open cyclic cases while separately naming an exact noncyclic 990 row.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the cyclic row is settled exactly, the theorem statement, frontier hook, and most of the mathematics are already determined by the residual-case packet.
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
- certificate compactness: high
- exact gap from source: tiny
- assessment: Lane-eligible. The row is explicit, the paper story is immediate, and the later-status picture is strong enough for a live micro-paper solve attempt.

## likely_paper_shape
- note title: The Cyclic (990,345,120) Difference-Set Case
- hypothetical title: On the cyclic (990,345,120) difference-set case
- paper shape: A short note closing one named small open cyclic difference-set row.
- publication if solved: A decisive existence or nonexistence result for the cyclic (990,345,120) case would read like the title theorem of a short residual-case note tied to Gordon's small open cyclic list.
- minimal artifact requirements: A cyclic proof or disproof, a clean multiplier-orbit or contracted-coefficient argument, and a compact status paragraph tying the 2019 residual table to the new theorem.

## hypothetical_abstract
We determine whether the cyclic group C_990 admits a (990,345,120)-difference set. Gordon's 2019 ArasuFest/LJDSR status slides still isolate this parameter row among the small open cyclic cases, with the same parameter set also appearing as a separate noncyclic residual row. A direct solution would close one named cell in the residual table and would leave only light contextual writeup around the main proof.

## single_solve_explanation
The source packet already isolates the exact cyclic row, so one clean proof or disproof would provide the honest title theorem and nearly all of the paper's mathematics. What remains after the solve is mainly a short introduction, the polished proof, and a brief status discussion about the neighboring noncyclic 990 row. This is not a feeder instance: the solve itself is the paper-shaped contribution.

## broader_theorem_nonimplication
The 2019 status slides still separate the cyclic 990 row from the exact noncyclic [2,G9,5,11] row, so the honest theorem does not automatically collapse into a broader ambient classification result. A stronger all-group obstruction may exist, but the bounded audit did not surface one, and the cyclic slice remains explicitly named as a frontier residue.

## literature_gap
The surfaced 2019 status packet stops at listing the cyclic (990,345,120) row as open, and the capped 2026-04-16 exact/alternate search did not surface a later exact-tuple closure.

## transfer_kit
- lemma: The ArasuFest Ryser-conjecture slide explicitly lists (990,345,120,225) among the small open cyclic cases.
- lemma: The same slide packet separately lists the exact 990 noncyclic row [2,G9,5,11], so parameter-level arithmetic alone does not settle the cyclic slice.
- lemma: The same source family uses multiplier and character criteria as the first-line elimination tools for residual difference-set rows.
- lemma: The parameter arithmetic n = k - lambda = 225 supplies immediate 3-part and 5-part multiplier pressure on quotient contractions of C_990.
- toy example: Contract a hypothetical cyclic set modulo 45 or 90 and test whether the 3- and 5-orbit counts can satisfy the group-ring equations with k = 345 and lambda = 120.
- known obstruction: Any cyclic solution must reconcile simultaneous 3-part and 5-part multiplier structure with the 2 and 11 factors of C_990.
- prior-work stop sentence: Gordon's 2019 status slides still list the cyclic (990,345,120) row as open among the small Ryser-conjecture cases.
- recommended first attack: Normalize by a 3- or 5-multiplier, contract to a quotient on the 45- or 90-part, and force the orbit counts against the difference-set equations.
- paper if solved: If solved exactly, the paper would be a short note closing the cyclic 990 residual row in Gordon's small open table.

## bounded_source_list
- Daniel M. Gordon, "The La Jolla Difference Set Repository" (ArasuFest talk slides, August 3, 2019), especially the Ryser-conjecture slide listing (990,345,120,225) among the small open cyclic cases and the Lander-conjecture slide listing the exact 990 row [2,G9,5,11].
- Gordon's 2019 ArasuFest/LJDSR slide packet, bounded exact-statement searches for "990,345,120" difference set and cyclic difference set 990 345 120 on 2026-04-16, and local attempt/source/paper/search memory.
- artifacts/cyclic-difference-set-990-345-120/record.md
- artifacts/cyclic-difference-set-990-345-120/status.json
