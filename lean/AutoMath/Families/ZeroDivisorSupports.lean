import Mathlib.Data.Fintype.Basic

namespace AutoMath
namespace Families
namespace ZeroDivisorSupports

/-
These support-level lemmas intentionally formalize the coordinatewise zero-product logic that
drives the two active zero-divisor publication campaigns. They do not yet classify full ring
elements into support classes; instead they pin down the exact support graphs once the class labels
`A,B,C,D` and `A,B,C,D,E,F` are fixed from the ring law.
-/

inductive BinaryCoordSupport where
  | zero
  | nonzero
deriving DecidableEq, Repr

def fieldCoordZeroMul : BinaryCoordSupport → BinaryCoordSupport → Prop
  | .zero, _ => True
  | _, .zero => True
  | .nonzero, .nonzero => False

inductive Z25CoordSupport where
  | zero
  | nonzeroFive
  | unit
deriving DecidableEq, Repr

def fieldCoordZeroMulB : BinaryCoordSupport → BinaryCoordSupport → Bool
  | .zero, _ => true
  | _, .zero => true
  | .nonzero, .nonzero => false

def z25CoordZeroMulB : Z25CoordSupport → Z25CoordSupport → Bool
  | .zero, _ => true
  | _, .zero => true
  | .nonzeroFive, .nonzeroFive => true
  | .nonzeroFive, .unit => false
  | .unit, .nonzeroFive => false
  | .unit, .unit => false

inductive F25Support where
  | A
  | B
  | C
  | D
deriving DecidableEq, Repr

def f25FirstCoordSupport : F25Support → BinaryCoordSupport
  | .A => .zero
  | .B => .zero
  | .C => .nonzero
  | .D => .nonzero

def f25SecondCoordSupport : F25Support → Z25CoordSupport
  | .A => .unit
  | .B => .nonzeroFive
  | .C => .zero
  | .D => .nonzeroFive

/-- Support-level zero-product relation for the `Γ(Z_p × Z_25)` campaign. This is the actual
ring-law condition after collapsing a vertex to the two coordinate support types it carries. -/
def f25SupportAdj (x y : F25Support) : Prop :=
  fieldCoordZeroMulB (f25FirstCoordSupport x) (f25FirstCoordSupport y) = true ∧
    z25CoordZeroMulB (f25SecondCoordSupport x) (f25SecondCoordSupport y) = true

/-- The four-class zero-divisor support graph for `Γ(Z_p × Z_25)` has exactly the edge types
`A-C`, `B-B`, `B-C`, and `B-D`, together with their reversals. -/
theorem support_decomposition_F25 (x y : F25Support) :
    f25SupportAdj x y ↔
      ((x = F25Support.A ∧ y = F25Support.C) ∨
       (x = F25Support.C ∧ y = F25Support.A) ∨
       (x = F25Support.B ∧ y = F25Support.B) ∨
       (x = F25Support.B ∧ y = F25Support.C) ∨
       (x = F25Support.C ∧ y = F25Support.B) ∨
       (x = F25Support.B ∧ y = F25Support.D) ∨
       (x = F25Support.D ∧ y = F25Support.B)) := by
  cases x <;> cases y <;>
    simp [f25SupportAdj, f25FirstCoordSupport, f25SecondCoordSupport, fieldCoordZeroMulB, z25CoordZeroMulB]

inductive F2Support where
  | A
  | B
  | C
  | D
  | E
  | F
deriving DecidableEq, Repr

def f2FirstCoordSupport : F2Support → BinaryCoordSupport
  | .A => .nonzero
  | .B => .zero
  | .C => .zero
  | .D => .nonzero
  | .E => .nonzero
  | .F => .zero

def f2SecondCoordSupport : F2Support → BinaryCoordSupport
  | .A => .zero
  | .B => .nonzero
  | .C => .zero
  | .D => .nonzero
  | .E => .zero
  | .F => .nonzero

def f2ThirdCoordSupport : F2Support → BinaryCoordSupport
  | .A => .zero
  | .B => .zero
  | .C => .nonzero
  | .D => .zero
  | .E => .nonzero
  | .F => .nonzero

/-- Support-level zero-product relation for the `Γ(Z_p × Z_p × Z_2)` campaign. Because each factor
is a field, this is exactly support disjointness across the three coordinates. -/
def f2SupportAdj (x y : F2Support) : Prop :=
  fieldCoordZeroMulB (f2FirstCoordSupport x) (f2FirstCoordSupport y) = true ∧
    fieldCoordZeroMulB (f2SecondCoordSupport x) (f2SecondCoordSupport y) = true ∧
    fieldCoordZeroMulB (f2ThirdCoordSupport x) (f2ThirdCoordSupport y) = true

/-- The six-class zero-divisor support graph for `Γ(Z_p × Z_p × Z_2)` has exactly the edge types
`A-B`, `A-C`, `A-F`, `B-C`, `B-E`, and `C-D`, together with their reversals. -/
theorem support_decomposition_F2 (x y : F2Support) :
    f2SupportAdj x y ↔
      ((x = F2Support.A ∧ y = F2Support.B) ∨
       (x = F2Support.B ∧ y = F2Support.A) ∨
       (x = F2Support.A ∧ y = F2Support.C) ∨
       (x = F2Support.C ∧ y = F2Support.A) ∨
       (x = F2Support.A ∧ y = F2Support.F) ∨
       (x = F2Support.F ∧ y = F2Support.A) ∨
       (x = F2Support.B ∧ y = F2Support.C) ∨
       (x = F2Support.C ∧ y = F2Support.B) ∨
       (x = F2Support.B ∧ y = F2Support.E) ∨
       (x = F2Support.E ∧ y = F2Support.B) ∨
       (x = F2Support.C ∧ y = F2Support.D) ∨
       (x = F2Support.D ∧ y = F2Support.C)) := by
  cases x <;> cases y <;>
    simp [f2SupportAdj, f2FirstCoordSupport, f2SecondCoordSupport, f2ThirdCoordSupport, fieldCoordZeroMulB]

/-- Generic support-template transport lemma: once adjacency factors through a finite support graph,
classwise coprimality on support-adjacent classes is enough. -/
theorem classwise_template_lemma
    {V S : Type*}
    (Adj : V → V → Prop)
    (support : V → S)
    (SupportAdj : S → S → Prop)
    (label : V → Nat)
    (hAdj :
      ∀ x y, Adj x y → SupportAdj (support x) (support y))
    (hSupportCoprime :
      ∀ s t, SupportAdj s t →
        ∀ x y, support x = s → support y = t → Nat.Coprime (label x) (label y)) :
    ∀ x y, Adj x y → Nat.Coprime (label x) (label y) := by
  intro x y hxy
  exact hSupportCoprime (support x) (support y) (hAdj x y hxy) x y rfl rfl

end ZeroDivisorSupports
end Families
end AutoMath
