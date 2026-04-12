import Mathlib.Data.Finset.Card
import Mathlib.Data.Finset.Interval
import Mathlib.Tactic
import AutoMath.Families.ZeroDivisorRingBridges

namespace AutoMath
namespace Families
namespace ZeroDivisorF25FrozenWrapper

open ZeroDivisorRingBridges

/--
The vertex/label count for the family `Γ(Z_p × Z_25)`.
This is the size of the support classes
`A ∪ B ∪ C ∪ D = 20 + 4 + (p - 1) + 4 (p - 1) = 5p + 19`.
-/
def f25LabelBound (p : ℕ) : ℕ :=
  5 * p + 19

/--
The fixed frozen-wrapper spill set attached to the barrier `B = {1, 19, 23, 29}`.
It consists of the labels in `{1, ..., 5p + 19}` divisible by `19`, `23`, or `29`,
excluding the barrier labels `19`, `23`, and `29` themselves.
-/
def frozenWrapperSpill (p : ℕ) : Finset ℕ :=
  (Finset.Icc 1 (f25LabelBound p)).filter fun n =>
    (19 ∣ n ∨ 23 ∣ n ∨ 29 ∣ n) ∧ n ≠ 19 ∧ n ≠ 23 ∧ n ≠ 29

/-- The number of spill labels forced by the frozen wrapper at parameter `p`. -/
def frozenWrapperSpillCount (p : ℕ) : ℕ :=
  (frozenWrapperSpill p).card

/--
The fixed wrapper fits the `A` reservoir exactly when its spill count uses at most
the `20` labels available for the support class `A`.
-/
def frozenWrapperFitsAReservoir (p : ℕ) : Prop :=
  frozenWrapperSpillCount p ≤ 20

/--
The four-label zero-spill barrier set used by the live `F25` arithmetic front end:
the singleton `1` together with three barrier primes above half the active interval.
-/
def highBarrierLabelSet (b₁ b₂ b₃ : ℕ) : Set ℕ :=
  {n | n = 1 ∨ n = b₁ ∨ n = b₂ ∨ n = b₃}

/--
If a positive label `b` lies above half the active interval `{1, ..., N}`, then any
interval label divisible by `b` is forced to equal `b` itself. This is the core
zero-spill arithmetic behind the high-barrier `F25` regime.
-/
private theorem eq_of_dvd_of_mem_Icc_of_lt_two_mul
    {N b n : ℕ}
    (hbpos : 0 < b)
    (hbhalf : N < 2 * b)
    (hn : n ∈ Finset.Icc 1 N)
    (hdiv : b ∣ n) :
    n = b := by
  rcases Finset.mem_Icc.mp hn with ⟨hn1, hnN⟩
  rcases hdiv with ⟨k, rfl⟩
  have hb1 : 1 ≤ b := Nat.succ_le_of_lt hbpos
  have hk1 : 1 ≤ k := by
    by_cases hk0 : k = 0
    · subst hk0
      simp at hn1
    · omega
  have hk_eq_one : k = 1 := by
    have hmul_lt : b * k < 2 * b := lt_of_le_of_lt hnN hbhalf
    have hklt2 : k < 2 := by
      by_contra hkge
      push Not at hkge
      have hge : 2 * b ≤ b * k := by
        calc
          2 * b = b * 2 := by simp [Nat.mul_comm]
          _ ≤ b * k := Nat.mul_le_mul_left b hkge
      exact (Nat.not_lt_of_ge hge) hmul_lt
    omega
  simp [hk_eq_one]

/--
If a barrier prime lies above half the active `F25` label interval
`{1, ..., 5p + 19}`, then every other interval label is automatically coprime to
that barrier prime. This is the reusable zero-spill lemma needed by the live
high-barrier arithmetic slice.
-/
theorem zero_spill_coprime_of_prime_gt_half
    {p b n : ℕ}
    (hbprime : Nat.Prime b)
    (hbhalf : f25LabelBound p < 2 * b)
    (hn : n ∈ Finset.Icc 1 (f25LabelBound p))
    (hneq : n ≠ b) :
    Nat.Coprime b n := by
  rw [hbprime.coprime_iff_not_dvd]
  intro hdiv
  exact hneq (eq_of_dvd_of_mem_Icc_of_lt_two_mul hbprime.pos hbhalf hn hdiv)

