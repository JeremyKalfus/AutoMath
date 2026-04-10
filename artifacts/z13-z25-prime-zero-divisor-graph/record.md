# Solve Record: z13-z25-prime-zero-divisor-graph

## statement_lock

- Active title: `Is the zero-divisor graph Γ(Z_13 × Z_25) prime?`
- Active slug: `z13-z25-prime-zero-divisor-graph`
- Locked target statement: determine whether the zero-divisor graph `Γ(Z_13 × Z_25)` admits a prime labeling, meaning a bijection from its `84` vertices to `{1,2,...,84}` such that adjacent vertices receive coprime labels.
- This pass is locked to the exact feeder instance `Z_13 × Z_25`, not the full family `Γ(Z_p × Z_25)`.

## definitions

- Write vertices as pairs `(a,b)` with `a ∈ Z_13` and `b ∈ Z_25`.
- A nonzero zero-divisor is exactly a nonzero pair with either `a = 0` or `5 | b`.
- The nonzero zero-divisors split into the same four support classes as the `p = 5,7,11` line:
  - `A = {(0,u) : u ∈ Z_25^× and 5 ∤ u}`, size `20`.
  - `B = {(0,5),(0,10),(0,15),(0,20)}`, size `4`.
  - `C = {(a,0) : a ∈ Z_13^×}`, size `12`.
  - `D = {(a,5t) : a ∈ Z_13^×, t ∈ {1,2,3,4}}`, size `48`.
- Adjacency is by zero product:
  `(a,b) ~ (c,d)` iff `ac = 0 mod 13` and `bd = 0 mod 25`.
- Because `Z_13` is a field, the first-coordinate product vanishes iff at least one first coordinate is `0`.
- In `Z_25`, the product of two nonzero elements is `0` iff both are multiples of `5`.

## approach_A

Structural support decomposition.

- The exact edge pattern is unchanged from the earlier `Γ(Z_p × Z_25)` feeders:
  - `A-C` complete bipartite;
  - `B-B` a `K_4`;
  - `B-C` complete bipartite;
  - `B-D` complete bipartite;
  - no other edge types.
- Edge counts at `p = 13`:
  - `A-C = 20 · 12 = 240`;
  - `B-B = 6`;
  - `B-C = 4 · 12 = 48`;
  - `B-D = 4 · 48 = 192`.
- Total predicted edge count: `240 + 6 + 48 + 192 = 486`.

Self-check after Approach A:

- Vertex count check: `20 + 4 + 12 + 48 = 84`.
- Structural check: the instance stays exactly on the campaign support template `A-C`, `B-B`, `B-C`, `B-D`.

## approach_B

Arithmetic witness search, still reasoning-first.

- The old `p = 11` four-class template already isolates the real arithmetic burdens:
  - `A ∪ B` must avoid all prime factors used on `C`;
  - `B` must be pairwise coprime;
  - `D` must avoid nontrivial multiples of the barrier labels on `B`.
- The unchanged upper-half-prime-only `C` subtemplate fails at `p = 13`:
  - `|C| = 12`;
  - the interval `[43,84]` contains only the ten primes
    `43,47,53,59,61,67,71,73,79,83`.
- The key refinement is to admit two extra primes below half the interval:
  - take `37` and `41` as the missing `C` labels;
  - their only extra multiples in `{1,...,84}` are `74 = 2·37` and `82 = 2·41`;
  - those doubles need only stay out of `A ∪ B`, not out of the whole labeling, because `D` has no edges to `C`.
- Keep the same sparse barrier set as the verified `p = 11` feeder:
  - `B = {1,19,23,29}`;
  - nontrivial multiples up to `84` are
    `38,57,76` for `19`,
    `46,69` for `23`,
    and `58` for `29`.
- Those six spill labels fit comfortably inside the twenty `A` slots.

One explicit classwise partition suggested by this logic is:

- `C = {37,41,43,47,53,59,61,67,71,73,79,83}`.
- `B = {1,19,23,29}`.
- `A = {2,3,4,5,6,7,8,9,10,11,12,13,14,15,38,46,57,58,69,76}`.
- `D` gets the remaining `48` labels.

Self-check after Approach B:

- `B` is still pairwise coprime.
- `A ∪ B` avoids every `C` label and also avoids the only extra multiples `74` and `82` of `37` and `41`.
- `D` avoids every nontrivial multiple of `19`, `23`, and `29` up to `84`.

## lemma_graph

1. The vertex set is exactly `A ⊔ B ⊔ C ⊔ D` with sizes `20,4,12,48`.
2. The exact edge pattern is `A-C`, `B-B`, `B-C`, and `B-D`.
3. If every label on `A ∪ B` is coprime to every label on `C`, then all `A-C` and `B-C` edges are valid.
4. If the four labels on `B` are pairwise coprime, then all `B-B` edges are valid.
5. If every label on `D` is coprime to every label on `B`, then all `B-D` edges are valid.
6. Therefore any partition of `{1,...,84}` into class label sets satisfying those obligations gives a prime labeling.

## chosen_plan

- Reuse the verified four-class support decomposition.
- Keep the proven sparse barrier set `B = {1,19,23,29}`.
- Refine only the `C` block by allowing two primes below the half-interval threshold and sending their doubles to `D`.
- Use one tiny checker only after the explicit class partition is fixed.

## code_used

