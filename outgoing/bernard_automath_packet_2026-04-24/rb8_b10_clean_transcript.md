# Clean transcript: AutoMath run for `R(B8, B10)`

Prepared: 2026-04-24

## Target selected

AutoMath selected the one-gap book Ramsey problem:

`37 <= R(B8, B10) <= 38`

The target was to prove either:

- every graph on 37 vertices contains `B8` or its complement contains `B10`, giving `R(B8,B10) = 37`; or
- there is a 37-vertex graph avoiding `B8` whose complement avoids `B10`, giving `R(B8,B10) = 38`.

## Where the bound `38` came from

The upper bound was not produced by a search. It came from the general book Ramsey upper bound recorded in Radziszowski's dynamic survey DS1.17, Section 5.3(g):

If `2(m+n)+1 > (n-m)^2/3`, then

`R(B_m,B_n) <= 2(m+n+1)`.

For `(m,n) = (8,10)`, the hypothesis is:

`2(8+10)+1 = 37 > 4/3 = (10-8)^2/3`.

So the bound is:

`R(B8,B10) <= 2(8+10+1) = 38`.

The lower bound `37 <= R(B8,B10)` comes from Theorem 1 of Lidicky-McKinley-Pfender-Van Overberghe (2025): for `4 <= n <= 21`, `4n-3 <= R(B_{n-2},B_n)`. Taking `n = 10` gives `37 <= R(B8,B10)`.

## Solve-stage proof spine

AutoMath's solve stage used no code. The proof attempt was purely structural.

Assume a 37-vertex obstruction `G` exists: no `B8` in `G` and no `B10` in the complement.

Let `d(x)` be degrees in `G`, let `e` be the number of edges, and let `T` and `Tbar` be the triangle counts in `G` and its complement.

The book-avoidance conditions imply:

- every edge of `G` has at most 7 common neighbors, so `3T <= 7e`;
- every edge of the complement has at most 9 common neighbors, so `3Tbar <= 9 ebar`.

Goodman's identity then gives the exact inequality:

`sum_x (106 d(x) - 3 d(x)^2) >= 34632`.

The integer quadratic `106d - 3d^2` is maximized only at `d = 18`, where it equals `936`. Since `37 * 936 = 34632`, equality is forced everywhere. Therefore any obstruction must be 18-regular.

The equality conditions also force exact pair counts:

- every edge has exactly 7 common neighbors;
- every nonedge has exactly 10 common neighbors.

So any obstruction would have to be a strongly regular graph:

`srg(37,18,7,10)`.

For such a graph, the adjacency matrix `A` satisfies:

`A^2 = -3A + 8I + 10J`.

On the subspace orthogonal to the all-ones vector, eigenvalues satisfy:

`x^2 + 3x - 8 = 0`.

The two roots are irrational conjugates, so over an integer matrix they must occur with equal multiplicity. Since the orthogonal subspace has dimension 36, each would occur 18 times. Their trace contribution would be:

`18((-3 + sqrt(41))/2 + (-3 - sqrt(41))/2) = -54`.

But an 18-regular graph has adjacency trace 0 and the all-ones eigenvalue contributes 18, so the remaining eigenvalues must sum to `-18`, not `-54`. Contradiction.

Thus no 37-vertex obstruction exists, and the candidate conclusion is:

`R(B8,B10) = 37`.

## Verification status

The verify stage rechecked the arithmetic, equality propagation, and spectral obstruction. It recorded:

- `verify_verdict = VERIFIED`
- `classification = CANDIDATE`
- no code was used in the solve stage
- bounded prior-art checking did not establish rediscovery

## Publication status

The current corrected status is:

- `publication_status = PAPER_READY`
- `proof_artifacts_preserved = true`
- `lean_complete = false`

This means the theorem packet is publication-significant and ready for human mathematical scrutiny/write-up, but it is not formally sealed in Lean.

## Lean status

The Lean file `lean/RB8B10BookRamsey.lean` contains the intended obstruction statement and checked supporting pieces:

- the target `not IsSRGWith 37 18 7 10`;
- the specialized strongly regular matrix identity;
- zero trace of adjacency matrices;
- the final arithmetic contradiction once the spectral factor-count equations are available.

The missing Lean ingredient is the spectral/minpoly bridge from the SRG matrix identity to the factor-count equations. Therefore this is not counted in `lean_complete.json`.

## Raw logs

The full stdout logs for solve, verify, and Lean total 12,920 lines. I included the short stage-summary files rather than the full logs because they are much easier to read. The full raw logs can be provided if needed.

