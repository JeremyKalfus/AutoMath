import Mathlib

namespace AutoMath
namespace DSRG9112651

open Finset

/-- The fixed `91`-vertex universe for the exact dsrg instance `(91,12,6,5,1)`. -/
abbrev Vertex := Fin 91

/-- Out-neighbors of `x` in a directed graph relation `Adj`. -/
noncomputable def outNbrs (Adj : Vertex → Vertex → Prop) (x : Vertex) : Finset Vertex := by
  classical
  exact Finset.univ.filter (fun y => Adj x y)

/-- In-neighbors of `x` in a directed graph relation `Adj`. -/
noncomputable def inNbrs (Adj : Vertex → Vertex → Prop) (x : Vertex) : Finset Vertex := by
  classical
  exact Finset.univ.filter (fun y => Adj y x)

/-- Intermediate vertices of directed `2`-paths `x -> z -> y`. -/
noncomputable def twoPathSet (Adj : Vertex → Vertex → Prop) (x y : Vertex) : Finset Vertex := by
  classical
  exact (outNbrs Adj x).filter (fun z => Adj z y)

/--
Exact dsrg predicate locked by the selected problem:

- loopless directed graph on `91` vertices,
- indegree and outdegree `12`,
- exactly `6` directed `2`-paths from `x` back to itself,
- exactly `5` directed `2`-paths from `x` to `y` along an arc,
- exactly `1` directed `2`-path from `x` to `y` when `x ≠ y` and there is no arc.
-/
def IsDSRG9112651 (Adj : Vertex → Vertex → Prop) : Prop := by
  classical
  exact
    (∀ x, ¬ Adj x x) ∧
      (∀ x, (outNbrs Adj x).card = 12) ∧
      (∀ x, (inNbrs Adj x).card = 12) ∧
      ∀ x y, (twoPathSet Adj x y).card = if x = y then 6 else if Adj x y then 5 else 1

/-- The exact intended existential statement from the active dossier. -/
def intendedStatement : Prop :=
  ∃ Adj : Vertex → Vertex → Prop, IsDSRG9112651 Adj

/-- The exact disproof target for this slug. -/
def exactCounterexampleStatement : Prop :=
  ¬ intendedStatement

/-- Exact theorem statement for the active slug. -/
theorem no_dsrg_91_12_6_5_1_statement :
    exactCounterexampleStatement ↔
      ¬ ∃ Adj : Vertex → Vertex → Prop, IsDSRG9112651 Adj := by
  rfl

/-- Faithfulness check: the Lean target is exactly the negation of the selected existential claim. -/
theorem exact_counterexample_statement_faithful :
    exactCounterexampleStatement = ¬ intendedStatement := by
  rfl

/--
Proof skeleton for the exact theorem targeted in this slug:

```lean
theorem no_dsrg_91_12_6_5_1 :
    exactCounterexampleStatement := by
  intro hExists
  rcases hExists with ⟨Adj, hAdj⟩
  -- 1. Fix `x` and split the other vertices into the four blocks `M`, `O`, `I`, `N`.
  -- 2. Translate the dsrg `2`-path counts into block-total equations.
  -- 3. Derive a genuine contradiction from those exact equations.
```

The current Lean blocker is mathematical, not syntactic: the present handwritten proof uses the
incorrect row sum `a + b + c + d = 72` on the mutual block `M`, but every `y ∈ M` also has the
forced edge `y -> x`. The corrected identity is `6 + a + b + c + d = 72`, and with that fix the
displayed linear system is consistent rather than contradictory.
-/
theorem no_dsrg_91_12_6_5_1_skeleton
    (hNonexistence : ∀ Adj : Vertex → Vertex → Prop, IsDSRG9112651 Adj → False) :
    exactCounterexampleStatement := by
  intro hExists
  rcases hExists with ⟨Adj, hAdj⟩
  exact hNonexistence Adj hAdj

/-- Corrected row-sum consequence for the mutual block `M`: one must account for the six edges
from `M` back to the distinguished vertex `x`. -/
theorem corrected_mutual_block_row_sum
    {a b c d : Nat} (hrow : 6 + a + b + c + d = 72) (hac : a + c = 30) :
    b + d = 36 := by
  omega

/-- The analogous row-sum consequence for the out-only block `O`. -/
theorem corrected_out_only_block_row_sum
    {e f g h : Nat} (hrow : e + f + g + h = 72) (heg : e + g = 6) :
    f + h = 66 := by
  omega

/-- The corrected linear constraints coming from the current handwritten argument are jointly
satisfiable, so they do not yet prove nonexistence. -/
theorem counterexample_linear_constraints_consistent :
    ∃ a b c d e f g h : Nat,
      b + f = 30 ∧
      d + h = 72 ∧
      a + c = 30 ∧
      e + g = 6 ∧
      6 + a + b + c + d = 72 ∧
      e + f + g + h = 72 := by
  refine ⟨30, 0, 0, 36, 0, 30, 6, 36, ?_⟩
  omega

end DSRG9112651
end AutoMath
