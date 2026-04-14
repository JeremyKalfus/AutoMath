import Mathlib

namespace AutoMath
namespace RB8B10BookRamsey

open SimpleGraph

/--
Lean target for the current packet-sealing attempt:
the strongly regular obstruction forced by the verified artifact cannot exist.

This is the sharp reusable theorem slice extracted from the `R(B8, B10)` argument.
If a `37`-vertex witness avoiding `B8` and complement-`B10` exists, the solve and verify
artifacts show it must induce an `srg(37,18,7,10)`.
-/
def intendedStatement : Prop :=
  ∀ {V : Type} [Fintype V] [DecidableEq V] (G : SimpleGraph V) [DecidableRel G.Adj],
    ¬ G.IsSRGWith 37 18 7 10

/-- Faithfulness check: the Lean target is exactly the nonexistence statement for `srg(37,18,7,10)`. -/
theorem rb8b10_book_ramsey_statement :
    intendedStatement ↔
      ∀ {V : Type} [Fintype V] [DecidableEq V] (G : SimpleGraph V) [DecidableRel G.Adj],
        ¬ G.IsSRGWith 37 18 7 10 := by
  rfl

/-- The tuple `(37,18,7,10)` passes the basic strongly-regular parameter equation. -/
theorem parameters_satisfy_basic_srg_identity :
    18 * (18 - 7 - 1) = (37 - 18 - 1) * 10 := by
  norm_num

/-- Specialized strongly-regular adjacency-matrix identity for the forced obstruction parameters. -/
theorem srg_matrix_identity
    {V : Type} [Fintype V] [DecidableEq V] {G : SimpleGraph V} [DecidableRel G.Adj]
    (hG : G.IsSRGWith 37 18 7 10) :
    G.adjMatrix ℤ ^ 2 =
      18 • (1 : Matrix V V ℤ) + 7 • G.adjMatrix ℤ + 10 • Gᶜ.adjMatrix ℤ := by
  simpa using (SimpleGraph.IsSRGWith.matrix_eq (α := ℤ) hG)

/-- Any diagonal entry of an adjacency matrix is zero, so its trace is zero. -/
theorem trace_adjMatrix_zero
    {V : Type} [Fintype V] [DecidableEq V] (G : SimpleGraph V) [DecidableRel G.Adj] :
    Matrix.trace (G.adjMatrix ℤ) = 0 := by
  classical
  simp [Matrix.trace, SimpleGraph.adjMatrix]

/--
Arithmetic contradiction expected from the spectral step.

If the adjacency characteristic polynomial had only one linear `18`-factor contribution and
quadratic `x^2 + 3x - 8` contributions, then the degree and trace equations would be incompatible.
This is the final arithmetic check once the missing spectral/minpoly factorization lemma is in place.
-/
theorem spectral_factor_count_impossible
    {a b : Int}
    (hdeg : a + 2 * b = 37)
    (htrace : 18 * a - 3 * b = 0) : False := by
  omega

/--
Proof skeleton for the intended strongly-regular obstruction.

To finish the proof, it remains to formalize the spectral/minpoly step that turns the verified
matrix identity into the degree/trace factor-count equations appearing in
`spectral_factor_count_impossible`.

Concretely, the missing Lean ingredient is:

1. an annihilating-polynomial or minpoly argument for the adjacency matrix of a hypothetical
   `srg(37,18,7,10)`,
2. a derivation that only one linear `18`-factor and quadratic `x^2 + 3x - 8` factors can occur,
3. the induced equations `a + 2 b = 37` and `18 a - 3 b = 0`.
-/
theorem srg_37_18_7_10_nonexistence_skeleton
    (h_spectral :
      ∀ {V : Type} [Fintype V] [DecidableEq V] (G : SimpleGraph V) [DecidableRel G.Adj],
        G.IsSRGWith 37 18 7 10 →
          ∃ a b : Int, a + 2 * b = 37 ∧ 18 * a - 3 * b = 0) :
    intendedStatement := by
  intro V _ _ G _instAdj hG
  obtain ⟨a, b, hdeg, htrace⟩ := h_spectral (G := G) hG
  exact spectral_factor_count_impossible hdeg htrace

end RB8B10BookRamsey
end AutoMath
