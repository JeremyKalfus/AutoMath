# Working Packet: The Exact Value of R(B22, B22)

- slug: `r-b22-b22-diagonal-book-ramsey`
- title: Determine the exact value of R(B22, B22)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `66`
- single-solve-to-paper fraction: `0.7`

## statement
Determine the least n such that every red-blue coloring of K_n contains a monochromatic book B22.

## novelty_notes
- frontier basis: Current public sources leave the diagonal book Ramsey number at 89 <= R(B22, B22) <= 90. The theorem statement is still stable because the live frontier is an exact endpoint question, not a loose asymptotic campaign.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the endpoint 89 versus 90 is settled, the note still has a natural title theorem and an immediate placement in the diagonal book sequence. The main residue after the solve is just packaging the decisive witness or forcing proof, though the certificate may be less compact than for the smaller cases.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: moderate
- immediate corollary headroom: low
- isolated exact-case risk: low
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: small
- assessment: Pass, but only narrowly. The theorem slice remains stable and family-anchored, yet proof compactness is less secure than in the smaller diagonal cases.

## likely_paper_shape
- note title: The Exact Value of R(B22, B22)
- hypothetical title: The Exact Value of R(B22, B22)
- paper shape: A one-theorem exact-value note for a larger diagonal book Ramsey number with a stable theorem slice but weaker compactness expectations.
- publication if solved: An exact determination of R(B22, B22) could still support a short note because the public frontier remains a one-step diagonal book Ramsey gap in a named family.
- minimal artifact requirements: Either an explicit 89-vertex coloring avoiding monochromatic B22 or a compact proof that every 90-vertex coloring forces B22.

## hypothetical_abstract
We determine the diagonal book Ramsey number R(B22, B22). Previously available results left this number in the interval 89 <= R(B22, B22) <= 90. Our result closes the remaining one-step gap for this larger diagonal book pair.

## single_solve_explanation
This target barely clears the 70% paper threshold because the public frontier is still a single endpoint in an established family. A successful solve would already provide the title theorem and nearly all of the final narrative. The main reason it is weaker than B19-B21 is the increased risk of a bulkier certificate.

## broader_theorem_nonimplication
The broad diagonal-book theory still stops at the one-step interval and does not decide the endpoint at n = 22. A proof of the exact endpoint would therefore remain the honest title theorem rather than a trivial corollary of an existing published statement.

## literature_gap
Current public sources stop at 89 <= R(B22, B22) <= 90.

## transfer_kit
- lemma: The classical diagonal-book bounds summarized in Wesley (2026) leave R(B22, B22) in the one-step interval 89 <= R(B22, B22) <= 90.
- lemma: Wesley (2026) explains that diagonal lower bounds are built from Paley-type or block-circulant constructions, giving a concrete witness architecture to inspect.
- lemma: The 2025 paper reduces book counting to common-neighborhood counts along a spine edge, which is the natural forcing mechanism for any upper-bound proof.
- lemma: Recent smaller diagonal and almost-diagonal cases in the 2025 paper show that the family remains exact-value legible rather than purely asymptotic.
- toy example: The exact almost-diagonal case R(B20, B21) = 83 is the nearest audited exact benchmark for how a small note in this family is packaged.
- known obstruction: For larger diagonal books, the main risk is not theorem-slice drift but a longer list of structured critical colorings that weakens certificate compactness.
- prior-work stop sentence: Current public sources stop at 89 <= R(B22, B22) <= 90.
- recommended first attack: Start from the Paley-type lower-bound architecture described in the recent literature and test whether every one-vertex extension forces too many common neighbors on some spine edge.
- paper if solved: The paper would be a short exact-value note closing one more diagonal book Ramsey endpoint.

## bounded_source_list
- Classical diagonal book Ramsey bounds summarized in William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5) (2026)), introduction, together with Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey numbers for books, wheels, and generalizations" (Electronic Journal of Combinatorics 32(4) (2025)) for recent family context; and bounded 2026-04-14 exact-statement, alternate-notation, canonical-source, and recent-status web checks that did not reveal a later exact determination beyond the interval 89 <= R(B22, B22) <= 90.
- Classical diagonal-book interval summarized in Wesley (2026), recent family context from the 2025 EJC paper, and bounded 2026-04-14 exact-statement, synonym, and status searches.
- artifacts/r-b22-b22-diagonal-book-ramsey/record.md
- artifacts/r-b22-b22-diagonal-book-ramsey/status.json
