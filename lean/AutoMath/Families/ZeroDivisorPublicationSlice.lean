import AutoMath.Families.ZeroDivisorF25FrozenWrapper
import AutoMath.Families.ZeroDivisorRingBridges

namespace AutoMath
namespace Families
namespace ZeroDivisorPublicationSlice

open ZeroDivisorF25FrozenWrapper
open ZeroDivisorRingBridges

/--
Proposition alias for the current publication-facing `Γ(Z_p × Z_25)` slice.
It records the exact graph-faithful complementary-support wrapper already
checked in the backend, with no claim yet about producing the `C` block.
-/
def F25GraphWrapperSlice (p : ℕ) [Fact p.Prime] : Prop :=
  ∀ (label : F25RingElem p → Nat)
    (b₁ b₂ b₃ : ℕ)
    (C_lab D_lab : Set ℕ)
    (_ : Nat.Prime b₁)
    (_ : Nat.Prime b₂)
    (_ : Nat.Prime b₃)
    (_ : f25LabelBound p < 2 * b₁)
    (_ : f25LabelBound p < 2 * b₂)
    (_ : f25LabelBound p < 2 * b₃)
    (_ : b₁ ≠ b₂)
    (_ : b₁ ≠ b₃)
    (_ : b₂ ≠ b₃)
    (_ : Function.Injective label)
    (_ :
      ∀ x, f25SupportPredicate .A x → label x ∈ (fixedA0LabelSet : Set ℕ))
    (_ :
      ∀ x, f25SupportPredicate .B x → label x ∈ highBarrierLabelSet b₁ b₂ b₃)
    (_ :
      ∀ x, f25SupportPredicate .C x → label x ∈ C_lab)
    (_ :
      ∀ x, f25SupportPredicate .D x → label x ∈ D_lab)
    (_ :
      ∀ c, c ∈ C_lab → ∀ q, q.Prime → q ∣ c → q ≠ 2 ∧ q ≠ 3)
    (_ :
      ∀ c, c ∈ C_lab → ∀ q, q.Prime → q ∣ c → q ≠ b₁ ∧ q ≠ b₂ ∧ q ≠ b₃)
    (_ :
      ∀ d, d ∈ D_lab → d ∈ Finset.Icc 1 (f25LabelBound p))
    (_ :
      ∀ d, d ∈ D_lab → d ∉ highBarrierLabelSet b₁ b₂ b₃),
    ∀ x y,
      f25ZeroDivisorVertex x →
      f25ZeroDivisorVertex y →
      x ≠ y →
      x * y = 0 →
      Nat.Coprime (label x) (label y)

/--
Proposition alias for the current publication-facing `Γ(Z_p × Z_p × Z_2)`
slice. This is the closed three-interface theorem after fixing the singleton
support class `C` to label `1`.
-/
def F2ThreeInterfaceSlice (p : ℕ) [Fact p.Prime] : Prop :=
  ∀ (label : F2RingElem p → Nat)
    (_ :
      ∀ x y, f2SupportPredicate .A x → f2SupportPredicate .B y →
        Nat.Coprime (label x) (label y))
    (_ :
      ∀ x y, f2SupportPredicate .A x → f2SupportPredicate .F y →
        Nat.Coprime (label x) (label y))
    (_ :
      ∀ x y, f2SupportPredicate .B x → f2SupportPredicate .E y →
        Nat.Coprime (label x) (label y))
    (_ : ∀ x, f2SupportPredicate .C x → label x = 1),
    ∀ x y,
      f2ZeroDivisorVertex x →
      f2ZeroDivisorVertex y →
      x * y = 0 →
      Nat.Coprime (label x) (label y)

/--
Paired exact theorem-slice package for the active zero-divisor publication
campaign. It formalizes the strongest honest Lean target currently supported by
the family dossier: the graph-faithful `F25` wrapper together with the closed
three-interface `F2` slice.
-/
theorem zero_divisor_prime_labelings_paired_exact_slice
    {p : ℕ} [Fact p.Prime] :
    F25GraphWrapperSlice p ∧ F2ThreeInterfaceSlice p := by
  constructor
  · intro label b₁ b₂ b₃ C_lab D_lab
      hb₁prime hb₂prime hb₃prime
      hb₁half hb₂half hb₃half
      hb₁₂ hb₁₃ hb₂₃
      hinj
      hA_mem hB_mem hC_mem hD_mem
      hC_avoid23 hC_avoidBarrier
      hD_interval hD_out
    exact zp_z25_high_barrier_complementary_support_wrapper_graph_of_injective
      label b₁ b₂ b₃ C_lab D_lab
      hb₁prime hb₂prime hb₃prime
      hb₁half hb₂half hb₃half
      hb₁₂ hb₁₃ hb₂₃
      hinj
      hA_mem hB_mem hC_mem hD_mem
      hC_avoid23 hC_avoidBarrier
      hD_interval hD_out
  · intro label hAB hAF hBE hC1
    exact zp_zp_z2_three_interface_lead_theorem label hAB hAF hBE hC1

end ZeroDivisorPublicationSlice
end Families
end AutoMath
