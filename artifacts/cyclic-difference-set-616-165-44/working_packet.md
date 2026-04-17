# Working Packet: The cyclic (616,165,44) difference-set problem

- slug: `cyclic-difference-set-616-165-44`
- title: Does the cyclic group C_616 admit a (616,165,44)-difference set?
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `84`
- single-solve-to-paper fraction: `0.78`

## statement
Determine whether the cyclic group C_616 admits a (616,165,44)-difference set.

## novelty_notes
- frontier basis: Gordon's 2019 La Jolla slides list (616,165,44,121) among the six small open cyclic Ryser-conjecture cases.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The canonical source already supplies the exact theorem slice, the conjectural family anchor, and the literature stop line. A clean existence or nonexistence proof would therefore do almost all of the mathematical work of the note.
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
- assessment: This is the cleanest audited survivor in the current run. The theorem slice is stable, the family anchor is strong, and one exact solve would already look like the title theorem of a short note.

## likely_paper_shape
- note title: The cyclic (616,165,44) difference-set problem
- hypothetical title: On the cyclic (616,165,44) difference-set problem
- paper shape: A short exact-case Ryser-conjecture note.
- publication if solved: A proof or disproof for the cyclic (616,165,44) case would likely stand as a short Ryser-conjecture note because the source already isolates it as one of the six small open cyclic cases.
- minimal artifact requirements: A cyclic existence or nonexistence proof, the decisive contracted-count or multiplier argument, and a brief explanation of how the result closes this Ryser-case row.

## hypothetical_abstract
We determine whether the cyclic group C_616 admits a (616,165,44)-difference set. Gordon's La Jolla repository slides isolate this parameter set as one of the six small open cyclic cases attached to Ryser's conjecture. A decisive proof would close an exact residual row rather than contribute only feeder evidence, so the mathematical core of the note is concentrated in the single solve itself.

## single_solve_explanation
This target already comes with a crisp title theorem, a named family anchor, and a tiny literature gap. If the row is settled exactly, the remaining work is mostly to write the proof cleanly and place it against Ryser's conjecture and the standard cyclic tools. No extra campaign of feeder lemmas is needed to make the note paper-shaped.

## broader_theorem_nonimplication
The source still lists the exact cyclic row as open, and the bounded later-status sweep surfaced no theorem expressly removing cyclic n=121 cases with v = 616. The likely proof tools are standard cyclic-contraction methods, but they do not already imply nonexistence on the surfaced record.

## literature_gap
Prior work surfaced in this curation stops at Gordon's 2019 La Jolla slides listing (616,165,44,121) among the six small open cyclic Ryser cases; the bounded 2026-04-15 exact-tuple, synonym, and recent-publications sweep surfaced no later targeted settlement.

## transfer_kit
- lemma: Gordon 2019 isolates (616,165,44,121) as an exact small open cyclic case on the Ryser-conjecture slide.
- lemma: Baumert-Gordon 2003 state that cyclic cases with gcd(v,n) > 1 sit in the Ryser-conjecture lane and develop divisor-contraction equations for cyclic difference sets via Theorem 3.1.
- lemma: Baumert-Gordon 2003 Theorem 3.2 provides multiplier-fixed congruence constraints that can sharpen the contracted-count equations.
- toy example: Contract modulo w = 56 so that v/w = 11 and check whether 56 integer counts in [0,11] can satisfy sum 165 and energy n + lambda*(v/w) = 121 + 44*11 = 605.
- known obstruction: Ryser's conjecture predicts nonexistence because gcd(616,121) = 11 > 1, but the surfaced literature still leaves this exact cyclic row open.
- prior-work stop sentence: Gordon 2019 lists (616,165,44,121) among the six small open cyclic Ryser-conjecture cases.
- recommended first attack: Use divisor-contraction equations at a quotient of size 11 together with multiplier-fixed orbit constraints coming from n = 11^2.
- paper if solved: If solved exactly, the paper would be a short note settling one of the six small open cyclic Ryser cases.

## bounded_source_list
- Daniel M. Gordon, "The La Jolla Difference Set Repository" (ArasuFest talk slides, August 3, 2019), especially the Ryser-conjecture slide listing (616,165,44,121) among the six small open cyclic cases.
- Gordon 2019 La Jolla slides for the open-case listing, Baumert-Gordon 2003 for cyclic contracted-multiplier tools, and the bounded 2026-04-15 exact-tuple/synonym sweep plus Gordon's publications page through 2025 for later-status checking.
- artifacts/cyclic-difference-set-616-165-44/record.md
- artifacts/cyclic-difference-set-616-165-44/status.json
