# statement_lock

- Active slug: `cocktail-party-two-monochromatic-diameter-2-cover`
- Active title: `Does every 2-colored cocktail party graph admit a cover by two monochromatic diameter-2 subsets?`
- Working convention for this solve attempt:
  Let the cocktail party graph have partner pairs `(x_i, x_i')` deleted from the complete graph.
  A subset `S` is monochromatic diameter-2 in color `c` if every two vertices of `S` have distance at most `2` inside the induced color-`c` subgraph on `S`.
- Intended target for this solve attempt:
  In every red-blue coloring of the cocktail party graph, there exist two monochromatic diameter-2 subsets whose union is the full vertex set.
- Stronger convention used when convenient:
  a monochromatic star `N_c[v] ∪ {v}` is already diameter `1`, hence a valid diameter-2 set.

# definitions

- Ambiguity 1:
  `cover by two monochromatic diameter-2 subsets` does not explicitly force the two subsets to use different colors. I treat the target as allowing either color on each subset; any proof for one red and one blue set would be stronger.
- Ambiguity 2:
  `cover` should mean union equals the whole vertex set, not necessarily a partition.
- Fixed notation:
  choose a deleted matching edge `{p,q}`. For every other vertex `v`, record the pair
  `(col(pv), col(qv)) ∈ {RR, RB, BR, BB}`.
  Let `X_RR, X_RB, X_BR, X_BB` denote the corresponding classes.
- Immediate observation:
  `R_p := {p} ∪ X_RR ∪ X_RB` is a red star centered at `p`, `R_q := {q} ∪ X_RR ∪ X_BR` is a red star centered at `q`,
  `B_p := {p} ∪ X_BB ∪ X_BR` is a blue star centered at `p`, and `B_q := {q} ∪ X_BB ∪ X_RB` is a blue star centered at `q`.

# approach_A

- Structural / invariant route:
  lock a partner pair `{p,q}` and analyze only the four local color-pattern classes around it.
- Exact local cover identities:
  `R_p ∪ R_q = V \ X_BB`,
  `B_p ∪ B_q = V \ X_RR`,
  `R_p ∪ B_q = V \ X_BR`,
  `B_p ∪ R_q = V \ X_RB`.
- Consequence:
  if any one of the four classes is empty for some partner pair `{p,q}`, then the whole graph is covered by two monochromatic stars, hence by two monochromatic diameter-2 subsets.
- This gives a rigorous theorem slice:
  any counterexample must satisfy that for every deleted matching pair `{p,q}`, all four classes `X_RR, X_RB, X_BR, X_BB` are nonempty.
- Self-check:
  the four union identities were checked directly from the class definitions; each is exact and uses only existing graph edges from the chosen center.
- Why this matters:
  it converts the global problem into a critical-pair obstruction problem. A minimal counterexample cannot have any locally missing pattern around any deleted edge.

# approach_B

- Construction / extremal / contradiction route:
  assume a minimal counterexample and pick a partner pair `{p,q}`.
  By the slice from Approach A, every local class is nonempty.
- The unresolved hope:
  choose the orientation of the two cover colors so that one mixed class is the only uncovered residue, then absorb that residue by using edges between `X_RB` and `X_BR` or by adjoining one of the centers to a larger diameter-2 set.
- Critical mixed-pair heuristic:
  if `x ∈ X_BR` and `y ∈ X_RB`, then
  `xq` and `yp` are red while `xp` and `yq` are blue.
  The color of `xy` should control whether `x` can be absorbed into a red set containing `p` or whether `y` can be absorbed into a blue set containing `q`.
- Obstruction picture:
  if every such attempted absorption fails, the reduced pattern starts to resemble a rigid alternating configuration, plausibly a blow-up-of-`C_5` type critical graph.
- Current blocker:
  I do not yet have a clean internal-diameter argument that turns the mixed-class edge information into a full cover, because a star-union cover only gives one-step control while diameter `2` needs common internal witnesses for all leftover pairs.
