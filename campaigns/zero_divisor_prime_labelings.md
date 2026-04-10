# Zero-Divisor Prime Labelings

Priority: highest active campaign

Working objective:
Turn the existing exact-instance cluster on prime labelings of zero-divisor graphs into a publishable theorem slice, not merely more isolated examples.

## Current Campaign Status

- Primary theorem-slice statement:
  paired support-template reduction theorems showing that `Γ(Z_p × Z_25)` and `Γ(Z_p × Z_p × Z_2)` become prime-labeling problems on tiny support graphs once the actual ring-law support partitions are bridged into the checked classwise coprimality templates.
- Fallback theorem-slice statement:
  a paired `p = 13` arithmetic theorem slice for the current program: the old upper-half-prime-only `C` subtemplate already fails on the four-class line even though `Γ(Z_13 × Z_25)` stays prime after refinement, while `Γ(Z_13 × Z_13 × Z_2)` shows that the naive `{2,3}`-smooth six-class line still survives exactly at its first zero-slack boundary.
- Reusable support-template lemmas:
  `support_decomposition_F25`, `support_decomposition_F2`, `classwise_template_lemma`, `pairwise_coprime_clique_lemma`, `forbidden_multiples_reservoir_lemma`, `singleton_one_lemma`, `three_interface_pack_lemma`, and the Lean wrapper theorems in [lean/AutoMath/Families/ZeroDivisorReductions.lean](/Users/jeremykalfus/CodingProjects/AutoMath/lean/AutoMath/Families/ZeroDivisorReductions.lean), now factored through the new support surface in [lean/AutoMath/Families/ZeroDivisorSupports.lean](/Users/jeremykalfus/CodingProjects/AutoMath/lean/AutoMath/Families/ZeroDivisorSupports.lean).
- Missing support-decomposition lemmas:
  the family still lacks ring-level bridge lemmas proving that every nonzero zero-divisor of `Z_p × Z_25` lands in exactly one of the four support classes `A,B,C,D`, that every nonzero zero-divisor of `Z_p × Z_p × Z_2` lands in exactly one of the six support classes `A,B,C,D,E,F`, and that zero product in the ring occurs exactly on the class pairs named by the abstract support lemmas.
- Parameter-sensitive steps:
  supply `p - 1` labels for the `C` block in `Γ(Z_p × Z_25)`, now allowing a bounded number of sub-half primes whose doubles are pushed into `D` while keeping `A ∪ B` clear of every `C`-prime factor; choose a four-label sparse barrier set for the `B` clique whose spill labels fit inside the `20` available `A` slots; count enough smooth labels for `A ∪ E` in `Γ(Z_p × Z_p × Z_2)`; choose a disjoint complement block for `B ∪ F`; and keep the `F` block away from the prime support carried by `A`.
- Next decisive feeder and why:
  `Γ(Z_17 × Z_25)` is now the next decisive feeder because the paired `p = 13` frontier has already cleared on both active lines, so the next arithmetic discriminator is the smallest post-`13` test of whether the refined small-spill `C` block on the four-class line is a real family corollary or only a local repair.
- Strongest honest current claim:
  the paired support-template program is now backed by verified `p = 13` feeders on both active zero-divisor lines, checked Lean names for the paired abstract reduction theorems, and checked reusable family lemmas `support_decomposition_F25`, `support_decomposition_F2`, `singleton_one_lemma`, and `three_interface_pack_lemma`; the main uncertainty has shifted from “does the paired `p = 13` frontier survive?” to “can the actual ring-to-support bridge lemmas be formalized cleanly enough for a paper section, and does the refined four-class arithmetic keep scaling at `p = 17`?”
- `publication_status`: `SLICE_CANDIDATE`
- `publication_confidence`: `high`
- `campaign_health`: `warm`
- `next_action`: `formalize_ring_to_support_bridge_lemmas_then_run_z17_z25`
- `paper_title_hint`: `Support-template reductions and paired p = 13 feeders in two zero-divisor prime-labeling families`

## Why This Campaign Exists

The repo already contains a nontrivial exact inventory in [PROOFS.md](/Users/jeremykalfus/CodingProjects/AutoMath/PROOFS.md):

