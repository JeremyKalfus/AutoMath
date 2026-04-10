import Mathlib.Data.ZMod.Units
import AutoMath.Families.ZeroDivisorSupports

namespace AutoMath
namespace Families
namespace ZeroDivisorRingBridges

open ZeroDivisorSupports

/--
The ring-level carrier for the `Γ(Z_p × Z_p × Z_2)` family campaign.
The six support classes from `ZeroDivisorSupports.F2Support` are the six mixed
zero/nonzero coordinate patterns on these triples.
-/
abbrev F2RingElem (p : ℕ) := ZMod p × ZMod p × ZMod 2

/-- Ring-level realization of the six support classes for `Γ(Z_p × Z_p × Z_2)`. -/
def f2SupportPredicate {p : ℕ} : F2Support → F2RingElem p → Prop
  | .A, x => x.1 ≠ 0 ∧ x.2.1 = 0 ∧ x.2.2 = 0
  | .B, x => x.1 = 0 ∧ x.2.1 ≠ 0 ∧ x.2.2 = 0
  | .C, x => x.1 = 0 ∧ x.2.1 = 0 ∧ x.2.2 ≠ 0
  | .D, x => x.1 ≠ 0 ∧ x.2.1 ≠ 0 ∧ x.2.2 = 0
  | .E, x => x.1 ≠ 0 ∧ x.2.1 = 0 ∧ x.2.2 ≠ 0
  | .F, x => x.1 = 0 ∧ x.2.1 ≠ 0 ∧ x.2.2 ≠ 0

/-- The actual zero-divisor graph vertices: nonzero elements that annihilate a nonzero mate. -/
def f2ZeroDivisorVertex {p : ℕ} (x : F2RingElem p) : Prop :=
  x ≠ 0 ∧ ∃ y : F2RingElem p, y ≠ 0 ∧ x * y = 0

lemma f2SupportPredicate_ne_zero
    {p : ℕ} {s : F2Support} {x : F2RingElem p}
    (hx : f2SupportPredicate s x) :
    x ≠ 0 := by
  rcases s with _ <;> rcases hx with ⟨h1, h2, h3⟩ <;> intro hx0
  · exact h1 <| by simpa using congrArg Prod.fst hx0
  · exact h2 <| by simpa using congrArg (fun z => z.2.1) hx0
  · exact h3 <| by simpa using congrArg (fun z => z.2.2) hx0
  · exact h1 <| by simpa using congrArg Prod.fst hx0
  · exact h1 <| by simpa using congrArg Prod.fst hx0
  · exact h2 <| by simpa using congrArg (fun z => z.2.1) hx0

lemma f2ZeroDivisorVertex_of_supportPredicate
    {p : ℕ} [Fact p.Prime] {s : F2Support} {x : F2RingElem p}
    (hx : f2SupportPredicate s x) :
    f2ZeroDivisorVertex x := by
  refine ⟨f2SupportPredicate_ne_zero hx, ?_⟩
  rcases s with _ <;> rcases hx with ⟨h1, h2, h3⟩
  · refine ⟨(0, 0, 1), by simp, ?_⟩
    ext <;> simp [h2, h3]
  · refine ⟨(0, 0, 1), by simp, ?_⟩
    ext <;> simp [h1, h3]
  · refine ⟨(0, 1, 0), by simp, ?_⟩
    ext <;> simp [h1, h2]
  · refine ⟨(0, 0, 1), by simp, ?_⟩
    ext <;> simp [h3]
  · refine ⟨(0, 1, 0), by simp, ?_⟩
    ext <;> simp [h2]
  · refine ⟨(1, 0, 0), by simp, ?_⟩
    ext <;> simp [h1]

lemma f2SupportPredicate_of_vertex
    {p : ℕ} [Fact p.Prime] {x : F2RingElem p}
    (hx : f2ZeroDivisorVertex x) :
    f2SupportPredicate .A x ∨
      f2SupportPredicate .B x ∨
      f2SupportPredicate .C x ∨
      f2SupportPredicate .D x ∨
      f2SupportPredicate .E x ∨
      f2SupportPredicate .F x := by
  rcases hx with ⟨hx_ne_zero, y, hy_ne_zero, hxy⟩
  have hxy1 : x.1 * y.1 = 0 := by
    simpa using congrArg Prod.fst hxy
  have hxy2 : x.2.1 * y.2.1 = 0 := by
    simpa using congrArg (fun z => z.2.1) hxy
  have hxy3 : x.2.2 * y.2.2 = 0 := by
    simpa using congrArg (fun z => z.2.2) hxy
  have hnotAllNonzero : ¬ (x.1 ≠ 0 ∧ x.2.1 ≠ 0 ∧ x.2.2 ≠ 0) := by
    intro hall
    have hy1 : y.1 = 0 := (mul_eq_zero.mp hxy1).resolve_left hall.1
    have hy2 : y.2.1 = 0 := (mul_eq_zero.mp hxy2).resolve_left hall.2.1
    have hy3 : y.2.2 = 0 := (mul_eq_zero.mp hxy3).resolve_left hall.2.2
    apply hy_ne_zero
    ext <;> simp [hy1, hy2, hy3]
  by_cases hx1 : x.1 = 0
  · by_cases hx2 : x.2.1 = 0
    · by_cases hx3 : x.2.2 = 0
      · exfalso
        apply hx_ne_zero
        ext <;> simp [hx1, hx2, hx3]
      · exact Or.inr <| Or.inr <| Or.inl ⟨hx1, hx2, hx3⟩
    · by_cases hx3 : x.2.2 = 0
      · exact Or.inr <| Or.inl ⟨hx1, hx2, hx3⟩
      · exact Or.inr <| Or.inr <| Or.inr <| Or.inr <| Or.inr ⟨hx1, hx2, hx3⟩
  · by_cases hx2 : x.2.1 = 0
    · by_cases hx3 : x.2.2 = 0
      · exact Or.inl ⟨hx1, hx2, hx3⟩
      · exact Or.inr <| Or.inr <| Or.inr <| Or.inr <| Or.inl ⟨hx1, hx2, hx3⟩
    · by_cases hx3 : x.2.2 = 0
      · exact Or.inr <| Or.inr <| Or.inr <| Or.inl ⟨hx1, hx2, hx3⟩
      · exfalso
        exact hnotAllNonzero ⟨hx1, hx2, hx3⟩

/--
Ring-level support partition for the `Γ(Z_p × Z_p × Z_2)` family.
An element is a genuine nonzero zero-divisor vertex exactly when it lies in one
of the six support classes named by `F2Support`.
-/
theorem f2_ring_support_partition_lemma
    {p : ℕ} [Fact p.Prime] (x : F2RingElem p) :
    f2ZeroDivisorVertex x ↔
      f2SupportPredicate .A x ∨
      f2SupportPredicate .B x ∨
      f2SupportPredicate .C x ∨
      f2SupportPredicate .D x ∨
      f2SupportPredicate .E x ∨
      f2SupportPredicate .F x := by
  constructor
  · exact f2SupportPredicate_of_vertex
  · intro hx
    rcases hx with hA | hB | hC | hD | hE | hF
    · exact f2ZeroDivisorVertex_of_supportPredicate hA
    · exact f2ZeroDivisorVertex_of_supportPredicate hB
    · exact f2ZeroDivisorVertex_of_supportPredicate hC
    · exact f2ZeroDivisorVertex_of_supportPredicate hD
    · exact f2ZeroDivisorVertex_of_supportPredicate hE
    · exact f2ZeroDivisorVertex_of_supportPredicate hF

end ZeroDivisorRingBridges
end Families
end AutoMath
