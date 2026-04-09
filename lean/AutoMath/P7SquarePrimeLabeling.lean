import Mathlib

namespace AutoMath
namespace P7SquarePrimeLabeling

/-- Vertices of the exact graph instance `P_7^2`, encoded in path order as `0,1,...,6`
corresponding to `v_1,...,v_7`. -/
abbrev Vertex := Fin 7

/-- `Label = Fin 7` is read as the mathematical label set `{1,...,7}` via `labelValue i = i + 1`. -/
abbrev Label := Fin 7

def labelValue (ℓ : Label) : Nat := ℓ.val.succ

/-- Adjacency in the square of the seven-vertex path: two distinct path positions are adjacent
exactly when their path distance is at most `2`. -/
def Adj (v w : Vertex) : Prop :=
  v ≠ w ∧ Nat.dist v.val w.val ≤ 2

/-- Explicit witness copied from the verified artifact:
`(6,1,5,2,3,7,4)` on `v_1,...,v_7`. Since Lean uses zero-based `Fin 7`,
this is the permutation `0 ↦ 5, 1 ↦ 0, 2 ↦ 4, 3 ↦ 1, 4 ↦ 2, 5 ↦ 6, 6 ↦ 3`. -/
def rawLabel : Vertex → Label
  | ⟨0, _⟩ => ⟨5, by decide⟩
  | ⟨1, _⟩ => ⟨0, by decide⟩
  | ⟨2, _⟩ => ⟨4, by decide⟩
  | ⟨3, _⟩ => ⟨1, by decide⟩
  | ⟨4, _⟩ => ⟨2, by decide⟩
  | ⟨5, _⟩ => ⟨6, by decide⟩
  | ⟨6, _⟩ => ⟨3, by decide⟩

def label : Vertex → Label := rawLabel

theorem vertex_card : Fintype.card Vertex = 7 := by
  decide

theorem labelValue_bounds (ℓ : Label) : 1 ≤ labelValue ℓ ∧ labelValue ℓ ≤ 7 := by
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
theorem p7_square_prime_statement :
    intendedStatement ↔
      ∃ f : Vertex → Label,
        Function.Bijective f ∧
          (∀ x y, Adj x y → Nat.Coprime (labelValue (f x)) (labelValue (f y))) := by
  rfl

/-- Faithfulness check: the Lean target is exactly the existence of a prime labeling for `P_7^2`. -/
theorem intendedStatement_faithful :
    intendedStatement =
      ∃ f : Vertex → Label,
        Function.Bijective f ∧
          (∀ x y, Adj x y → Nat.Coprime (labelValue (f x)) (labelValue (f y))) := by
  rfl

/--
Proof skeleton for the exact theorem targeted in this slug:

```lean
theorem p7_square_prime :
    intendedStatement := by
  refine p7_square_prime_skeleton ?hbij ?hedge
```

The verified artifact already gives the candidate witness `(6,1,5,2,3,7,4)`;
it remains to prove that this witness is bijective and edge-coprime for the exact
adjacency relation of `P_7^2`.
-/
theorem p7_square_prime_skeleton
    (hbij : Function.Bijective label)
    (hedge : EdgeCoprime label) :
    intendedStatement := by
  exact ⟨label, hbij, hedge⟩

/-- The Lean witness matches the verified path-order labeling `(6,1,5,2,3,7,4)`. -/
theorem witness_values_match_record :
    labelValue (label ⟨0, by decide⟩) = 6 ∧
      labelValue (label ⟨1, by decide⟩) = 1 ∧
      labelValue (label ⟨2, by decide⟩) = 5 ∧
      labelValue (label ⟨3, by decide⟩) = 2 ∧
      labelValue (label ⟨4, by decide⟩) = 3 ∧
      labelValue (label ⟨5, by decide⟩) = 7 ∧
      labelValue (label ⟨6, by decide⟩) = 4 := by
  decide

theorem label_injective : Function.Injective label := by
  decide

theorem label_edgeCoprime : EdgeCoprime label := by
  decide

theorem p7_square_prime_checked : IsPrimeLabeling label := by
  refine ⟨?_, label_edgeCoprime⟩
  have hcard : Fintype.card Vertex = Fintype.card Label := by
    decide
  exact
    (Fintype.bijective_iff_injective_and_card label).2
      ⟨label_injective, hcard⟩

/-- Explicit natural-number form of the verified witness for the exact `P_7^2` instance. -/
theorem p7_square_prime_explicit :
    ∃ f : Vertex → Label,
      Function.Bijective f ∧
        (∀ x, 1 ≤ labelValue (f x) ∧ labelValue (f x) ≤ 7) ∧
        (∀ x y, Adj x y → Nat.Coprime (labelValue (f x)) (labelValue (f y))) := by
  refine ⟨label, ?_, ?_, ?_⟩
  exact p7_square_prime_checked.1
  intro x
  exact labelValue_bounds (label x)
  exact p7_square_prime_checked.2

/-- The square of the seven-vertex path admits a prime labeling. -/
theorem p7_square_prime : intendedStatement := by
  exact p7_square_prime_skeleton p7_square_prime_checked.1 p7_square_prime_checked.2

end P7SquarePrimeLabeling
end AutoMath
