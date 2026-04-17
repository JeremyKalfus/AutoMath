# Working Packet: The Cyclic (469,208,92) Difference-Set Case

- slug: `cyclic-difference-set-469-208-92`
- title: cyclic-difference-set-469-208-92
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `84`
- single-solve-to-paper fraction: `0.79`

## statement
Determine whether the cyclic group C_469 admits a (469,208,92)-difference set.

## novelty_notes
- frontier basis: Baumert-Gordon 2004 list (469,208,92) in Table 3, and Gordon-Schmidt 2015 still list [469] among the smallest open difference-set parameters.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: An exact resolution would already be a clean title theorem with bounded follow-up exposition because the ambient family and residual status are fully source-anchored.
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
- assessment: Lane-eligible. The candidate is exact, source-anchored, and close enough to paper-shaped that one solve would carry the note.

## likely_paper_shape
- note title: The Cyclic (469,208,92) Difference-Set Case
- hypothetical title: On the Cyclic (469,208,92) Difference-Set Problem
- paper shape: A short residual cyclic-difference-set paper anchored on the exact (469,208,92) theorem.
- publication if solved: A proof of existence or nonexistence would remove one of the smallest cyclic gcd(v,n)=1 survivors from Baumert-Gordon's k <= 300 table that still appears as open in the 2015 multiplier survey.
- minimal artifact requirements: Either a compact nonexistence proof in C_469 or an explicit cyclic construction, plus a brief source-faithful audit showing that previously published filters leave the case unresolved.

## hypothetical_abstract
We determine whether the cyclic group of order 469 admits a (469,208,92)-difference set. This parameter appears in Baumert-Gordon's list of unresolved cyclic cases with 150 <= k <= 300 and remains open in Gordon-Schmidt's 2015 multiplier-status table. The result therefore closes a canonical small-parameter cyclic residue and yields a naturally paper-shaped note.

## single_solve_explanation
The canonical source already packages the problem as a residual exact case, and the later survey confirms that it remained unsolved after additional multiplier-theorem progress. A complete proof would therefore provide the central mathematics and most of the novelty burden of the final note. The post-solve work is light framing rather than a further theorem campaign.

## broader_theorem_nonimplication
Baumert-Gordon's entire table-construction pipeline and the later multiplier-survey machinery both leave [469] unresolved, so the exact cyclic case is not already forced by the broader published theorems surfaced in this audit.

## literature_gap
Prior work stops at recording the cyclic parameter (469,208,92) as open in Baumert-Gordon 2004 and Gordon-Schmidt 2015.

## transfer_kit
- lemma: Baumert-Gordon's table-building starts from the standard parameter identity and the classical necessary conditions for cyclic difference sets.
- lemma: Their Section 3 gives the coefficient-vector equations for contracted polynomials theta[w](x), which are often enough to force contradictions for specific divisors w of v.
- lemma: Gordon-Schmidt 2015 identify the relevant prime divisors of n = 116 and frame the residual obstruction in multiplier language.
- lemma: The Xiang-Chen bound on cyclic multiplier groups, cited in later difference-set work, constrains any successful multiplier configuration once a candidate multiplier is forced.
- toy example: Work out the coefficient equations for a small cyclic difference set modulo a divisor w to illustrate how a polynomial reduction translates existence into a short integer-feasibility problem.
- known obstruction: Neither the standard small-parameter filters nor the later multiplier-survey machinery eliminates the case, so the final argument must extract a sharper orbit or cyclotomic obstruction.
- prior-work stop sentence: Baumert-Gordon list (469,208,92) as open in Table 3, and Gordon-Schmidt still list [469] as open in Table 2.
- recommended first attack: Exploit the factorization n = 4 * 29 and v = 7 * 67 to force a new multiplier or contracted multiplier, then test the resulting orbit counts against the contracted coefficient equations.
- paper if solved: If solved exactly, the paper would be a short note closing one of the smallest unresolved cyclic k <= 300 cases.

## bounded_source_list
- Leonard D. Baumert and Daniel M. Gordon, "On the existence of cyclic difference sets with small parameters" (Fields Institute Communications 41, 2004), especially Table 3 listing possible cyclic cases with 150 <= k <= 300 and gcd(v,n)=1; status rechecked against Daniel M. Gordon and Bernhard Schmidt, "A Survey of the Multiplier Conjecture" (2015), Table 2.
- Baumert-Gordon 2004 for the original small-parameter cyclic table and proof toolkit; Gordon-Schmidt 2015 for later open-status confirmation and multiplier framing.
- artifacts/cyclic-difference-set-469-208-92/record.md
- artifacts/cyclic-difference-set-469-208-92/status.json
