import Mathlib

namespace AutoMath
namespace C244512CNBC

open Finset

inductive Color where
  | red
  | blue
deriving DecidableEq, Fintype, Repr

/-- Vertices of the exact circulant instance `C_24(4,5,12)`. -/
abbrev Vertex := Fin 24

/-- A red/blue coloring of the `24` vertices. -/
abbrev Coloring := Vertex → Color

instance : DecidableEq Vertex := inferInstance
instance : Fintype Vertex := inferInstance
instance : DecidableEq Coloring := inferInstance
instance : Fintype Coloring := inferInstance

/-- The five open neighbors of `v`: the generators `±4`, `±5`, and `12 = -12 (mod 24)`. -/
def neighborSet (v : Vertex) : Finset Vertex :=
  [v + 4, v + 5, v + 12, v + 19, v + 20].toFinset

/-- Adjacency in the exact quintic circulant `C_24(4,5,12)`. -/
def Adj (v w : Vertex) : Prop :=
  w ∈ neighborSet v

/-- The closed neighborhood `N[v] = {v, v ± 4, v ± 5, v + 12}`. -/
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

instance instDecidableIsCNBColoring (color : Coloring) : Decidable (IsCNBColoring color) := by
  unfold IsCNBColoring
  infer_instance

instance : Decidable intendedStatement := by
  unfold intendedStatement
  infer_instance

instance : Decidable exactCounterexampleStatement := by
  unfold exactCounterexampleStatement
  infer_instance

/-- Signed encoding of a red/blue coloring. -/
def signed (color : Coloring) (v : Vertex) : Int :=
  match color v with
  | Color.red => 1
  | Color.blue => -1

theorem neighborSet_card (v : Vertex) : (neighborSet v).card = 5 := by
  fin_cases v <;> decide

theorem closedNeighborhood_card (v : Vertex) : (closedNeighborhood v).card = 6 := by
  fin_cases v <;> decide

/-- On any finite vertex set, the signed sum is `2 * red_count - card`. -/
theorem sum_signed_eq_twice_red_sub_card (color : Coloring) (s : Finset Vertex) :
    ∑ v in s, signed color v =
      2 * (((s.filter fun w => color w = Color.red).card : Nat) : Int) - s.card := by
  classical
  refine Finset.induction_on s ?_ ?_
  · simp [signed]
  · intro a s ha ih
    cases hca : color a with
    | red =>
        simp [signed, hca, ha, ih]
        omega
    | blue =>
        simp [signed, hca, ha, ih]
        omega

/-- Every CNB-coloring yields signed closed-neighborhood sum `0` on the exact instance. -/
theorem closedNeighborhood_signed_sum_zero (color : Coloring) (hcolor : IsCNBColoring color)
    (v : Vertex) :
    ∑ w in closedNeighborhood v, signed color w = 0 := by
  have hsum := sum_signed_eq_twice_red_sub_card color (closedNeighborhood v)
  rw [hcolor v, closedNeighborhood_card v] at hsum
  norm_num at hsum
  simpa using hsum

/-- Exact theorem statement for the active slug. -/
theorem no_c24_4_5_12_cnbc_statement :
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
theorem c24_4_5_12_not_cnbc :
    exactCounterexampleStatement := by
  intro hExists
  rcases hExists with ⟨color, hcolor⟩
  -- Show that every candidate coloring fails one of the twenty-four closed-neighborhood
  -- balance equations for the exact mask `{0, ±4, ±5, 12}`.
  exact no_coloring_works color hcolor
