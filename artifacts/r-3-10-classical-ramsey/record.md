# Solve Record: Determine the exact value of R(3,10)

## statement_lock
The live exact decision is:

Determine whether there exists a triangle-free graph `G` on `40` vertices with independence number `alpha(G) <= 9`.

This is equivalent to the Ramsey endpoint decision:

- if such a `40`-vertex graph exists, then `R(3,10) = 41`
- if no such `40`-vertex graph exists, then `R(3,10) = 40`

Packet correction:

Some packet lines describe the forcing side as proving that every triangle-free graph on `41` vertices has independence number at least `10`. That statement is already the known upper bound `R(3,10) <= 41`. The unresolved exact boundary is on `40` vertices.

Title theorem if solved:

`The Exact Value of R(3,10)`.

This still passes the 70-90% paper test if closed. A successful solve would already be about `0.84` of a short paper, with remaining work limited to certificate presentation, literature comparison, and compression of the final argument.

## definitions
Use the standard graph reformulation:

- a `(3,10;n)`-graph means a triangle-free graph on `n` vertices with independence number at most `9`
- the open case is whether a `(3,10;40)`-graph exists
- for `v in V(G)`, write `N(v)` for the open neighborhood and `N[v] = N(v) union {v}`
- write `H_v := G - N[v]`
- write `Z_v := {x in V(H_v) : x has no neighbor in N(v)}`

Conventions used below:

- because `G` is triangle-free, every `N(v)` is an independent set
- because `alpha(G) <= 9`, every independent set has size at most `9`
- smaller exact Ramsey values used as local forcing inputs:
  - `R(3,9) = 36`
  - `R(3,6) = 18`
  - `R(3,5) = 14`
  - `R(3,4) = 9`
  - `R(3,3) = 6`

## approach_A
Structural / invariant route:

Assume toward closure that `G` is a `(3,10;40)`-graph.

Step A1. Degree window.

Since `N(v)` is independent, `deg(v) <= 9` for every vertex `v`.

Also `H_v` is triangle-free, and any independent `9`-set in `H_v` together with `v` would give an independent `10`-set in `G`. Hence `alpha(H_v) <= 8`.

Because `R(3,9) = 36`, a triangle-free graph with independence number at most `8` has at most `35` vertices. Therefore

`|H_v| = 39 - deg(v) <= 35`,

so `deg(v) >= 4`.

Conclusion:

`4 <= delta(G) <= Delta(G) <= 9`.

Step A2. Chromatic consequence.

Since `alpha(G) <= 9`, every color class in a proper coloring has size at most `9`. Thus

`chi(G) >= ceil(40 / 9) = 5`.

So any `40`-vertex witness would be a triangle-free `5`-chromatic graph with degree window `[4,9]`.

Step A3. Closed-neighborhood complements are forced into the `(3,9)` strip.

For each vertex `v`, the graph `H_v` is triangle-free on `39 - deg(v)` vertices with `alpha(H_v) <= 8`. Thus:

| `deg(v)` | `|H_v|` | immediate status of `H_v` |
| --- | --- | --- |
| `4` | `35` | extremal `(3,9;35)` case |
| `5` | `34` | one step below extremal |
| `6` | `33` | two steps below extremal |
| `7` | `32` | three steps below extremal |
| `8` | `31` | four steps below extremal |
| `9` | `30` | five steps below extremal |

This is the main structural reduction: any proof that `R(3,10) = 40` can try to show that no `(3,9)`-near-extremal graph in this narrow range admits the required reattachment data.

Step A4. Anticomplete-to-neighborhood vertices are sharply limited.

The set `N(v)` is independent of size `d := deg(v)`. If `Z_v` contained an independent set of size `10 - d`, then that set together with `N(v)` would form an independent `10`-set in `G`. Hence

`alpha(Z_v) <= 9 - d`.

Applying smaller exact Ramsey values gives:

| `d` | bound on `|Z_v|` | vertices in `H_v` forced to touch `N(v)` |
| --- | --- | --- |
| `4` | `<= 17` | `>= 18` |
| `5` | `<= 13` | `>= 21` |
| `6` | `<= 8` | `>= 25` |
| `7` | `<= 5` | `>= 27` |
| `8` | `<= 1` | `>= 30` |
| `9` | `= 0` | `= 30` |

Interpretation:

- a degree-`4` vertex forces an extremal `(3,9;35)` residual graph and at least `18` residual vertices must attach back into `N(v)`
- a degree-`8` vertex leaves at most one residual vertex completely anticomplete to `N(v)`
- a degree-`9` vertex forces every residual vertex to meet `N(v)`

This is not enough to close the case by itself, but it compresses any eventual witness into a very rigid one-vertex extension problem.

Self-check for Approach A:

- the only nontrivial inputs are the standard graph reformulation and exact smaller Ramsey numbers already named above
- every deduction is monotone and does not assume hidden catalog data
- the off-by-one has been corrected explicitly, so all degree computations are now tied to the `40`-vertex boundary

## approach_B
Construction / extension / contradiction route:

