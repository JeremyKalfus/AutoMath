import Mathlib.Algebra.Field.ZMod
import Mathlib.Data.ZMod.Units
import Mathlib.Tactic
import AutoMath.Families.ZeroDivisorReductions
import AutoMath.Families.ZeroDivisorSupports

namespace AutoMath
namespace Families
namespace ZeroDivisorRingBridges

open ZeroDivisorSupports

/--
The ring-level carrier for the `Γ(Z_p × Z_25)` family campaign.
The four support classes from `ZeroDivisorSupports.F25Support` are the four mixed
zero / nonzero-multiple-of-`5` / unit patterns on these pairs.
-/
abbrev F25RingElem (p : ℕ) := ZMod p × ZMod 25

/-- Nonzero multiples of `5` in `ZMod 25`. These are the nonzero zero-divisors of the second
coordinate ring. -/
def z25NonzeroFive (b : ZMod 25) : Prop :=
  b ≠ 0 ∧ 5 ∣ b.val

/-- Nonzero elements of `ZMod 25` that are not multiples of `5`; these are exactly the units. -/
def z25UnitSupport (b : ZMod 25) : Prop :=
  b ≠ 0 ∧ ¬ 5 ∣ b.val

/-- Ring-level realization of the four support classes for `Γ(Z_p × Z_25)`. -/
def f25SupportPredicate {p : ℕ} : F25Support → F25RingElem p → Prop
  | .A, x => x.1 = 0 ∧ z25UnitSupport x.2
  | .B, x => x.1 = 0 ∧ z25NonzeroFive x.2
  | .C, x => x.1 ≠ 0 ∧ x.2 = 0
  | .D, x => x.1 ≠ 0 ∧ z25NonzeroFive x.2

/-- The actual zero-divisor graph vertices: nonzero elements that annihilate a nonzero mate. -/
def f25ZeroDivisorVertex {p : ℕ} (x : F25RingElem p) : Prop :=
  x ≠ 0 ∧ ∃ y : F25RingElem p, y ≠ 0 ∧ x * y = 0

lemma f25_mul_eq_zero_iff
    {p : ℕ} (x y : F25RingElem p) :
    x * y = 0 ↔ x.1 * y.1 = 0 ∧ x.2 * y.2 = 0 := by
  constructor
  · intro h
    refine ⟨?_, ?_⟩
    · simpa using congrArg Prod.fst h
    · simpa using congrArg Prod.snd h
  · rintro ⟨h1, h2⟩
    ext <;> simp [h1, h2]

lemma z25_support_trichotomy (b : ZMod 25) :
    b = 0 ∨ z25NonzeroFive b ∨ z25UnitSupport b := by
  by_cases hb : b = 0
  · exact Or.inl hb
  · by_cases hfive : 5 ∣ b.val
    · exact Or.inr <| Or.inl ⟨hb, hfive⟩
    · exact Or.inr <| Or.inr ⟨hb, hfive⟩

lemma z25_nonzeroFive_mul_five_eq_zero
    (b : ZMod 25) (hb : z25NonzeroFive b) :
    b * (5 : ZMod 25) = 0 := by
  rcases hb with ⟨_, ⟨k, hk⟩⟩
  rw [← ZMod.natCast_zmod_val b, hk, Nat.cast_mul, Nat.cast_ofNat]
  have hfive : ((5 : ZMod 25) * 5) = 0 := by decide
  calc
    (5 : ZMod 25) * ↑k * 5 = ((5 : ZMod 25) * 5) * ↑k := by ac_rfl
    _ = 0 * ↑k := by rw [hfive]
    _ = 0 := by simp

lemma z25_unitSupport_mul_eq_zero
    (b c : ZMod 25) (hb : z25UnitSupport b) (hbc : b * c = 0) :
    c = 0 := by
  have hcop : Nat.Coprime b.val 25 := by
    simpa using (show Nat.Coprime b.val (5 ^ 2) from
      (by decide : Nat.Prime 5).coprime_pow_of_not_dvd (m := 2) hb.2)
  have hUnitCast : IsUnit ((b.val : ℕ) : ZMod 25) :=
    (ZMod.isUnit_iff_coprime b.val 25).2 hcop
  have hUnit : IsUnit b := by
    simpa [ZMod.natCast_zmod_val b] using hUnitCast
  exact (IsUnit.mul_right_eq_zero hUnit).1 hbc

