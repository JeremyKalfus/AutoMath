# Family Record: zero_divisor_prime_labelings

## family_statement_lock

- Active family slug: `zero_divisor_prime_labelings`.
- Active dossier: `campaigns/zero_divisor_prime_labelings.md`.
- Family artifact path: `artifacts/families/zero_divisor_prime_labelings`.
- Locked family statements for this generalize pass:
  - `F25(p) := Γ(Z_p × Z_25)` for odd prime `p`, with support classes
    `A = {(0,u) : 5 ∤ u}`,
    `B = {(0,5t) : t in {1,2,3,4}}`,
    `C = {(a,0) : a in Z_p^×}`,
    `D = {(a,5t) : a in Z_p^×, t in {1,2,3,4}}`,
    of sizes `20, 4, p - 1, 4(p - 1)`.
  - `F2(p) := Γ(Z_p × Z_p × Z_2)` for odd prime `p`, with support classes
    `A = (*,0,0)`,
    `B = (0,*,0)`,
    `C = (0,0,1)`,
    `D = (*,*,0)`,
    `E = (*,0,1)`,
    `F = (0,*,1)`,
    of sizes `p - 1, p - 1, 1, (p - 1)^2, p - 1, p - 1`.
- Locked theorem target:
  - prove the actual ring-to-support bridge lemmas for `F25(p)` and `F2(p)`;
  - then package the checked abstract support reductions as the main theorem slice;
  - preserve the paired verified `p = 13` arithmetic checkpoints as corollaries/examples, not as a full odd-prime closure claim.
- Bounded-read set used in this pass:
  - `campaigns/zero_divisor_prime_labelings.md`;
  - `artifacts/families/zero_divisor_prime_labelings/record.md`;
  - `artifacts/families/zero_divisor_prime_labelings/status.json`;
  - `PROOFS.md`;
  - `artifacts/z5-z25-prime-zero-divisor-graph/record.md`;
  - `artifacts/z13-z25-prime-zero-divisor-graph/record.md`;
  - `artifacts/z5-z5-z2-prime-zero-divisor-graph/record.md`;
  - `artifacts/z11-z11-z2-prime-zero-divisor-graph/record.md`;
  - `artifacts/z13-z13-z2-prime-zero-divisor-graph/record.md`.

## existing_instance_inventory

- Lean-backed exact seeds preserved in `PROOFS.md`:
  - `F25(3)`, `F25(5)`, `F25(7)`;
  - `F2(5)`, `F2(7)`.
- Verified feeder state preserved in the dossier/current family state:
  - `F25(11)` and `F25(13)` on the four-class line;
  - `F2(11)` and `F2(13)` on the six-class line.
- Opened four-class seeds:
  - `F25(5)` already realizes the stable template:
    `C` is a large-prime block,
    `B` is a four-label pairwise-coprime barrier,
    `A` absorbs the small forbidden spill,
    and `D` takes the clean complement.
  - `F25(13)` keeps the same support graph but forces the first honest arithmetic repair:
    the old upper-half-prime-only `C` rule fails because `[43,84]` contains only `10` primes for `12` `C` slots;
    the repaired witness uses the sub-half primes `37` and `41`,
    sends their doubles `74` and `82` to `D`,
    and keeps the sparse barrier `B = {1,19,23,29}` with spill labels `38,46,57,58,69,76` parked in `A`.
- Opened six-class seeds:
  - `F2(5)` already shows the hinge move `C = 1`, after which only `A-B`, `A-F`, and `B-E` remain arithmetic.
  - `F2(11)` shows the naive `{2,3}`-smooth reservoir survives with one spare label:
    there are `21` nontrivial `{2,3}`-smooth labels up to `141` for the required `20` slots in `A ∪ E`.
  - `F2(13)` closes the first zero-slack boundary:
    there are exactly `24` nontrivial `{2,3}`-smooth labels up to `193`, exactly matching `|A ∪ E| = 24`,
    and the complement block for `B ∪ F` still fits cleanly.
- Inventory conclusion:
  - both active family lines have stable support decompositions and a repeated classwise proof template;
  - the strongest new arithmetic information is paired and asymmetric:
    `F25(13)` proves the old `C` subtemplate is too rigid but the graph still survives after a small-spill repair,
    while `F2(13)` proves the naive six-class template survives exactly at zero slack;
  - the next smallest discriminating feeder is `F25(17)`.