Try to realize `R(3,10) = 41` by extending a known `39`-vertex lower-bound witness.

If a `(3,10;40)`-graph `G` exists and `x` is any vertex, then `G - x` is a triangle-free graph on `39` vertices with independence number at most `9`. So every `40`-vertex witness contains a `39`-vertex witness one deletion away.

Reversing that viewpoint:

Start from a `(3,10;39)`-graph `F` and ask whether one can add a new vertex `x` so that the resulting graph remains triangle-free and still has `alpha <= 9`.

The new neighborhood `N_F(x)` must satisfy two exact conditions:

- `N_F(x)` must be an independent set in `F`, otherwise a triangle through `x` appears
- `N_F(x)` must hit every independent `9`-set of `F`, otherwise a `9`-set disjoint from `N_F(x)` together with `x` gives an independent `10`-set

So the lower-bound side reduces to a finite extension problem:

Does some `(3,10;39)` witness admit an independent hitting set for all of its independent `9`-sets?

This reduction is conceptually clean and paper-relevant, but it stalls here because the local solve scope does not include an audited catalogue of the `39`-vertex witness family or the explicit Exoo construction data.

Self-check for Approach B:

- the extension reformulation is exact, not heuristic
- the blocking issue is not logical but informational: no local witness family was provided in the allowed packet
- without that family, the route cannot honestly progress beyond the reduction statement

## lemma_graph
Proposed proof skeleton for the upper-bound side `R(3,10) = 40`:

1. Assume a `(3,10;40)`-graph `G` exists.
2. Pick a vertex `v` of minimal or maximal degree.
3. Use `4 <= deg(v) <= 9` and `alpha(H_v) <= 8` to place `H_v` inside the `(3,9)` near-extremal window.
4. Use the `Z_v` bound to show that many residual vertices must attach to `N(v)`.
5. Translate the attachment pattern into a hitting-set constraint on independent subsets of `H_v`.
6. Try to show that no admissible `(3,9)` near-extremal graph admits such an attachment.
7. Conclude no `(3,10;40)`-graph exists.

Proposed proof skeleton for the lower-bound side `R(3,10) = 41`:

1. Start from an explicit `(3,10;39)` witness.
2. Search for an independent neighborhood hitting all independent `9`-sets.
3. Verify the extension gives a `(3,10;40)`-graph.
4. Use the known upper bound `R(3,10) <= 41` to conclude exactness.

## chosen_plan
I chose the structural upper-bound lane.

Reason:

- it is the packet's recommended first attack
- it produces theorem-shaped reductions even without computation
- it keeps the micro-paper objective in view by targeting the exact endpoint, not a weaker side-goal

Concrete target of the attempt:

prove that a hypothetical `(3,10;40)`-graph cannot survive the degree-window plus reattachment constraints.

## self_checks
Major-step self-checks:

1. Statement lock check.
The live decision is on `40` vertices. This is now aligned with the known interval `40 <= R(3,10) <= 41`.

2. Structural reduction check.
The degree bounds and `H_v` reduction are rigorous and depend only on `R(3,9) = 36`.

3. Extension reduction check.
The lower-bound side is exactly an independent-hitting-set extension problem over `39`-vertex witnesses.

4. Closure check.
No contradiction was derived from the local information alone. I do not have an honest proof of either `R(3,10) = 40` or `R(3,10) = 41`.

## code_used
No code was used.

Reason:

- the problem is not marked `search_heavy`
- two reasoning routes were developed first, as required
- no theorem-driven bounded experiment was available inside the local packet without importing witness catalogues or upper-bound computation artifacts

## result
Best honest outcome of this solve pass:

partial structural reduction, not a closure.

What was established cleanly:

- any `40`-vertex witness would satisfy `4 <= delta(G) <= Delta(G) <= 9`
- any `40`-vertex witness would satisfy `chi(G) >= 5`
- for every vertex `v`, the residual graph `H_v = G - N[v]` lies in the tight `(3,9)` near-extremal window
- for every vertex `v`, the set of residual vertices anticomplete to `N(v)` is sharply bounded by smaller Ramsey numbers
- the lower-bound side can be reformulated as an exact one-vertex extension problem over `39`-vertex witnesses

What did not close:

- I did not derive an impossibility theorem for the `40`-vertex witness
- I did not produce a `40`-vertex construction

If the main claim closes later, the smallest immediate supporting structure already visible is:

- one proposition recording the degree window and residual-graph reduction
- one proposition recording the independent-hitting-set extension formulation

One natural boundary remark falls out immediately:

the final obstruction, if `R(3,10) = 40`, is unlikely to be broad extremal graph theory; it is likely a sharply finite incompatibility inside the narrow band of `(3,9)` near-extremal residual graphs.

## family_affinity
This candidate remains strongly anchored to the classical off-diagonal family `R(3,k)`.

The nearest solved benchmark is `R(3,9) = 36`, and the current reduction shows that the unresolved `R(3,10)` endpoint is literally controlled by one-vertex interaction with `(3,9)` near-extremal graphs. That is good family leverage: the proof language is not ad hoc, even though the endpoint is still instance-specific.

