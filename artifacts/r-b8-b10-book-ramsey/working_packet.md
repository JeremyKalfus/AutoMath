# Working Packet: The Exact Value of R(B8, B10)

- slug: `r-b8-b10-book-ramsey`
- title: Determine the exact value of R(B8, B10)
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `76`
- single-solve-to-paper fraction: `0.76`

## statement
Either prove that every graph on 37 vertices contains B8 or its complement contains B10 and thus show R(B8, B10) = 37, or construct a 37-vertex graph avoiding B8 whose complement avoids B10 and thus show R(B8, B10) = 38.

## novelty_notes
- frontier basis: The 2025 book-Ramsey paper implies the current lower bound 37 <= R(B8, B10) through its almost-diagonal theorem, while the older Rousseau-Sheehan upper-bound mechanism recorded in DS1.17 still gives R(B8, B10) <= 38. The sampled 2026 Wesley follow-up advertises new lower bounds for several book pairs and an infinite-family result for R(B_{n-1}, B_n), but it does not advertise an exact resolution of R(B8, B10).
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: This is already a canonical one-gap residue inside a named exact-value program. After a solve, the note would mainly need the extremal witness or forcing proof, a short comparison with the adjacent exact case R(B9, B10) = 39, and a brief comment on why the known infinite-family theorems stop short of B8 versus B10.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: high
- exact gap from source: tiny
- assessment: Pass. This is a fresh one-gap exact-value residue with a strong family anchor, a cheap novelty audit, and a short-note packet if solved.

## likely_paper_shape
- note title: The Exact Value of R(B8, B10)
- hypothetical title: The Exact Value of R(B8, B10)
- paper shape: A one-theorem exact-value note on an almost-diagonal book Ramsey residue.
- publication if solved: Closing the one-gap case R(B8, B10) would already read as the title theorem of a short note on almost-diagonal book Ramsey numbers.
- minimal artifact requirements: Either a proof that every 37-vertex graph forces B8 or a complement B10, or one explicit 37-vertex witness graph showing the threshold is 38.

## hypothetical_abstract
We determine the book Ramsey number R(B8, B10). Existing work leaves this almost-diagonal case in the one-gap window 37 <= R(B8, B10) <= 38. Our result closes a natural residue in the recent book-Ramsey program around the almost-diagonal family R(B_{n-2}, B_n).

## single_solve_explanation
The exact value is already the honest title theorem, and the surrounding literature has done most of the setup. A successful solve would leave only the proof or explicit witness, a compact comparison with neighboring solved book pairs, and a short remark on the boundary of the known family theorems. That is comfortably inside the 70-90% micro-paper band.

## broader_theorem_nonimplication
Known exact families settle R(B_{n-1}, B_n) and many diagonal cases, but they do not settle R(B_{n-2}, B_n) for n = 10. The recent 2026 follow-up advertises infinite-family progress only for the second case, so the B8/B10 slice is not already forced by a broader published theorem.

## literature_gap
Current public sources support only the one-gap window 37 <= R(B8, B10) <= 38, and the bounded 2026-04-13 audit did not uncover a later exact determination.

## transfer_kit
- lemma: Theorem 1 of the 2025 book-Ramsey paper gives the lower bound 37 <= R(B8, B10).
- lemma: DS1.17 Section 5.3(g) gives the generic upper bound R(Bm, Bn) <= 2(m + n + 1); for (m, n) = (8, 10) this is R(B8, B10) <= 38.
- lemma: The same 2025 paper proves the neighboring exact value R(B9, B10) = 39, which gives a local benchmark one step closer to the diagonal.
- toy example: The exact case R(B9, B10) = 39 is the nearest solved almost-diagonal example showing how the 4n - 1 line behaves one notch above the target.
- known obstruction: A proof of 37 must eliminate every 37-vertex critical graph allowed by the current lower bound, while a proof of 38 needs a single 37-vertex graph avoiding B8 with complement avoiding B10.
- prior-work stop sentence: Current sources stop at the one-gap window 37 <= R(B8, B10) <= 38.
- recommended first attack: Exploit the 2025 lower-bound construction paradigm and test whether any 37-vertex extension survives the B8 and complement-B10 constraints, using SAT modulo symmetries or tightly pruned block-circulant search only as a certificate generator after a structural setup.
- paper if solved: The paper would be a short exact-value note closing an almost-diagonal book Ramsey residue.

## bounded_source_list
- Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Theorem 1; Stanislaw P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, 2024), Section 5.3(g); William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5), 2026), abstract-level status check; and bounded exact-term, canonical-source, outside-source, and recent-status web checks performed on 2026-04-13.
- Lidicky-McKinley-Pfender-Van Overberghe 2025, DS1.17 Section 5.3(g), Wesley 2026 abstract-level status check, and bounded 2026-04-13 exact-term, canonical-source, outside-source, and recent-status searches for R(B8, B10).
- artifacts/r-b8-b10-book-ramsey/record.md
- artifacts/r-b8-b10-book-ramsey/status.json
