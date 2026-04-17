# Working Packet: The Cyclic (639,232,84) Difference-Set Problem

- slug: `cyclic-difference-set-639-232-84`
- title: cyclic-difference-set-639-232-84
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `76`
- single-solve-to-paper fraction: `0.73`

## statement
Determine whether the cyclic group C_639 admits a (639,232,84)-difference set.

## novelty_notes
- frontier basis: Baumert-Gordon 2004 retain (639,232,84) in Table 3, and Gordon-Schmidt 2015 still list both [639] and the noncyclic variant [3,213] as open.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: An exact cyclic resolution would already remove one residual row from a canonical open table and would need only bounded contextualization around the older elimination program.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: tiny
- assessment: Lane-eligible, but weaker than the first two choices. The family anchor is strong, yet the exact theorem is a little more table-row-shaped.

## likely_paper_shape
- note title: The Cyclic (639,232,84) Difference-Set Problem
- hypothetical title: On Cyclic (639,232,84) Difference Sets
- paper shape: A compact exact-case note on the cyclic (639,232,84) problem.
- publication if solved: A proof of existence or nonexistence would settle another small cyclic survivor that persisted from Baumert-Gordon's k <= 300 table into the 2015 multiplier-status survey.
- minimal artifact requirements: A concise proof in C_639, ideally multiplier-driven or cyclotomic, together with a literature audit that distinguishes the cyclic [639] case from the separate abelian [3,213] variant.

## hypothetical_abstract
We determine whether the cyclic group of order 639 admits a (639,232,84)-difference set. This parameter survives Baumert-Gordon's k <= 300 cyclic search and remains present in Gordon-Schmidt's 2015 list of open difference-set parameters. The result would close a clearly documented residual case with a short, exact-case paper.

## single_solve_explanation
The tuple is already isolated in the literature, so an exact proof would contribute the core mathematics and most of the novelty of the final note. Remaining work would consist of comparing the cyclic [639] case with the distinct noncyclic [3,213] row and explaining why existing multiplier tools stop short. That is still inside the micro-paper band, though less crisp than the smaller 465 and 469 cases.

## broader_theorem_nonimplication
The later survey explicitly continues to list both the cyclic and noncyclic group types for this parameter, showing that the published multiplier machinery does not collapse the exact cyclic theorem into an already-known ambient statement.

## literature_gap
Prior work stops at listing the cyclic [639] realization of (639,232,84) as open in Baumert-Gordon 2004 and Gordon-Schmidt 2015.

## transfer_kit
- lemma: Baumert-Gordon's contracted coefficient equations apply to every divisor w of 639 and convert a putative cyclic difference set into a short integer correlation system.
- lemma: Their search pipeline already absorbs the standard Schutzenberger, BRC, Mann, Lander, and Yamamoto tests before declaring the case open.
- lemma: Gordon-Schmidt 2015 record both [639] and [3,213] as unresolved, clarifying that group type matters and that a cyclic proof is not automatically inherited from a broader abelian theorem.
- toy example: Use a small cyclic difference set to show how one compares the coefficient vector for [v] with that of a noncyclic group of the same order; this matters here because [639] and [3,213] must be separated.
- known obstruction: The cyclic case coexists in the survey with a distinct noncyclic open row, so a final proof has to use structure special to C_639 rather than only parameter arithmetic.
- prior-work stop sentence: Baumert-Gordon keep (639,232,84) in Table 3, and Gordon-Schmidt still list [639] as open in Table 2.
- recommended first attack: Use the prime factors of n = 148 to force or obstruct candidate multipliers in C_639, then apply the contracted coefficient equations at divisors 3, 9, and 71.
- paper if solved: If solved exactly, the paper would be a short exact-case note separating the cyclic group of order 639 from the remaining open abelian variants.

## bounded_source_list
- Leonard D. Baumert and Daniel M. Gordon, "On the existence of cyclic difference sets with small parameters" (Fields Institute Communications 41, 2004), especially Table 3 listing possible cyclic cases with 150 <= k <= 300 and gcd(v,n)=1; status rechecked against Daniel M. Gordon and Bernhard Schmidt, "A Survey of the Multiplier Conjecture" (2015), Table 2.
- Baumert-Gordon 2004 for the original cyclic table; Gordon-Schmidt 2015 for later open-status confirmation and multiplier-theorem context.
- artifacts/cyclic-difference-set-639-232-84/record.md
- artifacts/cyclic-difference-set-639-232-84/status.json
