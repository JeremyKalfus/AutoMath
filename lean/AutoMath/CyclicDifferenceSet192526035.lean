import Mathlib

namespace AutoMath
namespace CyclicDifferenceSet192526035

/--
Lean target for the packet-sealing attempt on the cyclic `(1925,260,35)` row.

The solve and verification artifacts reduce a hypothetical difference set to the
following exact orbit-refinement system on the `3`-orbits of `C_175`.  This theorem
formalizes the terminal arithmetic obstruction: the forced projections to `C_25`
and `C_7` cannot satisfy the required square-sum identity.
-/
def intendedStatement : Prop :=
  ∀ A B C D E F e₁ e₂ f₁ f₂ : ℕ,
    A + 6 * D = 20 →
    B + 3 * E = 5 →
    C + 3 * F = 11 →
    A + 4 * B + 20 * C = 50 →
    E = e₁ + e₂ →
    F = f₁ + f₂ →
    A ^ 2 + 4 * B ^ 2 + 20 * C ^ 2 + 6 * D ^ 2
        + 12 * (e₁ ^ 2 + e₂ ^ 2) + 60 * (f₁ ^ 2 + f₂ ^ 2) = 610 →
    False

/--
The reduced `C_175` orbit-refinement equations for the cyclic `(1925,260,35)`
packet have no natural-number solution.
-/
theorem c175_orbit_refinement_impossible :
    intendedStatement := by
  intro A B C D E F e₁ e₂ f₁ f₂ hAD hBE hCF hABC hE hF hsq
  have hforced : A = 2 ∧ B = 2 ∧ C = 2 ∧ D = 3 ∧ E = 1 ∧ F = 3 := by
    omega
  rcases hforced with ⟨rfl, rfl, rfl, rfl, rfl, rfl⟩
  have he₁_le : e₁ ≤ 1 := by omega
  have he₂_le : e₂ ≤ 1 := by omega
  have hf₁_le : f₁ ≤ 3 := by omega
  have hf₂_le : f₂ ≤ 3 := by omega
  interval_cases e₁ <;> interval_cases e₂ <;>
    interval_cases f₁ <;> interval_cases f₂ <;>
    omega

/-- Faithfulness check: the named theorem proves the intended reduced obstruction. -/
theorem cyclic_difference_set_1925_260_35_statement :
    intendedStatement := c175_orbit_refinement_impossible

/--
Packet-facing theorem slice.

Any hypothetical cyclic `(1925,260,35)` difference set which has already been reduced
by the verified multiplier and contraction arguments to the displayed orbit equations
would yield a contradiction.
-/
theorem no_compatible_c175_refinement
    (A B C D E F e₁ e₂ f₁ f₂ : ℕ)
    (hAD : A + 6 * D = 20)
    (hBE : B + 3 * E = 5)
    (hCF : C + 3 * F = 11)
    (hABC : A + 4 * B + 20 * C = 50)
    (hE : E = e₁ + e₂)
    (hF : F = f₁ + f₂)
    (hsq :
      A ^ 2 + 4 * B ^ 2 + 20 * C ^ 2 + 6 * D ^ 2
          + 12 * (e₁ ^ 2 + e₂ ^ 2) + 60 * (f₁ ^ 2 + f₂ ^ 2) = 610) :
    False :=
  c175_orbit_refinement_impossible A B C D E F e₁ e₂ f₁ f₂
    hAD hBE hCF hABC hE hF hsq

end CyclicDifferenceSet192526035
end AutoMath
