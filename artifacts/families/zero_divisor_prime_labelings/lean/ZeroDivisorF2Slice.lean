import AutoMath.Families.ZeroDivisorRingBridges

namespace AutoMath
namespace Families
namespace ZeroDivisorPrimeLabelings

open ZeroDivisorRingBridges

/--
Artifact-local mirror of the closed `F2` theorem slice for the
`zero_divisor_prime_labelings` family campaign.

The official backend proof lives in `AutoMath.Families.ZeroDivisorRingBridges`;
this file preserves the exact checked statement under the family artifact
directory without introducing any new axioms or placeholders.
-/
theorem family_zero_divisor_prime_labelings_f2_slice
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
  zp_zp_z2_three_interface_lead_theorem label hAB hAF hBE hC1

end ZeroDivisorPrimeLabelings
end Families
end AutoMath