/--
Reusable zero-spill barrier lemma for the live `Γ(Z_p × Z_25)` arithmetic slice.
If a barrier label belongs to `{1, b₁, b₂, b₃}`, with each prime barrier above half
the active interval `{1, ..., 5p + 19}`, then every other interval label is coprime
to that barrier label.
-/
theorem high_barrier_label_coprime_of_mem
    {p b₁ b₂ b₃ b n : ℕ}
    (hb₁prime : Nat.Prime b₁)
    (hb₂prime : Nat.Prime b₂)
    (hb₃prime : Nat.Prime b₃)
    (hb₁half : f25LabelBound p < 2 * b₁)
    (hb₂half : f25LabelBound p < 2 * b₂)
    (hb₃half : f25LabelBound p < 2 * b₃)
    (hb : b ∈ highBarrierLabelSet b₁ b₂ b₃)
    (hn : n ∈ Finset.Icc 1 (f25LabelBound p))
    (hneq : n ≠ b) :
    Nat.Coprime b n := by
  simp [highBarrierLabelSet] at hb
  rcases hb with rfl | rfl | rfl | rfl
  · simp
  · exact zero_spill_coprime_of_prime_gt_half hb₁prime hb₁half hn hneq
  · exact zero_spill_coprime_of_prime_gt_half hb₂prime hb₂half hn hneq
  · exact zero_spill_coprime_of_prime_gt_half hb₃prime hb₃half hn hneq

/--
`B-D` discharge package for the high-barrier `F25` regime.
If `b` lies in the barrier set `{1, b₁, b₂, b₃}` and `d` is any other active interval
label outside that barrier set, then `b` and `d` are automatically coprime.
-/
theorem high_barrier_set_coprime_of_mem_of_not_mem
    {p b₁ b₂ b₃ b d : ℕ}
    (hb₁prime : Nat.Prime b₁)
    (hb₂prime : Nat.Prime b₂)
    (hb₃prime : Nat.Prime b₃)
    (hb₁half : f25LabelBound p < 2 * b₁)
    (hb₂half : f25LabelBound p < 2 * b₂)
    (hb₃half : f25LabelBound p < 2 * b₃)
    (hb : b ∈ highBarrierLabelSet b₁ b₂ b₃)
    (hd : d ∈ Finset.Icc 1 (f25LabelBound p))
    (hd_out : d ∉ highBarrierLabelSet b₁ b₂ b₃) :
    Nat.Coprime b d := by
  apply high_barrier_label_coprime_of_mem
    hb₁prime hb₂prime hb₃prime hb₁half hb₂half hb₃half hb hd
  intro hdb
  exact hd_out (hdb ▸ hb)

/--
The fixed 20-label reservoir `A₀` used by the live `Γ(Z_p × Z_25)` headline
slice. Every element of this set has prime support contained in `{2, 3}`.
-/
def fixedA0LabelSet : Finset ℕ :=
  {2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 27, 32, 36, 48, 54, 64, 72, 81, 96, 108}

/--
Every element of the fixed reservoir `A₀` already lies in the static interval
`{1, ..., 108}`.
-/
private theorem mem_Icc_1_108_of_mem_fixedA0LabelSet
    {a : ℕ} (ha : a ∈ fixedA0LabelSet) :
    a ∈ Finset.Icc 1 108 := by
  simp [fixedA0LabelSet, Finset.mem_Icc] at ha ⊢
  rcases ha with
    rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl |
    rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl <;>
    norm_num

