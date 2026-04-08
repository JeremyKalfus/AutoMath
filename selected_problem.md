# Is the zero-divisor graph Γ(Z_5 × Z_5 × Z_3) prime?

- slug: `z5-z5-z3-prime-zero-divisor-graph`
- canonical_source: Fox and Mooney, "On prime labelings of zero-divisor graphs," Congressus Numerantium 236 (2025), Conjecture 4.3, https://doi.org/10.61091/cn236-06
- open_status_checked_on: 2026-04-07
- attack_style: `['support-type decomposition', 'prime-scarcity packing', 'explicit constructive labeling']`
- curation_confidence: `high`

## question
Does the zero-divisor graph of the ring Z_5 × Z_5 × Z_3 admit a prime labeling?

## canonical_statement
Conjecture 4.3. The zero-divisor graph Γ(Z_p × Z_p × Z_q) is prime for all prime numbers p and q.

## intended_statement
The zero-divisor graph Γ(Z_5 × Z_5 × Z_3) is prime.

## definitions
- Z_p denotes the ring of integers modulo the prime p.
- For a commutative ring R, Γ(R) has as vertices the nonzero zero-divisors of R, with x adjacent to y iff xy = 0.
- For R = Z_5 × Z_5 × Z_3, multiplication is coordinatewise, so adjacency depends only on which coordinates are zero.
- A prime labeling of an N-vertex graph is a bijection to {1, ..., N} such that adjacent vertices receive coprime labels.

## why_reasoning_friendly
The same support-pattern structure from Conjecture 4.3 remains intact here, and the graph is still small enough at 42 vertices for a deliberate hand-built labeling. The extra third-factor size may permit cleaner parity and coprimality packing than the q = 2 case.

## why_low_token
The graph has 42 vertices, still small enough for a full witness and cheap checker. The description by support classes remains compact.

## verifier_hint
Enumerate the 42 nonzero zero-divisors of Z_5 × Z_5 × Z_3 and check the gcd condition on every edge of a proposed labeling.

## lean_hint
Use ZMod 5 × ZMod 5 × ZMod 3 or an explicit finite support-class model, then formalize a bijection to Fin 42 with Nat.Coprime along adjacency edges.

## rediscovery_risk
Moderate: this is a second-step instance from the same fresh family conjecture, so there is more chance of an unadvertised note or example than for the smallest omitted case; exact and alternate searches still failed to surface any instance-specific resolution.

## why_still_appears_open
The exact-instance search returned no relevant match, the alternate ASCII search produced only generic or unrelated pages, and the canonical source still moves directly from the solved p = 2 and p = 3 families to Conjecture 4.3 with no theorem, proposition, example, or observation settling the p = 5, q = 3 case. The shared 2025-2026 DOI/source search showed no later sequel.

## red_flags
- This is not the smallest omitted case in Conjecture 4.3, so rediscovery risk is a little higher than for Z_5 × Z_5 × Z_2.
- The larger label set makes a hand construction slightly more fiddly.