- `z3-z25-prime-zero-divisor-graph`
- `z5-z25-prime-zero-divisor-graph`
- `z7-z25-prime-zero-divisor-graph`
- `z5-z5-z2-prime-zero-divisor-graph`
- `z5-z5-z3-prime-zero-divisor-graph`
- `z7-z7-z2-prime-zero-divisor-graph`
- `z2-power-8-prime-zero-divisor-graph`

That is already enough evidence for a campaign. The repeated decomposition patterns are stronger than a random exact-instance queue and should now drive the harness.

Verified feeder evidence beyond [PROOFS.md](/Users/jeremykalfus/CodingProjects/AutoMath/PROOFS.md):

- [artifacts/z11-z25-prime-zero-divisor-graph/record.md](/Users/jeremykalfus/CodingProjects/AutoMath/artifacts/z11-z25-prime-zero-divisor-graph/record.md) is now a preserved `VERIFIED` feeder on the `Γ(Z_p × Z_25)` line.
- [artifacts/z11-z11-z2-prime-zero-divisor-graph/record.md](/Users/jeremykalfus/CodingProjects/AutoMath/artifacts/z11-z11-z2-prime-zero-divisor-graph/record.md) is now a preserved `VERIFIED` feeder on the `Γ(Z_p × Z_p × Z_2)` line.
- [artifacts/z13-z25-prime-zero-divisor-graph/record.md](/Users/jeremykalfus/CodingProjects/AutoMath/artifacts/z13-z25-prime-zero-divisor-graph/record.md) is now a preserved `VERIFIED` feeder showing that the four-class `p = 13` frontier survives after refining the `C` block.
- [artifacts/z13-z13-z2-prime-zero-divisor-graph/record.md](/Users/jeremykalfus/CodingProjects/AutoMath/artifacts/z13-z13-z2-prime-zero-divisor-graph/record.md) is now a preserved `VERIFIED` feeder showing that the six-class line also survives the first zero-slack `p = 13` frontier with the naive `{2,3}`-smooth template intact.
- They do not belong in `PROOFS.md` yet because Lean has not completed, but together they materially upgrade the family campaign because the paired theorem-slice program has now survived the campaign-designated `p = 11` checkpoint on both active lines and the paired `p = 13` frontier on both active lines.

## Strongest Current Publication Targets

1. A theorem slice for `Γ(Z_p × Z_25)` with odd prime `p`, starting from the exact `p = 3,5,7` cluster.
2. A theorem slice for `Γ(Z_p × Z_p × Z_2)` with odd prime `p`, starting from the exact `p = 5,7` cluster.
3. A reusable support-template theorem that reduces both families to coprimality constraints on a small support graph.
4. Only if justified by current evidence, a carefully scoped direction for `Γ((Z_2)^n)`.
5. If a full slice theorem stalls, a smallest-counterexample or smallest-breakpoint feeder search, with `p = 13` now the first honest frontier after the paired `p = 11` checkpoint.

## Seed Inventory

### `Γ(Z_p × Z_25)` exacts

- [artifacts/z3-z25-prime-zero-divisor-graph/record.md](/Users/jeremykalfus/CodingProjects/AutoMath/artifacts/z3-z25-prime-zero-divisor-graph/record.md)
- [artifacts/z5-z25-prime-zero-divisor-graph/record.md](/Users/jeremykalfus/CodingProjects/AutoMath/artifacts/z5-z25-prime-zero-divisor-graph/record.md)
- [artifacts/z7-z25-prime-zero-divisor-graph/record.md](/Users/jeremykalfus/CodingProjects/AutoMath/artifacts/z7-z25-prime-zero-divisor-graph/record.md)

Shared support-class decomposition:

- `A = {(0,u) : u ∈ Z_25^× and 5 ∤ u}`, size `20`
- `B = {(0,5),(0,10),(0,15),(0,20)}`, size `4`
- `C = {(a,0) : a ∈ Z_p^×}`, size `p - 1`
- `D = {(a,5t) : a ∈ Z_p^×, t ∈ {1,2,3,4}}`, size `4(p - 1)`

Shared edge families:

- `A-C`
- `B-B`
- `B-C`
- `B-D`

No other edge types appear in the exact proofs.

Shared label-role template:

- `C` receives large primes whose only multiples in the label interval are themselves.
- after the verified `p = 13` feeder, the honest refined version allows a bounded number of `C` primes below the half-interval cutoff so long as their nontrivial multiples are pushed into `D` rather than into `A ∪ B`.
- `B` receives a pairwise-coprime barrier set with sparse forbidden multiples.
- `A` receives labels avoiding the primes assigned to `C`.
- `D` receives the residual label reservoir avoiding the barrier primes in `B`.

