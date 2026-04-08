# Is the zero-divisor graph Γ(Z_3 × Z_25) prime?

- slug: `z3-z25-prime-zero-divisor-graph`
- canonical_source: Fox and Mooney, "On prime labelings of zero-divisor graphs," Congressus Numerantium 236 (2025), Conjecture 4.4, https://doi.org/10.61091/cn236-06
- open_status_checked_on: 2026-04-07
- attack_style: `['vertex-class decomposition', 'explicit constructive labeling', 'small obstruction counting']`
- curation_confidence: `high`

## question
Does the zero-divisor graph of the ring Z_3 × Z_25 admit a prime labeling?

## canonical_statement
Conjecture 4.4. The zero-divisor graph Γ(Z_p × Z_{q^2}) is prime for all prime numbers p and q.

## intended_statement
The zero-divisor graph Γ(Z_3 × Z_25) is prime.

## definitions
- Z_n denotes the ring of integers modulo n.
- For a commutative ring R, Γ(R) has as vertices the nonzero zero-divisors of R, with x adjacent to y iff xy = 0.
- In Z_25, the nonzero zero-divisors are exactly the nonzero multiples of 5.
- A prime labeling of an N-vertex graph is a bijection to {1, ..., N} such that adjacent vertices receive coprime labels.

## why_reasoning_friendly
This is the first concrete case omitted by Conjecture 4.4 after the source proves Z_p × Z_4, Z_p × Z_9, and Z_2 × Z_{q^2}. The graph has only 34 vertices and an evident split into coordinate-zero and multiple-of-5 classes.

## why_low_token
There are only 34 vertices, and the second factor has a single obvious zero-divisor chain. A full witness or counterexample certificate stays compact.

## verifier_hint
Enumerate the 34 nonzero zero-divisors of Z_3 × Z_25, generate edges by zero product, and test coprimality on each labeled edge.

## lean_hint
Formalize the graph from ZMod 3 × ZMod 25 or from explicit vertex classes, then prove a bijection to Fin 34 respects Nat.Coprime on edges.

## rediscovery_risk
Low to moderate: Theorems 2.12, 2.14, and 2.15 settle only the q = 2, q = 3, and p = 2 border families, so this p = 3, q = 5 case is inferred as the first omitted instance; exact and alternate searches did not reveal a later resolution.

## why_still_appears_open
The exact-instance search produced no useful hit, the alternate ASCII search surfaced only generic zero-divisor-graph material, and inside the canonical source the solved earlier results stop at Z_p × Z_4, Z_p × Z_9, and Z_2 × Z_{q^2} before Conjecture 4.4 is stated. The 2025-2026 DOI/source search showed the paper and archive page but no instance-specific follow-up.

## red_flags
- The target is inferred as the smallest unsolved instance rather than named explicitly in the paper.
- A successful labeling may still need careful coordination across the two main vertex classes.