/--
Availability of the fixed reservoir `A₀` in the headline `F25` regime.
Once `p ≥ 19`, every element of `A₀` lies in the active interval
`{1, ..., 5p + 19}`.
-/
theorem A0_available_of_p_ge_19
    {p a : ℕ}
    (hp : 19 ≤ p)
    (ha : a ∈ fixedA0LabelSet) :
    a ∈ Finset.Icc 1 (f25LabelBound p) := by
  rcases Finset.mem_Icc.mp (mem_Icc_1_108_of_mem_fixedA0LabelSet ha) with ⟨ha1, ha108⟩
  refine Finset.mem_Icc.mpr ⟨ha1, ?_⟩
  dsimp [f25LabelBound]
  omega

/--
Every label in the fixed reservoir `A₀` divides the master `{2,3}`-smooth
number `2^6 * 3^4 = 5184`. This packages the finite arithmetic content of the
reservoir into a single reusable divisibility lemma.
-/
private theorem dvd_two_pow_six_mul_three_pow_four_of_mem_fixedA0LabelSet
    {a : ℕ} (ha : a ∈ fixedA0LabelSet) :
    a ∣ 2 ^ 6 * 3 ^ 4 := by
  simp [fixedA0LabelSet] at ha
  rcases ha with
    rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl |
    rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl <;>
    norm_num

/--
Reusable fixed-`A₀` coprimality lemma for the live `F25` slice.
If `a` belongs to the fixed reservoir `A₀` and `q` is a prime outside
`{2, 3}`, then `a` and `q` are automatically coprime.
-/
theorem coprime_of_mem_fixedA0LabelSet_of_prime_ne_two_ne_three
    {a q : ℕ}
    (ha : a ∈ fixedA0LabelSet)
    (hq : Nat.Prime q)
    (hq2 : q ≠ 2)
    (hq3 : q ≠ 3) :
    Nat.Coprime a q := by
  rw [Nat.coprime_comm, hq.coprime_iff_not_dvd]
  intro hqa
  have hq_smooth : q ∣ 2 ^ 6 * 3 ^ 4 := by
    exact dvd_trans hqa (dvd_two_pow_six_mul_three_pow_four_of_mem_fixedA0LabelSet ha)
  have hq_eq_two_or_three : q = 2 ∨ q = 3 := by
    rcases hq.dvd_mul.mp hq_smooth with hq_two | hq_three
    · left
      exact Nat.prime_eq_prime_of_dvd_pow hq (by decide : Nat.Prime 2) hq_two
    · right
      exact Nat.prime_eq_prime_of_dvd_pow hq (by decide : Nat.Prime 3) hq_three
  rcases hq_eq_two_or_three with rfl | rfl
  · exact hq2 rfl
  · exact hq3 rfl

/--
Composite-label support-avoidance version of the fixed-`A₀` coprimality lemma.
If every prime divisor of `c` avoids `{2, 3}`, then every label in the frozen
reservoir `A₀` is automatically coprime to `c`.
-/
theorem coprime_of_mem_fixedA0_of_support_avoids_two_three
    {a c : ℕ}
    (ha : a ∈ fixedA0LabelSet)
    (havoid : ∀ q, q.Prime → q ∣ c → q ≠ 2 ∧ q ≠ 3) :
    Nat.Coprime a c := by
  apply Nat.coprime_of_dvd
  intro q hq hqa
  have hq_smooth : q ∣ 2 ^ 6 * 3 ^ 4 := by
    exact dvd_trans hqa (dvd_two_pow_six_mul_three_pow_four_of_mem_fixedA0LabelSet ha)
  intro hqc
  have hq_eq_two_or_three : q = 2 ∨ q = 3 := by
    rcases hq.dvd_mul.mp hq_smooth with hq_two | hq_three
    · left
      exact Nat.prime_eq_prime_of_dvd_pow hq (by decide : Nat.Prime 2) hq_two
    · right
      exact Nat.prime_eq_prime_of_dvd_pow hq (by decide : Nat.Prime 3) hq_three
  have hq_avoids := havoid q hq hqc
  rcases hq_eq_two_or_three with rfl | rfl
  · exact hq_avoids.1 rfl
  · exact hq_avoids.2 rfl

