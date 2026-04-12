import AutoMath.Families.ZeroDivisorF25FrozenWrapper

namespace AutoMath
namespace Families
namespace ZeroDivisorPrimeLabelings

open ZeroDivisorF25FrozenWrapper
open AutoMath.Families.ZeroDivisorRingBridges

/--
Artifact-local mirror of the bounded frozen-wrapper arithmetic boundary for the
`zero_divisor_prime_labelings` family campaign.

The official backend proof lives in `AutoMath.Families.ZeroDivisorF25FrozenWrapper`;
this mirrored theorem preserves the checked `p = 31` / `p = 37` boundary package
inside the family artifact directory.
-/
theorem family_zero_divisor_prime_labelings_f25_frozen_wrapper_boundary :
    frozenWrapperFitsAReservoir 31 ∧
      frozenWrapperSpillCount 31 = 19 ∧
      frozenWrapperSpillCount 37 = 22 ∧
      ¬ frozenWrapperFitsAReservoir 37 := by
  exact frozen_wrapper_boundary_31_37

/--
Artifact-local mirror of the reusable zero-spill arithmetic lemma for the live
high-barrier `F25` slice: a prime barrier label above half the active interval
is automatically coprime to every other interval label.
-/
theorem family_zero_divisor_prime_labelings_f25_zero_spill_coprime
    {p b n : ℕ}
    (hbprime : Nat.Prime b)
    (hbhalf : f25LabelBound p < 2 * b)
    (hn : n ∈ Finset.Icc 1 (f25LabelBound p))
    (hneq : n ≠ b) :
    Nat.Coprime b n := by
  exact zero_spill_coprime_of_prime_gt_half hbprime hbhalf hn hneq

/--
Artifact-local mirror of the reusable high-barrier `B-D` discharge package for the
live `F25` arithmetic slice. This is the bounded family lemma currently needed to
turn the zero-spill barrier choice `B = {1, b₁, b₂, b₃}` into a single checked
coprimality statement against the residual `D` labels.
-/
theorem family_zero_divisor_prime_labelings_f25_high_barrier_set_coprime
    {p b₁ b₂ b₃ b d : ℕ}
    (hb₁prime : Nat.Prime b₁)
    (hb₂prime : Nat.Prime b₂)
    (hb₃prime : Nat.Prime b₃)
    (hb₁half : f25LabelBound p < 2 * b₁)
    (hb₂half : f25LabelBound p < 2 * b₂)
    (hb₃half : f25LabelBound p < 2 * b₃)
    (hb : b ∈ ZeroDivisorF25FrozenWrapper.highBarrierLabelSet b₁ b₂ b₃)
    (hd : d ∈ Finset.Icc 1 (f25LabelBound p))
    (hd_out : d ∉ ZeroDivisorF25FrozenWrapper.highBarrierLabelSet b₁ b₂ b₃) :
    Nat.Coprime b d := by
  exact ZeroDivisorF25FrozenWrapper.high_barrier_set_coprime_of_mem_of_not_mem
    hb₁prime hb₂prime hb₃prime hb₁half hb₂half hb₃half hb hd hd_out

/--
Artifact-local mirror of the fixed-`A₀` coprimality lemma for the live `F25`
headline slice. This preserves the checked fact that every label in the frozen
reservoir `A₀` is automatically coprime to any prime outside `{2,3}`.
-/
theorem family_zero_divisor_prime_labelings_f25_fixedA0_coprime_to_complementary_primes
    {a q : ℕ}
    (ha : a ∈ (fixedA0LabelSet : Finset ℕ))
    (hq : Nat.Prime q)
    (hq2 : q ≠ 2)
    (hq3 : q ≠ 3) :
    Nat.Coprime a q := by
  exact coprime_of_mem_fixedA0LabelSet_of_prime_ne_two_ne_three ha hq hq2 hq3

/--
Artifact-local mirror of the uniform availability lemma for the frozen `A₀`
reservoir: once `p ≥ 19`, every label in `A₀` lies inside the active interval
`{1, ..., 5p + 19}`.
-/
theorem family_zero_divisor_prime_labelings_f25_A0_available_of_p_ge_19
    {p a : ℕ}
    (hp : 19 ≤ p)
    (ha : a ∈ (fixedA0LabelSet : Finset ℕ)) :
    a ∈ Finset.Icc 1 (f25LabelBound p) := by
  exact A0_available_of_p_ge_19 hp ha

