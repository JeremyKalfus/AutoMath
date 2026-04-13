# Solve Record: 1-11-Representability of Graphs on 9 Vertices

## statement_lock
- Active slug: `all-9-vertex-graphs-1-11-representable`
- Active title: `Are all graphs on 9 vertices 1-11-representable?`
- Exact intended statement for this run: determine whether every graph on 9 vertices is 1-11-representable, or else exhibit a 9-vertex counterexample with a rigorous certificate.
- Exact title theorem if the full solve closes: `Every graph on 9 vertices is 1-11-representable.` Equivalently, the note title remains `1-11-Representability of Graphs on 9 Vertices`.
- The dossier's publication logic is credible: a full settlement of the 9-vertex slice would already be about 70-90% of a paper; the curated estimate is `single_solve_to_paper_fraction = 0.76`.
- This run does not have enough local structural detail to claim the full slice. The best honest target is therefore a theorem-facing reduction that provably shrinks the residue.

## definitions
- I use the dossier definition: for distinct letters `x,y`, the induced two-letter subword `W|_{x,y}` determines adjacency. If `W|_{x,y}` has at most one occurrence of consecutive equal letters (`xx` or `yy`), then `xy` is an edge; if it has at least two such occurrences, then `xy` is a non-edge.
- A graph is `1-11-representable` if some word `W` over its vertex set witnesses all pairs in that sense.
- The 2025 source result, taken as input from the packet, is: every graph on at most 8 vertices is 1-11-representable.
- Convention for this record: `G + z` means adjoining a new isolated vertex `z` to a graph `G`.
- Missing local detail: the full 2024-2025 reinsertion toolbox is not present in the repository materials I read, so any claim here must be derivable directly from the definition above.

## approach_A
Structural / invariant route: try to force a minimal 9-vertex counterexample into a narrower residue by deleting one vertex and reinserting it into an 8-vertex representation.

The cleanest test case is an isolated vertex. If `G` is 1-11-representable with witness word `W`, define

`W' := zz W zz`

for a new letter `z`.

Then:
- for any old pair `x,y` from `V(G)`, deleting `z` from `W'` gives exactly `W|_{x,y}`, so all old adjacencies are preserved;
- for any old vertex `x`, the two-letter subword `W'|_{z,x}` begins with `zz` and ends with `zz`, so it contains at least two consecutive-equal occurrences regardless of how many `x`'s appear in between.

Hence `z` is nonadjacent to every old vertex, so `W'` represents `G + z`.

This proves an exact reduction:

**Lemma A.** If `G` is 1-11-representable, then `G + z` is 1-11-representable for every new isolated vertex `z`.

Combining Lemma A with the known up-to-8-vertex theorem gives:

**Corollary A1.** Every graph on 9 vertices that has an isolated vertex is 1-11-representable.

This is a genuine slice reduction. Any 9-vertex counterexample must therefore have minimum degree at least `1`.

Self-check after Approach A: the construction is definition-level and does not use any unimported toolbox lemma. The only load-bearing point is that `zz` at the front and back survive in every `z/x` projection, which they do.

## approach_B
Construction / extremal / contradiction route: assume a 9-vertex obstruction exists and try to make it sparse or disconnected enough that the 8-vertex theorem plus a simple gluing argument rules it out.

Two natural variants were tested conceptually:
- disconnected obstruction route: if disjoint-union closure were easy, one could reduce componentwise to 8-vertex pieces and glue the words;
- low-degree reinsertion route: if universal, pendant, or twin vertices admitted equally direct insertion formulas, one could push a minimal obstruction into a narrow high-minimum-degree residue.

With the local materials available here, neither route can be made rigorous yet:
- I do not have a definition-level proof that arbitrary disjoint unions preserve 1-11-representability;
- I do not currently have a correct insertion formula for universal or pendant vertices that can be checked pairwise without importing the omitted 2024-2025 toolbox.

So Approach B identifies the right obstruction profile, but does not close it:
- a minimal 9-vertex obstruction cannot have an isolated vertex;
- beyond that, the residue is still too broad to classify honestly from the current local information.

Self-check after Approach B: this is a controlled failure, not a silent fallback. I am recording the exact place where the argument stops rather than implying a nonexistent general reinsertion lemma.

