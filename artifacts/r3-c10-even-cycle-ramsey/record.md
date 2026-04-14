# Solve Record: The Exact Value of R(C10, C10, C10)

## statement_lock
We work on the active paper candidate `r3-c10-even-cycle-ramsey`.

The exact intended statement for this solve pass is:

- either prove that every 3-coloring of `K20` contains a monochromatic `C10`, which would give `R(C10, C10, C10) = 20`;
- or construct a 3-coloring of `K20` with no monochromatic `C10`, which would imply `R(C10, C10, C10) >= 21`.

The clean title theorem if the upper-bound path closes is:

- `The Exact Value of R(C10, C10, C10)`.

Publication framing:

- if the upper bound `R(C10, C10, C10) = 20` closes, this is already about `80%` of a short paper, consistent with the packet's `single_solve_to_paper_fraction = 0.82`;
- if only a `20`-vertex counterexample is found, that is mathematically real and still important, but it is not the same exact-value note and would need a sharper extremal narrative before it feels equally paper-shaped.

## definitions
Let the three monochromatic graphs of a 3-coloring of `K20` be `G_red`, `G_blue`, and `G_green`, all on the same vertex set.

Conventions used in this solve note:

- a monochromatic `C10` means a simple cycle on exactly `10` vertices inside one color class;
- a `pure four-block blow-up` means a partition of the vertex set into four parts, with every cross-part edge assigned a single reduced color depending only on the pair of parts, and with no reliance on internal-part structure to create or destroy the cycle;
- a `translation-invariant distance coloring` on `Zn` means the color of `{x,y}` depends only on the cyclic distance `|x-y| mod n`, with the usual symmetry `d` and `n-d` identified.

Ambiguities and limits for this run:

- the packet does not specify the exact known `19`-vertex extremal construction, so I do not assume a precise reduced template beyond the general "even-cycle blow-up" guidance;
- no external literature was consulted in solve, so any theorem quoted from memory would be unsafe unless derivable here;
- Lean is intentionally off in this pass.

## approach_A
Structural / invariant route:

Start from a hypothetical counterexample on `20` vertices and try to force a monochromatic `C10` from coarse local structure.

Safe forcing observations:

- any monochromatic `K_{5,5}` already contains a monochromatic `C10`;
- more generally, if a reduced monochromatic block pattern lets one cycle through `10` distinct vertices while alternating across fully monochromatic cross-part pairs, then the full coloring already contains a monochromatic `C10`.

This makes the following upper-bound strategy plausible:

- identify the standard `19`-vertex lower-bound lane;
- prove that any extension to `20` vertices necessarily creates one of the coarse monochromatic lifts above;
- then upgrade that lift to a forced monochromatic `C10`.

Why this stalls in the current packet-only setting:

- the obvious density route is too weak without an exact small-`n` extremal bound for `C10`;
- I do not have the exact `19`-vertex construction in hand, so I cannot write a genuine stability proof around it;
- neighborhood arguments around a single vertex do not immediately force a `10`-cycle without a stronger local cycle theorem than I can justify internally here.

Self-check after Approach A:

- this is a credible proof lane for `R(C10, C10, C10) = 20`;
- I do not currently have enough packet-local structure to make it rigorous end to end.

## approach_B
Construction / extremal route:

Interrogate the most obvious counterexample families first, because the packet explicitly points to extremal blow-up patterns.

Two sharply bounded template families were tested:

- fully translation-invariant distance colorings on `K19` and `K20`;
- pure four-block reduced-color blow-ups on block sizes `5+5+5+5` and `5+5+5+4`.

Why these are the right first experiments:

- they are the smallest exact slices that directly test whether the coarsest known lower-bound heuristics can survive at `20`;
- they are bounded enough to enumerate exactly without turning solve into a generic search campaign;
- a failure of these template lanes is theorem-facing information, not just random computational noise.

Self-check after Approach B setup:

- these families do not cover all 3-colorings of `K20`;
- any positive result from them must be reported only as a restricted-family slice.

## lemma_graph
The proof skeleton suggested by this run is:

1. In any candidate lower-bound construction, a monochromatic `K_{5,5}` is already fatal because it contains a monochromatic `C10`.
2. Therefore coarse block constructions must avoid reduced monochromatic patterns that lift to `10`-vertex cycles using only cross-block edges.
3. Exact bounded enumeration shows that pure four-block reduced constructions on `5+5+5+5` and even the nearby `5+5+5+4` case already fail.
4. Exact bounded enumeration also shows that full cyclic distance-uniform constructions do not survive on `20`, and in fact not even on `19`.
5. Hence any genuine counterexample, if it exists, must be finer than both of those coarse lanes.

## chosen_plan
Approach A did not close with packet-local information, so I chose the narrower construction-elimination route.

The best use of the solve budget was:

- kill the coarsest extremal-template lanes exactly;
- preserve that as a candidate theorem slice;
- avoid overclaiming a general upper bound from evidence that only speaks to specific families.

## self_checks
Major-step checks:

- Statement lock check: the run stayed on the exact intended statement `R(C10, C10, C10)`.
- Scope check: only the active selection packet, `AGENTS.md`, the working packet, and the local artifact state were read.
- Code check: no SAT, ILP, CP-SAT, or broad brute-force search over arbitrary colorings was used.
- Claim check: every computational statement below is explicitly restricted to the tested families.
- Publication check: I do not treat the current slice as a finished micro-paper result.

## code_used
Yes, but only as a bounded checker.

Exact bounded experiments run:

- translation-invariant distance-colorings on `K19` and `K20`;
- pure four-block reduced-color blow-ups on block sizes `5+5+5+5` and `5+5+5+4`.