- Self-check:
  this route is mathematically plausible but not yet rigorous; it identifies the right obstruction mechanism but does not close it.

# lemma_graph

- Lemma 1:
  For a fixed deleted pair `{p,q}`, each of `R_p, R_q, B_p, B_q` is a monochromatic star, hence a valid diameter-2 subset.
- Lemma 2:
  The four exact union identities above hold.
- Corollary 3:
  If any one of `X_RR, X_RB, X_BR, X_BB` is empty, then the conjecture holds for that coloring.
- Corollary 4:
  Any minimal counterexample must have at least six vertices, and in fact every deleted pair must see all four classes.
- Lemma 5 candidate:
  If a deleted pair has a sufficiently small residual class, then that residue can be absorbed and the conjecture still holds.
- Lemma 5 status:
  not proved. The singleton-residue case looks like the right next target.

# chosen_plan

- Best current path:
  push Approach A as far as it goes, record the exact star-cover slice rigorously, then use one bounded exact experiment on the smallest nontrivial size to test whether the unresolved obstruction already disappears on six vertices.
- Reason for choosing it:
  this stays close to the intended publication object, gives a real theorem slice even without closing the conjecture, and keeps code bounded to a checker/search only after two reasoning attempts.
- Self-check:
  this respects the solve-stage rule: reasoning first, code only after structural and extremal routes were both attempted.

# self_checks

- Statement check:
  I am targeting the exact cocktail-party conjecture, not the broader `f(2,2)=3` program.
- Scope check:
  no web use and no campaign drift.
- Proof check:
  the only fully rigorous positive statement so far is the star-cover slice from Approach A.
- Risk check:
  the mixed-class absorption step is the real gap between the relaxed 2-reachable theorem and internal diameter `2`.
- Experiment check:
  any computational claim below is exact only for the six-vertex case; it is not evidence of a general proof by itself.

# code_used

- One bounded exact experiment was used after the two reasoning approaches stalled:
  exhaustive enumeration of all `2^12 = 4096` red-blue colorings of the six-vertex cocktail-party graph.
- Checker semantics:
  for a chosen subset `S` and color `c`, every pair of vertices in `S` must either be joined by a color-`c` edge or have a common color-`c` neighbor inside `S`.
- Exact computational outcome:
  every one of the `4096` colorings admits a cover by two monochromatic diameter-2 subsets when the two subsets are allowed to use arbitrary monochromatic colors.
- Stronger interpretation test:
  if one insists that the two covering sets must be one red and one blue, there are `20` six-vertex colorings with no such red-blue cover.
- Additional exact note:
  those `20` exceptional colorings do not have the whole six-vertex graph as a single red diameter-2 set or a single blue diameter-2 set, so the flexibility really comes from allowing two sets of the same color.

# result

- Strong rigorous progress:
  proved a clean local slice. If some deleted matching pair misses even one of the four local color-pattern classes, then two monochromatic stars already cover the graph.
- Therefore any genuine counterexample must be locally saturated:
  every deleted pair must realize all four patterns `RR, RB, BR, BB`.
- Exact small-case progress:
  exhaustive computation settles the six-vertex case positively under the ordinary reading that the two covering subsets need only be monochromatic, not forced to have different colors.
- Interpretation warning:
  the stronger red-plus-blue-only formulation is already false on six vertices by exact search, so the conjecture must be read with care when compared against the 2026 wording.
- General conjecture status:
  unresolved in this solve attempt so far.
- Self-check:
  this is a real obstruction lemma plus a complete smallest-case computation, but still not the main theorem.

# family_affinity

- Moderate.
- The local-pattern method is specific to cocktail-party graphs because it uses the deleted perfect matching as a distinguished nonedge system.
- The style may extend to other `alpha = 2` host graphs only when there is an equally rigid nonedge structure.

# generalization_signal

- The promising scalable signal is:
  convert global two-cover existence into local forbidden pattern statements around a deleted pair.
