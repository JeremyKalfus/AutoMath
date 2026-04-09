import Mathlib.Data.Fin.Basic
import Mathlib.Data.Fintype.Basic
import Mathlib.Data.Fintype.EquivFin
import Mathlib.Data.Fintype.Prod
import Mathlib.Data.Nat.GCD.Basic

namespace AutoMath
namespace Z7Z25

/-- Standard representatives for elements of `Z_7 × Z_25`. -/
abbrev Raw := Fin 7 × Fin 25

instance : DecidableEq Raw := inferInstance

instance : Fintype Raw := inferInstance

/-- Vertices of `Γ(Z_7 × Z_25)` are the nonzero zero-divisors of the product ring, encoded by the
standard representatives `(a, b)` with `a ∈ {0, …, 6}` and `b ∈ {0, …, 24}`. -/
def IsVertex (x : Raw) : Prop :=
  ((x.1.val ≠ 0) ∨ (x.2.val ≠ 0)) ∧ (x.1.val = 0 ∨ x.2.val % 5 = 0)

abbrev Vertex := {x : Raw // IsVertex x}

instance : DecidablePred IsVertex := by
  intro x
  unfold IsVertex
  infer_instance

instance : Fintype Vertex := Subtype.fintype IsVertex

def aCoordRaw (x : Raw) : Nat := x.1.val

def bCoordRaw (x : Raw) : Nat := x.2.val

def aCoord (x : Vertex) : Nat := aCoordRaw x.1

def bCoord (x : Vertex) : Nat := bCoordRaw x.1

/-- Adjacency in the simple zero-divisor graph: distinct vertices whose coordinatewise product is
zero in both factors. -/
def Adj (x y : Vertex) : Prop :=
  x ≠ y ∧ ((aCoord x * aCoord y) % 7 = 0) ∧ ((bCoord x * bCoord y) % 25 = 0)

/-- `Label` is the machine encoding of the mathematical label set `{1, …, 54}` via `i ↦ i + 1`. -/
abbrev Label := Fin 54

def labelValue (ℓ : Label) : Nat := ℓ.val.succ

def rawLabel (x : Raw) : Label :=
  match aCoordRaw x, bCoordRaw x with
  | 0, 1 => ⟨1, by decide⟩
  | 0, 2 => ⟨2, by decide⟩
  | 0, 3 => ⟨3, by decide⟩
  | 0, 4 => ⟨4, by decide⟩
  | 0, 5 => ⟨0, by decide⟩
  | 0, 6 => ⟨5, by decide⟩
  | 0, 7 => ⟨6, by decide⟩
  | 0, 8 => ⟨7, by decide⟩
  | 0, 9 => ⟨8, by decide⟩
  | 0, 10 => ⟨10, by decide⟩
  | 0, 11 => ⟨9, by decide⟩
  | 0, 12 => ⟨11, by decide⟩
  | 0, 13 => ⟨13, by decide⟩
  | 0, 14 => ⟨14, by decide⟩
  | 0, 15 => ⟨12, by decide⟩
  | 0, 16 => ⟨21, by decide⟩
  | 0, 17 => ⟨25, by decide⟩
  | 0, 18 => ⟨32, by decide⟩
  | 0, 19 => ⟨33, by decide⟩
  | 0, 20 => ⟨16, by decide⟩
  | 0, 21 => ⟨38, by decide⟩
  | 0, 22 => ⟨43, by decide⟩
  | 0, 23 => ⟨50, by decide⟩
  | 0, 24 => ⟨51, by decide⟩
  | 1, 0 => ⟨28, by decide⟩
  | 1, 5 => ⟨15, by decide⟩
  | 1, 10 => ⟨17, by decide⟩
  | 1, 15 => ⟨18, by decide⟩
  | 1, 20 => ⟨19, by decide⟩
  | 2, 0 => ⟨30, by decide⟩
  | 2, 5 => ⟨20, by decide⟩
  | 2, 10 => ⟨22, by decide⟩
  | 2, 15 => ⟨23, by decide⟩
  | 2, 20 => ⟨24, by decide⟩
  | 3, 0 => ⟨36, by decide⟩
  | 3, 5 => ⟨26, by decide⟩
  | 3, 10 => ⟨27, by decide⟩
  | 3, 15 => ⟨29, by decide⟩
  | 3, 20 => ⟨31, by decide⟩
  | 4, 0 => ⟨40, by decide⟩
  | 4, 5 => ⟨34, by decide⟩
  | 4, 10 => ⟨35, by decide⟩
  | 4, 15 => ⟨37, by decide⟩
  | 4, 20 => ⟨39, by decide⟩
  | 5, 0 => ⟨42, by decide⟩
  | 5, 5 => ⟨41, by decide⟩
  | 5, 10 => ⟨44, by decide⟩
  | 5, 15 => ⟨45, by decide⟩
  | 5, 20 => ⟨47, by decide⟩
  | 6, 0 => ⟨46, by decide⟩
  | 6, 5 => ⟨48, by decide⟩
  | 6, 10 => ⟨49, by decide⟩
  | 6, 15 => ⟨52, by decide⟩
  | 6, 20 => ⟨53, by decide⟩
  | _, _ => ⟨0, by decide⟩

def label (x : Vertex) : Label := rawLabel x.1

theorem vertex_card : Fintype.card Vertex = 54 := by
  decide +kernel

theorem labelValue_bounds (ℓ : Label) : 1 ≤ labelValue ℓ ∧ labelValue ℓ ≤ 54 := by
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
      (aCoordRaw x * aCoordRaw y) % 7 = 0 →
      (bCoordRaw x * bCoordRaw y) % 25 = 0 →
      Nat.Coprime (labelValue (rawLabel x)) (labelValue (rawLabel y)) := by
  decide +kernel

theorem label_injective : Function.Injective label := by
  intro x y hxy
  apply Subtype.ext
  exact raw_label_injective_on_vertices x.1 y.1 x.2 y.2 hxy

theorem label_edgeCoprime : EdgeCoprime label := by
  intro x y hxy
  rcases hxy with ⟨hne, h7, h25⟩
  have hne' : x.1 ≠ y.1 := fun h => hne (Subtype.ext h)
  exact raw_label_edgeCoprime x.1 y.1 x.2 y.2 hne' h7 h25

theorem z7_z25_zeroDivisorGraph_prime_checked : IsPrimeLabeling label := by
  refine ⟨?_, label_edgeCoprime⟩
  exact (Fintype.bijective_iff_injective_and_card label).2 ⟨label_injective, by
    simpa using vertex_card⟩

/-- Explicit natural-number form of the witness: the actual labels are the integers `{1, …, 54}`,
read from `Label` via `labelValue`. -/
theorem z7_z25_zeroDivisorGraph_prime_explicit :
    ∃ f : Vertex → Label,
      Function.Bijective f ∧
      (∀ x, 1 ≤ labelValue (f x) ∧ labelValue (f x) ≤ 54) ∧
      (∀ x y, Adj x y → Nat.Coprime (labelValue (f x)) (labelValue (f y))) := by
  refine ⟨label, ?_, ?_, ?_⟩
  exact z7_z25_zeroDivisorGraph_prime_checked.1
  intro x
  exact labelValue_bounds (label x)
  exact z7_z25_zeroDivisorGraph_prime_checked.2

/-- The zero-divisor graph `Γ(Z_7 × Z_25)` admits a prime labeling. Here `Label = Fin 54` is read
as the mathematical label set `{1, …, 54}` via `labelValue i = i + 1`. -/
theorem z7_z25_zeroDivisorGraph_prime : ∃ f : Vertex → Label, IsPrimeLabeling f := by
  exact ⟨label, z7_z25_zeroDivisorGraph_prime_checked⟩

end Z7Z25
end AutoMath
