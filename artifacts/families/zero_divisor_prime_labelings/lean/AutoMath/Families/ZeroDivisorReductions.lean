import AutoMath.Families.PrimeSupportTemplates

namespace AutoMath
namespace Families
namespace ZeroDivisorReductions

/-
The publication campaign for zero-divisor prime labelings is currently targeting theorem slices,
not a full all-primes closure. These wrapper theorems pin the campaign's two honest structural
claims to stable Lean names so later feeder instances can plug into them directly.
-/

/-- The `Γ(Z_p × Z_25)` family slice reduces to the four support-class interfaces visible in the
exact `p = 3, 5, 7` cluster. Any classwise labeling that satisfies those coprimality constraints
already certifies every adjacent pair in the blowup graph. -/
theorem zp_z25_support_template_reduction
    {V : Type*}
    (Adj : V → V → Prop)
    (A B C D : V → Prop)
    (label : V → Nat)
    (hAdj :
      ∀ x y, Adj x y →
        ((A x ∧ C y) ∨ (C x ∧ A y) ∨
         (B x ∧ B y) ∨
         (B x ∧ C y) ∨ (C x ∧ B y) ∨
         (B x ∧ D y) ∨ (D x ∧ B y)))
    (hAC : ∀ x y, A x → C y → Nat.Coprime (label x) (label y))
    (hBB : ∀ x y, B x → B y → Nat.Coprime (label x) (label y))
    (hBC : ∀ x y, B x → C y → Nat.Coprime (label x) (label y))
    (hBD : ∀ x y, B x → D y → Nat.Coprime (label x) (label y)) :
    ∀ x y, Adj x y → Nat.Coprime (label x) (label y) :=
  PrimeSupportTemplates.edgeCoprime_of_zp_z25_template Adj A B C D label hAdj hAC hBB hBC hBD

/-- If the hinge class `C` in the `Γ(Z_p × Z_p × Z_2)` support graph is assigned label `1`, then
every edge touching `C` is automatically coprime. This isolates the reusable family step that
frees the `D` class before the remaining three interfaces are handled arithmetically. -/
theorem singleton_one_lemma
    {V : Type*}
    (A B C D : V → Prop)
    (label : V → Nat)
    (hC1 : ∀ x, C x → label x = 1) :
    ∀ x y,
      ((A x ∧ C y) ∨ (C x ∧ A y) ∨
       (B x ∧ C y) ∨ (C x ∧ B y) ∨
       (C x ∧ D y) ∨ (D x ∧ C y)) →
      Nat.Coprime (label x) (label y) := by
  intro x y hxy
  rcases hxy with h | h | h | h | h | h
  · rw [hC1 y h.2]
    simp
  · rw [hC1 x h.1]
    simp
  · rw [hC1 y h.2]
    simp
  · rw [hC1 x h.1]
    simp
  · rw [hC1 x h.1]
    simp
  · rw [hC1 y h.2]
    simp

/-- After the singleton class `C` is fixed to label `1` in the six-class
`Γ(Z_p × Z_p × Z_2)` support graph, only the interfaces `A-B`, `A-F`, and `B-E`
remain arithmetic. All edges touching `C` are discharged by `singleton_one_lemma`. -/
theorem three_interface_pack_lemma
    {V : Type*}
    (Adj : V → V → Prop)
    (A B C D E F : V → Prop)
    (label : V → Nat)
    (hAdj :
      ∀ x y, Adj x y →
        ((A x ∧ B y) ∨ (B x ∧ A y) ∨
         (A x ∧ C y) ∨ (C x ∧ A y) ∨
         (A x ∧ F y) ∨ (F x ∧ A y) ∨
         (B x ∧ C y) ∨ (C x ∧ B y) ∨
         (B x ∧ E y) ∨ (E x ∧ B y) ∨
         (C x ∧ D y) ∨ (D x ∧ C y)))
    (hAB : ∀ x y, A x → B y → Nat.Coprime (label x) (label y))
    (hAF : ∀ x y, A x → F y → Nat.Coprime (label x) (label y))
    (hBE : ∀ x y, B x → E y → Nat.Coprime (label x) (label y))
    (hC1 : ∀ x, C x → label x = 1) :
    ∀ x y, Adj x y → Nat.Coprime (label x) (label y) := by
  intro x y hxy
  have hSingleton := singleton_one_lemma A B C D label hC1 x y
  rcases hAdj x y hxy with h | h | h | h | h | h | h | h | h | h | h | h
  · exact hAB x y h.1 h.2
  · simpa [Nat.coprime_comm] using hAB y x h.2 h.1
  · exact hSingleton (Or.inl h)
  · exact hSingleton (Or.inr (Or.inl h))
  · exact hAF x y h.1 h.2
  · simpa [Nat.coprime_comm] using hAF y x h.2 h.1
  · exact hSingleton (Or.inr (Or.inr (Or.inl h)))
  · exact hSingleton (Or.inr (Or.inr (Or.inr (Or.inl h))))
  · exact hBE x y h.1 h.2
  · simpa [Nat.coprime_comm] using hBE y x h.2 h.1
  · exact hSingleton (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl h)))))
  · exact hSingleton (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr h)))))

/-- The `Γ(Z_p × Z_p × Z_2)` family slice reduces to three interfaces once the singleton support
class is fixed to label `1`. This is the Lean skeleton for the current publication target. -/
theorem zp_zp_z2_support_template_reduction_of_singleton_one
    {V : Type*}
    (Adj : V → V → Prop)
    (A B C D E F : V → Prop)
    (label : V → Nat)
    (hAdj :
      ∀ x y, Adj x y →
        ((A x ∧ B y) ∨ (B x ∧ A y) ∨
         (A x ∧ C y) ∨ (C x ∧ A y) ∨
         (A x ∧ F y) ∨ (F x ∧ A y) ∨
         (B x ∧ C y) ∨ (C x ∧ B y) ∨
         (B x ∧ E y) ∨ (E x ∧ B y) ∨
         (C x ∧ D y) ∨ (D x ∧ C y)))
    (hAB : ∀ x y, A x → B y → Nat.Coprime (label x) (label y))
    (hAF : ∀ x y, A x → F y → Nat.Coprime (label x) (label y))
    (hBE : ∀ x y, B x → E y → Nat.Coprime (label x) (label y))
    (hC1 : ∀ x, C x → label x = 1) :
    ∀ x y, Adj x y → Nat.Coprime (label x) (label y) :=
  three_interface_pack_lemma Adj A B C D E F label hAdj hAB hAF hBE hC1

end ZeroDivisorReductions
end Families
end AutoMath