## lemma_graph
1. Input theorem from the dossier: every graph on at most 8 vertices is 1-11-representable.
2. Lemma A: adjoining an isolated vertex preserves 1-11-representability via `W' = zz W zz`.
3. Corollary A1: every 9-vertex graph with an isolated vertex is 1-11-representable.
4. Consequence for obstruction search: any 9-vertex counterexample must satisfy `delta(G) >= 1`.
5. Remaining frontier: isolate-free 9-vertex graphs, especially the non-word-representable residue singled out by the packet.

Self-check after lemma graph: each edge in the graph is justified either by the packet's 8-vertex theorem input or by the explicit word construction above.

## chosen_plan
Choose the positive reduction path that can be proved exactly from the dossier definition, rather than overreaching toward a full 9-vertex classification without the needed local toolbox.

The best honest output of this solve attempt is:
- an exact theorem slice;
- a minimal-counterexample restriction;
- a precise statement of what extra structure would make the full result paper-shaped.

What extra structure would make the main result paper-shaped if the full claim closes?
- a residue description reducing the 9-vertex census to a small list of isolate-free non-word-representable classes;
- either explicit representing words for each residue class or one certified obstruction;
- a tiny checker only after the residue list is fixed.

Minimal remaining packaging work if the full 9-vertex theorem later closes:
- a short literature frame around the up-to-8-vertex theorem;
- a compact reduction table for the surviving 9-vertex classes;
- one immediate corollary or frontier remark.

Self-check after plan selection: this stays in the micro-paper lane because the slice theorem materially shortens the residue, but I am not claiming that the current package alone is paper-ready.

## self_checks
- Statement lock check: the intended statement remains the full 9-vertex slice, not a drift to a different family.
- Definition check: every proof step uses only the local two-letter-subword definition and the packet's stated 8-vertex theorem.
- Conservatism check: no use of `EXACT`, no claim of full classification, no claim about rediscovery.
- Publication check: the current theorem slice is real but still too thin by itself for the micro-paper lane; the full note remains the 9-vertex classification, not merely the isolated-vertex subcase.

## code_used
- No code used.
- Reason: the dossier permits code only after reasoning justifies it. At this point the missing ingredient is not a small witness search; it is a structural residue description or a local reinsertion lemma beyond isolated vertices.
- A brute-force search now would violate the packet's warning about drifting into an unreadable census before the structural reductions are in hand.

## result
Strongest proved statement from this run:

**Theorem slice.** Every graph on 9 vertices with an isolated vertex is 1-11-representable.

**Proof.** Let `H` be a graph on 9 vertices with an isolated vertex `z`. Then `H - z` has 8 vertices, so by the packet's source theorem it is 1-11-representable; let `W` be a representing word for `H - z`. Form `W' = zz W zz`. For every pair `x,y` in `V(H-z)`, the projection `W'|_{x,y}` equals `W|_{x,y}`, so the old adjacencies are unchanged. For every `x` in `V(H-z)`, the projection `W'|_{z,x}` starts with `zz` and ends with `zz`, hence contains at least two occurrences of consecutive equal letters. Therefore `z` is nonadjacent to every old vertex. So `W'` is a 1-11 representation of `H`. `qed`

Immediate boundary consequence:
- any 9-vertex counterexample must be isolate-free;
- in particular, a minimal 9-vertex counterexample must satisfy `delta(G) >= 1`.

What part of the argument scales:
- the isolated-vertex insertion works in every order, not just order `9`;
- repeated application shows that adjoining any number of isolated vertices preserves 1-11-representability.

What part does not scale:
- this argument says nothing about reinserting a vertex with positive degree;
- it does not classify disconnected graphs in general, because component-gluing was not proved here.

What theorem slice is suggested:
- `If all isolate-free 9-vertex graphs are 1-11-representable, then all 9-vertex graphs are 1-11-representable.`
- More concretely: the 9-vertex frontier may be reduced to isolate-free residue classes before any search.

What one or two next parameter shifts would help most:
- universal-vertex insertion: if this also admits a short formula, the frontier would shrink to graphs with `1 <= delta(G) <= Delta(G) <= 7`;
- pendant-vertex insertion: even a restricted leaf-extension lemma could compress the residue substantially.

Whether the current package is still just an instance or already closer to a paper-shaped claim:
- closer to a paper-shaped claim than a raw example, because it identifies a clean theorem slice and an obstruction constraint;
- still too thin on its own for the micro-paper lane, because it does not yet settle the isolate-free residue.