- A tiny local checker `check_witness.py` was used only after the reasoning and explicit class partition were fixed.
- The checker enumerates the `84` nonzero zero-divisors of `Z_13 × Z_25`, generates edges directly from the ring multiplication rule, checks bijectivity onto `{1,...,84}`, and tests `gcd = 1` on every edge.
- Result after running the checker:
  - `vertex_count = 84`
  - `edge_count = 486`
  - `edge_type_counts = {A-C: 240, B-B: 6, B-C: 48, B-D: 192}`
  - `label_bijection_ok = 1`
  - `edge_coprime_ok = 1`

## result

Current best candidate witness:

- Put the labels `37,41,43,47,53,59,61,67,71,73,79,83` on `C` in any order.
- Put the labels `1,19,23,29` on `B` in any order.
- Put the labels `2,3,4,5,6,7,8,9,10,11,12,13,14,15,38,46,57,58,69,76` on `A` in any order.
- Put the remaining `48` labels
  `16,17,18,20,21,22,24,25,26,27,28,30,31,32,33,34,35,36,39,40,42,44,45,48,49,50,51,52,54,55,56,60,62,63,64,65,66,68,70,72,74,75,77,78,80,81,82,84`
  on `D` in any order.

Why this works:

- `B-B` edges:
  `1,19,23,29` are pairwise coprime.
- `A-C` and `B-C` edges:
  every label on `C` is prime, and within `{1,...,84}` the only extra forbidden labels are `74` and `82`, coming from `37` and `41`. None of those forbidden labels is used on `A ∪ B`.
- `B-D` edges:
  every nontrivial multiple of `19`, `23`, and `29` up to `84` is one of `38,46,57,58,69,76`, and those six labels were deliberately placed in `A`.
- There are no other edges.

Therefore the intended statement appears true for this exact feeder instance.

Strong-result extraction:

- The four-class arithmetic program survives the first `p = 13` test on the `Γ(Z_p × Z_25)` line.
- What breaks is only the overly rigid subtemplate “put all `C` labels above half the interval.”
- The honest refinement is:
  - allow a bounded number of `C` primes below the half-interval cutoff;
  - require only that their nontrivial multiples stay out of `A ∪ B`, not out of the whole label interval.
- This is a stronger campaign result than a raw exact win because it upgrades the four-class theorem-slice target itself.

## verify_rediscovery

- PASS 1 used a bounded web audit aimed at the exact instance, the family notation, and the most relevant recent source already in the campaign record.
- Exact-instance searches on `Γ(Z_13 × Z_25)`, `Z_13 × Z_25` with `zero-divisor graph`, and family searches on `Γ(Z_p × Z_25)` with `prime labeling` did not establish an earlier theorem, proposition, example, or corollary settling this exact case within budget.
- I rechecked the 2025 paper `On Prime Labelings of Zero-Divisor Graphs`. It still presents `Γ(Z_p × Z_q^2)` as an open conjectural family rather than a finished theorem line, and the bounded pass did not reveal the exact `p = 13, q = 5` case there.
- Verdict for PASS 1: no rediscovery established within budget.

## verify_faithfulness

- The record stays locked to the exact intended feeder statement: existence of a prime labeling for the full zero-divisor graph `Γ(Z_13 × Z_25)`.
- The graph definition used here matches the campaign dossier exactly: vertices are the nonzero zero-divisors of `Z_13 × Z_25`, the graph is simple, adjacency is coordinatewise zero product, and the labels form a bijection onto `{1,...,84}`.
- No quotient graph, orbit graph, or weaker proxy theorem is substituted for the exact instance.

## verify_proof

- I recomputed the support decomposition from the ring definition and recovered the exact class pattern `A-C`, `B-B`, `B-C`, `B-D` with counts `240, 6, 48, 192`.
- Given that edge pattern, the proof reduces correctly to three arithmetic obligations:
  - every label on `A ∪ B` is coprime to every label on `C`;
  - the four labels on `B` are pairwise coprime;
  - every label on `D` is coprime to every label on `B`.
- Those obligations hold for the proposed label sets:
  - `C` consists of primes, and the only extra multiples up to `84` are `74` and `82`, both kept out of `A ∪ B`;
  - `B = {1,19,23,29}` is pairwise coprime;
  - the nontrivial multiples of `19`, `23`, and `29` up to `84` are exactly `38,46,57,58,69,76`, all placed in `A`.
- First incorrect step found: none.

## verify_adversarial

- I reran the checker `artifacts/z13-z25-prime-zero-divisor-graph/check_witness.py`.
- It reported `vertex_count = 84`, `edge_count = 486`, `edge_type_counts = {'A-C': 240, 'B-B': 6, 'B-C': 48, 'B-D': 192}`, `label_bijection_ok = 1`, and `edge_coprime_ok = 1`.
- I also checked that the four label classes are disjoint and cover exactly `{1,...,84}`.
- No hidden edge type or missed divisibility obstruction appeared.

## verify_verdict

- `VERIFIED`
- The exact feeder survives skeptical verification and materially changes the family story at `p = 13`.
- The right publication interpretation is not “the old `F25` subtemplate survived unchanged.” It is “the four-class line survives `p = 13`, but only after refining the `C` block.”

## publication_use

- This feeder materially sharpens the theorem-slice target:
  - the four-class `Γ(Z_p × Z_25)` line now has verified feeders at `p = 11` and `p = 13`;
  - the old upper-half-prime `C` heuristic is now honestly replaced by a refined doubled-prime-exception version;
  - the next decisive zero-divisor feeder shifts to `Γ(Z_13 × Z_13 × Z_2)`.