## shared_structure

- Common decomposition / invariant:
  - in both families, adjacency depends only on coordinate support, so the full zero-divisor graph is a blowup of a tiny support graph;
  - vertices inside one support class have identical neighborhoods, so any bijection within a class preserves every adjacency obligation.
- Common decomposition / construction:
  1. classify every nonzero zero-divisor by support type;
  2. prove the exact class-pair adjacency table from the ring law;
  3. invoke the classwise support-template lemma on the resulting support graph;
  4. solve only the remaining class-interface coprimality problem.
- Four-class support graph for `F25(p)`:
  - exact edge families are `A-C`, `B-B`, `B-C`, `B-D`;
  - `B` is the unique clique class;
  - `C` only constrains `A ∪ B`;
  - `D` only constrains `B`.
- Six-class support graph for `F2(p)`:
  - exact edge families are `A-B`, `A-C`, `A-F`, `B-C`, `B-E`, `C-D`;
  - `C` is the unique hinge vertex;
  - once `C = 1`, the edges touching `C` are automatic and the whole `D` class becomes free;
  - only `A-B`, `A-F`, and `B-E` remain parameter-sensitive.
- Shared proof template extracted from the opened seeds:
  - the structural part scales because it is support-theoretic, not instance-specific;
  - the arithmetic part is a tiny interval-partition problem once the support graph is fixed.

## parameter_sensitive_steps

- Steps that genuinely scale in the parameters:
  - the support partitions themselves once the ring-to-support bridge lemmas are formalized;
  - the classwise-template reduction from the full graph to the support graph;
  - for `F25(p)`, the reduction to one clique condition on `B` plus interface conditions `C` against `A ∪ B` and `B` against `D`;
  - for `F2(p)`, the hinge reduction `C = 1` and the three-interface packing problem.
- Parameter-sensitive arithmetic burdens:
  - choose `p - 1` labels for `C` in `F25(p)` while keeping every nontrivial multiple of a `C` prime out of `A ∪ B`;
  - choose a four-label sparse barrier set on `B` whose forbidden multiples fit inside the fixed `20` `A` slots;
  - count enough labels for `A ∪ E` in `F2(p)` supported on a fixed small prime set;
  - choose `B ∪ F` as a complement block avoiding that prime support.
- Steps that remain instance-specific in the current evidence:
  - the precise sub-half repair `37,41` in `F25(13)`;
  - the exact barrier choice `B = {1,19,23,29}` in the verified `p = 13` four-class witness;
  - the finite smooth-reservoir splits used in `F2(11)` and `F2(13)`;
  - the exact displayed label lists in every feeder witness.
- Smallest proven obstruction already on disk:
  - the unchanged upper-half-prime-only `C` subtemplate for `F25(p)` fails first at `p = 13`.
- Smallest likely unresolved obstruction:
  - `F25(17)` for the refined small-spill `C` program;
  - this is the first post-`13` case that can distinguish a real four-class corollary from a local repair.

## candidate_theorem_slices

- Slice A: paired ring-to-support bridge theorems.
  - For odd prime `p`, formalize the actual support partitions and adjacency tables for `F25(p)` and `F2(p)`, then instantiate the checked abstract reductions `zp_z25_support_template_reduction` and `zp_zp_z2_support_template_reduction_of_singleton_one`.
- Slice B: four-class sufficient-condition corollary.
  - For odd prime `p`, if `{1,...,5p+19}` admits a partition into `L_A,L_B,L_C,L_D` of sizes `20,4,p-1,4(p-1)` with `L_B` pairwise coprime, `L_C` cross-coprime to `L_A ∪ L_B`, and `L_D` cross-coprime to `L_B`, then `F25(p)` is prime.
  - The honest `p = 13` refinement is that `L_C` may include a bounded number of below-half primes provided their nontrivial multiples land in `L_D`.
- Slice C: six-class sufficient-condition corollary.
  - For odd prime `p`, after fixing `L_C = {1}`, it is enough to choose `2(p - 1)` labels for `L_A ∪ L_E` supported on a small prime set `S` and `2(p - 1)` labels for `L_B ∪ L_F` coprime to every prime in `S`.
- Slice D: obstruction slice.
  - The old four-class upper-half-prime-only `C` template fails at `p = 13` even though the graph `F25(13)` itself remains prime after refinement.

## chosen_slice

