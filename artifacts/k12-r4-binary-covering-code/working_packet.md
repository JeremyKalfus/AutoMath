# Working Packet: The Covering Number K(12,4)

- slug: `k12-r4-binary-covering-code`
- title: k12-r4-binary-covering-code
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `81`
- single-solve-to-paper fraction: `0.76`

## statement
Determine the least cardinality of a binary code of length 12 whose covering radius is 4.

## novelty_notes
- frontier basis: The 2008 source states that values are known for n <= 2R+3 and that K(2R+4,R) is the first open case; it proves K(10,3)=12 but does not close K(12,4).
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If K(12,4) is settled exactly, the note already has a named family anchor, a smallest-open-case framing, and a compact target statement. What remains after the solve is mostly a clean presentation of the code or impossibility certificate and a short comparison with K(10,3)=12.
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
- search-heavy: True
- certificate compactness: moderate
- exact gap from source: small
- assessment: Lane-eligible. The target is narrow, first-open-case anchored, and paper-shaped if solved, although it likely requires computation and certificate management.

## likely_paper_shape
- note title: The Covering Number K(12,4)
- hypothetical title: The Covering Number K(12,4)
- paper shape: A single-theorem note determining the first unresolved small parameter in the K(2R+4,R) covering-code line.
- publication if solved: An exact determination of K(12,4) would plausibly be publishable as a short coding-theory note on the smallest unresolved member of the first-open-case family K(2R+4,R).
- minimal artifact requirements: Either an explicit optimal length-12 binary covering code of the claimed size with radius-4 verification, or a compact impossibility proof excluding all smaller sizes.

## hypothetical_abstract
We determine the exact value of K(12,4), the minimum size of a binary code of length 12 with covering radius 4. The 2008 Keri-Ostergard paper identifies K(2R+4,R) as the first unresolved general slice and proves only the R=3 instance K(10,3)=12. Settling K(12,4) would therefore close the next smallest specific case in that line and yield a compact stand-alone coding-theory note.

## single_solve_explanation
An exact K(12,4) determination is itself the title theorem. The remaining paper work is light: describe the witness code or impossibility mechanism, explain how it sits immediately after K(10,3)=12, and record any small equivalence or uniqueness data. That keeps the solve comfortably inside the 70-90% paper band.

## broader_theorem_nonimplication
The cited source proves only the R=3 instance and a structural obstruction for self-complementary codes; it does not give a general formula that forces the R=4 case. Bounded 2026 status searching in this run did not surface a later exact theorem implying K(12,4).

## literature_gap
Prior work determines K(n,R) for n <= 2R+3 and proves K(10,3)=12, but the next concrete case K(12,4) is not closed by that paper.

## transfer_kit
- lemma: For arbitrary R, K(n,R) is known when n <= 2R+3, and the corresponding optimal codes are classified up to equivalence.
- lemma: The 2008 paper proves K(10,3)=12, giving the nearest solved benchmark on the K(2R+4,R) line.
- lemma: The same paper proves that if K(2R+4,R) < 12 for some R, that inequality cannot be witnessed by a self-complementary code.
- toy example: The solved neighboring case is K(10,3)=12.
- known obstruction: The self-complementary route cannot certify any improvement below 12 in the first-open-case family, so a successful K(12,4) attack needs a different structural or computational certificate.
- prior-work stop sentence: Current checked sources solve the first-open-case family only at R=3 via K(10,3)=12 and do not settle K(12,4).
- recommended first attack: Start from the sphere-covering lower bound and classify candidate 11-word and 12-word radius-4 codes up to equivalence using shortening and automorphism pruning before any heavier search.
- paper if solved: If solved exactly, the paper would be a short note determining the next smallest unresolved case in the K(2R+4,R) covering-code program.

## bounded_source_list
- Gerzson Keri and Patric R. J. Ostergard, "On the minimum size of binary codes with length 2R + 4 and covering radius R," Designs, Codes and Cryptography 48 (2008), especially the abstract identifying K(2R+4,R) as the first open case and proving K(10,3)=12; bounded 2026 exact-statement and status searches in this run did not surface a later exact determination of K(12,4).
- The 2008 DCC paper and bounded 2026 exact-statement and status searches performed in this curation run.
- artifacts/k12-r4-binary-covering-code/record.md
- artifacts/k12-r4-binary-covering-code/status.json
