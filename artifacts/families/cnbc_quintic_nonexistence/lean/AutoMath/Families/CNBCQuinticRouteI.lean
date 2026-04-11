import AutoMath.Families.CNBCCriteria

namespace AutoMath
namespace Families
namespace CNBCQuinticRouteI

open Finset
open scoped BigOperators
open CNBCCriteria

/-!
Route I for the `cnbc_quintic_nonexistence` campaign is the structural implication

`nowhere-zero symbol -> trivial kernel -> no CNBC coloring`.

This backend file records the family-side pieces that are already honest in the current repo
state: the CNB-to-kernel translation for the six-term quintic mask, together with the theorem-slice
skeleton that will consume the future Fourier / invertibility lemma.
-/

abbrev Vertex (n : Nat) := Fin n

abbrev Coloring (n : Nat) := Vertex n → Color

/-- The closed-neighborhood mask `{0, ±a, ±b, m}` written on `Fin n`. The distinctness of these
six vertices is tracked separately by a cardinality hypothesis. -/
def quinticClosedNeighborhood (n a b m : Nat) (v : Vertex n) : Finset (Vertex n) :=
  [v, v + a, v + b, v + m, v + (n - a), v + (n - b)].toFinset

/-- Family-level CNBC predicate for the quintic circulant mask `{0, ±a, ±b, m}`. -/
def IsQuinticCNBColoring (n a b m : Nat) (color : Coloring n) : Prop :=
  ∀ v, ((quinticClosedNeighborhood n a b m v).filter fun w => color w = Color.red).card = 3

/-- The existential Route I target before the Fourier obstruction is applied. -/
def intendedStatement (n a b m : Nat) : Prop :=
  ∃ color : Coloring n, IsQuinticCNBColoring n a b m color

theorem signed_ne_zero {n : Nat} (color : Coloring n) (v : Vertex n) :
    signed color v ≠ 0 := by
  cases h : color v <;> simp [signed, h]

/-- Any CNBC coloring for the six-term quintic mask yields the zero signed relation at every
vertex, provided the closed neighborhood really has six distinct vertices. This is the family
translation needed before Fourier diagonalization enters. -/
theorem quintic_signed_sum_zero_of_cnb
    {n a b m : Nat}
    (color : Coloring n)
    (hcolor : IsQuinticCNBColoring n a b m color)
    (hcard : ∀ v, (quinticClosedNeighborhood n a b m v).card = 6) :
    ∀ v, (quinticClosedNeighborhood n a b m v).sum (fun w => signed color w) = 0 := by
  intro v
  exact signed_sum_zero_of_half_red color (quinticClosedNeighborhood n a b m v) 3
    (by simpa using hcard v) (hcolor v)

/-- A quintic CNBC coloring produces a nonzero integer kernel witness for the six-term
closed-neighborhood operator. This is the reusable family lemma that the Route I skeleton consumes
before the Fourier-side invertibility argument is plugged in. -/
theorem kernel_witness_of_intendedStatement
    {n a b m : Nat}
    (hn : 0 < n)
    (hcard : ∀ v, (quinticClosedNeighborhood n a b m v).card = 6)
    (hExists : intendedStatement n a b m) :
    ∃ x : Vertex n → Int,
        x ≠ 0 ∧
          ∀ v, (quinticClosedNeighborhood n a b m v).sum (fun w => x w) = 0 := by
  rcases hExists with ⟨color, hcolor⟩
  refine ⟨fun v => signed color v, ?_, ?_⟩
  · intro hzero
    let v0 : Vertex n := ⟨0, hn⟩
    have hv0 : signed color v0 = 0 := by
      exact congrArg (fun f => f v0) hzero
    exact signed_ne_zero color v0 hv0
  · exact quintic_signed_sum_zero_of_cnb color hcolor hcard

/-- The Route I theorem slice reduces to ruling out nonzero integer-valued kernel vectors for the
six-term closed-neighborhood operator. In the intended publication proof, that kernel obstruction
will come from Fourier diagonalization plus the nowhere-zero symbol hypothesis. -/
theorem routeI_spectral_obstruction_skeleton
    {n a b m : Nat}
    (hn : 0 < n)
    (hcard : ∀ v, (quinticClosedNeighborhood n a b m v).card = 6)
    (hkernel :
      ¬ ∃ x : Vertex n → Int,
          x ≠ 0 ∧
            ∀ v, (quinticClosedNeighborhood n a b m v).sum (fun w => x w) = 0) :
    ¬ intendedStatement n a b m := by
  intro hExists
  apply hkernel
  exact kernel_witness_of_intendedStatement hn hcard hExists

end CNBCQuinticRouteI
end Families
end AutoMath
