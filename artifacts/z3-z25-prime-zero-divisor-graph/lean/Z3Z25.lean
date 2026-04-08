import Mathlib.Data.Fin.Basic
import Mathlib.Data.Fintype.Basic
import Mathlib.Data.Fintype.EquivFin
import Mathlib.Data.Fintype.Prod
import Mathlib.Data.Nat.GCD.Basic

namespace AutoMath
namespace Z3Z25

/-- Vertices of `Γ(Z_3 × Z_25)` are the nonzero zero-divisors of the product ring, encoded by
the standard representatives `(a, b)` with `a ∈ {0,1,2}` and `b ∈ {0, …, 24}`. -/
def IsVertex (x : Fin 3 × Fin 25) : Prop :=
  ((x.1.val ≠ 0) ∨ (x.2.val ≠ 0)) ∧ (x.1.val = 0 ∨ x.2.val % 5 = 0)

abbrev Vertex := {x : Fin 3 × Fin 25 // IsVertex x}

instance : DecidablePred IsVertex := by
  intro x
  unfold IsVertex
  infer_instance

instance : Fintype Vertex := Subtype.fintype IsVertex

def aCoord (x : Vertex) : Nat := x.1.1.val

def bCoord (x : Vertex) : Nat := x.1.2.val

/-- Adjacency in the simple zero-divisor graph: distinct vertices whose coordinatewise product is
zero in both factors. -/
def Adj (x y : Vertex) : Prop :=
  x ≠ y ∧ ((aCoord x * aCoord y) % 3 = 0) ∧ ((bCoord x * bCoord y) % 25 = 0)

/-- `Label` is the machine encoding of the mathematical label set `{1, …, 34}` via `i ↦ i + 1`. -/
abbrev Label := Fin 34

def labelValue (ℓ : Label) : Nat := ℓ.val.succ

def rawLabel (x : Fin 3 × Fin 25) : Label :=
  match x.1.val, x.2.val with
  | 0, 1 => ⟨5, by decide⟩
  | 0, 2 => ⟨8, by decide⟩
  | 0, 3 => ⟨9, by decide⟩
  | 0, 4 => ⟨11, by decide⟩
  | 0, 5 => ⟨0, by decide⟩
  | 0, 6 => ⟨13, by decide⟩
  | 0, 7 => ⟨14, by decide⟩
  | 0, 8 => ⟨17, by decide⟩
  | 0, 9 => ⟨18, by decide⟩
  | 0, 10 => ⟨2, by decide⟩
  | 0, 11 => ⟨19, by decide⟩
  | 0, 12 => ⟨20, by decide⟩
  | 0, 13 => ⟨22, by decide⟩
  | 0, 14 => ⟨23, by decide⟩
  | 0, 15 => ⟨4, by decide⟩
  | 0, 16 => ⟨24, by decide⟩
  | 0, 17 => ⟨26, by decide⟩
  | 0, 18 => ⟨27, by decide⟩
  | 0, 19 => ⟨28, by decide⟩
  | 0, 20 => ⟨6, by decide⟩
  | 0, 21 => ⟨29, by decide⟩
  | 0, 22 => ⟨30, by decide⟩
  | 0, 23 => ⟨31, by decide⟩
  | 0, 24 => ⟨32, by decide⟩
  | 1, 0 => ⟨12, by decide⟩
  | 1, 5 => ⟨1, by decide⟩
  | 1, 10 => ⟨3, by decide⟩
  | 1, 15 => ⟨7, by decide⟩
  | 1, 20 => ⟨10, by decide⟩
  | 2, 0 => ⟨16, by decide⟩
  | 2, 5 => ⟨15, by decide⟩
  | 2, 10 => ⟨21, by decide⟩
  | 2, 15 => ⟨25, by decide⟩
  | 2, 20 => ⟨33, by decide⟩
  | _, _ => ⟨0, by decide⟩

def label (x : Vertex) : Label := rawLabel x.1

theorem vertex_card : Fintype.card Vertex = 34 := by
  decide +kernel

theorem labelValue_bounds (ℓ : Label) : 1 ≤ labelValue ℓ ∧ labelValue ℓ ≤ 34 := by
  exact ⟨Nat.succ_le_succ (Nat.zero_le _), Nat.succ_le_of_lt ℓ.is_lt⟩

def EdgeCoprime (f : Vertex → Label) : Prop :=
  ∀ x y, Adj x y → Nat.Coprime (labelValue (f x)) (labelValue (f y))

def IsPrimeLabeling (f : Vertex → Label) : Prop :=
  Function.Bijective f ∧ EdgeCoprime f

theorem raw_label_injective_on_vertices :
    ∀ x y : Fin 3 × Fin 25, IsVertex x → IsVertex y → rawLabel x = rawLabel y → x = y := by
  decide +kernel

theorem raw_label_edgeCoprime :
    ∀ x y : Fin 3 × Fin 25,
      IsVertex x →
      IsVertex y →
      x ≠ y →
      (x.1.val * y.1.val) % 3 = 0 →
      (x.2.val * y.2.val) % 25 = 0 →
      Nat.Coprime (labelValue (rawLabel x)) (labelValue (rawLabel y)) := by
  decide +kernel

theorem label_injective : Function.Injective label := by
  intro x y hxy
  apply Subtype.ext
  exact raw_label_injective_on_vertices x.1 y.1 x.2 y.2 hxy

theorem label_edgeCoprime : EdgeCoprime label := by
  intro x y hxy
  rcases hxy with ⟨hne, h3, h25⟩
  have hne' : x.1 ≠ y.1 := fun h => hne (Subtype.ext h)
  exact raw_label_edgeCoprime x.1 y.1 x.2 y.2 hne' h3 h25

theorem z3_z25_zeroDivisorGraph_prime_checked : IsPrimeLabeling label := by
  refine ⟨?_, label_edgeCoprime⟩
  exact (Fintype.bijective_iff_injective_and_card label).2 ⟨label_injective, by simpa using vertex_card⟩

/-- Explicit natural-number form of the witness: the actual labels are the integers `{1, …, 34}`,
read from `Label` via `labelValue`. -/
theorem z3_z25_zeroDivisorGraph_prime_explicit :
    ∃ f : Vertex → Label,
      Function.Bijective f ∧
      (∀ x, 1 ≤ labelValue (f x) ∧ labelValue (f x) ≤ 34) ∧
      (∀ x y, Adj x y → Nat.Coprime (labelValue (f x)) (labelValue (f y))) := by
  refine ⟨label, ?_, ?_, ?_⟩
  exact z3_z25_zeroDivisorGraph_prime_checked.1
  intro x
  exact labelValue_bounds (label x)
  exact z3_z25_zeroDivisorGraph_prime_checked.2

/-- The zero-divisor graph `Γ(Z_3 × Z_25)` admits a prime labeling. Here `Label = Fin 34` is read
as the mathematical label set `{1, …, 34}` via `labelValue i = i + 1`. -/
theorem z3_z25_zeroDivisorGraph_prime : ∃ f : Vertex → Label, IsPrimeLabeling f := by
  exact ⟨label, z3_z25_zeroDivisorGraph_prime_checked⟩

end Z3Z25
end AutoMath
