import Mathlib

namespace AutoMath
namespace P4xP4GridPrimeLabeling

/-- Rows of the exact `4 x 4` grid `P_4 x P_4`. -/
abbrev Row := Fin 4

/-- Columns of the exact `4 x 4` grid `P_4 x P_4`. -/
abbrev Col := Fin 4

/-- Grid vertices are coordinates `(r,c)` with `r,c ∈ {0,1,2,3}`. -/
abbrev Vertex := Row × Col

/-- `Label = Fin 16` is read as the mathematical label set `{1,...,16}` via `labelValue`. -/
abbrev Label := Fin 16

def labelValue (ℓ : Label) : Nat := ℓ.val.succ

/-- Exact adjacency in `P_4 x P_4`: horizontal or vertical neighbors, equivalently
Manhattan distance `1`. -/
def Adj (v w : Vertex) : Prop :=
  Nat.dist v.1.val w.1.val + Nat.dist v.2.val w.2.val = 1

/-- Explicit witness copied from the verified artifact, in row-major order:

```
| 15 | 2  | 3  | 10 |
| 4  | 11 | 8  | 7  |
| 9  | 16 | 13 | 6  |
| 14 | 5  | 12 | 1  |
```

Since Lean uses zero-based `Fin`, each entry stores the corresponding label minus `1`. -/
def rawLabel : Vertex → Label
  | (⟨0, _⟩, ⟨0, _⟩) => ⟨14, by decide⟩
  | (⟨0, _⟩, ⟨1, _⟩) => ⟨1, by decide⟩
  | (⟨0, _⟩, ⟨2, _⟩) => ⟨2, by decide⟩
  | (⟨0, _⟩, ⟨3, _⟩) => ⟨9, by decide⟩
  | (⟨1, _⟩, ⟨0, _⟩) => ⟨3, by decide⟩
  | (⟨1, _⟩, ⟨1, _⟩) => ⟨10, by decide⟩
  | (⟨1, _⟩, ⟨2, _⟩) => ⟨7, by decide⟩
  | (⟨1, _⟩, ⟨3, _⟩) => ⟨6, by decide⟩
  | (⟨2, _⟩, ⟨0, _⟩) => ⟨8, by decide⟩
  | (⟨2, _⟩, ⟨1, _⟩) => ⟨15, by decide⟩
  | (⟨2, _⟩, ⟨2, _⟩) => ⟨12, by decide⟩
  | (⟨2, _⟩, ⟨3, _⟩) => ⟨5, by decide⟩
  | (⟨3, _⟩, ⟨0, _⟩) => ⟨13, by decide⟩
  | (⟨3, _⟩, ⟨1, _⟩) => ⟨4, by decide⟩
  | (⟨3, _⟩, ⟨2, _⟩) => ⟨11, by decide⟩
  | (⟨3, _⟩, ⟨3, _⟩) => ⟨0, by decide⟩

def label : Vertex → Label := rawLabel

theorem vertex_card : Fintype.card Vertex = 16 := by
  decide

theorem labelValue_bounds (ℓ : Label) : 1 ≤ labelValue ℓ ∧ labelValue ℓ ≤ 16 := by
  exact ⟨Nat.succ_le_succ (Nat.zero_le _), Nat.succ_le_of_lt ℓ.is_lt⟩

def EdgeCoprime (f : Vertex → Label) : Prop :=
  ∀ x y, Adj x y → Nat.Coprime (labelValue (f x)) (labelValue (f y))

def IsPrimeLabeling (f : Vertex → Label) : Prop :=
  Function.Bijective f ∧ EdgeCoprime f

def intendedStatement : Prop :=
  ∃ f : Vertex → Label, IsPrimeLabeling f

instance instDecidableAdj (v w : Vertex) : Decidable (Adj v w) := by
  unfold Adj
  infer_instance

instance instDecidableEdgeCoprime (f : Vertex → Label) : Decidable (EdgeCoprime f) := by
  unfold EdgeCoprime
  infer_instance

instance instDecidableIsPrimeLabeling (f : Vertex → Label) : Decidable (IsPrimeLabeling f) := by
  unfold IsPrimeLabeling
  infer_instance

instance : Decidable intendedStatement := by
  unfold intendedStatement
  infer_instance