- The current exact scalable claim is only the empty-class slice.
- The six-vertex computation suggests:
  the first true obstruction, if it exists, must start at at least eight vertices under the ordinary two-monochromatic-subsets reading.
- The next scalable target would be:
  prove that a locally saturated deleted pair still forces a cover unless the mixed classes form a very specific critical reduced graph.

# proof_template_reuse

- Reusable template:
  fix a canonical nonedge, partition by color signatures to its endpoints, and express candidate monochromatic cover sets as unions of signature classes.
- This template should also be useful for:
  sharp obstruction theorems and minimal-counterexample classification in other rigid two-colored host graphs with a canonical pairing structure.

# candidate_theorem_slice

- Slice proved in this attempt:
  In a red-blue coloring of a cocktail party graph, if there exists a deleted matching pair `{p,q}` such that one of the four signature classes `X_RR, X_RB, X_BR, X_BB` is empty, then the vertex set is covered by two monochromatic diameter-2 subsets, in fact by two monochromatic stars.
- Exact computational slice established:
  the six-vertex cocktail-party graph satisfies the full conjecture for every coloring under the ordinary two-monochromatic-subsets reading.
- Stronger slice still open:
  prove the singleton-residual strengthening or give a structural classification of locally saturated eight-vertex colorings.

# smallest_param_shift_to_test

- Smallest exact next test:
  extract a human-readable classification of the locally saturated six-vertex colorings and then move to the `n = 4` locally saturated case.
- Smallest structural shift:
  prove or refute the singleton-residual strengthening of the star-cover lemma:
  if some deleted pair has a signature class of size at most `1`, does the conjecture already follow?

# why_this_is_or_is_not_publishable

- Not publishable yet.
- What is publishable already if solved:
  a full proof or explicit counterexample family would already be 70-90% of a short paper, because the 2026 relaxation paper already supplies the motivation and near-neighbor theorem.
- Exact paper claim if solved:
  every red-blue coloring of the cocktail party graph admits a cover by two monochromatic diameter-2 subsets, or else a minimal counterexample family exists and is described explicitly.
- Minimal remaining packaging after a successful solve:
  clean statement, comparison with the 2026 2-reachable theorem, one verification/checker appendix, and short discussion of the obstruction mechanism.
- Why the current packet is not yet paper-shaped:
  the empty-class slice is useful but too weak on its own; it does not yet bridge the relaxed theorem to the frontier claim.
- Minimal package currently visible:
  a note could emerge if the empty-class lemma, the singleton-residual lemma, and the locally saturated classification close together, but that closure is not in hand yet.

# likely_failure_points

- Main technical gap:
  converting external witness availability into internal witness availability inside one of the two chosen cover sets.
- Mixed-class risk:
  `X_RB` and `X_BR` may interact in a way that defeats naive absorption into star-based covers.
- Counterexample risk:
  a locally saturated reduced configuration may persist for all deleted pairs and genuinely block two internal diameter-2 sets.
- Interpretation risk:
  if the literature silently means one red set plus one blue set, then the six-vertex exact computation shows that stronger formulation already fails.
- Proof-writing risk:
  even if the conjecture is true, a proof that repeatedly swaps centers may become case-heavy unless the critical-pair structure is compressed into a clean lemma.

# what_verify_should_check

- Verify the four union identities exactly.
- Verify the theorem slice:
  empty signature class around one deleted pair implies a two-star cover.
- If code is used next, independently confirm the checker’s interpretation of `diameter-2 subset`, especially for deleted partner pairs inside a chosen subset.
- Verify the six-vertex exhaustive claim against all `4096` colorings.
- Verify the interpretation point explicitly against the source wording:
  does the conjecture require two arbitrary monochromatic subsets, or specifically one red and one blue subset?

# verify_rediscovery

- Limited PASS 1 checked the canonical 2026 source and a bounded later-status search for any diameter-2 resolution of the cocktail-party conjecture.
- The canonical source still states the exact diameter-2 claim as `Conjecture 2` and proves only the relaxed `2`-reachable statement as `Theorem 1`.
- Within the allowed search budget, I found no later paper or note clearly resolving the exact diameter-2 conjecture.
- Rediscovery verdict: not established.