## family_affinity
- High family affinity: the argument is not an ad hoc witness for one graph. It isolates a hereditary-looking reduction principle inside the 1-11-representability program.
- It fits the family's likely proof grammar: delete one vertex to land in the known `<= 8` regime, then reinsert by a word surgery.
- That is exactly the kind of move that could support a finite-slice classification note once enough low-complexity reinsertions are available.

## generalization_signal
- Positive signal: the isolated-vertex surgery is order-independent and extends immediately to any number of isolated vertices.
- Moderate signal: the proof suggests that other low-complexity vertex types may admit similarly explicit surgeries, but this has not been proved here.
- Current generalization ceiling: no justified claim beyond isolated vertices.

## proof_template_reuse
- Reusable template: start from a known representing word on `n-1` vertices, then add a short controlled wrapper whose two-letter projections force the desired adjacency pattern for the new vertex while leaving old projections untouched.
- For isolated vertices, the wrapper is `zz` on both ends.
- The open reuse question is whether analogous wrappers exist for universal, pendant, or twin vertices without importing heavier structure.

## candidate_theorem_slice
- Candidate theorem slice: `Every graph on 9 vertices with an isolated vertex is 1-11-representable; equivalently, any 9-vertex counterexample must have minimum degree at least 1.`
- This is the cleanest exact slice currently supported by the local solve.

## smallest_param_shift_to_test
- First shift: prove or refute a universal-vertex insertion lemma.
- Second shift: prove or refute a pendant-vertex insertion lemma.
- These two shifts would most efficiently decide whether the remaining 9-vertex frontier collapses to a compact high-core residue.

## why_this_is_or_is_not_publishable
- By itself, this is not yet publishable in the repository's micro-paper lane.
- Reason: the result is theorem-shaped and correct, but it is only a supporting slice, not the title theorem promised by the dossier.
- If the full 9-vertex slice later closes, the current theorem becomes a short reduction lemma inside a paper that would already be roughly `70-90%` written once the main classification is secured.
- Right now the package is still too thin: it reduces the search space, but does not settle the finite frontier.

## paper_shape_support
- Exact title theorem if the full program closes: `Every graph on 9 vertices is 1-11-representable.`
- Current supporting theorem: the isolated-vertex slice above.
- One immediate corollary / remark already available: any first 9-vertex obstruction must be isolate-free.
- Minimal packaging work after a future full closure would be light: a short reduction section, a compact residue table, and one frontier remark.

## boundary_remark
- The present solve moves the boundary from `all 9-vertex graphs` to `isolate-free 9-vertex graphs`.
- That is a real simplification, but not yet the decisive finite census promised by the working packet.
- A counterexample, if it exists, cannot be sparse in the weakest possible way.

## likely_failure_points
- The main failure point is missing local access to the 2024-2025 reinsertion toolbox; without it I cannot honestly shrink the residue beyond isolated vertices.
- A second failure point is definitional: disjoint-union closure is tempting but not proved from the limited local data, so I avoided using it.
- If later work turns into full search before the residue is structurally reduced, the result risks becoming a machine dump rather than a micro-paper.

## what_verify_should_check
- Check the exact definition of `1-11` against the source wording to confirm that counting the leading `zz` and trailing `zz` in `W'|_{z,x}` is legitimate exactly as used here.
- Check whether the 2024-2025 toolbox already contains stronger insertion lemmas for isolated, universal, pendant, or twin vertices; if so, absorb them into the next solve pass.
- Check whether the positive 8-vertex theorem in the source is stated in the exact generality used here.
- If stronger insertion lemmas exist, update the residue description before any bounded computational step.

## verify_rediscovery
- PASS 1 used a bounded web check against the canonical 2025 paper, the 2024 toolbox paper, and direct 9-vertex-status searches.
- The exact intended statement for this dossier remains the full 9-vertex slice: settle whether every graph on 9 vertices is 1-11-representable, or produce a 9-vertex obstruction. Within the bounded search budget, I found no later paper or preprint settling that exact statement.
- However, the actual theorem slice claimed in the solve record is not frontier-novel. The canonical 2025 paper explicitly includes Lemma 2.3(a): if `G_1` and `G_2` are 1-11-representable, then their disjoint union is 1-11-representable. Combining that with Theorem 3.5 from the same paper (all graphs on at most 8 vertices are 1-11-representable) immediately implies that every 9-vertex graph with an isolated vertex is 1-11-representable.
- Therefore: no rediscovery found for the exact intended 9-vertex classification, but the solver's delivered slice is already implied by prior art.