Reusable coprimality lemmas visible already:

- pairwise coprime clique lemma for the `B` class
- large-prime singleton-role lemma for the `C` class
- residual-reservoir lemma for `D` once `B` is chosen
- classwise template theorem: if labels satisfy the class constraints, any bijection within classes works
- checked Lean wrapper theorem `zp_z25_support_template_reduction`
- checked Lean wrapper theorem `zp_zp_z2_support_template_reduction_of_singleton_one`
- checked Lean family lemma `singleton_one_lemma`, isolating the automatic `A-C`, `B-C`, and `C-D` hinge edges once `C = 1`

Parameter-sensitive steps:

- existence of `p - 1` sufficiently large primes inside the active label range for `C`
- existence of a refined `C` block if the pure upper-half-prime version runs short, while still keeping every nontrivial `C` multiple out of `A ∪ B`
- keeping the `B` forbidden multiples sparse enough so `D` still has a reservoir
- proving the reservoir-count argument without hand-picked instance arithmetic

### `Γ(Z_p × Z_p × Z_2)` exacts

- [artifacts/z5-z5-z2-prime-zero-divisor-graph/record.md](/Users/jeremykalfus/CodingProjects/AutoMath/artifacts/z5-z5-z2-prime-zero-divisor-graph/record.md)
- [artifacts/z7-z7-z2-prime-zero-divisor-graph/record.md](/Users/jeremykalfus/CodingProjects/AutoMath/artifacts/z7-z7-z2-prime-zero-divisor-graph/record.md)

Shared support-class decomposition:

- `A = (*,0,0)`, size `p - 1`
- `B = (0,*,0)`, size `p - 1`
- `C = (0,0,1)`, size `1`
- `D = (*,*,0)`, size `(p - 1)^2`
- `E = (*,0,1)`, size `p - 1`
- `F = (0,*,1)`, size `p - 1`

Shared edge families:

- `A-B`
- `A-C`
- `A-F`
- `B-C`
- `B-E`
- `C-D`

Structural takeaways:

- `C` is the hinge vertex and the actual support graph is `A-B`, `A-C`, `A-F`, `B-C`, `B-E`, `C-D`
- once `C` gets label `1`, the edges `A-C`, `B-C`, and `C-D` become automatic and the `D` class becomes essentially unconstrained
- the real burden is only on the three cross-coprime interfaces `A-B`, `A-F`, `B-E`
- this is a very small support graph and looks theorem-slice friendly

Shared label-role template:

- `A` takes low smooth numbers, usually `2,3`-smooth
- `B` takes large odd primes
- `E` takes additional `2,3`-smooth numbers
- `F` avoids primes used by `A`
- `C` gets `1`
- `D` absorbs the leftovers

Parameter-sensitive steps:

- making the `A` and `E` smooth reservoirs scale with `p`
- choosing `B ∪ F` as a coprime complement block without exhausting the interval
- proving enough label supply without hand-tuned finite lists, with `p = 13` now the first zero-slack test for the naive `{2,3}`-smooth version

### `Γ((Z_2)^n)` evidence

- exact at `n = 8` in [artifacts/z2-power-8-prime-zero-divisor-graph/record.md](/Users/jeremykalfus/CodingProjects/AutoMath/artifacts/z2-power-8-prime-zero-divisor-graph/record.md)
- rediscovered at `n = 5`, so novelty is already risky

Shared structural signal:

- owner-set / required-support containment template
- repeated prime-factor ownership assigned by coordinate
- disjointness automatically forces coprimality if owner sets are respected

Campaign stance:

- keep this as a supporting template source only
- do not let `Γ((Z_2)^n)` dominate unless a genuinely frontier-novel theorem slice appears

## Candidate Theorem Slices

### Slice A: support-template reduction for `Γ(Z_p × Z_25)`

Strongest honest near-term claim:

- a theorem reducing prime labelability of `Γ(Z_p × Z_25)` to a small explicit arithmetic allocation problem on the four support classes `A,B,C,D`

Why this matters:

- it turns three exact proofs into one structural theorem
- it isolates the real parameter-sensitive constraints
- it is Lean-friendly and publication-friendly even before a full all-primes result