lemma f25SupportPredicate_ne_zero
    {p : ℕ} {s : F25Support} {x : F25RingElem p}
    (hx : f25SupportPredicate s x) :
    x ≠ 0 := by
  cases s <;> simp [f25SupportPredicate, z25NonzeroFive, z25UnitSupport] at hx
  all_goals
    intro hx0
  · exact hx.2.1 <| by simpa using congrArg Prod.snd hx0
  · exact hx.2.1 <| by simpa using congrArg Prod.snd hx0
  · exact hx.1 <| by simpa using congrArg Prod.fst hx0
  · exact hx.1 <| by simpa using congrArg Prod.fst hx0

lemma f25ZeroDivisorVertex_of_supportPredicate
    {p : ℕ} [Fact p.Prime] {s : F25Support} {x : F25RingElem p}
    (hx : f25SupportPredicate s x) :
    f25ZeroDivisorVertex x := by
  refine ⟨f25SupportPredicate_ne_zero hx, ?_⟩
  cases s <;> simp [f25SupportPredicate] at hx
  · refine ⟨((1 : ZMod p), (0 : ZMod 25)), ?_, ?_⟩
    · intro h
      have h1 : (1 : ZMod p) = 0 := by simpa using congrArg Prod.fst h
      have h0 : (0 : ZMod p) = 1 := by simpa using h1.symm
      exact zero_ne_one h0
    rcases hx with ⟨h1, h2⟩
    ext <;> simp [h1]
  · refine ⟨((1 : ZMod p), (0 : ZMod 25)), ?_, ?_⟩
    · intro h
      have h1 : (1 : ZMod p) = 0 := by simpa using congrArg Prod.fst h
      have h0 : (0 : ZMod p) = 1 := by simpa using h1.symm
      exact zero_ne_one h0
    rcases hx with ⟨h1, h2⟩
    ext <;> simp [h1]
  · refine ⟨((0 : ZMod p), (1 : ZMod 25)), ?_, ?_⟩
    · intro h
      have h1 : (1 : ZMod 25) = 0 := by simpa using congrArg Prod.snd h
      exact (show (1 : ZMod 25) ≠ 0 by decide) h1
    rcases hx with ⟨h1, h2⟩
    ext <;> simp [h2]
  · refine ⟨((0 : ZMod p), (5 : ZMod 25)), ?_, ?_⟩
    · intro h
      have h5 : (5 : ZMod 25) = 0 := by simpa using congrArg Prod.snd h
      exact (show (5 : ZMod 25) ≠ 0 by decide) h5
    rcases hx with ⟨h1, h2⟩
    ext
    · simp
    · exact z25_nonzeroFive_mul_five_eq_zero x.2 h2

lemma f25SupportPredicate_of_vertex
    {p : ℕ} [Fact p.Prime] {x : F25RingElem p}
    (hx : f25ZeroDivisorVertex x) :
    f25SupportPredicate .A x ∨
      f25SupportPredicate .B x ∨
      f25SupportPredicate .C x ∨
      f25SupportPredicate .D x := by
  rcases hx with ⟨hx_ne_zero, y, hy_ne_zero, hxy⟩
  have hxy1 : x.1 * y.1 = 0 := by
    simpa using congrArg Prod.fst hxy
  have hxy2 : x.2 * y.2 = 0 := by
    simpa using congrArg Prod.snd hxy
  by_cases hx1 : x.1 = 0
  · have hx2_ne : x.2 ≠ 0 := by
      intro hx2
      apply hx_ne_zero
      ext <;> simp [hx1, hx2]
    rcases z25_support_trichotomy x.2 with hx2 | hx2 | hx2
    · exact False.elim (hx2_ne hx2)
    · exact Or.inr <| Or.inl ⟨hx1, hx2⟩
    · exact Or.inl ⟨hx1, hx2⟩
  · have hy1 : y.1 = 0 := (mul_eq_zero.mp hxy1).resolve_left hx1
    rcases z25_support_trichotomy x.2 with hx2 | hx2 | hx2
    · exact Or.inr <| Or.inr <| Or.inl ⟨hx1, hx2⟩
    · exact Or.inr <| Or.inr <| Or.inr ⟨hx1, hx2⟩
    · have hy2 : y.2 = 0 := z25_unitSupport_mul_eq_zero x.2 y.2 hx2 hxy2
      apply False.elim
      apply hy_ne_zero
      ext <;> simp [hy1, hy2]

