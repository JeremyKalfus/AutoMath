# d5-balanced-equi-30-square

## statement_lock
- Active slug: `d5-balanced-equi-30-square`
- Title: `Does a 5-balanced equi-30-square exist?`
- Locked intended statement: there exists a `30 x 30` matrix on `Z_30` in which each symbol occurs `30` times total and, whenever a symbol occurs in a row or column, it occurs there exactly `5` times.
- I am solving the direct equi-square statement, not a strengthened Latin-subrectangle proxy.

Self-check:
- The target is the exact dossier statement.
- I am not assuming any extra global row-block or column-block structure.

## definitions
- For a symbol `s`, let `R_s` be the set of rows containing `s`, and `C_s` the set of columns containing `s`.
- Because `s` occurs `30` times total and contributes `5` occurrences in each active row and active column, necessarily `|R_s| = |C_s| = 6`.
- Inside `R_s x C_s`, each active row has exactly one column where `s` is absent, and each active column has exactly one row where `s` is absent. Therefore the support of `s` is
  `K_{6,6}` minus a perfect matching:
  there is a bijection `pi_s : R_s -> C_s` such that
  `s` occupies exactly the cells `(r,c)` with `r in R_s`, `c in C_s`, and `c != pi_s(r)`.
- Dually, each row contains exactly `6` symbols, each appearing `5` times, and each column also contains exactly `6` symbols.
- For two symbols `s,t`, write
  `x_{s,t} = |R_s cap R_t|` and `y_{s,t} = |C_s cap C_t|`.

Self-check:
- The `6 x 6` minus matching model is exact, not heuristic.
- The row and column regularity numbers are forced by the stated counts.

## approach_A
Structural / invariant approach: push the direct `R_s, C_s, pi_s` model and look for unavoidable overlap contradictions.

1. Fix two symbols `s,t` with at least one common row `r`.
   In that row, `s` occupies `C_s \\ {pi_s(r)}` and `t` occupies `C_t \\ {pi_t(r)}`.
   These two `5`-sets are disjoint because every cell in row `r` carries only one symbol.
   Hence any common column of `s` and `t` must lie in `{pi_s(r), pi_t(r)}`.
   So if `x_{s,t} > 0`, then `y_{s,t} <= 2`.

2. By symmetry, if `y_{s,t} > 0`, then `x_{s,t} <= 2`.

3. Therefore any pair of symbols that overlaps in both rows and columns must satisfy
   `1 <= x_{s,t} <= 2` and `1 <= y_{s,t} <= 2`.
   In particular, if two symbols share `3` or more rows, they share no columns at all; and if they share `3` or more columns, they share no rows at all.

4. Global row-pair counting gives
   `sum_{s < t} x_{s,t} = 30 * C(6,2) = 450`,
   because each symbol contributes its `15` row-pairs.
   Likewise `sum_{s < t} y_{s,t} = 450`.
   Since there are `C(30,2) = 435` row-pairs, the average row-pair shares about `1.034` symbols.

5. There is also a support-overlap identity.
   Let `m(r,c)` be the number of non-occupying symbols whose `6 x 6` support still contains the cell `(r,c)`.
   Then each cell has support multiplicity `1 + m(r,c)`, and
   `sum_{r,c} m(r,c) = 30 * 6 = 180`,
   because each symbol omits exactly `6` cells from its `6 x 6` support.
   Counting pairs of symbols through support-overlap cells gives
   `sum_{s < t} x_{s,t} y_{s,t} = sum_{r,c} C(1 + m(r,c), 2) >= 180`.

6. That lower bound forces many symbol pairs to overlap in both rows and columns, but the previous lemma confines every such pair to the tiny range
   `(x_{s,t}, y_{s,t}) in {(1,1), (1,2), (2,1), (2,2)}`.
   I tried to turn this into a contradiction, but the remaining integer slack is still large enough that no clean impossibility drops out.

Self-check:
- The overlap lemma itself is rigorous.
- The global counts are exact.
- The failure point is not an incorrect step; it is that these invariants still admit too many feasible overlap patterns.

## approach_B
Construction / extremal approach: test the narrowest natural existence ansatz, namely a cyclic translate construction.

1. Suppose one symbol, say `0`, has template data `(R, C, phi)` where `R, C subseteq Z_30`, `|R| = |C| = 6`, and `phi : R -> C` is a bijection.
   Develop this template by translation:
   symbol `s` uses row-set `R + s`, column-set `C + s`, and omits the translated matching given by `phi`.

