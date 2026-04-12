import AutoMath.Families.ZeroDivisorRingBridges

namespace AutoMath
namespace Families
namespace ZeroDivisorPrimeLabelings

open ZeroDivisorRingBridges

/--
Artifact-local mirror of the closed `F25` companion theorem slice for the
`zero_divisor_prime_labelings` family campaign.

The official backend proof lives in `AutoMath.Families.ZeroDivisorRingBridges`;
this file preserves the exact checked statement under the family artifact
directory without introducing any new axioms or placeholders.
-/
theorem family_zero_divisor_prime_labelings_f25_slice
    {p : ℕ} [Fact p.Prime]
    (label : F25RingElem p → Nat)
    (hAC :
      ∀ x y, f25SupportPredicate .A x → f25SupportPredicate .C y →
        Nat.Coprime (label x) (label y))
    (hBB :
      ∀ x y, f25SupportPredicate .B x → f25SupportPredicate .B y →
        Nat.Coprime (label x) (label y))
    (hBC :
      ∀ x y, f25SupportPredicate .B x → f25SupportPredicate .C y →
        Nat.Coprime (label x) (label y))
    (hBD :
      ∀ x y, f25SupportPredicate .B x → f25SupportPredicate .D y →
        Nat.Coprime (label x) (label y)) :
    ∀ x y,
      f25ZeroDivisorVertex x → f25ZeroDivisorVertex y → x * y = 0 →
      Nat.Coprime (label x) (label y) := by
  exact zp_z25_four_interface_companion_theorem label hAC hBB hBC hBD

/--
Artifact-local mirror of the paper-facing label-set packaging for the `F25`
companion slice. This keeps the checked theorem statement aligned with the
family record's `A_lab/B_lab/C_lab/D_lab` phrasing.
-/
theorem family_zero_divisor_prime_labelings_f25_label_set_slice
    {p : ℕ} [Fact p.Prime]
    (label : F25RingElem p → Nat)
    (A_lab B_lab C_lab D_lab : Set Nat)
    (hA_mem : ∀ x, f25SupportPredicate .A x → label x ∈ A_lab)
    (hB_mem : ∀ x, f25SupportPredicate .B x → label x ∈ B_lab)
    (hC_mem : ∀ x, f25SupportPredicate .C x → label x ∈ C_lab)
    (hD_mem : ∀ x, f25SupportPredicate .D x → label x ∈ D_lab)
    (hAC_lab :
      ∀ a c, a ∈ A_lab → c ∈ C_lab → Nat.Coprime a c)
    (hBB_lab :
      ∀ b₁ b₂, b₁ ∈ B_lab → b₂ ∈ B_lab → Nat.Coprime b₁ b₂)
    (hBC_lab :
      ∀ b c, b ∈ B_lab → c ∈ C_lab → Nat.Coprime b c)
    (hBD_lab :
      ∀ b d, b ∈ B_lab → d ∈ D_lab → Nat.Coprime b d) :
    ∀ x y,
      f25ZeroDivisorVertex x → f25ZeroDivisorVertex y → x * y = 0 →
      Nat.Coprime (label x) (label y) := by
  exact zp_z25_four_interface_companion_theorem_of_label_sets
    label A_lab B_lab C_lab D_lab
    hA_mem hB_mem hC_mem hD_mem hAC_lab hBB_lab hBC_lab hBD_lab

/--
Artifact-local mirror of the graph-faithful `F25` companion theorem slice.
This is the same structural reduction as the closed backend theorem, but it now
matches the simple zero-divisor graph by requiring the final vertices to be
distinct and weakening the `B-B` clause accordingly.
-/
theorem family_zero_divisor_prime_labelings_f25_distinct_vertex_slice
    {p : ℕ} [Fact p.Prime]
    (label : F25RingElem p → Nat)
    (hAC :
      ∀ x y, f25SupportPredicate .A x → f25SupportPredicate .C y →
        Nat.Coprime (label x) (label y))
    (hBB :
      ∀ x y, f25SupportPredicate .B x → f25SupportPredicate .B y →
        x ≠ y → Nat.Coprime (label x) (label y))
    (hBC :
      ∀ x y, f25SupportPredicate .B x → f25SupportPredicate .C y →
        Nat.Coprime (label x) (label y))
    (hBD :
      ∀ x y, f25SupportPredicate .B x → f25SupportPredicate .D y →
        Nat.Coprime (label x) (label y)) :
    ∀ x y,
      f25ZeroDivisorVertex x → f25ZeroDivisorVertex y → x ≠ y → x * y = 0 →
      Nat.Coprime (label x) (label y) := by
  exact zp_z25_four_interface_companion_theorem_on_distinct_vertices
    label hAC hBB hBC hBD

end ZeroDivisorPrimeLabelings
end Families
end AutoMath