/--
Ring-level support partition for the `Γ(Z_p × Z_25)` family.
An element is a genuine nonzero zero-divisor vertex exactly when it lies in one
of the four support classes named by `F25Support`.
-/
theorem f25_ring_support_partition_lemma
    {p : ℕ} [Fact p.Prime] (x : F25RingElem p) :
    f25ZeroDivisorVertex x ↔
      f25SupportPredicate .A x ∨
      f25SupportPredicate .B x ∨
      f25SupportPredicate .C x ∨
      f25SupportPredicate .D x := by
  constructor
  · exact f25SupportPredicate_of_vertex
  · intro hx
    rcases hx with hA | hB | hC | hD
    · exact f25ZeroDivisorVertex_of_supportPredicate hA
    · exact f25ZeroDivisorVertex_of_supportPredicate hB
    · exact f25ZeroDivisorVertex_of_supportPredicate hC
    · exact f25ZeroDivisorVertex_of_supportPredicate hD

lemma z25_nonzeroFive_mul_nonzeroFive_eq_zero
    (b c : ZMod 25) (hb : z25NonzeroFive b) (hc : z25NonzeroFive c) :
    b * c = 0 := by
  rcases hc with ⟨_, ⟨k, hk⟩⟩
  rw [← ZMod.natCast_zmod_val c, hk, Nat.cast_mul, Nat.cast_ofNat]
  calc
    b * ((5 : ZMod 25) * ↑k) = (b * 5) * ↑k := by ac_rfl
    _ = 0 * ↑k := by rw [z25_nonzeroFive_mul_five_eq_zero b hb]
    _ = 0 := by simp

lemma z25_unitSupport_mul_eq_zero_iff
    (b c : ZMod 25) (hb : z25UnitSupport b) :
    b * c = 0 ↔ c = 0 := by
  constructor
  · exact z25_unitSupport_mul_eq_zero b c hb
  · intro hc
    simp [hc]

lemma z25_mul_unitSupport_eq_zero_iff
    (b c : ZMod 25) (hc : z25UnitSupport c) :
    b * c = 0 ↔ b = 0 := by
  simpa [mul_comm] using z25_unitSupport_mul_eq_zero_iff c b hc

/--
Ring-level adjacency bridge for the `Γ(Z_p × Z_25)` family.
Once two ring elements are known to occupy support classes `s` and `t`, their
zero-product relation is exactly the abstract support adjacency relation on
`F25Support`.
-/
theorem f25_ring_support_adjacency_lemma
    {p : ℕ} [Fact p.Prime] {s t : F25Support} {x y : F25RingElem p}
    (hx : f25SupportPredicate s x)
    (hy : f25SupportPredicate t y) :
    x * y = 0 ↔ f25SupportAdj s t := by
  cases s <;> cases t <;>
    simp_all [f25_mul_eq_zero_iff, f25SupportPredicate, f25SupportAdj,
      f25FirstCoordSupport, f25SecondCoordSupport, fieldCoordZeroMulB,
      z25CoordZeroMulB, z25NonzeroFive, z25UnitSupport,
      z25_nonzeroFive_mul_nonzeroFive_eq_zero,
      z25_unitSupport_mul_eq_zero_iff, z25_mul_unitSupport_eq_zero_iff]

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

lemma f2_mul_eq_zero_iff
    {p : ℕ} (x y : F2RingElem p) :
    x * y = 0 ↔ x.1 * y.1 = 0 ∧ x.2.1 * y.2.1 = 0 ∧ x.2.2 * y.2.2 = 0 := by
  constructor
  · intro h
    refine ⟨?_, ?_, ?_⟩
    · simpa using congrArg Prod.fst h
    · simpa using congrArg (fun z => z.2.1) h
    · simpa using congrArg (fun z => z.2.2) h
  · rintro ⟨h1, h2, h3⟩
    ext <;> simp [h1, h2, h3]

lemma f2SupportPredicate_ne_zero
    {p : ℕ} {s : F2Support} {x : F2RingElem p}
    (hx : f2SupportPredicate s x) :
    x ≠ 0 := by
  cases s <;> simp [f2SupportPredicate] at hx
  all_goals
    rcases hx with ⟨h1, h2, h3⟩
    intro hx0
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
  cases s <;> simp [f2SupportPredicate] at hx
  all_goals rcases hx with ⟨h1, h2, h3⟩
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
    letI : Fact (Nat.Prime 2) := ⟨by decide⟩
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

