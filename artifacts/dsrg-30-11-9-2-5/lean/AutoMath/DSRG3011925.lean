import Mathlib

namespace AutoMath
namespace DSRG3011925

open Finset

/-- The fixed `30`-vertex universe for the exact dsrg instance `(30,11,9,2,5)`. -/
abbrev Vertex := Fin 30

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

- loopless directed graph on `30` vertices,
- indegree and outdegree `11`,
- exactly `9` directed `2`-paths from `x` back to itself,
- exactly `2` directed `2`-paths from `x` to `y` along an arc,
- exactly `5` directed `2`-paths from `x` to `y` when `x ≠ y` and there is no arc.
-/
def IsDSRG3011925 (Adj : Vertex → Vertex → Prop) : Prop := by
  classical
  exact
    (∀ x, ¬ Adj x x) ∧
      (∀ x, (outNbrs Adj x).card = 11) ∧
      (∀ x, (inNbrs Adj x).card = 11) ∧
      ∀ x y, (twoPathSet Adj x y).card = if x = y then 9 else if Adj x y then 2 else 5

/-- The exact intended existential statement from the active dossier. -/
def intendedStatement : Prop :=
  ∃ Adj : Vertex → Vertex → Prop, IsDSRG3011925 Adj

/-- The exact disproof target for this slug. -/
def exactCounterexampleStatement : Prop :=
  ¬ intendedStatement

/-- Exact theorem statement for the active slug. -/
theorem no_dsrg_30_11_9_2_5_statement :
    exactCounterexampleStatement ↔
      ¬ ∃ Adj : Vertex → Vertex → Prop, IsDSRG3011925 Adj := by
  rfl

/-- Faithfulness check: the Lean target is exactly the negation of the selected existential claim. -/
theorem exact_counterexample_statement_faithful :
    exactCounterexampleStatement = ¬ intendedStatement := by
  rfl

/--
Proof skeleton for the exact theorem targeted in this slug:

```lean
theorem no_dsrg_30_11_9_2_5 :
    exactCounterexampleStatement := by
  intro hExists
  rcases hExists with ⟨Adj, hAdj⟩
  -- 1. Fix a vertex `x` and split the other vertices into `M`, `O`, `I`, `N`.
  -- 2. Translate the dsrg `2`-path counts into the local block-total equations.
  -- 3. Derive a genuine contradiction from those exact equations.
```

The current Lean blocker is mathematical, not syntactic: the verifier's advertised repair uses
`a + b + c + d = 99` for the total number of arcs from the mutual block `M` into `M ∪ O ∪ I ∪ N`.
That drops the forced edge from each `y ∈ M` back to the distinguished vertex `x`. The faithful
block-total row sum excluding `x` is `a + b + c + d = 90`, and with that correction the displayed
linear system no longer contradicts itself.
-/
theorem no_dsrg_30_11_9_2_5_skeleton
    (hNonexistence : ∀ Adj : Vertex → Vertex → Prop, IsDSRG3011925 Adj → False) :
    exactCounterexampleStatement := by
  intro hExists
  rcases hExists with ⟨Adj, hAdj⟩
  exact hNonexistence Adj hAdj

/-- What the verifier's claimed repair would force if the incorrect row sum `99` were used. -/
theorem wrong_row_sum_consequence
    {a b c d : Nat} (hac : a + c = 18) (hrow : a + b + c + d = 99) :
    d = 81 - b := by
  omega

/-- The faithful row-sum consequence for the mutual block is `d = 72 - b`, not `81 - b`. -/
theorem correct_row_sum_consequence
    {a b c d : Nat} (hac : a + c = 18) (hrow : a + b + c + d = 90) :
    d = 72 - b := by
  omega

/-- The out-only block still forces `h = 8 + b` from the remaining valid local equations. -/
theorem out_only_row_sum_consequence
    {b e f g h : Nat} (heg : e + g = 10) (hbf : b + f = 4) (hrow : e + f + g + h = 22) :
    h = 8 + b := by
  omega

/-- With the faithful row sums, the displayed local equations force `d + h = 80`; there is no
contradiction left to close the exact nonexistence theorem. -/
theorem corrected_local_constraints_force_d_plus_h
    {a b c d e f g h : Nat}
    (hac : a + c = 18)
    (heg : e + g = 10)
    (hbf : b + f = 4)
    (hrowM : a + b + c + d = 90)
    (hrowO : e + f + g + h = 22) :
    d + h = 80 := by
  omega

/-- The faithful local linear system is consistent, so the current verification note is not yet a
formalizable exact disproof of the selected dsrg statement. -/
theorem corrected_local_constraints_consistent :
    ∃ a b c d e f g h : Nat,
      a + c = 18 ∧
      e + g = 10 ∧
      b + f = 4 ∧
      a + b + c + d = 90 ∧
      e + f + g + h = 22 ∧
      d + h = 80 := by
  refine ⟨8, 2, 10, 70, 10, 2, 0, 10, ?_⟩
  omega

end DSRG3011925
end AutoMath
