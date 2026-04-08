import Mathlib.Data.Fin.Basic
import Mathlib.Data.Fintype.Basic
import Mathlib.Data.Fintype.EquivFin
import Mathlib.Data.Fintype.Prod
import Mathlib.Data.Nat.GCD.Basic

namespace AutoMath
namespace Z5Z5Z2

/-- Vertices of `Γ(Z_5 × Z_5 × Z_2)` are the nonzero zero-divisors of the product ring, encoded by
the standard representatives `(a, b, c)` with `a, b ∈ {0, …, 4}` and `c ∈ {0, 1}`. -/
abbrev Raw := Fin 5 × Fin 5 × Fin 2

instance : DecidableEq Raw := inferInstance

instance : Fintype Raw := inferInstance

def IsVertex (x : Raw) : Prop :=
  ((x.1.val ≠ 0) ∨ (x.2.1.val ≠ 0) ∨ (x.2.2.val ≠ 0)) ∧
    (x.1.val = 0 ∨ x.2.1.val = 0 ∨ x.2.2.val = 0)

abbrev Vertex := {x : Raw // IsVertex x}

instance : DecidablePred IsVertex := by
  intro x
  unfold IsVertex
  infer_instance

instance : Fintype Vertex := Subtype.fintype IsVertex

def aCoordRaw (x : Raw) : Nat := x.1.val

def bCoordRaw (x : Raw) : Nat := x.2.1.val

def cCoordRaw (x : Raw) : Nat := x.2.2.val

def aCoord (x : Vertex) : Nat := aCoordRaw x.1

def bCoord (x : Vertex) : Nat := bCoordRaw x.1

def cCoord (x : Vertex) : Nat := cCoordRaw x.1

/-- Adjacency in the simple zero-divisor graph: distinct vertices whose coordinatewise product is
zero in all three factors. -/
def Adj (x y : Vertex) : Prop :=
  x ≠ y ∧
    ((aCoord x * aCoord y) % 5 = 0) ∧
    ((bCoord x * bCoord y) % 5 = 0) ∧
    ((cCoord x * cCoord y) % 2 = 0)

/-- `Label` is the machine encoding of the mathematical label set `{1, …, 33}` via `i ↦ i + 1`. -/
abbrev Label := Fin 33

def labelValue (ℓ : Label) : Nat := ℓ.val.succ

def rawLabel (x : Raw) : Label :=
  match aCoordRaw x, bCoordRaw x, cCoordRaw x with
  | 1, 0, 0 => ⟨1, by decide⟩
  | 2, 0, 0 => ⟨3, by decide⟩
  | 3, 0, 0 => ⟨7, by decide⟩
  | 4, 0, 0 => ⟨15, by decide⟩
  | 0, 1, 0 => ⟨2, by decide⟩
  | 0, 2, 0 => ⟨4, by decide⟩
  | 0, 3, 0 => ⟨8, by decide⟩
  | 0, 4, 0 => ⟨24, by decide⟩
  | 0, 0, 1 => ⟨0, by decide⟩
  | 1, 1, 0 => ⟨5, by decide⟩
  | 1, 2, 0 => ⟨9, by decide⟩
  | 1, 3, 0 => ⟨11, by decide⟩
  | 1, 4, 0 => ⟨14, by decide⟩
  | 2, 1, 0 => ⟨17, by decide⟩
  | 2, 2, 0 => ⟨18, by decide⟩
  | 2, 3, 0 => ⟨19, by decide⟩
  | 2, 4, 0 => ⟨20, by decide⟩
  | 3, 1, 0 => ⟨22, by decide⟩
  | 3, 2, 0 => ⟨23, by decide⟩
  | 3, 3, 0 => ⟨26, by decide⟩
  | 3, 4, 0 => ⟨27, by decide⟩
  | 4, 1, 0 => ⟨28, by decide⟩
  | 4, 2, 0 => ⟨29, by decide⟩
  | 4, 3, 0 => ⟨30, by decide⟩
  | 4, 4, 0 => ⟨32, by decide⟩
  | 1, 0, 1 => ⟨13, by decide⟩
  | 2, 0, 1 => ⟨21, by decide⟩
  | 3, 0, 1 => ⟨25, by decide⟩
  | 4, 0, 1 => ⟨31, by decide⟩
  | 0, 1, 1 => ⟨6, by decide⟩
  | 0, 2, 1 => ⟨10, by decide⟩
  | 0, 3, 1 => ⟨12, by decide⟩
  | 0, 4, 1 => ⟨16, by decide⟩
  | _, _, _ => ⟨0, by decide⟩

def label (x : Vertex) : Label := rawLabel x.1

theorem vertex_card : Fintype.card Vertex = 33 := by
  decide +kernel

theorem labelValue_bounds (ℓ : Label) : 1 ≤ labelValue ℓ ∧ labelValue ℓ ≤ 33 := by
  exact ⟨Nat.succ_le_succ (Nat.zero_le _), Nat.succ_le_of_lt ℓ.is_lt⟩

def EdgeCoprime (f : Vertex → Label) : Prop :=
  ∀ x y, Adj x y → Nat.Coprime (labelValue (f x)) (labelValue (f y))

def IsPrimeLabeling (f : Vertex → Label) : Prop :=
  Function.Bijective f ∧ EdgeCoprime f

theorem raw_label_injective_on_vertices :
    ∀ x y : Raw, IsVertex x → IsVertex y → rawLabel x = rawLabel y → x = y := by
  decide +kernel

theorem raw_label_edgeCoprime :
    ∀ x y : Raw,
      IsVertex x →
      IsVertex y →
      x ≠ y →
      (aCoordRaw x * aCoordRaw y) % 5 = 0 →
      (bCoordRaw x * bCoordRaw y) % 5 = 0 →
      (cCoordRaw x * cCoordRaw y) % 2 = 0 →
      Nat.Coprime (labelValue (rawLabel x)) (labelValue (rawLabel y)) := by
  decide +kernel

theorem label_injective : Function.Injective label := by
  intro x y hxy
  apply Subtype.ext
  exact raw_label_injective_on_vertices x.1 y.1 x.2 y.2 hxy

theorem label_edgeCoprime : EdgeCoprime label := by
  intro x y hxy
  rcases hxy with ⟨hne, h5a, h5b, h2⟩
  have hne' : x.1 ≠ y.1 := fun h => hne (Subtype.ext h)
  exact raw_label_edgeCoprime x.1 y.1 x.2 y.2 hne' h5a h5b h2

theorem z5_z5_z2_zeroDivisorGraph_prime_checked : IsPrimeLabeling label := by
  refine ⟨?_, label_edgeCoprime⟩
  exact (Fintype.bijective_iff_injective_and_card label).2 ⟨label_injective, by
    simpa using vertex_card⟩

/-- Explicit natural-number form of the witness: the actual labels are the integers `{1, …, 33}`,
read from `Label` via `labelValue`. -/
theorem z5_z5_z2_zeroDivisorGraph_prime_explicit :
    ∃ f : Vertex → Label,
      Function.Bijective f ∧
      (∀ x, 1 ≤ labelValue (f x) ∧ labelValue (f x) ≤ 33) ∧
      (∀ x y, Adj x y → Nat.Coprime (labelValue (f x)) (labelValue (f y))) := by
  refine ⟨label, ?_, ?_, ?_⟩
  exact z5_z5_z2_zeroDivisorGraph_prime_checked.1
  intro x
  exact labelValue_bounds (label x)
  exact z5_z5_z2_zeroDivisorGraph_prime_checked.2

/-- The zero-divisor graph `Γ(Z_5 × Z_5 × Z_2)` admits a prime labeling. Here `Label = Fin 33` is
read as the mathematical label set `{1, …, 33}` via `labelValue i = i + 1`. -/
theorem z5_z5_z2_zeroDivisorGraph_prime : ∃ f : Vertex → Label, IsPrimeLabeling f := by
  exact ⟨label, z5_z5_z2_zeroDivisorGraph_prime_checked⟩

end Z5Z5Z2
end AutoMath