## verify_faithfulness
- The solve artifact is not faithful to the intended statement. The intended statement is the full 9-vertex classification; the solve record proves only the isolated-vertex subcase.
- This is theorem drift, not a full settlement. The best faithful label for the run result is `VARIANT`, not `CANDIDATE` for the intended statement and certainly not `EXACT`.
- The record itself is internally clear about the downgrade, but the verified mathematical output is a nearby supporting slice rather than the title theorem promised by the dossier.

## verify_proof
- First incorrect step found: none in the explicit `W' = zz W zz` argument.
- The proof is mathematically correct under the canonical definition quoted in the 2025 source: for each old vertex `x`, the projection `W'|_{z,x}` contains two distinct consecutive-equality events, one from the leading `zz` and one from the trailing `zz`, so `zx` is forced to be a non-edge.
- Old adjacencies are preserved because deleting `z` from `W'` recovers `W`.
- The real issue is not correctness but novelty and scope: the proof establishes only a known corollary of published closure machinery.

## verify_adversarial
- No code, checker, or witness-search artifact exists in this directory, so there was nothing computational to rerun.
- I adversarially checked the only load-bearing construction by testing the projection logic: for any vertex `x` appearing in `W`, the subword `W'|_{z,x}` has the form `zz ... zz`, so the two `zz` events survive regardless of how often `x` occurs. This does not break the claim.
- I also checked the stronger challenge: could the argument be unnecessary because the source already contains a direct closure theorem? Yes. Lemma 2.3(a) subsumes the isolated-vertex slice via disjoint union with a one-vertex graph, so the new proof is redundant even though correct.

## verify_theorem_worthiness
- Exactness: the proved slice is exact as stated, but it is not the dossier's intended exact statement.
- Novelty: for the slice actually proved, novelty is absent; it is already implied by published prior art.
- Reproducibility: high for the slice, since the proof is short and definition-level.
- Lean readiness: no. Formalizing a known supporting corollary does not seal the real publication packet.
- Paper leverage: negligible for the frontier objective, because the verified output does not shorten the open isolate-free residue in a novel way.
- Would this result, if correct and Lean-sealed, already constitute most of a publishable note? No.
- What percentage of the paper would one solve already provide? About `0.05` for the present verified slice, because the slice is known and the actual 9-vertex frontier remains untouched.
- What title theorem is actually visible? `Every graph on 9 vertices with an isolated vertex is 1-11-representable.`
- What part of the argument scales? The wrapper proof scales to adjoining isolated vertices in any order, and the source already has the more general disjoint-union closure.
- What part clearly does not? Nothing here advances the isolate-free 9-vertex residue, which is the genuinely frontier-relevant part.
- Best honest publication status: `REDISCOVERY` for the current output packet, even though the intended 9-vertex classification itself still appears open.

## verify_verdict
- `VARIANT`
- Rationale: the solver proved a nearby but different statement from the intended one, and that nearby statement is already implied by the canonical source.

## minimal_repair_if_any
- Minimal conservative repair: keep the isolated-vertex argument only as a checked corollary, explicitly cite canonical Lemma 2.3(a) and Theorem 3.5, and remove any implication that this slice is new progress toward a publishable frontier claim.
- Next action should return to the real open target: use the published toolbox to compress the isolate-free 9-vertex residue before any bounded search.

## publication_prior_art_audit
- Audit date: `2026-04-13`.
- Exact-statement search: bounded web queries for `1-11-representable` plus `9 vertices` found the canonical 2025 article and mirrors, but no later paper or preprint settling whether every 9-vertex graph is 1-11-representable and no 9-vertex obstruction announcement.
- Alternate-notation search: bounded queries using `11-representable`, `1-11-representation`, and `graphs on 9 vertices` produced the same literature surface rather than a separate follow-up line.
- Canonical-source check: the 2025 paper states Theorem 3.5, `All graphs on at most 8 vertices are 1-11-representable`, and in its concluding remarks explicitly says that better techniques could help establish the 9-vertex case `if they are indeed 1-11-representable`, which confirms that the 9-vertex slice was still open there.
- Canonical-source implication check: Lemma 2.3(a) in the same 2025 paper states that disjoint unions of 1-11-representable graphs are 1-11-representable. Combined with Theorem 3.5 and the one-vertex graph, this already implies the packet's isolated-vertex slice.
- Outside-status check: a bounded outside search on `2025-2026` surfaces found repository mirrors of the canonical paper, but no independent later source reporting a 9-vertex classification or a first obstruction theorem.
- Prior-art verdict: the intended full 9-vertex statement still appears open on this bounded audit, but the strongest local proved slice is already implied by published prior art, so the current packet is a `REDISCOVERY`.

