import Mathlib

namespace AutoMath
namespace Families
namespace CNBCCriteria

open Finset
open scoped BigOperators

inductive Color where
  | red
  | blue
deriving DecidableEq, Repr

/-- Signed encoding of a red/blue coloring. -/
def signed {α : Type*} (color : α → Color) (a : α) : Int :=
  match color a with
  | Color.red => 1
  | Color.blue => -1

/-- On any finite set, the signed sum equals `2 * red_count - card`. This is the reusable algebraic
backbone behind the exact CNBC counterexample files. -/
theorem sum_signed_eq_twice_red_sub_card
    {α : Type*} [DecidableEq α] (color : α → Color) (s : Finset α) :
    s.sum (fun a => signed color a) =
      2 * (((s.filter fun b => color b = Color.red).card : Nat) : Int) - s.card := by
  refine Finset.induction_on s ?_ ?_
  · simp [signed]
  · intro a s ha ih
    cases hca : color a with
    | red =>
        let redSet := s.filter fun b => color b = Color.red
        have ha_redSet : a ∉ redSet := by
          simp [redSet, ha]
        have hfilter :
            (insert a s).filter (fun b => color b = Color.red) = insert a redSet := by
          ext b
          by_cases hb : b = a
          · subst hb
            simp [redSet, hca, ha]
          · simp [redSet, hb]
        have hcard_red : (insert a redSet).card = redSet.card + 1 := by
          simp [ha_redSet]
        have hcard_s : (insert a s).card = s.card + 1 := by
          simp [ha]
        rw [Finset.sum_insert ha, ih, hfilter, hcard_red, hcard_s]
        simp [signed, hca, redSet]
        omega
    | blue =>
        have hfilter :
            (insert a s).filter (fun b => color b = Color.red) = s.filter fun b => color b = Color.red := by
          ext b
          by_cases hb : b = a
          · subst hb
            simp [hca]
          · simp [hb]
        have hcard_s : (insert a s).card = s.card + 1 := by
          simp [ha]
        rw [Finset.sum_insert ha, ih, hfilter, hcard_s]
        simp [signed, hca]
        omega

/-- If exactly half of a finite set is red, the signed sum is zero. -/
theorem signed_sum_zero_of_half_red
    {α : Type*} [DecidableEq α] (color : α → Color) (s : Finset α) (k : Nat)
    (hcard : s.card = 2 * k)
    (hred : (s.filter fun b => color b = Color.red).card = k) :
    s.sum (fun a => signed color a) = 0 := by
  have hsum := sum_signed_eq_twice_red_sub_card color s
  rw [hcard, hred] at hsum
  norm_num at hsum
  simpa using hsum

end CNBCCriteria
end Families
end AutoMath
