namespace AutoMath
namespace Families
namespace CNBCQuinticRouteI

/-!
Route I for the `cnbc_quintic_nonexistence` campaign is the structural implication

`nowhere-zero symbol -> trivial kernel -> no CNBC coloring`.

The Fourier diagonalization and the nowhere-zero-symbol lemma are still missing. This file records
the strongest honest checked shell available in the current worktree:

* the exact six-term CNB-to-kernel translation, written directly on the six closed-neighborhood
  vertices `{v, v + a, v + b, v + m, v - a, v - b}`
* the reusable Route I closure theorem `routeI_of_trivialKernel`

No new axioms, `sorry`, or placeholders are introduced here.
-/

abbrev Vertex (n : Nat) := Fin n

inductive Color where
  | red
  | blue
deriving DecidableEq, Repr

abbrev Coloring (n : Nat) := Vertex n → Color

def signedColor : Color → Int
  | Color.red => 1
  | Color.blue => -1

def redWeight : Color → Nat
  | Color.red => 1
  | Color.blue => 0

def signed {n : Nat} (color : Coloring n) (v : Vertex n) : Int :=
  signedColor (color v)

def shift {n : Nat} (v : Vertex n) (k : Nat) : Vertex n := by
  refine ⟨(v.val + k) % n, ?_⟩
  have hn : 0 < n :=
    Nat.lt_of_lt_of_le (Nat.succ_pos v.val) (Nat.succ_le_of_lt v.isLt)
  exact Nat.mod_lt _ hn

/-- The exact six-term red count on the closed-neighborhood mask `{0, ±a, ±b, m}`. Under the
standing distinctness regime `1 <= a < b < m` with `n = 2m`, this is the literal CNB count on the
closed neighborhood. -/
def quinticClosedNeighborhoodRedCount
    (n a b m : Nat) (color : Coloring n) (v : Vertex n) : Nat :=
  redWeight (color v) +
    redWeight (color (shift v a)) +
    redWeight (color (shift v b)) +
    redWeight (color (shift v m)) +
    redWeight (color (shift v (n - a))) +
    redWeight (color (shift v (n - b)))

/-- Family-level CNBC predicate for the quintic circulant mask `{0, ±a, ±b, m}`. -/
def IsQuinticCNBColoring (n a b m : Nat) (color : Coloring n) : Prop :=
  ∀ v, quinticClosedNeighborhoodRedCount n a b m color v = 3

/-- The existential Route I target before the Fourier obstruction is applied. -/
def intendedStatement (n a b m : Nat) : Prop :=
  ∃ color : Coloring n, IsQuinticCNBColoring n a b m color

theorem signed_ne_zero {n : Nat} (color : Coloring n) (v : Vertex n) :
    signed color v ≠ 0 := by
  cases h : color v <;> simp [signed, signedColor, h]

/-- Integer-valued kernel witness for the six-term quintic closed-neighborhood operator. -/
def QuinticKernelWitness (n a b m : Nat) (x : Vertex n → Int) : Prop :=
  ∀ v,
    x v +
        x (shift v a) +
        x (shift v b) +
        x (shift v m) +
        x (shift v (n - a)) +
        x (shift v (n - b)) = 0

/-- Route I rules out CNBC by showing the six-term integer kernel contains no nonzero witness. -/
def NoNonzeroQuinticKernel (n a b m : Nat) : Prop :=
  ¬ ∃ x : Vertex n → Int, x ≠ (fun _ => (0 : Int)) ∧ QuinticKernelWitness n a b m x

/-- This is the family-level kernel triviality criterion that the future Fourier diagonalization is
expected to supply from the nowhere-zero symbol hypothesis. -/
def TrivialQuinticKernel (n a b m : Nat) : Prop :=
  ∀ x : Vertex n → Int, QuinticKernelWitness n a b m x → x = (fun _ => (0 : Int))