- Strongest honest slice for this pass:
  - Slice A, the paired ring-to-support bridge slice.
- Proposed theorem slice:
  - for odd prime `p`, the family graphs `Γ(Z_p × Z_25)` and `Γ(Z_p × Z_p × Z_2)` reduce from ring-level zero-product claims to explicit support-graph coprimality allocation problems;
  - on the six-class line, the true arithmetic core after the bridge is only the three interfaces `A-B`, `A-F`, and `B-E`;
  - on the four-class line, the honest arithmetic corollary must allow the refined small-spill `C` block already forced by `p = 13`.
- Why this is the strongest honest slice:
  - it is the part already supported by repeated exact seeds, verified feeders, and checked abstract Lean support assets;
  - it cleanly separates scalable structure from finite witness tuning;
  - it does not overclaim a closed all-odd-prime arithmetic theorem that the current evidence still does not justify.
- Strongest plausible theorem slice right now:
  - a paired bridge-lemma section plus paired `p = 13` arithmetic checkpoints;
  - not yet a full odd-prime theorem on either family line.

## reusable_lemmas

- Checked abstract support assets already aligned with the slice:
  - `support_decomposition_F25`;
  - `support_decomposition_F2`;
  - `classwise_template_lemma`;
  - `pairwise_coprime_clique_lemma`;
  - `forbidden_multiples_reservoir_lemma`;
  - `singleton_one_lemma`;
  - `three_interface_pack_lemma`;
  - `zp_z25_support_template_reduction`;
  - `zp_zp_z2_support_template_reduction_of_singleton_one`.
- Next reusable bridge lemmas to formalize:
  - `f25_ring_support_partition_lemma`;
  - `f25_ring_support_adjacency_lemma`;
  - `f25_family_wrapper_bridge_lemma`;
  - `f2_ring_support_partition_lemma`;
  - `f2_ring_support_adjacency_lemma`;
  - `f2_family_wrapper_bridge_lemma`.
- Arithmetic lemmas worth isolating only after the bridge closes:
  - `small_spill_C_block_lemma`;
  - `sparse_barrier_set_lemma`;
  - `smooth_reservoir_count_lemma`;
  - `coprime_complement_pack_lemma`.

## proof_plan

- Main proof path:
  1. Write the ring-level support partition for `F25(p)` and prove every nonzero zero-divisor lands in exactly one of `A,B,C,D`.
  2. Prove from the ring law that zero product occurs exactly on `A-C`, `B-B`, `B-C`, and `B-D`.
  3. Instantiate `zp_z25_support_template_reduction` to obtain the four-class bridge theorem.
  4. Write the ring-level support partition for `F2(p)` and prove every nonzero zero-divisor lands in exactly one of `A,B,C,D,E,F`.
  5. Prove from the ring law that zero product occurs exactly on `A-B`, `A-C`, `A-F`, `B-C`, `B-E`, and `C-D`.
  6. Instantiate `zp_zp_z2_support_template_reduction_of_singleton_one`, then factor the arithmetic statement through `singleton_one_lemma` and `three_interface_pack_lemma`.
  7. Present the verified `p = 13` records as arithmetic checkpoints:
     `F25(13)` forces the refined small-spill `C` statement,
     `F2(13)` shows the naive `{2,3}`-smooth six-class template survives at zero slack.
- Strongest path forward:
  - close the bridge lemmas first, because that already yields a defensible theorem slice even before any all-`p` arithmetic supply lemma is proved.
- Fallback path:
  - if the bridge lemmas close but the arithmetic corollaries still stall, preserve the structural reduction theorems as the main slice and keep the arithmetic story at the level of the paired `p = 13` checkpoints.

## fallback_counterexample_plan

- Do not claim a graph-level counterexample unless an actual non-prime family member is proved.
- Smallest likely counterexample or obstruction currently visible:
  - the old upper-half-prime-only four-class `C` template already fails at `p = 13`, because `[43,84]` has only `10` primes for `12` `C` slots.
- If the refined four-class arithmetic fails next:
  - test `F25(17)` and preserve any failure as a counterexample to the current small-spill arithmetic corollary, not as a theorem that `Γ(Z_17 × Z_25)` is non-prime.
- If the six-class line later fails beyond the zero-slack case:
  - preserve the first failing parameter as an obstruction to the current smooth-reservoir template, again without upgrading it to graph non-primality unless the graph itself is disproved.