/--
Ring-level adjacency bridge for the `Γ(Z_p × Z_p × Z_2)` family.
Once two ring elements are known to occupy support classes `s` and `t`, their
zero-product relation is exactly the abstract support adjacency relation on
`F2Support`.
-/
theorem f2_ring_support_adjacency_lemma
    {p : ℕ} [Fact p.Prime] {s t : F2Support} {x y : F2RingElem p}
    (hx : f2SupportPredicate s x)
    (hy : f2SupportPredicate t y) :
    x * y = 0 ↔ f2SupportAdj s t := by
  letI : Fact (Nat.Prime 2) := ⟨by decide⟩
  cases s <;> cases t <;>
    simp_all [f2_mul_eq_zero_iff, f2SupportPredicate, f2SupportAdj,
      f2FirstCoordSupport, f2SecondCoordSupport, f2ThirdCoordSupport, fieldCoordZeroMulB]

lemma f2_support_of_vertex
    {p : ℕ} [Fact p.Prime] {x : F2RingElem p}
    (hx : f2ZeroDivisorVertex x) :
    ∃ s : F2Support, f2SupportPredicate s x := by
  rcases (f2_ring_support_partition_lemma x).mp hx with hA | hB | hC | hD | hE | hF
  · exact ⟨.A, hA⟩
  · exact ⟨.B, hB⟩
  · exact ⟨.C, hC⟩
  · exact ⟨.D, hD⟩
  · exact ⟨.E, hE⟩
  · exact ⟨.F, hF⟩

lemma f2_support_edge_pattern
    {p : ℕ} [Fact p.Prime] {s t : F2Support} {x y : F2RingElem p}
    (hx : f2SupportPredicate s x)
    (hy : f2SupportPredicate t y)
    (hxy : x * y = 0) :
    ((s = F2Support.A ∧ t = F2Support.B) ∨
     (s = F2Support.B ∧ t = F2Support.A) ∨
     (s = F2Support.A ∧ t = F2Support.C) ∨
     (s = F2Support.C ∧ t = F2Support.A) ∨
     (s = F2Support.A ∧ t = F2Support.F) ∨
     (s = F2Support.F ∧ t = F2Support.A) ∨
     (s = F2Support.B ∧ t = F2Support.C) ∨
     (s = F2Support.C ∧ t = F2Support.B) ∨
     (s = F2Support.B ∧ t = F2Support.E) ∨
     (s = F2Support.E ∧ t = F2Support.B) ∨
     (s = F2Support.C ∧ t = F2Support.D) ∨
     (s = F2Support.D ∧ t = F2Support.C)) := by
  have hsupport : f2SupportAdj s t := (f2_ring_support_adjacency_lemma hx hy).mp hxy
  exact (support_decomposition_F2 s t).mp hsupport