2. In such a cyclic model, a cell `(x,y)` is occupied by symbol `s` exactly when
   `y - x = c - r` for some template pair `(r,c)` that is not deleted.
   Therefore the cyclic construction works if and only if the `30` kept differences
   `c - r (mod 30)` are exactly the `30` residues once each.

3. Equivalently, the `6 x 6` difference table `(c - r)` must have the property that after deleting one entry from each row and each column, the remaining `30` entries are `0,1,...,29` in some order.

4. I bounded this hypothesis further by normalizing the row template to
   `R = {0,1,2,3,4,5}` and exhaustively checking every `6`-subset `C subseteq Z_30`.
   The script in `artifacts/d5-balanced-equi-30-square/cyclic_normalized_search.py` iterates all `593775` such `C`.
   It found `2280` support candidates where the full difference multiset already covers all `30` residues with exactly six duplicates, but none admitted a deleted permutation whose complement is a perfect residue system.

5. So the simplest normalized cyclic starter fails.
   This does not disprove cyclic constructions in general, because a working template could use a non-consecutive row-set `R`.
   It also says nothing decisive about non-cyclic solutions.

Self-check:
- The cyclic reduction is exact for that ansatz.
- The script tests the normalized ansatz exhaustively, not heuristically.
- The negative script output is correctly scoped: it rules out only one narrow cyclic normalization.

## lemma_graph
1. Every symbol support is a `6 x 6` complete bipartite block minus a perfect matching.
2. Every row and every column contains exactly `6` active symbols.
3. If two symbols share a row, then they share at most `2` columns.
4. If two symbols share a column, then they share at most `2` rows.
5. Hence any pair of symbols overlapping in both directions has overlap type only in `{(1,1), (1,2), (2,1), (2,2)}`.
6. Global counts force
   `sum x_{s,t} = sum y_{s,t} = 450`
   and
   `sum x_{s,t} y_{s,t} >= 180`.
7. A cyclic translate witness would reduce the whole problem to a single `6 x 6` difference-table starter.

## chosen_plan
Use the direct equi-square model first, because it stays faithful to the intended statement and immediately yields exact `6 x 6` support structure.
Push that structure through pair-overlap counting and support-overlap counting.
When those invariants stalled, test one tightly justified construction ansatz rather than jumping to a generic brute-force search.

Rigorous attempt:

- Exact support structure:
  each symbol `s` has `6` active rows and `6` active columns, and its support is `K_{6,6}` minus a matching.

- Exact overlap lemma:
  if `s,t` share a row `r`, then all common columns of `s,t` must lie among the two missing columns `pi_s(r), pi_t(r)`, so `y_{s,t} <= 2`.
  The column-wise dual gives `x_{s,t} <= 2` whenever `y_{s,t} > 0`.

- Exact global counts:
  `sum x_{s,t} = sum y_{s,t} = 450`,
  and the omitted-support count gives
  `sum x_{s,t} y_{s,t} >= 180`.

- Why this did not finish the problem:
  those constraints are strong enough to narrow the local geometry, but I do not yet see a contradiction from them alone.
  The remaining feasible overlap types are few, but the distributional slack is still nontrivial.

- Narrow construction test:
  for cyclic translates, the problem reduces to a residue-complete starter in one `6 x 6` difference table.
  The normalized consecutive-row case was checked exhaustively and failed.

Self-check:
- The proof attempt reaches a genuine partial theorem about symbol-pair overlaps.
- The script-backed cyclic failure is an auxiliary negative result, not the main claim.
- I do not have an exact proof or an exact counterexample for the full dossier statement.

## self_checks
- Statement fidelity check: all main lemmas are written directly in the original equi-square language.
- Structural check: the `6 x 6` minus matching reduction is the right normal form for a `5`-balanced equi-`30` symbol.
- Scope check: the cyclic computation only addresses a deliberately narrow ansatz and is labeled that way.
- Conservatism check: I am not promoting the result above `PARTIAL`.

## code_used
- Minimal code was used only after the handwritten structure and the cyclic-starter hypothesis were written down.
- Script: `artifacts/d5-balanced-equi-30-square/cyclic_normalized_search.py`
- Purpose: exhaustively test the normalized cyclic ansatz with row template `R = {0,1,2,3,4,5}`.
- Output on this run:
  - `no normalized cyclic starter found`
  - `support candidates checked 2280`

## result
- Provisional solve-stage verdict: `PARTIAL`
- Confidence: `medium-low`
- Strongest rigorous output from this solve pass:
  - every symbol must be a `6 x 6` support minus a perfect matching;
  - any two symbols that overlap in both rows and columns can do so only with overlap sizes at most `2` in each direction;
  - the global support-overlap count is at least `180`;
  - the simplest normalized cyclic construction does not exist.