- Minimal obstruction data to preserve:
  - the exact template statement being tested;
  - the exact counting or divisibility bottleneck;
  - the distinction between template failure and graph failure;
  - the smallest repaired template suggested by the failing feeder.

## next_best_feeder_instances

- `z17-z25-prime-zero-divisor-graph`
  - highest-value next feeder;
  - smallest post-`13` test of whether the refined small-spill `C` program genuinely scales.
- `z17-z17-z2-prime-zero-divisor-graph`
  - secondary feeder only after the bridge lemmas or the four-class stress test settle cleanly;
  - smallest next test of whether the six-class line needs a reservoir larger than the current `{2,3}`-smooth template after the exact zero-slack `p = 13` case.

## publication_value

- The proposed publication package is now clear:
  - the main theorem slice is the paired bridge from the ring law to the checked support-template reductions;
  - the main arithmetic evidence is the paired verified `p = 13` story:
    four-class survival with a repaired small-spill `C` block,
    six-class survival at the first zero-slack boundary with the naive template intact.
- One strongest path forward:
  - formalize the bridge lemmas and family wrapper theorems, then run `z17-z25` as the first post-`13` arithmetic discriminator.
- One fallback path:
  - if the arithmetic does not yet close, publish the structural slice plus the paired `p = 13` checkpoints and explicitly isolate the smallest broken subtemplate rather than overclaiming a family theorem.
- Honest publication verdict:
  - `publication_status = SLICE_CANDIDATE`;
  - not `SLICE_EXACT`, because the ring-to-support bridge lemmas are still missing;
  - not `PAPER_READY`, because the first post-`13` four-class stress test is still open and the family-level arithmetic lemmas are not closed.

## publication_prior_art_audit

- Audit date: `2026-04-10`.
- Exact statement search:
  - bounded web searches for `Γ(Z_13 × Z_25)` with `prime labeling` and for `Γ(Z_13 × Z_13 × Z_2)` with `prime labeling` returned no hits within budget.
  - alternate ASCII versions `Z_13 x Z_25`, `Z_13 x Z_13 x Z_2`, `Z_13 x Z_5^2`, and `Γ(Z_325)` with `zero-divisor graph` and `prime labeling` also returned no hits within budget.
- Alternate-notation family search:
  - the narrow family searches that did return relevant literature were on the broader forms `Γ(Z_p × Z_q^2)` and `Γ(Z_p × Z_p × Z_q)`.
- Canonical source check:
  - the closest canonical source remains Fox and Mooney, `On prime labelings of zero-divisor graphs` (Congressus Numerantium 236, published online 2025-11-21).
  - inside that source, the theorem / proposition / example / corollary / observation / sufficient-condition check relevant to this campaign gave:
    - Theorem 2.12 proves `Γ(Z_p × Z_4)` is prime for all primes `p`;
    - Theorem 2.14 proves `Γ(Z_p × Z_9)` is prime for all primes `p`;
    - Theorem 2.15 proves `Γ(Z_2 × Z_(p^2))` is prime for all primes `p`;
    - Conjecture 4.3 states `Γ(Z_p × Z_p × Z_q)` is prime for all primes `p,q`;
    - Conjecture 4.4 states `Γ(Z_p × Z_(q^2))` is prime for all primes `p,q`.
  - therefore the canonical source does not already settle either active family line or the exact `p = 13` feeders; it explicitly frames both ambient family directions as open.
- Outside-source status search:
  - an independent bounded search surfaced Gaded and Narayana, `On zero divisors graphs of direct product of finite fields` (Journal of Computational Mathematica, 2023), which studies structural graph invariants for `Γ(F_1 × ... × F_n)`.
  - publication implication: for the `Γ(Z_p × Z_p × Z_2)` line, the raw support-pattern / direct-product graph structure should be treated as standard background, not as the campaign's main novelty.
- Recent citation / discussion / follow-up check:
  - a 180-day bounded search on the Fox-Mooney title and DOI returned only the Combinatorial Press paper itself and no independent follow-up, citation, or discussion source within budget.
- Prior-art verdict:
  - no rediscovery was established in the bounded pass.
  - the honest novelty is not the existence of support classes by itself; it is the prime-labeling theorem slice that links the ring law to the support-template reductions and packages the paired `p = 13` arithmetic checkpoints honestly.

## publication_statement_faithfulness