## generalization_signal
Moderate.

What scales:

- the closed-neighborhood complement trick `H_v = G - N[v]`
- the degree upper bound `deg(v) <= alpha(G)`
- the use of smaller exact `R(3,t)` values to control the anticomplete-to-neighborhood set `Z_v`
- the extension viewpoint reducing `R(3,k)` witnesses to independent hitting sets on `R(3,k)-2` or `R(3,k)-1` boundary graphs

What does not obviously scale:

- the exact numerical rigidity here comes from the one-step gap `40` versus `41`
- any actual contradiction will probably depend on the special catalogue of `(3,9)` near-extremals, not just on family-level inequalities

## proof_template_reuse
Reusable template:

1. lock the exact unresolved order `n`
2. assume a triangle-free graph on `n` vertices with `alpha <= k-1`
3. pass to `H_v = G - N[v]`
4. force `alpha(H_v) <= k-2`
5. use exact `R(3,k-1)` to bound degrees
6. define `Z_v` anticomplete to `N(v)` and use exact `R(3,k-d(v))` values to bound `|Z_v|`
7. reduce closure to a one-vertex extension or non-extension problem over near-extremal `(3,k-1)` graphs

This is a real proof template for nearby one-step off-diagonal gaps, but by itself it is not a publication result.

## candidate_theorem_slice
Smallest theorem-shaped slice currently visible:

`Proposition. If G is a triangle-free graph on 40 vertices with alpha(G) <= 9, then 4 <= delta(G) <= Delta(G) <= 9 and chi(G) >= 5. Moreover, for every vertex v of degree d, the graph H_v = G - N[v] is triangle-free on 39 - d vertices with alpha(H_v) <= 8, and the set Z_v of vertices in H_v anticomplete to N(v) has size at most 17, 13, 8, 5, 1, 0 for d = 4, 5, 6, 7, 8, 9 respectively.`

This is theorem-shaped and correct, but still too thin to be a micro-paper on its own.

## smallest_param_shift_to_test
Best next parameter shifts:

1. stay at the same parameter and import explicit `(3,10;39)` witness data, since the unresolved step is genuinely one-vertex local
2. within the same parameter, isolate whether degree `4` or degree `5` can occur in a hypothetical `(3,10;40)` witness; those are the most leverage-heavy residual cases because they force `H_v` nearest to the extremal `(3,9;35)` boundary

I do not recommend drifting to a different Ramsey pair at solve time. The live value is already narrow enough that the right next shift is structural, not thematic.

## why_this_is_or_is_not_publishable
This is not yet publishable.

Why not:

- there is no exact determination of `R(3,10)`
- there is no new counterexample
- the current record contains only a clean reduction and some necessary conditions

If the main claim closed, it would already be roughly 70-90 percent of a short paper:

- exact title theorem: `The Exact Value of R(3,10)`
- minimal remaining packaging work: present the final witness or forcing certificate, compare against Exoo and Angeltveit, and compress the residual-case handling into a short note
- one immediate corollary or remark: the smallest currently exposed one-step off-diagonal classical Ramsey gap would be closed

Current honesty check:

the present package is still too thin for the micro-paper lane. It is useful solver scaffolding, not a publication packet.

## paper_shape_support
What extra structure would make the result paper-shaped if the main claim closes:

- one audited finite extension lemma showing how `(3,9)` near-extremal residual graphs can or cannot reattach to a degree-`d` neighborhood
- either an explicit `40`-vertex witness certificate or an exhaustive exclusion of all admissible reattachments
- a compact proposition turning the computation or finite check into a theorem-facing obstruction statement

If exact closure is achieved, the paper almost writes itself:

- theorem
- proof/certificate section
- comparison with the previous interval `40 <= R(3,10) <= 41`
- short concluding remark on the `R(3,k)` frontier

## boundary_remark
Boundary remark:

The reduction strongly suggests that this problem sits exactly at the edge where broad inequalities stop and finite residual structure begins. The eventual argument is likely to be neither a soft asymptotic bound nor a huge search from scratch, but a narrow one-vertex extension obstruction over `(3,9)` near-extremal graphs.

## likely_failure_points
Most likely blockers from here:

- the residual `(3,9)` family may still be too large without imported catalogue data
- low-degree cases `d = 4, 5` may require case splits that are small but still computational
- a successful lower-bound construction may depend on a highly tuned explicit witness rather than a reusable structural idea
- the current packet does not include the concrete artifacts behind the known upper bound or lower-bound witness

## what_verify_should_check
Verification should check:

- the off-by-one correction in the statement lock
- the exact smaller Ramsey values used in the `Z_v` table
- whether the candidate theorem slice is already implicit in known `e(3,k,n)` literature and should be treated as routine rather than novel
- whether local repository artifacts exist for the Exoo lower-bound witness or the Angeltveit upper-bound computation that can be pulled into the next solve pass
- whether degree `4` and degree `5` cases have already been ruled out in existing upper-bound computations