/-- Exact theorem statement for the active slug. -/
theorem p4x_p4_grid_prime_statement :
    intendedStatement ↔
      ∃ f : Vertex → Label,
        Function.Bijective f ∧
          (∀ x y, Adj x y → Nat.Coprime (labelValue (f x)) (labelValue (f y))) := by
  rfl

/-- Faithfulness check: the Lean target is exactly the existence of a prime labeling on `P_4 x P_4`. -/
theorem intendedStatement_faithful :
    intendedStatement =
      ∃ f : Vertex → Label,
        Function.Bijective f ∧
          (∀ x y, Adj x y → Nat.Coprime (labelValue (f x)) (labelValue (f y))) := by
  rfl

/--
Proof skeleton for the exact theorem targeted in this slug:

```lean
theorem p4x_p4_grid_prime :
    intendedStatement := by
  refine p4x_p4_grid_prime_skeleton ?hbij ?hedge
```

The verified artifact already gives the candidate witness matrix; it remains to prove
that this exact witness is bijective and edge-coprime for the exact `P_4 x P_4`
adjacency relation.
-/
theorem p4x_p4_grid_prime_skeleton
    (hbij : Function.Bijective label)
    (hedge : EdgeCoprime label) :
    intendedStatement := by
  exact ⟨label, hbij, hedge⟩

/-- The Lean witness matches the verified `4 x 4` matrix from the record. -/
theorem witness_values_match_record :
    labelValue (label (⟨0, by decide⟩, ⟨0, by decide⟩)) = 15 ∧
      labelValue (label (⟨0, by decide⟩, ⟨1, by decide⟩)) = 2 ∧
      labelValue (label (⟨0, by decide⟩, ⟨2, by decide⟩)) = 3 ∧
      labelValue (label (⟨0, by decide⟩, ⟨3, by decide⟩)) = 10 ∧
      labelValue (label (⟨1, by decide⟩, ⟨0, by decide⟩)) = 4 ∧
      labelValue (label (⟨1, by decide⟩, ⟨1, by decide⟩)) = 11 ∧
      labelValue (label (⟨1, by decide⟩, ⟨2, by decide⟩)) = 8 ∧
      labelValue (label (⟨1, by decide⟩, ⟨3, by decide⟩)) = 7 ∧
      labelValue (label (⟨2, by decide⟩, ⟨0, by decide⟩)) = 9 ∧
      labelValue (label (⟨2, by decide⟩, ⟨1, by decide⟩)) = 16 ∧
      labelValue (label (⟨2, by decide⟩, ⟨2, by decide⟩)) = 13 ∧
      labelValue (label (⟨2, by decide⟩, ⟨3, by decide⟩)) = 6 ∧
      labelValue (label (⟨3, by decide⟩, ⟨0, by decide⟩)) = 14 ∧
      labelValue (label (⟨3, by decide⟩, ⟨1, by decide⟩)) = 5 ∧
      labelValue (label (⟨3, by decide⟩, ⟨2, by decide⟩)) = 12 ∧
      labelValue (label (⟨3, by decide⟩, ⟨3, by decide⟩)) = 1 := by
  decide

theorem label_bijective : Function.Bijective label := by
  decide

theorem label_edgeCoprime : EdgeCoprime label := by
  decide

theorem p4x_p4_grid_prime_checked : IsPrimeLabeling label := by
  exact ⟨label_bijective, label_edgeCoprime⟩

/-- Explicit natural-number form of the verified witness for the exact `P_4 x P_4` instance. -/
theorem p4x_p4_grid_prime_explicit :
    ∃ f : Vertex → Label,
      Function.Bijective f ∧
        (∀ x, 1 ≤ labelValue (f x) ∧ labelValue (f x) ≤ 16) ∧
        (∀ x y, Adj x y → Nat.Coprime (labelValue (f x)) (labelValue (f y))) := by
  refine ⟨label, label_bijective, ?_, label_edgeCoprime⟩
  intro x
  exact labelValue_bounds (label x)

/-- The `4 x 4` grid `P_4 x P_4` admits a prime labeling. -/
theorem p4x_p4_grid_prime : intendedStatement := by
  exact p4x_p4_grid_prime_skeleton label_bijective label_edgeCoprime

end P4xP4GridPrimeLabeling
end AutoMath