- The strongest honest claim is stronger than “here is an example,” but only if it is stated as a paired theorem-slice candidate:
  - the real claim is that both active zero-divisor families admit reusable support-template reduction statements once the actual ring-to-support bridge lemmas are formalized.
- There is a real parameterized theorem slice here:
  - `Γ(Z_p × Z_25)` should reduce to a four-class coprimality allocation problem;
  - `Γ(Z_p × Z_p × Z_2)` should reduce to a three-interface packing problem after fixing the singleton class to label `1`.
- The current proof surface is only partly family-level:
  - the structural reduction is parameterized and reusable;
  - the arithmetic closure is still partly feeder-specific, especially on the four-class line where the first honest repair appears at `p = 13`.
- This would survive a referee asking “what is the theorem?” only if the paper states the theorem as a reduction / bridge theorem slice.
- It would not yet survive that question if phrased as “both families are prime for all odd primes.”
- The claim is still too dependent on hand-picked small cases for a full family theorem:
  - the paired `p = 13` feeders are valuable checkpoints, but the current arithmetic story still leans on hand-selected witness partitions and has not been closed by general supply lemmas.
- Faithfulness verdict:
  - keep the headline at the bridge-lemma slice plus paired `p = 13` checkpoints.
  - do not advertise a full odd-prime theorem, a family theorem, or a paper-ready classification result.

## publication_theorem_worthiness

- Is the strongest honest claim stronger than “here is an example”?
  - yes.
  - the reusable part is the support-theoretic reduction program shared by two different zero-divisor families, not merely the existence of two more witnesses.
- Is there a real parameterized theorem, theorem slice, or counterexample theorem here?
  - yes, there is a real theorem slice candidate:
    paired ring-to-support bridge theorems feeding the checked support-template reductions.
  - there is also a real obstruction statement:
    the old upper-half-prime-only `C` subtemplate on the four-class line fails first at `p = 13`.
- Is the proof structural or merely instance-specific?
  - structural on the support side;
  - still partly instance-specific on the arithmetic side.
- Would this survive a referee asking “what is the theorem?”
  - yes, if the theorem is the paired reduction statement and the `p = 13` data are presented as corollaries / checkpoints.
  - no, if the theorem is phrased as a closed family prime-labeling theorem.
- Is the claim still too dependent on hand-picked small cases?
  - yes for arithmetic closure;
  - no for the support-graph reduction skeleton.
- Is the generalization route strong enough to merit campaign priority?
  - yes.
  - the campaign has paired verified `p = 13` feeders, named reusable Lean support assets, and a crisp next blocker rather than diffuse exploratory work.
- Theorem-worthiness verdict:
  - the campaign is worthy of continued publication priority as a theorem-slice program.
  - the strongest honest target remains `SLICE_CANDIDATE`, not `FAMILY_CANDIDATE` and not `PAPER_READY`.

## publication_publishability

- Current publication status remains `SLICE_CANDIDATE`.
- It is not `INSTANCE_ONLY`:
  - the campaign now contains a genuine reusable slice candidate, not just isolated examples.
- It is not `REDISCOVERY`:
  - the bounded literature pass did not locate an earlier theorem settling either active family line or the exact `p = 13` feeders, and the canonical source still lists the relevant families as open conjectures.
- It is not `SLICE_EXACT`:
  - the missing ring-to-support bridge lemmas mean the family-level slice is not yet formally closed.
- It is not `PAPER_READY`:
  - the arithmetic corollaries are still too dependent on feeder checkpoints;
  - the four-class line still needs the first post-`13` stress test `Γ(Z_17 × Z_25)`;
  - the paper-level theorem statement is not yet supported by fully closed family lemmas.
- Proof-artifact audit:
  - the relevant family Lean files and names are preserved on disk;
  - the targeted family modules contain no `sorry` / `admit` markers by text scan in this pass;
  - this Lean pass reran targeted checks successfully inside `lean/`, including `lake build AutoMath.Families.ZeroDivisorRingBridges` and `lake build AutoMath`.
- Publishability verdict:
  - there is enough here for a serious theorem-slice campaign, and enough structure to justify keeping this family at the front of publication mode;
  - there is not yet enough closed mathematics to claim a paper-ready theorem package.

## strongest_honest_claim

