## statement_lock

Title: Does the 4x4 grid `P_4 x P_4` admit a prime labeling?

Exact intended statement used in this solve pass:
There exists a bijection `f : V(P_4 x P_4) -> {1,2,...,16}` such that for every grid edge `uv`, `gcd(f(u), f(v)) = 1`.

Coordinate model:
Use vertices `(r,c)` with `r,c in {1,2,3,4}` and edges between pairs at Manhattan distance `1`.

I will treat `P_4 x P_4 is prime` as the claim to prove by explicit construction. Since solve is offline and rediscovery risk is nonzero, even a successful construction should be classified only as `CANDIDATE` here.

## definitions

- Prime labeling means a bijection from the 16 vertices to `{1,...,16}` with coprime labels on every horizontal or vertical edge.
- The natural checkerboard bipartition is by parity of `r+c`.
- Ambiguity check: the dossier already fixes the graph as the ordinary Cartesian-product grid, so there is no diagonal adjacency.
- Ambiguity check: no additional requirement is imposed on nonadjacent pairs.
- Convention used below: I will try a checkerboard placement with odd labels on the `r+c` even cells and even labels on the `r+c` odd cells.

## approach_A

Structural / invariant route:

1. Any two even labels have gcd at least `2`, so no edge can join two even labels.
2. A checkerboard odd/even placement therefore removes all even-even conflicts at once.
3. After that reduction, the only bad odd-even pairs among `{1,...,16}` are:
   - `3` with `6,12`
   - `5` with `10`
   - `7` with `14`
   - `9` with `6,12`
   - `15` with `6,10,12`
4. The odd labels `1,11,13` are universally safe against all even labels, so they are ideal for high-degree odd positions.
5. The restrictive labels `15,3,9,5,7` should be assigned to low-degree odd positions, then the neighboring even cells can be chosen to avoid only a handful of forbidden values.

Heuristic consequence:
Put `11` and `13` on the two odd interior cells of degree `4`, put the most restrictive label `15` on an odd corner, and try to complete the remaining six odd cells so that `6,10,12,14` can be parked away from their forbidden odd neighbors.

## approach_B

Construction / contradiction route:

Fix the odd cells (those with `r+c` even) as

- corners: `(1,1)`, `(4,4)`
- edges: `(1,3)`, `(2,4)`, `(3,1)`, `(4,2)`
- interiors: `(2,2)`, `(3,3)`

Try the odd assignment

- `(1,1)=15`
- `(1,3)=3`
- `(2,2)=11`
- `(2,4)=7`
- `(3,1)=9`
- `(3,3)=13`
- `(4,2)=5`
- `(4,4)=1`

This creates only local bans on the even cells:

- neighbors of `15` cannot be `6,10,12`
- neighbors of `3` or `9` cannot be `6,12`
- neighbors of `7` cannot be `14`
- neighbors of `5` cannot be `10`

The resulting even-cell restrictions are manageable:

- `(1,2)` and `(2,1)` cannot be `6,10,12`
- `(1,4)` and `(2,3)` cannot be `6,12,14`
- `(3,2)` and `(4,1)` cannot be `6,10,12`
- `(3,4)` cannot be `14`
- `(4,3)` cannot be `10`

This strongly suggests parking the hard even labels as follows:

- `6` at `(3,4)`
- `12` at `(4,3)`
- `10` at `(1,4)`
- `14` at `(4,1)`

and then filling the remaining even cells with the unrestricted set `{2,4,8,16}`.

## lemma_graph

1. Checkerboard placement kills all even-even edge conflicts.
2. Only five odd labels are restrictive: `3,5,7,9,15`.
3. The safe odd labels `1,11,13` can absorb the degree-4 burden.
4. If `15` sits on a corner, its two neighbors can both be chosen from `{2,4,8,14,16}`.
5. If `3` and `9` are kept away from `6` and `12`, and `5` is kept away from `10`, and `7` is kept away from `14`, then every edge is coprime automatically because all remaining odd-even pairs in `{1,...,16}` are coprime.
6. Therefore an explicit witness should finish the proof.

## chosen_plan

Use approach_B, because the local-ban system is small enough to solve by hand.

Candidate labeling matrix:

| 15 | 2  | 3  | 10 |
| 4  | 11 | 8  | 7  |
| 9  | 16 | 13 | 6  |
| 14 | 5  | 12 | 1  |

Reason this should work:

- every horizontal and vertical edge is odd-even
- the only potentially bad odd-even pairs are the nine pairs listed in `approach_A`
- the candidate neighborhoods are:
  - `15` adjacent to `2,4`
  - `3` adjacent to `2,10,8`
  - `7` adjacent to `10,8,6`
  - `9` adjacent to `4,16,14`
  - `5` adjacent to `16,14,12`
  - `1` adjacent to `6,12`
  - `11` adjacent to `2,4,8,16`
  - `13` adjacent to `8,16,6,12`
- none of those neighbors is forbidden for its odd label