```
 -/
theorem c24_4_5_12_not_cnbc_skeleton
    (no_coloring_works : ∀ color : Coloring, ¬ IsCNBColoring color) :
    exactCounterexampleStatement := by
  intro hExists
  rcases hExists with ⟨color, hcolor⟩
  exact no_coloring_works color hcolor

/-- The exact balance equations force the signed sum on vertices `0,1,2` to be `0`. -/
theorem three_residue_sum_zero (color : Coloring) (hcolor : IsCNBColoring color) :
    signed color 0 + signed color 1 + signed color 2 = 0 := by
  have h0 : signed color 0 + signed color 4 + signed color 5 + signed color 12 +
      signed color 19 + signed color 20 = 0 := by
    simpa [closedNeighborhood, neighborSet, add_assoc, add_left_comm, add_comm] using
      closedNeighborhood_signed_sum_zero color hcolor (0 : Vertex)
  have h1 : signed color 0 + signed color 1 + signed color 5 + signed color 6 +
      signed color 13 + signed color 21 = 0 := by
    simpa [closedNeighborhood, neighborSet, add_assoc, add_left_comm, add_comm] using
      closedNeighborhood_signed_sum_zero color hcolor (1 : Vertex)
  have h2 : signed color 1 + signed color 2 + signed color 6 + signed color 7 +
      signed color 14 + signed color 22 = 0 := by
    simpa [closedNeighborhood, neighborSet, add_assoc, add_left_comm, add_comm] using
      closedNeighborhood_signed_sum_zero color hcolor (2 : Vertex)
  have h3 : signed color 2 + signed color 3 + signed color 7 + signed color 8 +
      signed color 15 + signed color 23 = 0 := by
    simpa [closedNeighborhood, neighborSet, add_assoc, add_left_comm, add_comm] using
      closedNeighborhood_signed_sum_zero color hcolor (3 : Vertex)
  have h4 : signed color 0 + signed color 3 + signed color 4 + signed color 8 +
      signed color 9 + signed color 16 = 0 := by
    simpa [closedNeighborhood, neighborSet, add_assoc, add_left_comm, add_comm] using
      closedNeighborhood_signed_sum_zero color hcolor (4 : Vertex)
  have h5 : signed color 1 + signed color 4 + signed color 5 + signed color 9 +
      signed color 10 + signed color 17 = 0 := by
    simpa [closedNeighborhood, neighborSet, add_assoc, add_left_comm, add_comm] using
      closedNeighborhood_signed_sum_zero color hcolor (5 : Vertex)
  have h6 : signed color 2 + signed color 5 + signed color 6 + signed color 10 +
      signed color 11 + signed color 18 = 0 := by
    simpa [closedNeighborhood, neighborSet, add_assoc, add_left_comm, add_comm] using
      closedNeighborhood_signed_sum_zero color hcolor (6 : Vertex)
  have h7 : signed color 3 + signed color 6 + signed color 7 + signed color 11 +
      signed color 12 + signed color 19 = 0 := by
    simpa [closedNeighborhood, neighborSet, add_assoc, add_left_comm, add_comm] using
      closedNeighborhood_signed_sum_zero color hcolor (7 : Vertex)
  have h8 : signed color 4 + signed color 7 + signed color 8 + signed color 12 +
      signed color 13 + signed color 20 = 0 := by
    simpa [closedNeighborhood, neighborSet, add_assoc, add_left_comm, add_comm] using
      closedNeighborhood_signed_sum_zero color hcolor (8 : Vertex)
  have h9 : signed color 5 + signed color 8 + signed color 9 + signed color 13 +
      signed color 14 + signed color 21 = 0 := by
    simpa [closedNeighborhood, neighborSet, add_assoc, add_left_comm, add_comm] using
      closedNeighborhood_signed_sum_zero color hcolor (9 : Vertex)
  have h10 : signed color 6 + signed color 9 + signed color 10 + signed color 14 +
      signed color 15 + signed color 22 = 0 := by
    simpa [closedNeighborhood, neighborSet, add_assoc, add_left_comm, add_comm] using
      closedNeighborhood_signed_sum_zero color hcolor (10 : Vertex)
  have h11 : signed color 7 + signed color 10 + signed color 11 + signed color 15 +
      signed color 16 + signed color 23 = 0 := by
    simpa [closedNeighborhood, neighborSet, add_assoc, add_left_comm, add_comm] using
      closedNeighborhood_signed_sum_zero color hcolor (11 : Vertex)
  have h12 : signed color 0 + signed color 8 + signed color 11 + signed color 12 +
      signed color 16 + signed color 17 = 0 := by
    simpa [closedNeighborhood, neighborSet, add_assoc, add_left_comm, add_comm] using
      closedNeighborhood_signed_sum_zero color hcolor (12 : Vertex)
  have h13 : signed color 1 + signed color 9 + signed color 12 + signed color 13 +
      signed color 17 + signed color 18 = 0 := by
    simpa [closedNeighborhood, neighborSet, add_assoc, add_left_comm, add_comm] using
      closedNeighborhood_signed_sum_zero color hcolor (13 : Vertex)
  have h14 : signed color 2 + signed color 10 + signed color 13 + signed color 14 +
      signed color 18 + signed color 19 = 0 := by
    simpa [closedNeighborhood, neighborSet, add_assoc, add_left_comm, add_comm] using
      closedNeighborhood_signed_sum_zero color hcolor (14 : Vertex)
  have h15 : signed color 3 + signed color 11 + signed color 14 + signed color 15 +
      signed color 19 + signed color 20 = 0 := by
    simpa [closedNeighborhood, neighborSet, add_assoc, add_left_comm, add_comm] using
      closedNeighborhood_signed_sum_zero color hcolor (15 : Vertex)
  have h16 : signed color 4 + signed color 12 + signed color 15 + signed color 16 +
      signed color 20 + signed color 21 = 0 := by
    simpa [closedNeighborhood, neighborSet, add_assoc, add_left_comm, add_comm] using
      closedNeighborhood_signed_sum_zero color hcolor (16 : Vertex)
  have h17 : signed color 5 + signed color 13 + signed color 16 + signed color 17 +
      signed color 21 + signed color 22 = 0 := by
    simpa [closedNeighborhood, neighborSet, add_assoc, add_left_comm, add_comm] using
      closedNeighborhood_signed_sum_zero color hcolor (17 : Vertex)
  have h18 : signed color 6 + signed color 14 + signed color 17 + signed color 18 +
      signed color 22 + signed color 23 = 0 := by
    simpa [closedNeighborhood, neighborSet, add_assoc, add_left_comm, add_comm] using
      closedNeighborhood_signed_sum_zero color hcolor (18 : Vertex)
  have h19 : signed color 0 + signed color 7 + signed color 15 + signed color 18 +
      signed color 19 + signed color 23 = 0 := by
    simpa [closedNeighborhood, neighborSet, add_assoc, add_left_comm, add_comm] using
      closedNeighborhood_signed_sum_zero color hcolor (19 : Vertex)
  have h20 : signed color 0 + signed color 1 + signed color 8 + signed color 16 +
      signed color 19 + signed color 20 = 0 := by
    simpa [closedNeighborhood, neighborSet, add_assoc, add_left_comm, add_comm] using
      closedNeighborhood_signed_sum_zero color hcolor (20 : Vertex)
  have h21 : signed color 1 + signed color 2 + signed color 9 + signed color 17 +
      signed color 20 + signed color 21 = 0 := by
    simpa [closedNeighborhood, neighborSet, add_assoc, add_left_comm, add_comm] using
      closedNeighborhood_signed_sum_zero color hcolor (21 : Vertex)
  have h22 : signed color 2 + signed color 3 + signed color 10 + signed color 18 +
      signed color 21 + signed color 22 = 0 := by
    simpa [closedNeighborhood, neighborSet, add_assoc, add_left_comm, add_comm] using
      closedNeighborhood_signed_sum_zero color hcolor (22 : Vertex)
  have h23 : signed color 3 + signed color 4 + signed color 11 + signed color 19 +
      signed color 22 + signed color 23 = 0 := by
    simpa [closedNeighborhood, neighborSet, add_assoc, add_left_comm, add_comm] using
      closedNeighborhood_signed_sum_zero color hcolor (23 : Vertex)
  linarith [h0, h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11,
    h12, h13, h14, h15, h16, h17, h18, h19, h20, h21, h22, h23]

/-- No assignment of three signs from `{1,-1}` can sum to `0`. -/
theorem no_three_signs_sum_zero (color : Coloring) :
    signed color 0 + signed color 1 + signed color 2 ≠ 0 := by
  intro hsum
  cases h0 : color 0 <;> cases h1 : color 1 <;> cases h2 : color 2 <;>
    norm_num [signed, h0, h1, h2] at hsum

/-- Every exact candidate coloring fails the forced `0,1,2` signed-sum relation. -/
theorem no_coloring_works : ∀ color : Coloring, ¬ IsCNBColoring color := by
  intro color hcolor
  exact no_three_signs_sum_zero color (three_residue_sum_zero color hcolor)

/-- Expanded exact statement: there is no red/blue CNB-coloring of `C_24(4,5,12)`. -/
theorem c24_4_5_12_not_cnbc_explicit :
    ¬ ∃ color : Coloring,
      ∀ v, ((closedNeighborhood v).filter fun w => color w = Color.red).card = 3 := by
  intro hExists
  rcases hExists with ⟨color, hcolor⟩
  exact no_coloring_works color hcolor

/-- The quintic circulant `C_24(4,5,12)` does not admit a closed-neighborhood balanced coloring. -/
theorem c24_4_5_12_not_cnbc : exactCounterexampleStatement := by
  exact c24_4_5_12_not_cnbc_skeleton no_coloring_works

end C244512CNBC
end AutoMath