### Slice B: support-template reduction for `Γ(Z_p × Z_p × Z_2)`

Strongest honest near-term claim:

- a theorem reducing prime labelability of `Γ(Z_p × Z_p × Z_2)` to a three-interface coprimality packing problem after fixing `C = 1`

Why this matters:

- it packages the repeated `p = 5,7` exact arguments into a clean family-support theorem
- it sharply separates scalable structure from hand-picked labels

### Slice C: explicit finite prime ranges

Possible next step after the template theorem:

- prove the slice for a nontrivial range of odd primes supported by current exacts and a supply-count lemma

Candidate next breakpoint:

- `p = 17` on the four-class line

Reason:

- the four-class line now survives `p = 13` after refining the `C` block
- the six-class line now survives its first zero-slack `p = 13` arithmetic test
- the smallest honest next discriminator is therefore whether the refined small-spill four-class arithmetic scales even one more prime

## Chosen Campaign Target

Primary target:

- a publication-grade theorem slice that packages the `Γ(Z_p × Z_25)` and `Γ(Z_p × Z_p × Z_2)` exact proofs into reusable support-template theorems

Secondary target:

- targeted feeder instances at `p = 13`, chosen to distinguish “the paired arithmetic program really scales” from “the current `p = 11` success is still a small-prime phenomenon”

## Primary Theorem-Slice Target

- Prove paired support-template reduction theorems:
  - `Γ(Z_p × Z_25)` reduces to a four-class coprimality allocation problem on `A,B,C,D`
  - `Γ(Z_p × Z_p × Z_2)` reduces to a three-interface coprimality packing problem once the singleton class gets label `1`

## Fallback Target

- If the arithmetic closure still fails to scale, package the first honest `p = 13` breakpoint as a smallest-template-failure obstruction for the current arithmetic program rather than as a graph-level non-primality claim.

## Strongest Path Forward

1. Package the paired verified `p = 11` feeders as arithmetic evidence for the existing support-template reduction program.
2. Package the paired `p = 13` gains honestly: the four-class line needs the refined small-spill `C` block, while the six-class line survives the first zero-slack case without a further repair.
3. Prove the cleanest honest theorem slice first, even if it remains a sufficient-condition theorem.
4. Formalize the ring-to-support bridge lemmas so the current Lean support surface becomes a real paper section rather than campaign prose.
5. Use `Γ(Z_17 × Z_25)` next to test whether the refined four-class arithmetic lemma is really scalable beyond the first repaired case.

## Fallback Path

If the theorem slice stalls:

- run smallest-breakpoint feeder instances
- search for the first parameter where the current label-role template breaks
- turn that into either:
  - a smallest counterexample theorem, or
  - a refined slice with explicit hypotheses

## Next Best Feeders

Highest value next instance:

- `Γ(Z_17 × Z_25)`

Why this:

- the paired `p = 13` checkpoint is now closed on both active lines
- `Γ(Z_17 × Z_25)` is the smallest post-`13` discriminator for the refined small-spill `C` block
- it directly tests whether the current paired support-template logic is genuinely scalable beyond the first repaired four-class case

## Blockers

- The support-graph reductions are visible, but they still need family-specific bridge lemmas from the actual ring law rather than only abstract support-template statements.
- The Lean surface now has checked support lemmas and reduction wrappers, but the repo still lacks the formal ring-to-support partition and adjacency lemmas deriving the actual `F25(p)` and `F2(p)` support graphs from zero-divisor structure.
- The refined four-class arithmetic line still needs one honest post-`13` stress test at `Γ(Z_17 × Z_25)` before the paired theorem slice can claim more than a `p = 13` frontier package.
- The four-class `p = 13` gain is now explicit, but it must be packaged honestly as a refined `C`-block lemma rather than as survival of the old upper-half-prime-only subtemplate.
- The next honest publication question is now concentrated on whether the six-class arithmetic program survives the first zero-slack `p = 13` frontier without overclaiming.

## Publication Value

The current repo already has enough exact and verified-feeder evidence to justify a paper-oriented campaign. A publishable outcome still does not require proving every odd-prime case immediately. A clean support-template theorem backed by paired verified `p = 11` feeders, the verified refined `F25(13)` checkpoint, and either a six-class `p = 13` success or a clean smallest-break obstruction theorem would already be stronger than “here are more isolated examples.”