/--
Barrier-support version of the complementary-support coprimality lemma.
If `b` belongs to the high-barrier set `{1, b₁, b₂, b₃}` and every prime divisor
of `c` avoids the three barrier primes, then `b` and `c` are automatically
coprime.
-/
theorem coprime_to_high_barrier_of_support_avoids_barrier_primes
    {b₁ b₂ b₃ b c : ℕ}
    (hb₁prime : Nat.Prime b₁)
    (hb₂prime : Nat.Prime b₂)
    (hb₃prime : Nat.Prime b₃)
    (hb : b ∈ highBarrierLabelSet b₁ b₂ b₃)
    (havoid : ∀ q, q.Prime → q ∣ c → q ≠ b₁ ∧ q ≠ b₂ ∧ q ≠ b₃) :
    Nat.Coprime b c := by
  simp [highBarrierLabelSet] at hb
  rcases hb with hb | hb | hb | hb
  · subst hb
    simp
  · subst hb
    rw [hb₁prime.coprime_iff_not_dvd]
    intro hdiv
    exact (havoid _ hb₁prime hdiv).1 rfl
  · subst hb
    rw [hb₂prime.coprime_iff_not_dvd]
    intro hdiv
    exact (havoid _ hb₂prime hdiv).2.1 rfl
  · subst hb
    rw [hb₃prime.coprime_iff_not_dvd]
    intro hdiv
    exact (havoid _ hb₃prime hdiv).2.2 rfl

/--
Reusable complementary-support pack for the live `Γ(Z_p × Z_25)` headline slice.
If `a ∈ A₀`, `b ∈ {1, b₁, b₂, b₃}`, and the prime support of `c` avoids both
`{2,3}` and the barrier primes `{b₁, b₂, b₃}`, then `c` is automatically
coprime to both `a` and `b`.
-/
theorem complementary_support_pack_lemma
    {a b₁ b₂ b₃ b c : ℕ}
    (ha : a ∈ fixedA0LabelSet)
    (hb₁prime : Nat.Prime b₁)
    (hb₂prime : Nat.Prime b₂)
    (hb₃prime : Nat.Prime b₃)
    (hb : b ∈ highBarrierLabelSet b₁ b₂ b₃)
    (havoid23 : ∀ q, q.Prime → q ∣ c → q ≠ 2 ∧ q ≠ 3)
    (havoidBarrier : ∀ q, q.Prime → q ∣ c → q ≠ b₁ ∧ q ≠ b₂ ∧ q ≠ b₃) :
    Nat.Coprime a c ∧ Nat.Coprime b c := by
  refine ⟨?_, ?_⟩
  · exact coprime_of_mem_fixedA0_of_support_avoids_two_three ha havoid23
  · exact coprime_to_high_barrier_of_support_avoids_barrier_primes
      hb₁prime hb₂prime hb₃prime hb havoidBarrier

