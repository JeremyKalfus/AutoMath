# Working Packet: The d = 8 slice of the forbidden out-degree orientation conjecture

- slug: `eight-regular-forbidden-outdegree-three-set`
- title: Does every 8-regular graph admit an F-avoiding orientation for every 3-element forbidden set?
- publication status: `SLICE_CANDIDATE`
- packet quality: `strong`

## statement
Close the exact d=8 slice left after the 2026 advance by proving that every 8-regular graph avoids every 3-element forbidden list, or by finding a minimal 8-regular counterexample.

## novelty_notes
- frontier basis: The canonical 2026 paper proves d <= 6 and all forbidden sets of size at most 2, leaving the d = 8, |F| = 3 slice as a precise next unresolved theorem target.
- why still open: The 2026 paper proves d <= 6 and all |F| <= 2 cases, which leaves d=8 with |F|=3 as a precise unresolved slice, and bounded later web search did not reveal a d=8 resolution.
- attempted conflict check: No matching slug, title, or near-duplicate forbidden-outdegree d=8 slice appeared in the repo exclusion sweep; only the distinct d=7 slice is currently selected elsewhere in repo memory.
- rediscovery risk: low-medium

## proof_sketch
- attack style: compress the 3-element forbidden-list patterns using complement symmetry and extend the lasso-based local repair method from the 2026 paper
- likely route: A proof or counterexample on this exact next slice would read as a direct follow-up theorem note to the 2026 paper, with the conjectural framing already supplied by the source.
- verifier focus: Positive certificates are explicit orientations checked by out-degree counts; negative results need a fully specified 8-regular witness plus a proof that all orientations hit F somewhere.

## likely_paper_shape
- note title: The d = 8 slice of the forbidden out-degree orientation conjecture
- paper shape: A next-slice theorem paper: reduce to the distinct 3-element list types, prove the slice, and note the conjectural context.
- publication if solved: A clean d=8 theorem or counterexample would already be a short follow-up paper to the 2026 d<=6 result.
- minimal artifact requirements: A structural proof across the normalized 3-element forbidden-set types or a minimal 8-regular counterexample family, plus explicit orientation checking where relevant.

## bounded_source_list
- Owen Henderschedt and Jessica McDonald, "On orientations with forbidden out-degrees" (Discrete Applied Mathematics 387, 2026).
- Canonical 2026 forbidden-outdegree paper plus one bounded outside-status check for a post-2026 d = 8 advance.
- artifacts/eight-regular-forbidden-outdegree-three-set/record.md
- artifacts/eight-regular-forbidden-outdegree-three-set/status.json