- The strongest honest publication-facing claim is a paired theorem-slice candidate, not a full family theorem:
  - for odd prime `p`, the two active zero-divisor families `Γ(Z_p × Z_25)` and `Γ(Z_p × Z_p × Z_2)` admit small support-graph reductions whose abstract Lean skeleton is already preserved on disk;
  - the verified `p = 13` feeders show that this slice is mathematically nontrivial and still alive on both lines:
    `Γ(Z_13 × Z_25)` survives only after an honest refinement of the four-class `C` block,
    while `Γ(Z_13 × Z_13 × Z_2)` survives exactly at the first zero-slack boundary of the naive six-class template;
  - what is still missing is the actual family bridge from ring elements to those support classes, plus the first post-`13` arithmetic stress test on the four-class line.

## paper_title_hint

- `Ring-to-support reductions and paired p = 13 checkpoints in two zero-divisor prime-labeling families`

## next_action

- Formalize the actual ring-to-support partition and adjacency lemmas for both active family lines, then instantiate the checked abstract support reductions at the family level.
- After those bridge lemmas are stable, run `z17-z25-prime-zero-divisor-graph` as the first post-`13` publication-pressure feeder on the refined four-class arithmetic line.
- If the arithmetic corollary still stalls after the bridge closes, preserve the structural slice plus the paired `p = 13` checkpoints as the publication package and stop short of a family-theorem claim.

## lean_statement

- Lean date: `2026-04-10`.
- Targeted reusable family lemma:
  `AutoMath.Families.ZeroDivisorRingBridges.f2_ring_support_partition_lemma`.
- Exact Lean target for this bounded pass:
  for odd prime `p` and `x : ZMod p × ZMod p × ZMod 2`,
  `x` is a genuine nonzero zero-divisor vertex if and only if it lies in one of the six support classes `A,B,C,D,E,F` already named by `ZeroDivisorSupports.F2Support`.
- Honest scope choice:
  formalize the `F2(p)` ring-level support partition first, because it is a real family bridge lemma and it is materially simpler than the still-missing `F25(p)` bridge.

## lean_skeleton

- Add a bounded family bridge module under `lean/AutoMath/Families/ZeroDivisorRingBridges.lean`, mirrored under
  `artifacts/families/zero_divisor_prime_labelings/lean/AutoMath/Families/ZeroDivisorRingBridges.lean`.
- Define:
  `F2RingElem`,
  `f2SupportPredicate`,
  `f2ZeroDivisorVertex`.
- Prove the reverse bridge first:
  each support class gives a genuine vertex by an explicit annihilating witness.
- Prove the forward bridge second:
  if `x * y = 0` for a nonzero mate `y`, then `x` cannot have all three coordinates nonzero; combine that with `x ≠ 0` and dispatch the six zero/nonzero coordinate patterns.
- Put the checked lemma on the publication-safe root import path through `lean/AutoMath/Publications.lean`.

## lean_result

- Added backend Lean file:
  `lean/AutoMath/Families/ZeroDivisorRingBridges.lean`.
- Added mirrored family artifact Lean file:
  `artifacts/families/zero_divisor_prime_labelings/lean/AutoMath/Families/ZeroDivisorRingBridges.lean`.
- Added publication-safe import:
  `lean/AutoMath/Publications.lean`.
- Checked commands in this pass:
  - `cd lean && lake build AutoMath.Families.ZeroDivisorRingBridges`
  - `cd lean && lake env lean ../artifacts/families/zero_divisor_prime_labelings/lean/AutoMath/Families/ZeroDivisorRingBridges.lean`
  - `cd lean && lake build AutoMath`
- Honest Lean outcome:
  the `F2(p)` ring-level support partition bridge now checks inside the official backend and on the mirrored artifact copy.
- Honest classification impact:
  this is real theorem-slice progress, but it does not close the paired family slice.
  The run does **not** justify `classification = EXACT`,
  does **not** justify `publication_status = SLICE_EXACT`,
  and does **not** justify `PAPER_READY`.

## lean_blockers

- Missing `F2` bridge half:
  the exact ring-level adjacency table for `Γ(Z_p × Z_p × Z_2)` is still not formalized, so the checked partition lemma does not yet instantiate the full six-class wrapper theorem.
- Missing `F25` bridge:
  the four-class `Γ(Z_p × Z_25)` partition and adjacency lemmas remain open in Lean.
- Missing publication-pressure arithmetic closure:
  even after the bridge work, the first post-`13` four-class stress test `Γ(Z_17 × Z_25)` is still the next arithmetic discriminator.