- What remains open locally:
  - I do not have a contradiction for the full direct model;
  - I do not have a witness for existence.

## likely_failure_points
- The pair-overlap invariants may still be too coarse; a sharper argument probably needs a second-order constraint that couples several symbols or several rows at once.
- The cyclic search only excludes one normalized starter family, not all cyclic constructions and not the full problem.
- I did not use the Latin-subrectangle equivalence because the repo has already shown that this family is easy to over-strengthen in the wrong way.

## what_verify_should_check
- Audit the `6 x 6` minus matching reduction and the overlap lemma `x_{s,t} > 0 => y_{s,t} <= 2` and its dual.
- Re-run `artifacts/d5-balanced-equi-30-square/cyclic_normalized_search.py` and confirm the reported exhaustive negative result for `R = {0,1,2,3,4,5}`.
- Check whether the support-overlap lower bound
  `sum x_{s,t} y_{s,t} >= 180`
  can be sharpened enough to force a contradiction.
- If using the Latin-square equivalent in verify, be careful not to strengthen the source definition of `5 x 6` subrectangles beyond what the paper actually uses.

## verify_rediscovery
- PASS 1 used a bounded web audit focused on the exact instance and the canonical source, including searches for `5-balanced equi-30-square`, `balanced equi-n-squares 30 5`, `Latin square 30 5 x 6 subrectangles`, the paper title, the DOI `10.37236/9118`, and exact-instance open-status phrasing.
- I also checked the canonical 2020 paper itself for the `n = 30, d = 5` case and for nearby theorem / proposition / example / corollary style results that might already force this instance.
- Within the search budget, I found the canonical 2020 source leaving this case unresolved and did not find a later paper, citation trail, survey, or discussion page that clearly solves or directly implies the exact intended statement.
- Rediscovery is therefore not established within budget. This is only a bounded negative audit, not a proof of novelty.

## verify_faithfulness
- The solve-stage writeup stays faithful to the dossier statement.
- It works directly with the equi-square definition and explicitly avoids promoting the Latin-square subrectangle reformulation to a stronger grid-aligned condition.
- The claimed outputs are partial structural lemmas plus one negative result for a narrow cyclic ansatz.
- I found no wrong-theorem drift, quantifier drift, or silent strengthening of the target claim.

## verify_proof
- I found no incorrect step in the stated partial lemmas.
- The reduction from the symbol conditions to `|R_s| = |C_s| = 6` and then to `K_{6,6}` minus a perfect matching is correct: each active row and column has degree `5` inside a `6 x 6` bipartite support, so the complement is `1`-regular.
- The overlap lemma is correct. If symbols `s` and `t` share a row `r`, then any common column not equal to one of the two omitted columns would force both symbols into the same cell `(r,c)`, impossible. Hence `y_{s,t} <= 2`; the column-dual argument gives the corresponding bound on `x_{s,t}`.
- The row-pair and column-pair counting identities `sum x_{s,t} = sum y_{s,t} = 450` are correct because each row and each column contains exactly `6` active symbols.
- The support-overlap identity `sum x_{s,t} y_{s,t} = sum_{r,c} C(1 + m(r,c), 2) >= 180` is also correct as stated.
- The real gap is only that these valid constraints do not yet yield a contradiction or a construction for the full exact instance.

## verify_adversarial
- I reran `artifacts/d5-balanced-equi-30-square/cyclic_normalized_search.py`.
- Output reproduced exactly:
  - `no normalized cyclic starter found`
  - `support candidates checked 2280`
- The script matches the narrow claim it is used for. In the normalized cyclic ansatz with `R = {0,1,2,3,4,5}`, the kept difference multiset must contain each residue mod `30` exactly once, so deleting one entry from each row and each column must remove exactly one copy of each duplicated residue. The script checks precisely that.
- I did not find evidence that the script overclaims. Its conclusion remains properly scoped to one normalized cyclic family, not to all cyclic constructions and not to the full problem.

## verify_verdict
- `UNVERIFIED`
- Reason: the solve-stage mathematics contains correct partial structural results and a correctly scoped computational exclusion of one ansatz, but it does not prove or disprove the exact intended statement.
- Classification remains `PARTIAL`, not `CANDIDATE`, because there is no full exact argument yet.
- `lean_ready = false` because there is nothing exact to send to Lean, and PASS 1 did not establish rediscovery.

## minimal_repair_if_any
- No mathematical repair was needed.
- Conservative repair in classification only: keep the run below `CANDIDATE` and below Lean.