Method:

- a short in-shell Python checker built the corresponding monochromatic graphs;
- it then searched exactly for a simple monochromatic `10`-cycle;
- no repository code files were added for the checker, because the computation was small and one-off.

What the code was for:

- not to search the whole problem;
- only to eliminate the most obvious symmetric counterexample lanes after the reasoning stage had isolated them.

## result
Main claim status:

- I did not prove `R(C10, C10, C10) = 20`.
- I did not construct a `20`-vertex counterexample.

Strongest honest output from this run:

- every pure four-block reduced 3-coloring lifted to block sizes `5+5+5+5` already contains a monochromatic `C10` using only cross-block edges;
- the same is true for the nearby `19`-vertex pure four-block lift with block sizes `5+5+5+4`;
- every fully translation-invariant distance-coloring of `K20` contains a monochromatic `C10`;
- in fact, that cyclic-distance family does not even realize a `19`-vertex counterexample, so it is too narrow to model the known lower bound.

Best interpretation:

- the coarsest symmetric lower-bound lanes fail;
- if a `20`-vertex counterexample exists, it must use finer internal structure than a pure four-block blow-up and must also break full cyclic distance symmetry;
- if the upper bound `20` is true, these eliminations are the start of a stability narrative, but not yet the whole proof.

What part of the argument scales:

- reduced-template elimination by exact bounded checking;
- the idea of killing coarse extremal lanes before attempting a full forcing theorem.

What part does not scale yet:

- the global passage from "all obvious templates fail" to "every 3-coloring of `K20` has a monochromatic `C10`";
- any claim that the real `19`-vertex construction must lie in one of the tested families.

The suggested theorem slice is:

- every pure four-block reduced-color blow-up on block sizes `5+5+5+5` contains a monochromatic `C10`, and likewise for `5+5+5+4`.

One immediate corollary / remark:

- any future `20`-vertex counterexample must already be more irregular than the standard coarse four-block template.

Current package assessment:

- still an instance-support slice, not a paper-shaped solve;
- closer to a theorem packet than a random failed attempt, but not yet the micro-paper itself.

## family_affinity
High.

Reason:

- the slice attacks the exact extremal-template lane that the packet flags as the first obstruction for the open diagonal even-cycle problem;
- it is not a detached side observation.

## generalization_signal
Moderate.

Reason:

- the same reduced-template elimination idea can be reused for nearby small even-cycle diagonal residues;
- however, the exact computations here are still strongly tied to the `C10` target and the `20` / `19` vertex thresholds.

## proof_template_reuse
Reusable proof template:

- isolate the most natural extremal construction families from the literature packet;
- prove they all fail by exact bounded checking or a short reduced-graph argument;
- then feed that failure back into a narrower structural proof attempt.

This template is reusable, but only as support. It does not replace the genuine forcing argument for the full Ramsey claim.

## candidate_theorem_slice
Candidate exact slice from this solve run:

- `Every pure four-block blow-up of a 3-edge-colored K4 with part sizes (5,5,5,5) contains a monochromatic C10. The same conclusion holds for part sizes (5,5,5,4).`

This is the cleanest exact statement produced here.

## smallest_param_shift_to_test
Most valuable next parameter shifts:

- five-block reduced templates on `4+4+4+4+4`;
- four-block templates with nontrivial internal-part colorings rather than pure blow-ups.

These are the smallest natural enlargements of the coarse obstruction lane.

## why_this_is_or_is_not_publishable
This is not yet publishable as a micro-paper packet.

Why not:

- the main exact theorem is still open in the artifact;
- the current slice is supportive rather than title-level;
- on its own, it is closer to `25%` to `35%` of a paper than to the desired `70%` to `90%`.

What would make it publishable:

- either the full upper-bound proof `R(C10, C10, C10) = 20`;
- or a `20`-vertex counterexample plus a convincing extremal explanation showing why `20` fails and what structure replaces the folklore target.

Minimal remaining packaging work if the upper bound closes:

- integrate the forcing proof;
- keep the four-block elimination as a short obstruction/stability section;
- add one comparison paragraph to `R(C8, C8, C8) = 16` and the large-`n` even-cycle theorem.

## paper_shape_support
What extra structure would make the result paper-shaped if the main claim closes?

- one clean title-theorem proof or exact disproof;
- one short structural proposition explaining why the obvious extremal templates fail;
- one boundary remark locating the result between the solved `C8` case and the large-even-cycle regime.

If `R(C10, C10, C10) = 20` is proved, then this run already contributes a useful support lemma: the coarsest four-block obstruction lane is impossible.

## boundary_remark
Boundary remark:

- this run kills coarse cyclic and pure four-block counterexample templates, but it does not rule out finer nonuniform constructions;
- therefore the current evidence leans toward an upper bound of `20`, but it is not yet a proof.

## likely_failure_points
Most likely reasons this solve did not close:

- the true `19`-vertex lower-bound construction may use a finer pattern than the packet summary suggests;
- a valid upper-bound proof probably needs a more precise stability theorem around the actual extremal construction;
- the bounded computation on pure templates is exact inside those families, but the families themselves are still only a slice of the full problem.

## what_verify_should_check
Verification should check:

- independently rerun the bounded computations for the cyclic-distance family and the pure four-block blow-up families;
- determine whether the known `19`-vertex lower-bound construction lies outside both eliminated families;
- check whether the candidate theorem slice above is already implicit in prior work on small even-cycle Ramsey constructions;
- decide whether the next serious solve move is a five-block reduced search or a direct structural proof around the actual `19`-vertex template.
