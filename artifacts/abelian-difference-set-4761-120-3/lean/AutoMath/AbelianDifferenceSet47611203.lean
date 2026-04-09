import Mathlib

namespace AutoMath
namespace AbelianDifferenceSet47611203

structure FiniteAbelianModel where
  Carrier : Type
  instAddCommGroup : AddCommGroup Carrier
  instFintype : Fintype Carrier
  instDecidableEq : DecidableEq Carrier

attribute [instance] FiniteAbelianModel.instAddCommGroup
attribute [instance] FiniteAbelianModel.instFintype
attribute [instance] FiniteAbelianModel.instDecidableEq

/-- Ordered representation count of `g` as a difference `d₁ - d₂` with `d₁,d₂ ∈ D`. -/
def orderedDifferenceRepCount {G : Type} [AddCommGroup G] [Fintype G] [DecidableEq G]
    (D : Finset G) (g : G) : Nat :=
  ((D.product D).filter fun p : G × G => p.1 - p.2 = g).card

/-- Exact ordered-difference-set predicate used by the selected dossier. -/
def IsDifferenceSet {G : Type} [AddCommGroup G] [Fintype G] [DecidableEq G]
    (D : Finset G) (k lam : Nat) : Prop :=
  D.card = k ∧ ∀ g : G, g ≠ 0 → orderedDifferenceRepCount D g = lam

/-- The locked intended statement for the active slug. -/
def intendedStatement : Prop :=
  ∃ M : FiniteAbelianModel,
    Fintype.card M.Carrier = 4761 ∧
    ∃ D : Finset M.Carrier, IsDifferenceSet D 120 3

/-- The exact disproof target: the intended statement is false. -/
def exactCounterexampleStatement : Prop :=
  ¬ intendedStatement

/-- Exact theorem statement for the active slug. -/
theorem no_abelian_difference_set_4761_120_3_statement :
    exactCounterexampleStatement ↔
      ¬ ∃ M : FiniteAbelianModel,
          Fintype.card M.Carrier = 4761 ∧
          ∃ D : Finset M.Carrier, IsDifferenceSet D 120 3 := by
  rfl

/--
Proof skeleton for the exact theorem targeted in this slug:

```lean
theorem no_abelian_difference_set_4761_120_3 :
    exactCounterexampleStatement := by
  intro hExists
  obtain ⟨M, hcard, D, hD⟩ := hExists
  -- 1. Invoke the prime-multiplier theorem at `p = 13` to obtain `13D = D + g`.
  -- 2. Compress by the `3`-Sylow quotient `K` of order `23^2`.
  -- 3. Translate the affine invariance `a_x = a_{13x-c}` to linear invariance under `x ↦ 13x`.
  -- 4. Analyze the `13`-orbit sizes on `K`, which are `{1,11}` or `{1,11,253}`.
  -- 5. Reduce to `120 = b0 + 11 * m` with `b0 ≤ 9`.
  exact orbit_profile_residue_obstruction_of_total ?hb0 ?htotal
```

The current Lean blocker is step 1: neither the repository nor vendored mathlib provides the
prime-multiplier theorem for abelian difference sets, and the quotient-orbit bridge depends on it.
-/
theorem exact_counterexample_statement_faithful :
    exactCounterexampleStatement = ¬ intendedStatement := by
  rfl

/--
Checked proof skeleton: once the missing reduction from a hypothetical difference set to the
final residue equation is formalized, the exact disproof follows immediately.
-/
theorem no_abelian_difference_set_4761_120_3_skeleton
    (hReduction :
      intendedStatement → ∃ b0 m : Nat, b0 ≤ 9 ∧ 120 = b0 + 11 * m) :
    exactCounterexampleStatement := by
  intro hExists
  rcases hReduction hExists with ⟨b0, m, hb0, htotal⟩
  omega

/-- Any coefficient on a size-`253` orbit must vanish if the total contribution is at most `120`. -/
theorem large_orbit_coefficient_zero {r : Nat} (hr : r ≤ 9) (h : 253 * r ≤ 120) : r = 0 := by
  omega

/-- The final residue obstruction from the verified argument. -/
theorem orbit_profile_residue_obstruction :
    ¬ ∃ b0 m : Nat, b0 ≤ 9 ∧ 120 = b0 + 11 * m := by
  omega

theorem orbit_profile_residue_obstruction_of_total
    {b0 m : Nat} (hb0 : b0 ≤ 9) (htotal : 120 = b0 + 11 * m) : False := by
  exact orbit_profile_residue_obstruction ⟨b0, m, hb0, htotal⟩

end AbelianDifferenceSet47611203
end AutoMath