# verify_faithfulness

- The intended statement in `selected_problem.md` matches the source statement: cover `V(G^c)` by two monochromatic diameter-2 subsets in colors `i,j ∈ [2]`.
- The solver's reading that the two covering sets may use the same color is faithful to the source wording; the source does not require `i ≠ j`.
- Therefore the stronger "one red set and one blue set" reading is a different theorem, not the selected theorem.
- The strongest verified mathematical output is not the intended conjecture itself. It is a nearby obstruction lemma plus an exact six-vertex computation. By the harness rules, this is a `VARIANT`, not the target theorem.

# verify_proof

- No incorrect step was found in the proof of the empty-signature-class slice. The four union identities are exact from the class definitions, and each covering set is a monochromatic star, hence a valid diameter-2 subset.
- The first non-rigorous step appears in `approach_B`: the hoped absorption of the residual mixed class from cross-edge information is heuristic and does not yield a proof of the full conjecture.
- So the proof is correct only for the variant slice already isolated in the record, not for the intended full conjecture.

# verify_adversarial

- I independently recomputed the six-vertex case by exhaustive search over all `2^12 = 4096` red-blue colorings of the cocktail-party graph on six vertices, using the internal-diameter definition in `G[X]`.
- The recomputation confirmed that every coloring has a cover by two monochromatic diameter-2 subsets under the faithful source reading that the two colors may coincide.
- The recomputation also confirmed that exactly `20` colorings fail the different-colors-only variant, so the record's interpretation warning is real and not cosmetic.
- No contradiction was found to the stated six-vertex computation or to the empty-class slice.

# verify_theorem_worthiness

- The verified output is a real structural slice: if some deleted pair misses one of `RR, RB, BR, BB`, then two monochromatic stars cover the graph.
- That slice has honest theorem content and the six-vertex exact check gives a minimal-case anchor, but the locally saturated case remains the main frontier gap.
- For this packet, the best honest publication status is still `SLICE_CANDIDATE`, not a near-complete paper claim. The current material is not yet 70-90% of a paper resolving the selected conjecture.
- The smallest next stress test is the singleton-residual strengthening or a locally saturated eight-vertex obstruction analysis. That is the shortest route to learning whether the variant slice scales toward the intended theorem.
- Lean is not the bottleneck. The remaining work is mathematical closure of the locally saturated case, not formal sealing of the current slice.

# verify_verdict

- `verify_verdict = "VARIANT"`
- `classification = "VARIANT"`
- `publication_status = "SLICE_CANDIDATE"`
- strongest honest claim:
  if some deleted matching pair has an empty signature class, then the graph is covered by two monochromatic diameter-2 subsets; additionally, the six-vertex cocktail-party graph satisfies the full conjecture under the faithful same-or-different-color reading.

# minimal_repair_if_any

- No repair was needed for the verified slice itself.
- The conservative repair is interpretive: future stages should not silently strengthen the source statement into the different-colors-only variant.

# publication_prior_art_audit

- Bounded web pass used only the exact statement search, alternate notation search, the canonical 2026 source, and one outside-status sweep.
- Canonical source check:
  Gyarfas-Sarkozy, `2-Reachable Subsets in Two-Colored Graphs`, published online `2026-03-25`, still states the cocktail-party diameter-`2` claim as `Conjecture 2` and proves only the relaxed `2`-reachable result as `Theorem 1`.
- Canonical-source internal slice check:
  the source already contains nearby partial statements such as a star-cover observation for a critical nonedge, but no theorem / proposition / corollary / example / observation in that paper settles the full internal-diameter-`2` cocktail-party conjecture.
- Exact-statement and alternate-notation searches did not surface a later paper, note, or preprint explicitly resolving the selected conjecture under the faithful same-or-different-color reading.
- One outside-source status pass found only adjacent broader-diameter discussion, not a diameter-`2` cocktail-party closure.
- Rediscovery verdict for the selected theorem remains:
  not established.