lemma f2_support_edge_cases
    {p : ℕ} [Fact p.Prime] {s t : F2Support} {x y : F2RingElem p}
    (hx : f2SupportPredicate s x)
    (hy : f2SupportPredicate t y)
    (hxy : x * y = 0) :
    ((f2SupportPredicate .A x ∧ f2SupportPredicate .B y) ∨
     (f2SupportPredicate .B x ∧ f2SupportPredicate .A y) ∨
     (f2SupportPredicate .A x ∧ f2SupportPredicate .C y) ∨
     (f2SupportPredicate .C x ∧ f2SupportPredicate .A y) ∨
     (f2SupportPredicate .A x ∧ f2SupportPredicate .F y) ∨
     (f2SupportPredicate .F x ∧ f2SupportPredicate .A y) ∨
     (f2SupportPredicate .B x ∧ f2SupportPredicate .C y) ∨
     (f2SupportPredicate .C x ∧ f2SupportPredicate .B y) ∨
     (f2SupportPredicate .B x ∧ f2SupportPredicate .E y) ∨
     (f2SupportPredicate .E x ∧ f2SupportPredicate .B y) ∨
     (f2SupportPredicate .C x ∧ f2SupportPredicate .D y) ∨
     (f2SupportPredicate .D x ∧ f2SupportPredicate .C y)) := by
  rcases f2_support_edge_pattern hx hy hxy with
    hAB | hBA | hAC | hCA | hAF | hFA | hBC | hCB | hBE | hEB | hCD | hDC
  · rcases hAB with ⟨rfl, rfl⟩
    exact Or.inl ⟨hx, hy⟩
  · rcases hBA with ⟨rfl, rfl⟩
    exact Or.inr <| Or.inl ⟨hx, hy⟩
  · rcases hAC with ⟨rfl, rfl⟩
    exact Or.inr <| Or.inr <| Or.inl ⟨hx, hy⟩
  · rcases hCA with ⟨rfl, rfl⟩
    exact Or.inr <| Or.inr <| Or.inr <| Or.inl ⟨hx, hy⟩
  · rcases hAF with ⟨rfl, rfl⟩
    exact Or.inr <| Or.inr <| Or.inr <| Or.inr <| Or.inl ⟨hx, hy⟩
  · rcases hFA with ⟨rfl, rfl⟩
    exact Or.inr <| Or.inr <| Or.inr <| Or.inr <| Or.inr <| Or.inl ⟨hx, hy⟩
  · rcases hBC with ⟨rfl, rfl⟩
    exact Or.inr <| Or.inr <| Or.inr <| Or.inr <| Or.inr <| Or.inr <| Or.inl ⟨hx, hy⟩
  · rcases hCB with ⟨rfl, rfl⟩
    exact Or.inr <| Or.inr <| Or.inr <| Or.inr <| Or.inr <| Or.inr <| Or.inr <| Or.inl ⟨hx, hy⟩
  · rcases hBE with ⟨rfl, rfl⟩
    exact Or.inr <| Or.inr <| Or.inr <| Or.inr <| Or.inr <| Or.inr <| Or.inr <| Or.inr <| Or.inl ⟨hx, hy⟩
  · rcases hEB with ⟨rfl, rfl⟩
    exact Or.inr <| Or.inr <| Or.inr <| Or.inr <| Or.inr <| Or.inr <| Or.inr <| Or.inr <| Or.inr <| Or.inl ⟨hx, hy⟩
  · rcases hCD with ⟨rfl, rfl⟩
    exact Or.inr <| Or.inr <| Or.inr <| Or.inr <| Or.inr <| Or.inr <| Or.inr <| Or.inr <| Or.inr <| Or.inr <| Or.inl ⟨hx, hy⟩
  · rcases hDC with ⟨rfl, rfl⟩
    exact Or.inr <| Or.inr <| Or.inr <| Or.inr <| Or.inr <| Or.inr <| Or.inr <| Or.inr <| Or.inr <| Or.inr <| Or.inr ⟨hx, hy⟩

/--
Reusable structural corollary for the closed `Γ(Z_p × Z_p × Z_2)` slice.
If neither endpoint of a zero-product edge lies in the hinge singleton support
class `C`, then the edge is already one of the three live arithmetic interfaces
`A-B`, `A-F`, or `B-E`, together with their reversals.
-/
theorem f2_ring_nonhinge_edge_reduction
    {p : ℕ} [Fact p.Prime] {x y : F2RingElem p}
    (hx : f2ZeroDivisorVertex x)
    (hy : f2ZeroDivisorVertex y)
    (hxy : x * y = 0)
    (hxC : ¬ f2SupportPredicate .C x)
    (hyC : ¬ f2SupportPredicate .C y) :
    ((f2SupportPredicate .A x ∧ f2SupportPredicate .B y) ∨
     (f2SupportPredicate .B x ∧ f2SupportPredicate .A y) ∨
     (f2SupportPredicate .A x ∧ f2SupportPredicate .F y) ∨
     (f2SupportPredicate .F x ∧ f2SupportPredicate .A y) ∨
     (f2SupportPredicate .B x ∧ f2SupportPredicate .E y) ∨
     (f2SupportPredicate .E x ∧ f2SupportPredicate .B y)) := by
  obtain ⟨sx, hsx⟩ := f2_support_of_vertex hx
  obtain ⟨sy, hsy⟩ := f2_support_of_vertex hy
  rcases f2_support_edge_cases hsx hsy hxy with
    hAB | hBA | hAC | hCA | hAF | hFA | hBC | hCB | hBE | hEB | hCD | hDC
  · exact Or.inl hAB
  · exact Or.inr <| Or.inl hBA
  · exfalso
    exact hyC hAC.2
  · exfalso
    exact hxC hCA.1
  · exact Or.inr <| Or.inr <| Or.inl hAF
  · exact Or.inr <| Or.inr <| Or.inr <| Or.inl hFA
  · exfalso
    exact hyC hBC.2
  · exfalso
    exact hxC hCB.1
  · exact Or.inr <| Or.inr <| Or.inr <| Or.inr <| Or.inl hBE
  · exact Or.inr <| Or.inr <| Or.inr <| Or.inr <| Or.inr hEB
  · exfalso
    exact hxC hCD.1
  · exfalso
    exact hyC hDC.2