/--
Checked theorem-slice skeleton for the live complementary-support
`Γ(Z_p × Z_25)` wrapper. The fixed `A₀`, high-barrier `B`, complementary-support
`C`, and residual `D` packages automatically discharge the `A-C`, `B-C`, and
`B-D` interfaces; the only remaining input to the exact ring bridge is the
explicit `B-B` clique hypothesis on the chosen barrier labels.
-/
theorem zp_z25_high_barrier_complementary_support_wrapper_skeleton
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
  exact zp_z25_four_interface_companion_theorem_of_label_sets
    label
    (fixedA0LabelSet : Set ℕ)
    (highBarrierLabelSet b₁ b₂ b₃)
    C_lab
    D_lab
    hA_mem
    hB_mem
    hC_mem
    hD_mem
    (by
      intro a c ha hc
      have ha' : a ∈ fixedA0LabelSet := ha
      exact coprime_of_mem_fixedA0_of_support_avoids_two_three ha' (hC_avoid23 c hc))
    hBB
    (by
      intro b c hb hc
      exact coprime_to_high_barrier_of_support_avoids_barrier_primes
        hb₁prime hb₂prime hb₃prime hb (hC_avoidBarrier c hc))
    (by
      intro b d hb hd
      exact high_barrier_set_coprime_of_mem_of_not_mem
        hb₁prime hb₂prime hb₃prime hb₁half hb₂half hb₃half
        hb (hD_interval d hd) (hD_out d hd))

/--
Graph-faithful theorem-slice skeleton for the live complementary-support
`Γ(Z_p × Z_25)` wrapper. It discharges the `A-C`, `B-C`, and `B-D` interfaces
exactly as before, but only asks for the remaining `B-B` coprimality clause on
distinct barrier vertices.
-/
theorem zp_z25_high_barrier_complementary_support_wrapper_graph_skeleton
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
  exact zp_z25_four_interface_companion_theorem_on_distinct_vertices
    label
    (by
      intro x y hx hy
      exact coprime_of_mem_fixedA0_of_support_avoids_two_three
        (hA_mem x hx) (hC_avoid23 (label y) (hC_mem y hy)))
    hBB
    (by
      intro x y hx hy
      exact coprime_to_high_barrier_of_support_avoids_barrier_primes
        hb₁prime hb₂prime hb₃prime (hB_mem x hx) (hC_avoidBarrier (label y) (hC_mem y hy)))
    (by
      intro x y hx hy
      exact high_barrier_set_coprime_of_mem_of_not_mem
        hb₁prime hb₂prime hb₃prime hb₁half hb₂half hb₃half
        (hB_mem x hx) (hD_interval (label y) (hD_mem y hy)) (hD_out (label y) (hD_mem y hy)))

/--
Distinct labels inside the barrier set `{1, b₁, b₂, b₃}` are pairwise coprime
once `b₁`, `b₂`, and `b₃` are pairwise distinct primes.
-/
theorem high_barrier_pairwise_coprime_of_mem_of_ne
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
  simp [highBarrierLabelSet] at hb hb'
  rcases hb with rfl | rfl | rfl | rfl <;>
    rcases hb' with rfl | rfl | rfl | rfl
  · simp
  · simp
  · simp
  · simp
  · simp
  · exact False.elim (hneq rfl)
  · exact (Nat.coprime_primes hb₁prime hb₂prime).2 hb₁₂
  · exact (Nat.coprime_primes hb₁prime hb₃prime).2 hb₁₃
  · simp
  · exact (Nat.coprime_primes hb₂prime hb₁prime).2 hb₁₂.symm
  · exact False.elim (hneq rfl)
  · exact (Nat.coprime_primes hb₂prime hb₃prime).2 hb₂₃
  · simp
  · exact (Nat.coprime_primes hb₃prime hb₁prime).2 hb₁₃.symm
  · exact (Nat.coprime_primes hb₃prime hb₂prime).2 hb₂₃.symm
  · exact False.elim (hneq rfl)

/--
Barrier-clique discharge for the graph-faithful `F25` wrapper.
If the barrier labels lie in `{1, b₁, b₂, b₃}` and the labeling is injective,
then distinct `B`-class vertices automatically satisfy the remaining `B-B`
coprimality obligation.
-/
theorem high_barrier_BB_coprime_of_injective
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
  intro x y hx hy hxy
  apply high_barrier_pairwise_coprime_of_mem_of_ne
    hb₁prime hb₂prime hb₃prime hb₁₂ hb₁₃ hb₂₃
    (hB_mem x hx) (hB_mem y hy)
  intro hlabel
  exact hxy (hinj hlabel)

/--
Final graph-faithful wrapper theorem for the current complementary-support `F25`
slice, under the honest extra hypothesis actually needed by the campaign:
injective labeling on the barrier clique.
-/
theorem zp_z25_high_barrier_complementary_support_wrapper_graph_of_injective
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
  exact zp_z25_high_barrier_complementary_support_wrapper_graph_skeleton
    label b₁ b₂ b₃ C_lab D_lab
    hb₁prime hb₂prime hb₃prime
    hb₁half hb₂half hb₃half
    hA_mem hB_mem hC_mem hD_mem
    hC_avoid23 hC_avoidBarrier
    hD_interval hD_out
    (high_barrier_BB_coprime_of_injective
      label b₁ b₂ b₃
      hb₁prime hb₂prime hb₃prime
      hb₁₂ hb₁₃ hb₂₃ hinj hB_mem)

/--
The fixed complementary-support window `C₀` used by the preserved late-range
`Γ(Z_p × Z_25)` arithmetic front:
`C₀ = {n : 2 ≤ n ≤ 291 and gcd(n, 6) = 1}`.
-/
def fixedC0LabelSet : Set ℕ :=
  {n | n ∈ Finset.Icc 2 291 ∧ Nat.Coprime n 6}

/--
Finite counting surface for the fixed complementary-support window `C₀`.
This packages the exact preserved late-range data into a concrete finset for
the counted `C`-supply step.
-/
def fixedC0Finset : Finset ℕ :=
  (Finset.Icc 2 291).filter fun n => Nat.Coprime n 6

/--
Membership in the counted finset `fixedC0Finset` is exactly membership in the
set-level wrapper language `fixedC0LabelSet`.
-/
theorem mem_fixedC0Finset_iff
    {c : ℕ} :
    c ∈ fixedC0Finset ↔ c ∈ fixedC0LabelSet := by
  simp [fixedC0Finset, fixedC0LabelSet]

/--
Exact size of the preserved complementary-support window `C₀`.
This is the counted late-range supply behind the fixed-data `F25` wrapper
through the current `p ≤ 97` publication window.
-/
theorem fixedC0_card_eq_96 :
    fixedC0Finset.card = 96 := by
  native_decide

/--
Uniform counted `C₀`-supply for the fixed-data publication window.
Through `p ≤ 97`, the frozen complementary-support reservoir `C₀` contains at
least `p - 1` labels, which is exactly the size of the `C` support class in
`Γ(Z_p × Z_25)`.
-/
theorem fixedC0_card_ge_C_size_of_p_le_97
    {p : ℕ}
    (hp97 : p ≤ 97) :
    p - 1 ≤ fixedC0Finset.card := by
  rw [fixedC0_card_eq_96]
  omega

/--
Subset-selection packaging for the fixed complementary-support window `C₀`.
Whenever a requested size `n` is bounded by the counted reservoir
`fixedC0Finset.card`, one can choose an actual `n`-element sub-finset of
`fixedC0Finset`.
-/
theorem exists_fixedC0Finset_subset_card_eq
    {n : ℕ}
    (hn : n ≤ fixedC0Finset.card) :
    ∃ S : Finset ℕ, S ⊆ fixedC0Finset ∧ S.card = n := by
  exact Finset.exists_subset_card_eq hn

/--
Fixed-window subset-selection package for the preserved `Γ(Z_p × Z_25)` range.
Through `p ≤ 97`, the counted reservoir `C₀` contains an actual `p - 1` element
sub-finset, matching the size of the `C` support class.
-/
theorem exists_fixedC0_subset_card_eq_C_size_of_p_le_97
    {p : ℕ}
    (hp97 : p ≤ 97) :
    ∃ S : Finset ℕ, S ⊆ fixedC0Finset ∧ S.card = p - 1 := by
  exact exists_fixedC0Finset_subset_card_eq
    (fixedC0_card_ge_C_size_of_p_le_97 hp97)

private theorem mem_Icc_2_291_of_mem_fixedC0LabelSet
    {c : ℕ} (hc : c ∈ fixedC0LabelSet) :
    c ∈ Finset.Icc 2 291 := by
  exact hc.1

private theorem coprime_six_of_mem_fixedC0LabelSet
    {c : ℕ} (hc : c ∈ fixedC0LabelSet) :
    Nat.Coprime c 6 := by
  exact hc.2

/--
Availability of the fixed complementary-support window `C₀` in the preserved
late `F25` regime: once `p ≥ 59`, every label in `C₀` lies inside the active
interval `{1, ..., 5p + 19}`.
-/
theorem fixedC0_available_of_p_ge_59
    {p c : ℕ}
    (hp : 59 ≤ p)
    (hc : c ∈ fixedC0LabelSet) :
    c ∈ Finset.Icc 1 (f25LabelBound p) := by
  have hc2 : 2 ≤ c := (Finset.mem_Icc.mp (mem_Icc_2_291_of_mem_fixedC0LabelSet hc)).1
  have hc291 : c ≤ 291 := (Finset.mem_Icc.mp (mem_Icc_2_291_of_mem_fixedC0LabelSet hc)).2
  refine Finset.mem_Icc.mpr ⟨?_, ?_⟩
  · omega
  · dsimp [f25LabelBound]
    omega

/--
Every prime divisor of a label in the fixed window `C₀` avoids `{2, 3}`.
This is the exact support-avoidance fact needed for the `A-C` and `B-C`
discharge inside the late fixed-data `F25` wrapper.
-/
theorem fixedC0_support_avoids_two_three
    {c q : ℕ}
    (hc : c ∈ fixedC0LabelSet)
    (hq : q.Prime)
    (hqc : q ∣ c) :
    q ≠ 2 ∧ q ≠ 3 := by
  have hc2 : c.Coprime 2 :=
    Nat.Coprime.coprime_dvd_right (by decide : 2 ∣ 6)
      (coprime_six_of_mem_fixedC0LabelSet hc)
  have hc3 : c.Coprime 3 :=
    Nat.Coprime.coprime_dvd_right (by decide : 3 ∣ 6)
      (coprime_six_of_mem_fixedC0LabelSet hc)
  constructor
  · intro hq2
    subst hq2
    exact ((Nat.prime_two.coprime_iff_not_dvd).1 (Nat.coprime_comm.mp hc2)) hqc
  · intro hq3
    subst hq3
    exact (((by decide : Nat.Prime 3).coprime_iff_not_dvd).1 (Nat.coprime_comm.mp hc3)) hqc

/--
Every prime divisor of a label in `C₀` automatically avoids the preserved
late-range barrier primes `293`, `307`, and `311`, because every `C₀` label
lies below `292`.
-/
theorem fixedC0_support_avoids_high_barrier_293_307_311
    {c q : ℕ}
    (hc : c ∈ fixedC0LabelSet)
    (_hq : q.Prime)
    (hqc : q ∣ c) :
    q ≠ 293 ∧ q ≠ 307 ∧ q ≠ 311 := by
  have hc291 : c ≤ 291 := by
    exact (Finset.mem_Icc.mp (mem_Icc_2_291_of_mem_fixedC0LabelSet hc)).2
  have hcpos : 0 < c := by
    have hc2 : 2 ≤ c := (Finset.mem_Icc.mp (mem_Icc_2_291_of_mem_fixedC0LabelSet hc)).1
    omega
  constructor
  · intro hq293
    subst hq293
    have hle : 293 ≤ c := Nat.le_of_dvd hcpos hqc
    omega
  constructor
  · intro hq307
    subst hq307
    have hle : 307 ≤ c := Nat.le_of_dvd hcpos hqc
    omega
  · intro hq311
    subst hq311
    have hle : 311 ≤ c := Nat.le_of_dvd hcpos hqc
    omega

/--
In the preserved fixed-data window `p ≤ 97`, the barrier primes
`293`, `307`, and `311` all lie above half the active interval
`{1, ..., 5p + 19}`.
-/
theorem high_barrier_half_293_307_311_of_p_le_97
    {p : ℕ} (hp : p ≤ 97) :
    f25LabelBound p < 2 * 293 ∧
      f25LabelBound p < 2 * 307 ∧
      f25LabelBound p < 2 * 311 := by
  dsimp [f25LabelBound]
  omega

/--
Fixed-data graph-faithful wrapper skeleton for the preserved late `F25` window.
For every prime `p ≤ 97`, once the `A` class is frozen in `A₀`, the `B` class
is frozen in `{1, 293, 307, 311}`, and the `C` class is frozen inside
`C₀ = {n : 2 ≤ n ≤ 291 and gcd(n, 6) = 1}`, the remaining graph proof reduces
exactly to injectivity plus the residual `D`-class interval / barrier-exclusion
checks already present in the generic wrapper theorem.
-/
theorem zp_z25_fixed_C0_high_barrier_wrapper_graph_skeleton_of_p_le_97
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
      ∀ x, f25SupportPredicate .C x → label x ∈ fixedC0LabelSet)
    (hD_mem :
      ∀ x, f25SupportPredicate .D x → label x ∈ D_lab)
    (hD_interval :
      ∀ d, d ∈ D_lab → d ∈ Finset.Icc 1 (f25LabelBound p))
    (hD_out :
      ∀ d, d ∈ D_lab → d ∉ highBarrierLabelSet 293 307 311) :
    ∀ x y,
      f25ZeroDivisorVertex x → f25ZeroDivisorVertex y → x ≠ y → x * y = 0 →
      Nat.Coprime (label x) (label y) := by
  have h293prime : Nat.Prime 293 := by native_decide
  have h307prime : Nat.Prime 307 := by native_decide
  have h311prime : Nat.Prime 311 := by native_decide
  have h293307 : 293 ≠ 307 := by native_decide
  have h293311 : 293 ≠ 311 := by native_decide
  have h307311 : 307 ≠ 311 := by native_decide
  rcases high_barrier_half_293_307_311_of_p_le_97 hp97 with ⟨h293, h307, h311⟩
  exact zp_z25_high_barrier_complementary_support_wrapper_graph_of_injective
    label 293 307 311 fixedC0LabelSet D_lab
    h293prime h307prime h311prime
    h293 h307 h311
    h293307 h293311 h307311
    hinj
    hA_mem hB_mem hC_mem hD_mem
    (by
      intro c hc q hq hqc
      exact fixedC0_support_avoids_two_three hc hq hqc)
    (by
      intro c hc q hq hqc
      exact fixedC0_support_avoids_high_barrier_293_307_311 hc hq hqc)
    hD_interval hD_out