## publication_statement_faithfulness
- The dossier's intended statement is the full 9-vertex classification or first 9-vertex obstruction.
- The current packet proves only the isolated-vertex slice.
- That slice is mathematically correct, but it is not faithful to the intended title theorem and does not itself close the advertised finite frontier.
- Best honest role for the current proof: a known supporting corollary inside a future note, not the main theorem of the note.

## publication_theorem_worthiness
- Is the strongest honest claim stronger than `here is an example`? Yes. It is a theorem-shaped structural statement, not a single worked instance.
- Is there a real theorem slice here? Yes: every 9-vertex graph with an isolated vertex is 1-11-representable.
- Is the proof structural or merely instance-specific? Structural. The argument uses a general closure move, not hand-picked small cases.
- Would this survive a referee asking `what is the theorem`? The theorem statement is clear, but the referee would immediately ask for novelty, and the packet fails there because the slice is already implied by the canonical source.
- Theorem-worthiness verdict: theorem-shaped but not standalone-worthy for publication, because it does not contribute new frontier content.

## publication_publishability
- Would this result, if correct and Lean-sealed, already constitute most of a publishable note? No.
- What percentage of the paper would one solve already provide? About `0.05` for the current packet. The publishable content would still be almost entirely missing because the isolate-free 9-vertex residue remains untouched.
- Is there a real title theorem, theorem slice, or counterexample theorem here? Only a known supporting theorem slice.
- Is the claim still too dependent on hand-picked small cases? The proof itself is not hand-picked, but the packet is still too dependent on the published up-to-8-vertex frontier and gives no new control of the actual 9-vertex residue.
- If this is not yet paper-ready, is the remaining gap genuinely small or did the candidate only look attractive before audit? The candidate as a full target still looks attractive, but the current packet only looked attractive before audit. From the current packet to a paper, the remaining gap is still large.
- If this is not yet paper-ready, should it be moved aside rather than expanded into a larger theorem program? Yes. The current packet should be moved aside rather than inflated into a broader program around a known slice.

## publication_packet_audit
- Packet coherence: good as an internal proof note.
- Packet novelty: absent for the strongest proved claim.
- Publication packet quality: weak, because the packet does not contain a new title theorem, new theorem slice, or new obstruction certificate.
- Would Lean directly seal the packet? No. Lean would only formalize a known corollary rather than seal a publication-ready frontier result.
- Proof artifacts preserved: yes. The reasoning artifact is preserved in this record even though there is no checker or witness table yet.

## micro_paper_audit
- Micro-paper lane verdict for the current packet: fail.
- The full unresolved 9-vertex classification remains a good micro-paper target in principle, but this particular packet is not close to a micro-paper because its strongest honest claim is already known.
- The packet has no honest standalone title theorem with independent referee value.
- Lean would be archival polish for a known corollary, not the decisive seal on a publishable one-shot result.

## strongest_honest_claim
- As of `2026-04-13`, the strongest honest claim preserved in this artifact is: every graph on 9 vertices with an isolated vertex is 1-11-representable.
- However, this claim is already implied by canonical Lemma 2.3(a) together with Theorem 3.5, so it does not constitute new publication-facing progress on the 9-vertex frontier.

## paper_title_hint
- No honest standalone paper title is available for the current packet.
- At most, the packet supports an internal label such as `Known isolated-vertex reduction for the 9-vertex 1-11 frontier`, which is not publication-facing.

## next_action
- Do not promote the current packet to Lean or publication.
- Resume solve only if the next pass directly attacks the isolate-free 9-vertex residue using the published 2024-2025 toolbox or a tightly bounded residue census.
- Otherwise cool this attempt and avoid expanding a known supporting slice into a larger theorem program.