/--
Ring-level wrapper theorem for the structurally closed `Γ(Z_p × Z_p × Z_2)` line.
Once the singleton class `C` is fixed to label `1`, the only arithmetic interfaces
left to check are `A-B`, `A-F`, and `B-E`.
-/
theorem f2_ring_three_interface_reduction
    {p : ℕ} [Fact p.Prime]
    (label : F2RingElem p → Nat)
    (hAB :
      ∀ x y, f2SupportPredicate .A x → f2SupportPredicate .B y →
        Nat.Coprime (label x) (label y))
    (hAF :
      ∀ x y, f2SupportPredicate .A x → f2SupportPredicate .F y →
        Nat.Coprime (label x) (label y))
    (hBE :
      ∀ x y, f2SupportPredicate .B x → f2SupportPredicate .E y →
        Nat.Coprime (label x) (label y))
    (hC1 : ∀ x, f2SupportPredicate .C x → label x = 1) :
    ∀ x y,
      f2ZeroDivisorVertex x → f2ZeroDivisorVertex y → x * y = 0 →
      Nat.Coprime (label x) (label y) := by
  let Adj : F2RingElem p → F2RingElem p → Prop := fun x y =>
    f2ZeroDivisorVertex x ∧ f2ZeroDivisorVertex y ∧ x * y = 0
  have hAdj :
      ∀ x y, Adj x y →
        ((f2SupportPredicate .A x ∧ f2SupportPredicate .B y) ∨
         (f2SupportPredicate .B x ∧ f2SupportPredicate .A y) ∨
         (f2SupportPredicate .A x ∧ f2SupportPredicate .C y) ∨
         (f2SupportPredicate .C x ∧ f2SupportPredicate .A y) ∨
         (f2SupportPredicate .A x ∧ f2SupportPredicate .F y) ∨
         (f2SupportPredicate .F x ∧ f2SupportPredicate .A y) ∨
         (f2SupportPredicate .B x ∧ f2SupportPredicate .C y) ∨
         (f2SupportPredicate .C x ∧ f2SupportPredicate .B y) ∨
         (f2SupportPredicate .B x ∧ f2SupportPredicate .E y) ∨
         (f2SupportPredicate .E x ∧ f2SupportPredicate .B y) ∨
         (f2SupportPredicate .C x ∧ f2SupportPredicate .D y) ∨
         (f2SupportPredicate .D x ∧ f2SupportPredicate .C y)) := by
    intro x y hxy
    rcases hxy with ⟨hxv, hyv, hmul⟩
    obtain ⟨sx, hsx⟩ := f2_support_of_vertex hxv
    obtain ⟨sy, hsy⟩ := f2_support_of_vertex hyv
    exact f2_support_edge_cases hsx hsy hmul
  intro x y hx hy hxy
  exact ZeroDivisorReductions.zp_zp_z2_support_template_reduction_of_singleton_one
    Adj
    (f2SupportPredicate .A)
    (f2SupportPredicate .B)
    (f2SupportPredicate .C)
    (f2SupportPredicate .D)
    (f2SupportPredicate .E)
    (f2SupportPredicate .F)
    label
    hAdj
    hAB
    hAF
    hBE
    hC1
    x
    y
    ⟨hx, hy, hxy⟩

/--
Publication-facing lead theorem for the currently closed `Γ(Z_p × Z_p × Z_2)` slice.
It preserves the ring-level statement used in the family dossier: once the singleton
support class `C` is fixed to label `1`, every zero-product edge between nonzero
zero-divisor vertices is discharged by the three interfaces `A-B`, `A-F`, and `B-E`.
-/
theorem zp_zp_z2_three_interface_lead_theorem
    {p : ℕ} [Fact p.Prime]
    (label : F2RingElem p → Nat)
    (hAB :
      ∀ x y, f2SupportPredicate .A x → f2SupportPredicate .B y →
        Nat.Coprime (label x) (label y))
    (hAF :
      ∀ x y, f2SupportPredicate .A x → f2SupportPredicate .F y →
        Nat.Coprime (label x) (label y))
    (hBE :
      ∀ x y, f2SupportPredicate .B x → f2SupportPredicate .E y →
        Nat.Coprime (label x) (label y))
    (hC1 : ∀ x, f2SupportPredicate .C x → label x = 1) :
    ∀ x y,
      f2ZeroDivisorVertex x → f2ZeroDivisorVertex y → x * y = 0 →
      Nat.Coprime (label x) (label y) :=
  f2_ring_three_interface_reduction label hAB hAF hBE hC1

end ZeroDivisorRingBridges
end Families
end AutoMath
