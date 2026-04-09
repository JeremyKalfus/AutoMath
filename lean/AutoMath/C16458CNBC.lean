import Mathlib

namespace AutoMath
namespace C16458CNBC

open Finset

inductive Color where
  | red
  | blue
deriving DecidableEq, Fintype, Repr

/-- Vertices of the exact circulant instance `C_16(4,5,8)`. -/
abbrev Vertex := Fin 16

/-- A red/blue coloring of the `16` vertices. -/
abbrev Coloring := Vertex → Color

instance : DecidableEq Vertex := inferInstance
instance : Fintype Vertex := inferInstance
instance : DecidableEq Coloring := inferInstance
instance : Fintype Coloring := inferInstance

/-- The five open neighbors of `v`: the generators `±4`, `±5`, and `8 = -8 (mod 16)`. -/
def neighborSet (v : Vertex) : Finset Vertex :=
  [v + 4, v + 5, v + 8, v + 11, v + 12].toFinset

/-- Adjacency in the exact quintic circulant `C_16(4,5,8)`. -/
def Adj (v w : Vertex) : Prop :=
  w ∈ neighborSet v

/-- The closed neighborhood `N[v] = {v, v ± 4, v ± 5, v + 8}`. -/
def closedNeighborhood (v : Vertex) : Finset Vertex :=
  insert v (neighborSet v)

/-- Exact CNB predicate for this instance: every closed neighborhood has exactly three red
vertices, hence also three blue vertices because the closed neighborhood has size `6`. -/
def IsCNBColoring (color : Coloring) : Prop :=
  ∀ v, ((closedNeighborhood v).filter fun w => color w = Color.red).card = 3

/-- The exact intended statement from the active dossier. -/
def intendedStatement : Prop :=
  ∃ color : Coloring, IsCNBColoring color

/-- The exact disproof target for this slug. -/
def exactCounterexampleStatement : Prop :=
  ¬ intendedStatement

theorem neighborSet_card (v : Vertex) : (neighborSet v).card = 5 := by
  fin_cases v <;> decide

theorem closedNeighborhood_card (v : Vertex) : (closedNeighborhood v).card = 6 := by
  fin_cases v <;> decide

/-- Exact theorem statement for the active slug. -/
theorem no_c16_4_5_8_cnbc_statement :
    exactCounterexampleStatement ↔
      ¬ ∃ color : Coloring,
          ∀ v, ((closedNeighborhood v).filter fun w => color w = Color.red).card = 3 := by
  rfl

/-- Faithfulness check: the Lean target is exactly the negation of the selected existential claim. -/
theorem exact_counterexample_statement_faithful :
    exactCounterexampleStatement = ¬ intendedStatement := by
  rfl

/--
Proof skeleton for the exact theorem targeted in this slug:

```lean
theorem c16_4_5_8_not_cnbc :
    exactCounterexampleStatement := by
  intro hExists
  rcases hExists with ⟨color, hcolor⟩
  -- Show that every candidate coloring fails one of the sixteen closed-neighborhood
  -- balance equations for the exact mask `{0, ±4, ±5, 8}`.
  exact no_coloring_works color hcolor
```
 -/
theorem c16_4_5_8_not_cnbc_skeleton
    (no_coloring_works : ∀ color : Coloring, ¬ IsCNBColoring color) :
    exactCounterexampleStatement := by
  intro hExists
  rcases hExists with ⟨color, hcolor⟩
  exact no_coloring_works color hcolor

/-- Finite exhaustive check over all `2^16` red/blue colorings of the exact instance. -/
theorem no_coloring_works : ∀ color : Coloring, ¬ IsCNBColoring color := by
  native_decide

/-- Expanded exact statement: there is no red/blue CNB-coloring of `C_16(4,5,8)`. -/
theorem c16_4_5_8_not_cnbc_explicit :
    ¬ ∃ color : Coloring,
      ∀ v, ((closedNeighborhood v).filter fun w => color w = Color.red).card = 3 := by
  intro hExists
  rcases hExists with ⟨color, hcolor⟩
  exact no_coloring_works color hcolor

/-- The quintic circulant `C_16(4,5,8)` does not admit a closed-neighborhood balanced coloring. -/
theorem c16_4_5_8_not_cnbc : exactCounterexampleStatement := by
  exact c16_4_5_8_not_cnbc_skeleton no_coloring_works

end C16458CNBC
end AutoMath
