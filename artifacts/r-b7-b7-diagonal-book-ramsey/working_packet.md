# Working Packet: The Exact Value of R(B7, B7)

- slug: `r-b7-b7-diagonal-book-ramsey`
- title: Determine the exact value of R(B7, B7)
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `84`
- single-solve-to-paper fraction: `0.83`

## statement
Determine the least n such that every red-blue coloring of K_n contains a monochromatic copy of the 7-page book graph B7.

## novelty_notes
- frontier basis: The recent diagonal-book theorem leaves R(B7, B7) at the one-step interval 29 <= R(B7, B7) <= 30, and 29 = 2^2 + 5^2 so the available exactness shortcut does not settle it. The remaining gap is therefore a genuine small frontier claim with immediate table value.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: Once the exact value is decided, the proof or witness is already almost the complete note. The rest is limited to a concise family summary and a small verification appendix.
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
- assessment: Pass. It is a stable one-step gap with current literature context and low packaging cost.

## likely_paper_shape
- note title: The Exact Value of R(B7, B7)
- hypothetical title: The Exact Value of R(B7, B7)
- paper shape: A one-theorem note determining one unresolved diagonal book Ramsey value at a one-step gap.
- publication if solved: An exact determination of R(B7, B7) would already yield a compact note closing another one-step diagonal book Ramsey gap.
- minimal artifact requirements: Either a B7-free coloring of K29 or a proof that every coloring of K30 forces a monochromatic B7, with a compact certificate.

## hypothetical_abstract
We determine the diagonal book Ramsey number R(B7, B7). Recent work leaves this value in the interval 29 <= R(B7, B7) <= 30. Our result closes another sharp diagonal-book gap and strengthens the exact small-book Ramsey table.

## single_solve_explanation
A single exact solve would already supply the paper's title theorem and main body. The family narrative is already built in the recent literature, so the post-solve work is minimal. This is substantially closer to paper-ready than a broader campaign-style target.

## broader_theorem_nonimplication
The recent theorem bounds the value within one step but does not decide it, and the published exactness shortcut fails because 29 is a sum of two squares. No broader statement found in the bounded audit forces the answer.

## literature_gap
Current public sources stop at 29 <= R(B7, B7) <= 30.

## transfer_kit
- lemma: Pchelintsev, Rath, and Angeltveit (2025), Theorem 1, implies R(B7, B7) >= 29.
- lemma: The same theorem implies R(B7, B7) <= 30.
- lemma: The note after Theorem 1 explains why the non-sum-of-two-squares exactness criterion does not apply here, since 29 is a sum of two squares.
- lemma: The 2026 Wesley paper provides independent recent lower-bound progress for book Ramsey numbers and confirms that the family remains active.
- toy example: The exact solved diagonal case R(B8, B8) = 33 is a nearby benchmark for what the final note would look like.
- known obstruction: A lower-bound proof needs a K29 coloring avoiding monochromatic B7, while an upper-bound proof must rule out every such critical coloring.
- prior-work stop sentence: Current sources stop at 29 <= R(B7, B7) <= 30.
- recommended first attack: Test whether the recent constructive templates for diagonal books can be extended to K29, and if not, turn the failure pattern into a focused common-neighbor forcing argument for K30.
- paper if solved: The paper would be a concise exact-value note on another unresolved one-step diagonal book Ramsey number.

## bounded_source_list
- Maksim V. Pchelintsev, Peter Rath, and Sebastian Angeltveit, "New lower and upper bounds on Ramsey numbers" (Electronic Journal of Combinatorics 32(4) (2025), #P4.64), Theorem 1 and the note immediately following it, which imply 29 <= R(B7, B7) <= 30; together with William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5) (2026), 114913) as independent recent family context and bounded 2026-04-14 web checks that did not reveal a later exact closure.
- 2025 EJC P4.64 Theorem 1 and note, the 2026 Wesley paper, plus bounded 2026-04-14 exact-notation and recent-status web checks.
- artifacts/r-b7-b7-diagonal-book-ramsey/record.md
- artifacts/r-b7-b7-diagonal-book-ramsey/status.json