At this point the handwritten argument already looks complete enough for a candidate solve. A tiny checker is justified only as witness verification, not as search.

## self_checks

1. Statement lock check: the target is the exact 16-vertex witness question, not a broader family claim.
2. Definition check: only horizontal and vertical adjacencies matter.
3. Structural check: the bad odd-even pairs were exhaustively listed from `{1,...,16}`.
4. Construction check: the proposed matrix is bijective on `{1,...,16}` by inspection.
5. Risk check before code: the main possible failure is an overlooked bad edge in the matrix, so a tiny witness checker is justified.
6. Post-checker confirmation: a one-off exact checker confirmed bijectivity and gcd `1` on all `24` grid edges.

## code_used

Used exactly one tiny witness checker after the reasoning was complete. It did two things only:

- verified that the 16 entries are exactly `{1,...,16}`
- verified gcd `1` on all horizontal and vertical edges

No search, optimization, SAT, ILP, CP-SAT, or brute force was used.

## result

The solve pass produced an explicit prime-labeling witness:

| 15 | 2  | 3  | 10 |
| 4  | 11 | 8  | 7  |
| 9  | 16 | 13 | 6  |
| 14 | 5  | 12 | 1  |

The handwritten local-ban argument explains why this matrix should work, and the tiny checker confirmed that it is a bijection on `{1,...,16}` and that all `24` grid edges join coprime labels.

Solve-stage classification: `CANDIDATE`

Confidence: high

Lean readiness: yes for witness formalization, subject to verification's prior-art check.

## likely_failure_points

- I may have missed a forbidden adjacency while reading the matrix.
- The parity-based setup is used only as a construction heuristic here; I did not prove that every prime labeling must respect this exact checkerboard parity class.
- Because solve is offline, prior-art risk is unresolved and must be handled in verification rather than here.

## what_verify_should_check

- Recompute the full set of non-coprime odd-even pairs in `{1,...,16}`.
- Check the explicit witness matrix edge-by-edge.
- Confirm there is no hidden convention issue about `P_4 x P_4`.
- Do the bounded rediscovery pass carefully, because this exact instance is small and could already be known.

## verify_rediscovery

PASS 1 used a bounded web audit and stopped within budget.

Search patterns covered:

1. exact instance notation: `P_4 x P_4` prime labeling, `P4 x P4` prime labeling, `4x4 grid` prime labeling
2. alternative notation / family notation: `P_m x P_n` with `(4,4)`-style targeting and generic grid-graph prime-labeling searches
3. canonical sources: Gallian's dynamic survey DS6 and Curran's 2022 grid-graph paper
4. same-source theorem / example checks: targeted checks for whether the cited sources already list, imply, or exemplify the exact `4x4` case
5. recent status / discussion check: a recent family-level grid-labeling follow-up was checked to see whether the exact instance had since been absorbed by a broader theorem

Outcome:

- I did not find a source stating that `P_4 x P_4` is already known to be prime or non-prime.
- Gallian's survey records several grid families and specific positive instances, but the audit did not uncover an entry settling the composite square `P_4 x P_4` instance.
- Curran's 2022 planar-grid paper appears to treat broad grid families, especially prime-dimension cases, but this audit did not uncover a theorem / proposition / example that directly settles the exact `4x4` instance.
- The recent follow-up check also did not reveal an exact-instance settlement; it looked more like continued partial-family progress than a clean prior-art resolution of `P_4 x P_4`.

Verification judgment for PASS 1:

- `REDISCOVERY` is not established.
- Rediscovery risk remains nonzero because this is a very small instance and the literature is family-based, but within the bounded audit I found no explicit prior-art resolution of the exact intended statement.

If the current witness is mathematically correct, it still looks like a possible frontier-novel `CANDIDATE`, not an `EXACT` result.

## verify_faithfulness

The solver's claimed result matches the intended statement exactly.

- Target statement: there exists a prime labeling of the Cartesian grid graph `P_4 x P_4` using the labels `{1,...,16}`.
- Delivered object: a concrete `4 x 4` labeling matrix on exactly those labels.
- Checked definitions: adjacency is only horizontal / vertical, with no diagonal edges and no extra global requirement on nonadjacent pairs.

No wrong-theorem drift, quantifier drift, or definition change was found.

## verify_proof

First incorrect step found: none.

The proof is short enough that the decisive argument is simply the explicit witness plus direct verification.

I independently recomputed the complete set of bad odd-even pairs in `{1,...,16}`:

- `(3,6)`, `(3,12)`, `(5,10)`, `(7,14)`, `(9,6)`, `(9,12)`, `(15,6)`, `(15,10)`, `(15,12)`

This exactly matches the solver's list. I then checked the proposed matrix

| 15 | 2  | 3  | 10 |
| 4  | 11 | 8  | 7  |
| 9  | 16 | 13 | 6  |
| 14 | 5  | 12 | 1  |

against all `24` grid edges, and every horizontal and vertical edge has gcd `1`.

