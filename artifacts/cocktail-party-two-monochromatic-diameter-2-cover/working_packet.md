# Working Packet: Two monochromatic diameter-2 covers in 2-colored cocktail party graphs

- slug: `cocktail-party-two-monochromatic-diameter-2-cover`
- title: Does every 2-colored cocktail party graph admit a cover by two monochromatic diameter-2 subsets?
- publication status: `SLICE_CANDIDATE`
- packet quality: `excellent`

## statement
Upgrade the 2026 relaxed 2-reachable cover theorem to the original diameter-2 conjecture, or exhibit a minimal colored cocktail-party counterexample.

## novelty_notes
- frontier basis: The canonical 2026 source states the exact diameter-2 cocktail-party conjecture and proves only the relaxed 2-reachable version, so the diameter-2 claim itself remains the frontier object.
- why still open: The canonical 2026 paper states the diameter-2 cocktail-party conjecture explicitly, proves only the relaxed 2-reachable version, and the bounded recent-status search surfaced no later diameter-2 resolution.
- attempted conflict check: The repo memory sweep found no prior queue item, selected problem, failed slug, or campaign near-duplicate involving cocktail-party diameter-2 monochromatic covers.
- rediscovery risk: low-medium

## proof_sketch
- attack style: tighten the 2-reachable argument to internal diameter 2 via critical-pair analysis and blow-up-of-C5 obstruction control
- likely route: A proof or counterexample would directly resolve the named conjecture left open by the 2026 relaxation paper, so the theorem statement, motivation, and comparison section are already essentially fixed.
- verifier focus: A positive witness is a pair of color classes with direct internal diameter checks; a negative result needs a fully specified 2-coloring family with provable failure of every two-set cover.

## likely_paper_shape
- note title: Two monochromatic diameter-2 covers in 2-colored cocktail party graphs
- paper shape: One conjecture-resolution note: statement, structural proof or counterexample, and a short discussion of Ryser-style diameter bounds.
- publication if solved: Solving the original diameter-2 cocktail-party conjecture would read as a direct short follow-up to the 2026 relaxed theorem.
- minimal artifact requirements: One rigorous proof or explicit colored counterexample family, a short skeptical verification note, and a direct diameter-2 cover checker for any positive witness.

## bounded_source_list
- Andras Gyarfas and Gabor N. Sarkozy, "2-Reachable Subsets in Two-Colored Graphs" (Graphs and Combinatorics 42, 2026), which states and relaxes the English-McCourt-Mattes-Phillips conjecture.
- Canonical 2026 cocktail-party/2-reachable paper plus one bounded outside-status check for a later diameter-2 resolution.
- artifacts/cocktail-party-two-monochromatic-diameter-2-cover/record.md
- artifacts/cocktail-party-two-monochromatic-diameter-2-cover/status.json