theorem six_signed_sum_zero_of_three_red
    (c0 c1 c2 c3 c4 c5 : Color) :
    redWeight c0 +
        redWeight c1 +
        redWeight c2 +
        redWeight c3 +
        redWeight c4 +
        redWeight c5 = 3 →
      signedColor c0 +
          signedColor c1 +
          signedColor c2 +
          signedColor c3 +
          signedColor c4 +
          signedColor c5 = 0 := by
  cases c0 <;> cases c1 <;> cases c2 <;> cases c3 <;> cases c4 <;> cases c5 <;> decide

/-- Any CNBC coloring for the six-term quintic mask yields the zero signed relation at every
vertex. This is the exact CNB-to-kernel translation needed before the missing Fourier step enters.
-/
theorem quintic_signed_sum_zero_of_cnb
    {n a b m : Nat}
    (color : Coloring n)
    (hcolor : IsQuinticCNBColoring n a b m color) :
    QuinticKernelWitness n a b m (fun w => signed color w) := by
  intro v
  simpa [IsQuinticCNBColoring, QuinticKernelWitness, quinticClosedNeighborhoodRedCount, signed]
    using
      (six_signed_sum_zero_of_three_red
        (color v)
        (color (shift v a))
        (color (shift v b))
        (color (shift v m))
        (color (shift v (n - a)))
        (color (shift v (n - b)))
        (hcolor v))

/-- A quintic CNBC coloring produces a nonzero integer kernel witness for the six-term
closed-neighborhood operator. This is the reusable family lemma that the Route I skeleton consumes
before the Fourier-side invertibility argument is plugged in. -/
theorem kernel_witness_of_intendedStatement
    {n a b m : Nat}
    (hn : 0 < n)
    (hExists : intendedStatement n a b m) :
    ∃ x : Vertex n → Int,
        x ≠ (fun _ => (0 : Int)) ∧
          QuinticKernelWitness n a b m x := by
  rcases hExists with ⟨color, hcolor⟩
  refine ⟨fun v => signed color v, ?_, ?_⟩
  · intro hzero
    let v0 : Vertex n := ⟨0, hn⟩
    have hv0 : signed color v0 = 0 := by
      simpa using congrArg (fun f => f v0) hzero
    exact signed_ne_zero color v0 hv0
  · exact quintic_signed_sum_zero_of_cnb color hcolor

/-- A pointwise triviality statement for the six-term integer kernel immediately rules out any
nonzero kernel witness. This is the reusable bridge from future Fourier work back to the existing
Route I skeleton. -/
theorem no_nonzero_quintic_kernel_of_trivial_kernel
    {n a b m : Nat}
    (htrivial : TrivialQuinticKernel n a b m) :
    NoNonzeroQuinticKernel n a b m := by
  unfold NoNonzeroQuinticKernel
  intro hx
  rcases hx with ⟨x, hxne, hxkernel⟩
  exact hxne (htrivial x hxkernel)

/--
Proof skeleton for the intended Route I theorem slice:

```lean
theorem routeI_of_trivialKernel
    {n a b m : Nat}
    (hn : 0 < n)
    (htrivial : TrivialQuinticKernel n a b m) :
    ¬ intendedStatement n a b m := by
  intro hExists
  obtain ⟨x, hxne, hxkernel⟩ := kernel_witness_of_intendedStatement hn hExists
  exact hxne (htrivial x hxkernel)
```
-/
theorem routeI_spectral_obstruction_skeleton
    {n a b m : Nat}
    (hn : 0 < n)
    (hkernel : NoNonzeroQuinticKernel n a b m) :
    ¬ intendedStatement n a b m := by
  intro hExists
  exact hkernel (kernel_witness_of_intendedStatement hn hExists)

/-- Once the family Fourier argument proves that the six-term integer kernel is trivial, the Route
I theorem slice closes immediately. This is the strongest honest checked Lean target preserved in
the current worktree without claiming the Fourier diagonalization is already formalized. -/
theorem routeI_of_trivialKernel
    {n a b m : Nat}
    (hn : 0 < n)
    (htrivial : TrivialQuinticKernel n a b m) :
    ¬ intendedStatement n a b m := by
  apply routeI_spectral_obstruction_skeleton hn
  exact no_nonzero_quintic_kernel_of_trivial_kernel htrivial

end CNBCQuinticRouteI
end Families
end AutoMath
