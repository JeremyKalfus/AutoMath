# Working Packet: The First Open Non-Result-14 Balancedly Splittable Hadamard Parameter

- slug: `bshm-288-42-6-neg6`
- title: bshm-288-42-6-neg6
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `64`
- single-solve-to-paper fraction: `0.71`

## statement
Determine whether an order-288 Hadamard matrix exists that is balancedly splittable with parameters (288,42,6,-6).

## novelty_notes
- frontier basis: Open Question (ii) explicitly asks for the first case outside the special form (4u^2,2u^2-u,u,-u) and states that (288,42,6) is the smallest open instance.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The note would have a genuine frontier basis because the source itself brands this parameter as the first open case beyond the main family. After the solve, the remaining work is a short explanation of the family boundary and a compact witness or obstruction.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: low
- immediate corollary headroom: moderate
- isolated exact-case risk: moderate
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: high
- exact gap from source: tiny
- assessment: Lane-eligible but weaker than the first two BSHM cases. The paper packet is real, but there is more risk that a successful proof would naturally comment on a broader out-of-family phenomenon.

## likely_paper_shape
- note title: The First Open Non-Result-14 Balancedly Splittable Hadamard Parameter
- hypothetical title: A Balancedly Splittable Hadamard Matrix with Parameters (288,42,6,-6)
- paper shape: A short note on the first parameter outside the main positive BSHM family.
- publication if solved: A construction or obstruction for BSHM(288,42,6,-6) would plausibly be publishable as a short note on the first open non-Result-14 parameter in the balancedly splittable Hadamard-matrix theory.
- minimal artifact requirements: Either an explicit order-288 Hadamard matrix with a certified 42-row balanced split yielding inner products 6 and -6, or a compact proof excluding that parameter.

## hypothetical_abstract
We determine the existence status of a balancedly splittable Hadamard matrix with parameters (288,42,6,-6). Daniel and Praeger identified this parameter as the smallest open case outside the principal family (4u^2,2u^2-u,u,-u) in their 2023 study of balancedly splittable Hadamard matrices. Resolving it clarifies whether the known family boundary is genuine or whether new behavior already appears at the first remaining residue.

## single_solve_explanation
A yes-or-no answer for the 288-case already comes with a ready-made paper narrative because it is the first explicit test of whether the main family is exhaustive. The write-up after the solve would mainly explain the existing family, state why 288 is the first out-of-family residue, and present the certificate. That keeps the solve itself close to the full paper payload.

## broader_theorem_nonimplication
The source's positive family only covers parameters of the form (4u^2,2u^2-u,u,-u), and Open Question (ii) explicitly separates the 288-case from that family. No broader published theorem in the source already settles whether such an out-of-family parameter can occur.

## literature_gap
The checked 2023 source asks whether any BSHM(n,l,a,-a) exists outside the special form (4u^2,2u^2-u,u,-u) and identifies BSHM(288,42,6,-6) as the smallest open case.

## transfer_kit
- lemma: The source's main positive family has parameters (4u^2,2u^2-u,u,-u).
- lemma: Open Question (ii) explicitly asks whether any BSHM(n,l,a,-a) exists outside that special form.
- lemma: The same passage states that the smallest open out-of-family case is (n,l,a) = (288,42,6).
- lemma: The source notes that such parameters are equivalent to real flat ETFs arising as submatrices of Hadamard matrices.
- toy example: The neighboring positive benchmarks are the source's in-family constructions of BSHM(4u^2,2u^2-u,u,-u).
- known obstruction: Any solution must cross the explicit family boundary isolated by the source, so arguments that merely repackage Result 14 will not suffice.
- prior-work stop sentence: The current source stops at the explicit open question of whether any out-of-family BSHM(n,l,a,-a) exists, beginning with BSHM(288,42,6,-6).
- recommended first attack: Translate the 42-row split into the associated ETF and strongly regular graph data and test whether the resulting parameter set can be realized or ruled out before looking for broader out-of-family constructions.
- paper if solved: If solved exactly, the paper would be a short note on the first open parameter outside the main balancedly splittable Hadamard-matrix family.

## bounded_source_list
- Leah H. K. Daniel and Cheryl E. Praeger, "Balancedly splittable Hadamard matrices," The Electronic Journal of Combinatorics 30(1) (2023), especially Open Question (ii) on page 37: the paper asks whether any BSHM(n,l,a,-a) exists outside the special form (4u^2,2u^2-u,u,-u), and identifies (n,l,a) = (288,42,6) as the smallest open case.
- Daniel-Praeger (2023), especially Open Question (ii) and the surrounding parameter tables and ETF discussion.
- artifacts/bshm-288-42-6-neg6/record.md
- artifacts/bshm-288-42-6-neg6/status.json