/-- Exact frozen-wrapper spill count at the preserved `p = 31` boundary. -/
theorem frozen_wrapper_spill_count_at_31 :
    frozenWrapperSpillCount 31 = 19 := by
  native_decide

/-- Exact frozen-wrapper spill count at the first preserved overflow point `p = 37`. -/
theorem frozen_wrapper_spill_count_at_37 :
    frozenWrapperSpillCount 37 = 22 := by
  native_decide

/--
Bounded viability lemma for the frozen wrapper:
through the preserved range `p ≤ 31`, its spill still fits inside the `20`-slot
`A` reservoir.
-/
theorem frozen_wrapper_fits_A_reservoir_of_le_31
    {p : ℕ} (hp : p ≤ 31) :
    frozenWrapperFitsAReservoir p := by
  dsimp [frozenWrapperFitsAReservoir]
  interval_cases p <;> native_decide

/-- The preserved frozen wrapper already overflows the `A` reservoir at `p = 37`. -/
theorem frozen_wrapper_overflows_A_reservoir_at_37 :
    ¬ frozenWrapperFitsAReservoir 37 := by
  dsimp [frozenWrapperFitsAReservoir]
  native_decide

/--
The bounded boundary package used by the `zero_divisor_prime_labelings` family campaign:
the frozen wrapper fits through `p = 31`, has exact spill `19` there, and has exact
spill `22` at `p = 37`, where it first overflows the `20` labels of `A` in the
preserved campaign record.
-/
theorem frozen_wrapper_boundary_31_37 :
    frozenWrapperFitsAReservoir 31 ∧
      frozenWrapperSpillCount 31 = 19 ∧
      frozenWrapperSpillCount 37 = 22 ∧
      ¬ frozenWrapperFitsAReservoir 37 := by
  refine ⟨?_, frozen_wrapper_spill_count_at_31, frozen_wrapper_spill_count_at_37, ?_⟩
  · exact frozen_wrapper_fits_A_reservoir_of_le_31 (by decide)
  · exact frozen_wrapper_overflows_A_reservoir_at_37

end ZeroDivisorF25FrozenWrapper
end Families
end AutoMath