/--
Artifact-local mirror of the complementary-support pack used by the live
`Γ(Z_p × Z_25)` family slice. It simultaneously discharges the `A-C` and `B-C`
interfaces for composite `C` labels whose prime support avoids `{2,3}` and the
barrier primes.
-/
theorem family_zero_divisor_prime_labelings_f25_complementary_support_pack
    {a b₁ b₂ b₃ b c : ℕ}
    (ha : a ∈ (fixedA0LabelSet : Finset ℕ))
    (hb₁prime : Nat.Prime b₁)
    (hb₂prime : Nat.Prime b₂)
    (hb₃prime : Nat.Prime b₃)
    (hb : b ∈ ZeroDivisorF25FrozenWrapper.highBarrierLabelSet b₁ b₂ b₃)
    (havoid23 : ∀ q, q.Prime → q ∣ c → q ≠ 2 ∧ q ≠ 3)
    (havoidBarrier : ∀ q, q.Prime → q ∣ c → q ≠ b₁ ∧ q ≠ b₂ ∧ q ≠ b₃) :
    Nat.Coprime a c ∧ Nat.Coprime b c := by
  exact complementary_support_pack_lemma
    ha hb₁prime hb₂prime hb₃prime hb havoid23 havoidBarrier

/--
Artifact-local mirror of the checked complementary-support `F25` wrapper
skeleton. It packages the fixed `A₀`, high-barrier `B`, complementary-support
`C`, and residual `D` front end into the exact ring bridge, while leaving the
remaining `B-B` clique clause explicit.
-/
theorem family_zero_divisor_prime_labelings_f25_high_barrier_wrapper_skeleton
    {p : ℕ} [Fact p.Prime]
    (label : F25RingElem p → Nat)
    (b₁ b₂ b₃ : ℕ)
    (C_lab D_lab : Set ℕ)
    (hb₁prime : Nat.Prime b₁)
    (hb₂prime : Nat.Prime b₂)
    (hb₃prime : Nat.Prime b₃)
    (hb₁half : f25LabelBound p < 2 * b₁)
    (hb₂half : f25LabelBound p < 2 * b₂)
    (hb₃half : f25LabelBound p < 2 * b₃)
    (hA_mem :
      ∀ x, f25SupportPredicate .A x → label x ∈ (fixedA0LabelSet : Set ℕ))
    (hB_mem :
      ∀ x, f25SupportPredicate .B x → label x ∈ highBarrierLabelSet b₁ b₂ b₃)
    (hC_mem :
      ∀ x, f25SupportPredicate .C x → label x ∈ C_lab)
    (hD_mem :
      ∀ x, f25SupportPredicate .D x → label x ∈ D_lab)
    (hC_avoid23 :
      ∀ c, c ∈ C_lab → ∀ q, q.Prime → q ∣ c → q ≠ 2 ∧ q ≠ 3)
    (hC_avoidBarrier :
      ∀ c, c ∈ C_lab → ∀ q, q.Prime → q ∣ c → q ≠ b₁ ∧ q ≠ b₂ ∧ q ≠ b₃)
    (hD_interval :
      ∀ d, d ∈ D_lab → d ∈ Finset.Icc 1 (f25LabelBound p))
    (hD_out :
      ∀ d, d ∈ D_lab → d ∉ highBarrierLabelSet b₁ b₂ b₃)
    (hBB :
      ∀ b b',
        b ∈ highBarrierLabelSet b₁ b₂ b₃ →
        b' ∈ highBarrierLabelSet b₁ b₂ b₃ →
        Nat.Coprime b b') :
    ∀ x y,
      f25ZeroDivisorVertex x → f25ZeroDivisorVertex y → x * y = 0 →
      Nat.Coprime (label x) (label y) := by
  exact zp_z25_high_barrier_complementary_support_wrapper_skeleton
    label b₁ b₂ b₃ C_lab D_lab
    hb₁prime hb₂prime hb₃prime
    hb₁half hb₂half hb₃half
    hA_mem hB_mem hC_mem hD_mem
    hC_avoid23 hC_avoidBarrier
    hD_interval hD_out hBB

/--
Artifact-local mirror of the graph-faithful complementary-support `F25`
wrapper skeleton. This is the bounded Lean target for the current family pass:
it packages the live `A₀` / high-barrier / complementary-support front end and
leaves only the distinct-vertex `B-B` clique clause explicit.
-/
theorem family_zero_divisor_prime_labelings_f25_high_barrier_wrapper_graph_skeleton
    {p : ℕ} [Fact p.Prime]
    (label : F25RingElem p → Nat)
    (b₁ b₂ b₃ : ℕ)
    (C_lab D_lab : Set ℕ)
    (hb₁prime : Nat.Prime b₁)
    (hb₂prime : Nat.Prime b₂)
    (hb₃prime : Nat.Prime b₃)
    (hb₁half : f25LabelBound p < 2 * b₁)
    (hb₂half : f25LabelBound p < 2 * b₂)
    (hb₃half : f25LabelBound p < 2 * b₃)
    (hA_mem :
      ∀ x, f25SupportPredicate .A x → label x ∈ (fixedA0LabelSet : Set ℕ))
    (hB_mem :
      ∀ x, f25SupportPredicate .B x → label x ∈ highBarrierLabelSet b₁ b₂ b₃)
    (hC_mem :
      ∀ x, f25SupportPredicate .C x → label x ∈ C_lab)
    (hD_mem :
      ∀ x, f25SupportPredicate .D x → label x ∈ D_lab)
    (hC_avoid23 :
      ∀ c, c ∈ C_lab → ∀ q, q.Prime → q ∣ c → q ≠ 2 ∧ q ≠ 3)
    (hC_avoidBarrier :
      ∀ c, c ∈ C_lab → ∀ q, q.Prime → q ∣ c → q ≠ b₁ ∧ q ≠ b₂ ∧ q ≠ b₃)
    (hD_interval :
      ∀ d, d ∈ D_lab → d ∈ Finset.Icc 1 (f25LabelBound p))
    (hD_out :
      ∀ d, d ∈ D_lab → d ∉ highBarrierLabelSet b₁ b₂ b₃)
    (hBB :
      ∀ x y,
        f25SupportPredicate .B x →
        f25SupportPredicate .B y →
        x ≠ y →
        Nat.Coprime (label x) (label y)) :
    ∀ x y,
      f25ZeroDivisorVertex x → f25ZeroDivisorVertex y → x ≠ y → x * y = 0 →
      Nat.Coprime (label x) (label y) := by
  exact zp_z25_high_barrier_complementary_support_wrapper_graph_skeleton
    label b₁ b₂ b₃ C_lab D_lab
    hb₁prime hb₂prime hb₃prime
    hb₁half hb₂half hb₃half
    hA_mem hB_mem hC_mem hD_mem
    hC_avoid23 hC_avoidBarrier
    hD_interval hD_out hBB

/--
Artifact-local mirror of the barrier-clique lemma needed by the live `F25`
campaign: distinct labels inside `{1,b₁,b₂,b₃}` are pairwise coprime once the
three nontrivial barrier labels are pairwise distinct primes.
-/
theorem family_zero_divisor_prime_labelings_f25_high_barrier_pairwise_coprime
    {b₁ b₂ b₃ b b' : ℕ}
    (hb₁prime : Nat.Prime b₁)
    (hb₂prime : Nat.Prime b₂)
    (hb₃prime : Nat.Prime b₃)
    (hb₁₂ : b₁ ≠ b₂)
    (hb₁₃ : b₁ ≠ b₃)
    (hb₂₃ : b₂ ≠ b₃)
    (hb : b ∈ highBarrierLabelSet b₁ b₂ b₃)
    (hb' : b' ∈ highBarrierLabelSet b₁ b₂ b₃)
    (hneq : b ≠ b') :
    Nat.Coprime b b' := by
  exact ZeroDivisorF25FrozenWrapper.high_barrier_pairwise_coprime_of_mem_of_ne
    hb₁prime hb₂prime hb₃prime hb₁₂ hb₁₃ hb₂₃ hb hb' hneq

/--
Artifact-local mirror of the injective `B-B` discharge for the graph-faithful
complementary-support `F25` wrapper.
-/
theorem family_zero_divisor_prime_labelings_f25_high_barrier_BB_of_injective
    {p : ℕ}
    (label : F25RingElem p → Nat)
    (b₁ b₂ b₃ : ℕ)
    (hb₁prime : Nat.Prime b₁)
    (hb₂prime : Nat.Prime b₂)
    (hb₃prime : Nat.Prime b₃)
    (hb₁₂ : b₁ ≠ b₂)
    (hb₁₃ : b₁ ≠ b₃)
    (hb₂₃ : b₂ ≠ b₃)
    (hinj : Function.Injective label)
    (hB_mem :
      ∀ x, f25SupportPredicate .B x → label x ∈ highBarrierLabelSet b₁ b₂ b₃) :
    ∀ x y,
      f25SupportPredicate .B x →
      f25SupportPredicate .B y →
      x ≠ y →
      Nat.Coprime (label x) (label y) := by
  exact ZeroDivisorF25FrozenWrapper.high_barrier_BB_coprime_of_injective
    label b₁ b₂ b₃ hb₁prime hb₂prime hb₃prime hb₁₂ hb₁₃ hb₂₃ hinj hB_mem

/--
Artifact-local mirror of the closed graph-faithful wrapper theorem obtained by
combining the checked complementary-support skeleton with the new injective
barrier-clique discharge.
-/
theorem family_zero_divisor_prime_labelings_f25_high_barrier_wrapper_graph_of_injective
    {p : ℕ} [Fact p.Prime]
    (label : F25RingElem p → Nat)
    (b₁ b₂ b₃ : ℕ)
    (C_lab D_lab : Set ℕ)
    (hb₁prime : Nat.Prime b₁)
    (hb₂prime : Nat.Prime b₂)
    (hb₃prime : Nat.Prime b₃)
    (hb₁half : f25LabelBound p < 2 * b₁)
    (hb₂half : f25LabelBound p < 2 * b₂)
    (hb₃half : f25LabelBound p < 2 * b₃)
    (hb₁₂ : b₁ ≠ b₂)
    (hb₁₃ : b₁ ≠ b₃)
    (hb₂₃ : b₂ ≠ b₃)
    (hinj : Function.Injective label)
    (hA_mem :
      ∀ x, f25SupportPredicate .A x → label x ∈ (fixedA0LabelSet : Set ℕ))
    (hB_mem :
      ∀ x, f25SupportPredicate .B x → label x ∈ highBarrierLabelSet b₁ b₂ b₃)
    (hC_mem :
      ∀ x, f25SupportPredicate .C x → label x ∈ C_lab)
    (hD_mem :
      ∀ x, f25SupportPredicate .D x → label x ∈ D_lab)
    (hC_avoid23 :
      ∀ c, c ∈ C_lab → ∀ q, q.Prime → q ∣ c → q ≠ 2 ∧ q ≠ 3)
    (hC_avoidBarrier :
      ∀ c, c ∈ C_lab → ∀ q, q.Prime → q ∣ c → q ≠ b₁ ∧ q ≠ b₂ ∧ q ≠ b₃)
    (hD_interval :
      ∀ d, d ∈ D_lab → d ∈ Finset.Icc 1 (f25LabelBound p))
    (hD_out :
      ∀ d, d ∈ D_lab → d ∉ highBarrierLabelSet b₁ b₂ b₃) :
    ∀ x y,
      f25ZeroDivisorVertex x → f25ZeroDivisorVertex y → x ≠ y → x * y = 0 →
      Nat.Coprime (label x) (label y) := by
  exact ZeroDivisorF25FrozenWrapper.zp_z25_high_barrier_complementary_support_wrapper_graph_of_injective
    label b₁ b₂ b₃ C_lab D_lab
    hb₁prime hb₂prime hb₃prime
    hb₁half hb₂half hb₃half
    hb₁₂ hb₁₃ hb₂₃ hinj
    hA_mem hB_mem hC_mem hD_mem
    hC_avoid23 hC_avoidBarrier
    hD_interval hD_out

/--
Artifact-local mirror of the fixed `C₀` availability lemma for the preserved
late `F25` window. Once `p ≥ 59`, every label in
`C₀ = {n : 2 ≤ n ≤ 291 and gcd(n, 6) = 1}` lies in the active interval
`{1, ..., 5p + 19}`.
-/
theorem family_zero_divisor_prime_labelings_f25_fixedC0_available_of_p_ge_59
    {p c : ℕ}
    (hp : 59 ≤ p)
    (hc : c ∈ (ZeroDivisorF25FrozenWrapper.fixedC0LabelSet : Set ℕ)) :
    c ∈ Finset.Icc 1 (f25LabelBound p) := by
  exact fixedC0_available_of_p_ge_59 hp hc

/--
Artifact-local mirror of the counted fixed-window supply fact for the preserved
late `F25` campaign. The complementary-support reservoir
`C₀ = {n : 2 ≤ n ≤ 291 and gcd(n, 6) = 1}` has exact size `96`.
-/
theorem family_zero_divisor_prime_labelings_f25_fixedC0_card_eq_96 :
    (AutoMath.Families.ZeroDivisorF25FrozenWrapper.fixedC0Finset).card = 96 := by
  exact AutoMath.Families.ZeroDivisorF25FrozenWrapper.fixedC0_card_eq_96

/--
Artifact-local mirror of the bounded counted `C₀`-supply lemma for the fixed
publication window. Through `p ≤ 97`, the frozen `C₀` reservoir already has at
least `p - 1` labels available for the `C` support class.
-/
theorem family_zero_divisor_prime_labelings_f25_fixedC0_card_ge_C_size_of_p_le_97
    {p : ℕ}
    (hp97 : p ≤ 97) :
    p - 1 ≤ (AutoMath.Families.ZeroDivisorF25FrozenWrapper.fixedC0Finset).card := by
  exact AutoMath.Families.ZeroDivisorF25FrozenWrapper.fixedC0_card_ge_C_size_of_p_le_97 hp97

/--
Artifact-local mirror of the new subset-selection package for the preserved
fixed-window `F25` campaign. Through `p ≤ 97`, the counted reservoir
`C₀ = {n : 2 ≤ n ≤ 291 and gcd(n, 6) = 1}` contains an actual `p - 1` element
sub-finset.
-/
theorem family_zero_divisor_prime_labelings_f25_exists_fixedC0_subset_card_eq_C_size_of_p_le_97
    {p : ℕ}
    (hp97 : p ≤ 97) :
    ∃ S : Finset ℕ,
      S ⊆ AutoMath.Families.ZeroDivisorF25FrozenWrapper.fixedC0Finset ∧
      S.card = p - 1 := by
  exact AutoMath.Families.ZeroDivisorF25FrozenWrapper.exists_fixedC0_subset_card_eq_C_size_of_p_le_97 hp97

/--
Artifact-local mirror of the preserved fixed-data `F25` wrapper skeleton.
This is the bounded Lean target for the current family pass: it freezes the
late-range data `A₀`, `B = {1,293,307,311}`, and
`C₀ = {n : 2 ≤ n ≤ 291 and gcd(n, 6) = 1}`, and leaves only injectivity plus
the residual `D` interval / barrier-exclusion checks explicit.
-/
theorem family_zero_divisor_prime_labelings_f25_fixed_C0_high_barrier_wrapper_graph_skeleton_of_p_le_97
    {p : ℕ} [Fact p.Prime]
    (hp97 : p ≤ 97)
    (label : F25RingElem p → Nat)
    (D_lab : Set ℕ)
    (hinj : Function.Injective label)
    (hA_mem :
      ∀ x, f25SupportPredicate .A x → label x ∈ (fixedA0LabelSet : Set ℕ))
    (hB_mem :
      ∀ x, f25SupportPredicate .B x → label x ∈ highBarrierLabelSet 293 307 311)
    (hC_mem :
      ∀ x, f25SupportPredicate .C x →
        label x ∈ (ZeroDivisorF25FrozenWrapper.fixedC0LabelSet : Set ℕ))
    (hD_mem :
      ∀ x, f25SupportPredicate .D x → label x ∈ D_lab)
    (hD_interval :
      ∀ d, d ∈ D_lab → d ∈ Finset.Icc 1 (f25LabelBound p))
    (hD_out :
      ∀ d, d ∈ D_lab → d ∉ highBarrierLabelSet 293 307 311) :
    ∀ x y,
      f25ZeroDivisorVertex x → f25ZeroDivisorVertex y → x ≠ y → x * y = 0 →
      Nat.Coprime (label x) (label y) := by
  exact ZeroDivisorF25FrozenWrapper.zp_z25_fixed_C0_high_barrier_wrapper_graph_skeleton_of_p_le_97
    hp97 label D_lab hinj hA_mem hB_mem hC_mem hD_mem hD_interval hD_out

end ZeroDivisorPrimeLabelings
end Families
end AutoMath