# publication_statement_faithfulness

- The selected theorem is still:
  every red-blue coloring of the cocktail-party graph admits a cover by two monochromatic diameter-`2` subsets.
- The source wording allows the two covering subsets to use the same color; it does not require one red set and one blue set.
- The current packet is faithful to that wording.
- The stronger different-colors-only formulation is already false on six vertices by exact search, so publication-facing writing must not drift into that stronger statement.
- Strongest honest claim relative to the intended theorem:
  the packet does not prove the intended conjecture, but it does prove a genuine theorem slice strictly stronger than "here is an example."

# publication_theorem_worthiness

- The strongest honest claim is stronger than "here is an example":
  yes. The empty-signature-class implication is a quantified structural theorem slice over all cocktail-party graphs, and the six-vertex computation is only a supporting exact anchor.
- There is a real theorem slice here:
  if some deleted matching pair has one empty signature class among `RR, RB, BR, BB`, then two monochromatic stars already cover the graph.
- The proof is structural, not merely instance-specific:
  the four exact union identities give a uniform argument; only the `n = 6` confirmation is instance-specific.
- Would this survive a referee asking "what is the theorem?":
  as a slice, yes; as a standalone paper packet for the selected conjecture, not yet.
- The claim is still too dependent on hand-picked small cases to support the full selected paper candidate:
  yes. Beyond the exact slice, the packet still relies on the six-vertex case rather than a general locally saturated theorem.
- Conservative theorem-worthiness verdict:
  `SLICE_EXACT` for the exact empty-signature-class slice, but not a theorem-sized closure of the selected conjecture.

# publication_publishability

- If the selected `paper_candidate` were solved, would that already be `70-90%` of a paper?
  yes. The 2026 paper already fixes the motivation, nearby relaxed theorem, and comparison frame.
- Is there a real parameterized theorem, theorem slice, or counterexample theorem here now?
  yes, but only at the slice level.
- Is the remaining gap genuinely small, or did the candidate only look attractive before audit?
  the candidate still looks attractive, but the remaining gap is mathematically central rather than editorial. The unresolved locally saturated case is the main theorem gap, not final polish.
- Would Lean directly seal the packet?
  no. Lean would only archive the existing slice; it would not bridge the unsolved locally saturated argument.
- Publication verdict:
  not `PAPER_READY`. The packet is mathematically real and publication-adjacent, but it is not yet a referee-facing theorem-resolution note.

# publication_packet_audit

- strongest honest closed packet:
  exact empty-signature-class theorem slice plus exact `n = 6` verification of the full conjecture under the faithful reading.
- publication packet quality:
  promising but unsealed.
- paper-candidate verdict:
  still worth keeping active because a full solve would remain close to publication, but the current artifact is not yet the promised one-shot conjecture-resolution packet.
- proof artifacts preserved:
  yes. The local slice proof and bounded exact computation are recorded in the canonical artifact.
- lean seal verdict:
  keep Lean off for now; the shortest next path is still combinatorial closure of the locally saturated case.

# strongest_honest_claim

- In every red-blue coloring of a cocktail-party graph, if some deleted matching pair has an empty signature class among `RR, RB, BR, BB`, then the vertex set is covered by two monochromatic diameter-`2` subsets, in fact by two monochromatic stars. In addition, the full selected conjecture holds for the six-vertex cocktail-party graph by exhaustive exact check under the faithful source reading that the two covering colors may coincide.

# paper_title_hint

- Empty signature classes and the six-vertex case for two monochromatic diameter-`2` covers in cocktail-party graphs

# next_action

- Target the singleton-residual strengthening first:
  prove that a deleted pair with a signature class of size at most `1` already forces a two-set diameter-`2` cover.
- If that stalls, classify locally saturated colorings on the eight-vertex cocktail-party graph before attempting any broader family rhetoric.
- Keep the current exact slice as the fallback publication core, but do not market it as a resolution of the selected conjecture.