The solver's handwritten local-ban discussion is therefore sufficient but not actually needed: the explicit witness itself proves the existential claim once bijectivity and all `24` edge gcd checks are verified.

## verify_adversarial

I reran an independent checker locally.

Results:

- bijectivity on `{1,...,16}`: passed
- all `24` horizontal / vertical edge gcd checks: passed
- recomputed forbidden odd-even pairs: matched the proof text exactly

I also tried to break the claim conceptually by looking for hidden convention failures:

- wrong graph model: not found
- missing edge class: not found
- duplicate / omitted label: not found
- dependence on an unproved structural lemma: not needed, because the concrete witness alone settles the existential claim

Adversarial conclusion: the candidate survives this pass.

## verify_verdict

`VERIFIED`

Reason:

- PASS 1 did not establish rediscovery within the bounded audit.
- PASS 2 found that the solved claim matches the intended statement exactly.
- PASS 3 found no incorrect step; the witness is a complete exact proof of existence.
- PASS 4 independently rechecked the witness computationally and found no defect.

Harness classification after verify should remain `CANDIDATE`, not `EXACT`, because Lean has not yet formalized the witness.

## minimal_repair_if_any

No mathematical repair is needed.

## lean_statement
- Official Lean backend module: `lean/AutoMath/P4xP4GridPrimeLabeling.lean`.
- Mirrored artifact Lean file: `artifacts/p4x-p4-grid-prime-labeling/lean/AutoMath/P4xP4GridPrimeLabeling.lean`.
- Axiom audit file: `artifacts/p4x-p4-grid-prime-labeling/lean/AxiomAudit.lean`.
- Lean vertex model: `Vertex = Fin 4 × Fin 4`, interpreted as grid coordinates `(r,c)` with `r,c ∈ {0,1,2,3}`.
- Lean adjacency: `Adj (r1,c1) (r2,c2) := Nat.dist r1 r2 + Nat.dist c1 c2 = 1`, exactly the horizontal/vertical adjacency relation on `P_4 x P_4`.
- Lean label model: `Label = Fin 16`, interpreted as the mathematical label set `{1,...,16}` by `labelValue i = i + 1`.
- Exact target theorem: `AutoMath.P4xP4GridPrimeLabeling.p4x_p4_grid_prime : intendedStatement`.
- Expanded exact target: `intendedStatement := ∃ f : Vertex → Label, Function.Bijective f ∧ ∀ x y, Adj x y → Nat.Coprime (labelValue (f x)) (labelValue (f y))`.
- Faithfulness audit: `p4x_p4_grid_prime_statement` and `intendedStatement_faithful` are definitional (`rfl`), and `witness_values_match_record` matches the verified witness matrix
  `[[15,2,3,10],[4,11,8,7],[9,16,13,6],[14,5,12,1]]`.

## lean_skeleton
- Skeleton theorem: `AutoMath.P4xP4GridPrimeLabeling.p4x_p4_grid_prime_skeleton`.
- Skeleton content: if the verified witness `label` is shown bijective and edge-coprime for the exact `Adj` relation on `Fin 4 × Fin 4`, then the exact intended statement follows immediately.
- Remaining obligations isolated by the skeleton were `label_bijective` and `label_edgeCoprime`.

## lean_result
- `lake build AutoMath.P4xP4GridPrimeLabeling` succeeded in the official `lean/` backend.
- The backend file is imported by `lean/AutoMath.lean`, so the result is wired into the official AutoMath Lean project.
- `lake build` was also run repo-wide; it still fails in unrelated existing modules `lean/AutoMath/C16458CNBC.lean` and `lean/AutoMath/C244512CNBC.lean`, not in this new module.
- The exact witness is formalized by `label`, and `witness_values_match_record` confirms the row-major values
  `15, 2, 3, 10 / 4, 11, 8, 7 / 9, 16, 13, 6 / 14, 5, 12, 1`.
- `p4x_p4_grid_prime_checked` proves that this witness is a genuine prime labeling for the exact `P_4 x P_4` graph instance.
- `p4x_p4_grid_prime_explicit` records the explicit natural-number form of the verified witness.
- Axiom audit via `lake env lean ../artifacts/p4x-p4-grid-prime-labeling/lean/AxiomAudit.lean` reported only `[propext, Classical.choice, Quot.sound]` for the main theorem, the checked theorem, and the explicit theorem; no `sorryAx` appeared in the audit output.
- Lean conclusion: the exact intended statement `P_4 x P_4 is prime` is fully formalized and checked, so this run earns `classification = EXACT` and `lean_complete = true`.

## lean_blockers
- No blocker remains for the target theorem itself.
- `lean4checker --fresh` is unavailable on this machine, so no fresh-environment recheck was run.
- Repo-wide `lake build` still has unrelated pre-existing failures in `C16458CNBC` and `C244512CNBC`, but the target module checks independently.

Only a presentation-level tightening is advisable for later stages: when formalizing or summarizing the result, lead with the explicit witness and the direct `24`-edge verification, since that alone proves the statement without relying on the heuristic parity discussion.
