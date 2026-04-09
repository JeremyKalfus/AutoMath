import Mathlib

namespace AutoMath
namespace NorineQ7Variant

inductive Color where
  | red
  | blue
deriving DecidableEq, Repr

abbrev Vertex := Fin 7 → Bool

def zeroCoord : Fin 7 := ⟨0, by decide⟩
def oneCoord : Fin 7 := ⟨1, by decide⟩

def antipode (x : Vertex) : Vertex := fun i => !(x i)

/-- `x` and `y` differ in exactly the coordinate `i`. -/
def EdgeInDim (i : Fin 7) (x y : Vertex) : Prop :=
  y i = !(x i) ∧ ∀ j, j ≠ i → y j = x j

/-- The explicit solve-stage witness: red in dimension `0`, blue in the other six dimensions. -/
def witnessColor (i : Fin 7) : Color :=
  if i = zeroCoord then Color.red else Color.blue

def Step (color : Fin 7 → Color) (c : Color) (x y : Vertex) : Prop :=
  ∃ i, color i = c ∧ EdgeInDim i x y

abbrev MonoPath (color : Fin 7 → Color) (c : Color) : Vertex → Vertex → Prop :=
  Relation.ReflTransGen (Step color c)

theorem witnessColor_eq_red_iff {i : Fin 7} : witnessColor i = Color.red ↔ i = zeroCoord := by
  by_cases h : i = zeroCoord
  · simp [witnessColor, h]
  · simp [witnessColor, h]

theorem witnessColor_eq_blue_iff {i : Fin 7} : witnessColor i = Color.blue ↔ i ≠ zeroCoord := by
  by_cases h : i = zeroCoord
  · simp [witnessColor, h]
  · simp [witnessColor, h]

theorem bool_flip_ne (b : Bool) : (!b) ≠ b := by
  cases b <;> decide

theorem edgeInDim_symm {i : Fin 7} {x y : Vertex} (h : EdgeInDim i x y) : EdgeInDim i y x := by
  rcases h with ⟨hi, hrest⟩
  refine ⟨?_, ?_⟩
  · cases hx : x i <;> cases hy : y i <;> simp [hx, hy] at hi ⊢
  · intro j hj
    symm
    exact hrest j hj

theorem antipode_preserves_edgeInDim {i : Fin 7} {x y : Vertex} (h : EdgeInDim i x y) :
    EdgeInDim i (antipode x) (antipode y) := by
  rcases h with ⟨hi, hrest⟩
  refine ⟨?_, ?_⟩
  · simp [antipode, hi]
  · intro j hj
    simp [antipode, hrest j hj]

theorem redStep_is_zero {x y : Vertex} (h : Step witnessColor Color.red x y) :
    EdgeInDim zeroCoord x y := by
  rcases h with ⟨i, hcolor, hedge⟩
  exact (witnessColor_eq_red_iff.mp hcolor).symm ▸ hedge

theorem blueStep_preserves_zero {x y : Vertex} (h : Step witnessColor Color.blue x y) :
    y zeroCoord = x zeroCoord := by
  rcases h with ⟨i, hcolor, hedge⟩
  have hi : i ≠ zeroCoord := witnessColor_eq_blue_iff.mp hcolor
  have hzero : zeroCoord ≠ i := by
    intro hEq
    exact hi hEq.symm
  exact hedge.2 zeroCoord hzero

theorem redStep_preserves_other {x y : Vertex} {j : Fin 7} (hj : j ≠ zeroCoord)
    (h : Step witnessColor Color.red x y) : y j = x j := by
  exact (redStep_is_zero h).2 j hj

theorem redPath_preserves_other {x y : Vertex} (h : MonoPath witnessColor Color.red x y) :
    ∀ j, j ≠ zeroCoord → y j = x j := by
  induction h with
  | refl =>
      intro j hj
      rfl
  | tail hpath hstep ih =>
      intro j hj
      exact (redStep_preserves_other hj hstep).trans (ih j hj)

theorem bluePath_preserves_zero {x y : Vertex} (h : MonoPath witnessColor Color.blue x y) :
    y zeroCoord = x zeroCoord := by
  induction h with
  | refl =>
      rfl
  | tail hpath hstep ih =>
      exact (blueStep_preserves_zero hstep).trans ih

theorem antipode_coord_ne (x : Vertex) (i : Fin 7) : antipode x i ≠ x i := by
  unfold antipode
  exact bool_flip_ne (x i)

theorem no_red_antipodal_path (x : Vertex) :
    ¬ MonoPath witnessColor Color.red x (antipode x) := by
  intro h
  have hpres := redPath_preserves_other h oneCoord (by decide : oneCoord ≠ zeroCoord)
  exact antipode_coord_ne x oneCoord hpres

theorem no_blue_antipodal_path (x : Vertex) :
    ¬ MonoPath witnessColor Color.blue x (antipode x) := by
  intro h
  have hpres := bluePath_preserves_zero h
  exact antipode_coord_ne x zeroCoord hpres

/--
Lean-checked version of the explicit counterexample from the artifact:

- red edges are exactly the dimension-`0` edges;
- blue edges are exactly the dimension-`1` through dimension-`6` edges;
- antipodal edges remain in the same dimension;
- neither color admits a path from any vertex to its antipode.

This formalizes the copied statement from the repo artifact, not the canonical Norine conjecture.
-/
theorem norine_q7_variant_counterexample :
    ∃ color : Fin 7 → Color,
      (∀ {i x y}, EdgeInDim i x y → EdgeInDim i (antipode x) (antipode y)) ∧
      (∀ x, ¬ MonoPath color Color.red x (antipode x)) ∧
      (∀ x, ¬ MonoPath color Color.blue x (antipode x)) := by
  refine ⟨witnessColor, ?_, ?_, ?_⟩
  · intro i x y h
    exact antipode_preserves_edgeInDim h
  · intro x
    exact no_red_antipodal_path x
  · intro x
    exact no_blue_antipodal_path x

end NorineQ7Variant
end AutoMath
