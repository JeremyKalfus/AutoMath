import Mathlib

namespace AutoMath
namespace RB10B12BookRamsey

open SimpleGraph
open scoped BigOperators Polynomial

/--
Lean target for the current packet-sealing attempt:
the strongly regular obstruction forced by the verified `R(B10, B12)` packet cannot exist.

This is the publication-facing theorem slice extracted from the repaired proof: any `45`-vertex
counterexample would force an `srg(45,22,9,12)`, so ruling out that parameter set seals the sharp
spectral obstruction inside the packet.
-/
def intendedStatement : Prop :=
  ∀ {V : Type} [Fintype V] [DecidableEq V] (G : SimpleGraph V) [DecidableRel G.Adj],
    ¬ G.IsSRGWith 45 22 9 12

/-- Faithfulness check: the Lean target is exactly the nonexistence of `srg(45,22,9,12)`. -/
theorem rb10b12_book_ramsey_statement :
    intendedStatement ↔
      ∀ {V : Type} [Fintype V] [DecidableEq V] (G : SimpleGraph V) [DecidableRel G.Adj],
        ¬ G.IsSRGWith 45 22 9 12 := by
  rfl

/-- The parameter tuple passes the basic strongly regular parameter identity. -/
theorem parameters_satisfy_basic_srg_identity :
    22 * (22 - 9 - 1) = (45 - 22 - 1) * 12 := by
  norm_num

section Obstruction

variable {V : Type} [Fintype V] [DecidableEq V]
variable (G : SimpleGraph V) [DecidableRel G.Adj]

local notation "A" => G.adjMatrix ℝ
local notation "J" => (Matrix.of fun _ _ : V => (1 : ℝ))

theorem adjMatrix_mul_allOnes (hG : G.IsSRGWith 45 22 9 12) :
    A * J = 22 • J := by
  ext v w
  simp [SimpleGraph.adjMatrix_mul_apply, hG.regular.degree_eq]

theorem quadratic_matrix_identity (hG : G.IsSRGWith 45 22 9 12) :
    A ^ 2 + 3 • A - 10 • (1 : Matrix V V ℝ) = 12 • J := by
  have hA2 : A ^ 2 = 22 • (1 : Matrix V V ℝ) + 9 • A + 12 • Gᶜ.adjMatrix ℝ := by
    simpa using (SimpleGraph.IsSRGWith.matrix_eq (α := ℝ) hG)
  have hJ : (1 : Matrix V V ℝ) + A + Gᶜ.adjMatrix ℝ = J := by
    simpa [SimpleGraph.compl_adjMatrix_eq_adjMatrix_compl] using
      (SimpleGraph.one_add_adjMatrix_add_compl_adjMatrix_eq_of_one
        (G := G) (α := ℝ))
  calc
    A ^ 2 + 3 • A - 10 • (1 : Matrix V V ℝ)
        = (22 • (1 : Matrix V V ℝ) + 9 • A + 12 • Gᶜ.adjMatrix ℝ) + 3 • A -
            10 • (1 : Matrix V V ℝ) := by
              rw [hA2]
    _ = 12 • ((1 : Matrix V V ℝ) + A + Gᶜ.adjMatrix ℝ) := by
      ext v w
      simp only [Matrix.add_apply, Matrix.sub_apply, Matrix.smul_apply, Matrix.one_apply]
      ring
    _ = 12 • J := by
      rw [hJ]

theorem cubic_annihilates_adjMatrix (hG : G.IsSRGWith 45 22 9 12) :
    (A - 22 • (1 : Matrix V V ℝ)) * (A ^ 2 + 3 • A - 10 • (1 : Matrix V V ℝ)) = 0 := by
  rw [quadratic_matrix_identity (G := G) hG]
  calc
    (A - 22 • (1 : Matrix V V ℝ)) * (12 • J)
        = 12 • ((A - 22 • (1 : Matrix V V ℝ)) * J) := by
            rw [Matrix.mul_smul]
    _ = 0 := by
      rw [sub_mul, adjMatrix_mul_allOnes (G := G) hG, smul_mul_assoc, one_mul]
      ext v w
      simp only [Matrix.sub_apply, Matrix.smul_apply, Matrix.zero_apply]
      ring

theorem trace_adjMatrix :
    Matrix.trace A = 0 := by
  simp [SimpleGraph.trace_adjMatrix]

theorem trace_adjMatrix_sq (hG : G.IsSRGWith 45 22 9 12) :
    Matrix.trace (A ^ 2) = 990 := by
  calc
    Matrix.trace (A ^ 2)
        = Matrix.trace
            (22 • (1 : Matrix V V ℝ) + 9 • A + 12 • Gᶜ.adjMatrix ℝ) := by
              rw [SimpleGraph.IsSRGWith.matrix_eq (α := ℝ) hG]
    _ = 22 * 45 + 9 * 0 + 12 * 0 := by
      rw [Matrix.trace_add, Matrix.trace_add, Matrix.trace_smul, Matrix.trace_smul,
        Matrix.trace_smul, Matrix.trace_one, SimpleGraph.trace_adjMatrix,
        SimpleGraph.trace_adjMatrix]
      norm_num [hG.card]
    _ = 990 := by norm_num

/--
For a real Hermitian matrix, `trace(A^2)` is the sum of the squared eigenvalues.

This is the exact trace-square bridge needed for the `R(B10,B12)` packet: once the adjacency
eigenvalues are reduced to `{22, 2, -5}`, the remaining contradiction is pure finite arithmetic.
-/
theorem trace_sq_eq_sum_sq_eigenvalues
    {M : Matrix V V ℝ} (hM : M.IsHermitian) :
    Matrix.trace (M ^ 2) = ∑ i, (hM.eigenvalues i) ^ 2 := by
  classical
  let U : Matrix V V ℝ := ↑hM.eigenvectorUnitary
  let D : Matrix V V ℝ := Matrix.diagonal hM.eigenvalues
  have hspec : M = U * D * star U := by
    simpa [U, D, Unitary.conjStarAlgAut_apply] using hM.spectral_theorem
  calc
    Matrix.trace (M ^ 2)
        = Matrix.trace ((U * D * star U) * (U * D * star U)) := by
            simp [hspec, pow_two]
    _ = Matrix.trace (U * (D * (star U * U) * D) * star U) := by
          simp [Matrix.mul_assoc]
    _ = Matrix.trace ((star U * U) * (D * (star U * U) * D)) := by
          rw [Matrix.trace_mul_cycle]
    _ = Matrix.trace (D * D) := by
          simp [U]
    _ = ∑ i, (hM.eigenvalues i) ^ 2 := by
          simp [D, pow_two]

/--
Every adjacency eigenvalue of a hypothetical `srg(45,22,9,12)` lies in `{22, 2, -5}`.

This is the checked local spectral reduction needed by the packet: the cubic annihilator from the
SRG matrix identity forces the full adjacency spectrum into the three roots of
`(x - 22) (x^2 + 3x - 10)`.
-/
theorem adjacency_eigenvalue_cases
    (hG : G.IsSRGWith 45 22 9 12) (i : V) :
    let hH : (G.adjMatrix ℝ).IsHermitian := G.isHermitian_adjMatrix (R := ℝ)
    let lam := hH.eigenvalues i
    lam = 22 ∨ lam = 2 ∨ lam = -5 := by
  classical
  let hH : (G.adjMatrix ℝ).IsHermitian := G.isHermitian_adjMatrix (R := ℝ)
  let lam := hH.eigenvalues i
  let v : V → ℝ := (hH.eigenvectorBasis i).ofLp
  have hv_nonzero : v ≠ 0 := by
    simpa [v] using hH.eigenvectorBasis.orthonormal.ne_zero i
  have hAv : (G.adjMatrix ℝ).mulVec v = lam • v := by
    simp [v, lam, hH.mulVec_eigenvectorBasis]
  have hA2v : (G.adjMatrix ℝ ^ 2).mulVec v = lam ^ 2 • v := by
    calc
      (G.adjMatrix ℝ ^ 2).mulVec v = (G.adjMatrix ℝ).mulVec ((G.adjMatrix ℝ).mulVec v) := by
        simp [pow_two, Matrix.mulVec_mulVec]
      _ = (G.adjMatrix ℝ).mulVec (lam • v) := by
        simp [hAv]
      _ = lam • ((G.adjMatrix ℝ).mulVec v) := by
        rw [Matrix.mulVec_smul]
      _ = lam • (lam • v) := by
        simp [hAv]
      _ = lam ^ 2 • v := by
        simp [pow_two, smul_smul]
  have hqv :
      (G.adjMatrix ℝ ^ 2 + 3 • G.adjMatrix ℝ - 10 • 1).mulVec v =
        (lam ^ 2 + 3 * lam - 10) • v := by
    rw [Matrix.sub_mulVec, Matrix.add_mulVec, Matrix.smul_mulVec, Matrix.smul_mulVec, hA2v, hAv]
    simp [Matrix.one_mulVec]
    ext x
    simp [Pi.mul_def, smul_eq_mul]
    ring
  have hzero :
      ((G.adjMatrix ℝ - 22 • 1) * (G.adjMatrix ℝ ^ 2 + 3 • G.adjMatrix ℝ - 10 • 1)).mulVec v = 0 := by
    simpa using congrArg (fun M => M.mulVec v) (cubic_annihilates_adjMatrix (G := G) hG)
  have hzero' := hzero
  rw [← Matrix.mulVec_mulVec] at hzero'
  rw [hqv] at hzero'
  rw [Matrix.sub_mulVec, Matrix.mulVec_smul, Matrix.smul_mulVec, hAv] at hzero'
  simp [Matrix.one_mulVec] at hzero'
  have hcoord : ∀ x, ((lam - 22) * (lam ^ 2 + 3 * lam - 10)) * v x = 0 := by
    intro x
    have hx := congrFun hzero' x
    simp [Pi.mul_def, smul_eq_mul] at hx
    nlinarith
  have hscalar : ((lam - 22) * (lam ^ 2 + 3 * lam - 10)) • v = 0 := by
    ext x
    simpa [smul_eq_mul] using hcoord x
  have hprod : (lam - 22) * (lam ^ 2 + 3 * lam - 10) = 0 := by
    exact smul_eq_zero.mp hscalar |>.resolve_right hv_nonzero
  have hfac : (lam - 22) * ((lam - 2) * (lam + 5)) = 0 := by
    nlinarith [hprod]
  rcases mul_eq_zero.mp hfac with h22 | hrest
  · left
    linarith
  · rcases mul_eq_zero.mp hrest with h2 | h5
    · right
      left
      linarith
    · right
      right
      linarith

/--
Arithmetic contradiction from the full `45`-slot spectrum, using only the three allowed eigenvalues
`22`, `2`, `-5`, the trace identity, and the trace-square identity.
-/
theorem spectral_counts_impossible
    {h f g : Int}
    (hcard : h + f + g = 45)
    (htrace : 22 * h + 2 * f - 5 * g = 0)
    (htraceSq : 484 * h + 4 * f + 25 * g = 990) : False := by
  omega

/--
Finite-cardinality version of the final obstruction.

If every adjacency eigenvalue belongs to `{22, 2, -5}`, then counting the indices carrying each
value and applying the trace / squared-trace identities yields a contradiction.
-/
theorem no_srg_45_22_9_12 (hG : G.IsSRGWith 45 22 9 12) : False := by
  classical
  let hH : (G.adjMatrix ℝ).IsHermitian := G.isHermitian_adjMatrix (R := ℝ)
  let c22 : ℕ := (Finset.univ.filter fun i => hH.eigenvalues i = 22).card
  let c2 : ℕ := (Finset.univ.filter fun i => hH.eigenvalues i = 2).card
  let cneg5 : ℕ := (Finset.univ.filter fun i => hH.eigenvalues i = -5).card
  have hcases : ∀ i : V,
      hH.eigenvalues i = 22 ∨ hH.eigenvalues i = 2 ∨ hH.eigenvalues i = -5 :=
    by
      intro i
      simpa [hH] using adjacency_eigenvalue_cases (G := G) hG i
  have hcount_point :
      ∀ i : V,
        (if hH.eigenvalues i = 22 then (1 : ℕ) else 0) +
            (if hH.eigenvalues i = 2 then 1 else 0) +
            (if hH.eigenvalues i = -5 then 1 else 0) = 1 := by
    intro i
    rcases hcases i with h22 | h2 | hneg5
    · norm_num [h22]
    · norm_num [h2]
    · norm_num [hneg5]
  have hcard : c22 + c2 + cneg5 = 45 := by
    calc
      c22 + c2 + cneg5
          = ∑ i, ((if hH.eigenvalues i = 22 then (1 : ℕ) else 0) +
              (if hH.eigenvalues i = 2 then 1 else 0) +
              (if hH.eigenvalues i = -5 then 1 else 0)) := by
                simp [c22, c2, cneg5, add_assoc, Finset.sum_add_distrib]
      _ = ∑ _i : V, (1 : ℕ) := by
            refine Finset.sum_congr rfl ?_
            intro i hi
            exact hcount_point i
      _ = 45 := by
            simp [hG.card]
  have htrace_point :
      ∀ i : V,
        hH.eigenvalues i =
          22 * (if hH.eigenvalues i = 22 then (1 : ℝ) else 0) +
            2 * (if hH.eigenvalues i = 2 then 1 else 0) -
            5 * (if hH.eigenvalues i = -5 then 1 else 0) := by
    intro i
    rcases hcases i with h22 | h2 | hneg5
    · norm_num [h22]
    · norm_num [h2]
    · norm_num [hneg5]
  have htrace :
      22 * (c22 : ℝ) + 2 * (c2 : ℝ) - 5 * (cneg5 : ℝ) = 0 := by
    have hsum :
        ∑ i, hH.eigenvalues i = 0 := by
      simpa [hH.trace_eq_sum_eigenvalues] using trace_adjMatrix (G := G)
    have h22sum :
        22 * (c22 : ℝ) = ∑ i, if hH.eigenvalues i = 22 then (22 : ℝ) else 0 := by
      simpa [c22, mul_comm] using
        (Finset.sum_filter (s := Finset.univ) (p := fun i => hH.eigenvalues i = 22)
          (f := fun _ => (22 : ℝ)))
    have h2sum :
        2 * (c2 : ℝ) = ∑ i, if hH.eigenvalues i = 2 then (2 : ℝ) else 0 := by
      simpa [c2, mul_comm] using
        (Finset.sum_filter (s := Finset.univ) (p := fun i => hH.eigenvalues i = 2)
          (f := fun _ => (2 : ℝ)))
    have hneg5sum :
        (-5) * (cneg5 : ℝ) = ∑ i, if hH.eigenvalues i = -5 then (-5 : ℝ) else 0 := by
      simpa [cneg5, mul_comm] using
        (Finset.sum_filter (s := Finset.univ) (p := fun i => hH.eigenvalues i = -5)
          (f := fun _ => (-5 : ℝ)))
    have hneg5sum' :
        -(5 * (cneg5 : ℝ)) = ∑ i, if hH.eigenvalues i = -5 then (-5 : ℝ) else 0 := by
      simpa [neg_mul, mul_comm] using hneg5sum
    have hneg5sumPos :
        (∑ i, if hH.eigenvalues i = -5 then (-5 : ℝ) else 0) =
          -∑ i, if hH.eigenvalues i = -5 then (5 : ℝ) else 0 := by
      have hfun :
          (fun i => if hH.eigenvalues i = -5 then (-5 : ℝ) else 0) =
            fun i => -(if hH.eigenvalues i = -5 then (5 : ℝ) else 0) := by
        funext i
        split_ifs <;> norm_num
      rw [hfun, Finset.sum_neg_distrib]
    calc
      22 * (c22 : ℝ) + 2 * (c2 : ℝ) - 5 * (cneg5 : ℝ)
          = (∑ i, if hH.eigenvalues i = 22 then (22 : ℝ) else 0) +
              (∑ i, if hH.eigenvalues i = 2 then (2 : ℝ) else 0) +
              ∑ i, if hH.eigenvalues i = -5 then (-5 : ℝ) else 0 := by
                rw [sub_eq_add_neg, h22sum, h2sum, hneg5sum']
      _ = ∑ i, (22 * (if hH.eigenvalues i = 22 then (1 : ℝ) else 0) +
              2 * (if hH.eigenvalues i = 2 then 1 else 0) -
              5 * (if hH.eigenvalues i = -5 then 1 else 0)) := by
            rw [hneg5sumPos]
            simp [Finset.sum_add_distrib, add_assoc, sub_eq_add_neg]
      _ = ∑ i, hH.eigenvalues i := by
            refine Finset.sum_congr rfl ?_
            intro i hi
            symm
            exact htrace_point i
      _ = 0 := hsum
  have htraceSq_point :
      ∀ i : V,
        (hH.eigenvalues i) ^ 2 =
          484 * (if hH.eigenvalues i = 22 then (1 : ℝ) else 0) +
            4 * (if hH.eigenvalues i = 2 then 1 else 0) +
            25 * (if hH.eigenvalues i = -5 then 1 else 0) := by
    intro i
    rcases hcases i with h22 | h2 | hneg5
    · norm_num [h22]
    · norm_num [h2]
    · norm_num [hneg5]
  have htraceSq :
      484 * (c22 : ℝ) + 4 * (c2 : ℝ) + 25 * (cneg5 : ℝ) = 990 := by
    have hsum :
        ∑ i, (hH.eigenvalues i) ^ 2 = 990 := by
      simpa [trace_sq_eq_sum_sq_eigenvalues (hM := hH)] using trace_adjMatrix_sq (G := G) hG
    have h22sum :
        484 * (c22 : ℝ) = ∑ i, if hH.eigenvalues i = 22 then (484 : ℝ) else 0 := by
      simpa [c22, mul_comm] using
        (Finset.sum_filter (s := Finset.univ) (p := fun i => hH.eigenvalues i = 22)
          (f := fun _ => (484 : ℝ)))
    have h2sum :
        4 * (c2 : ℝ) = ∑ i, if hH.eigenvalues i = 2 then (4 : ℝ) else 0 := by
      simpa [c2, mul_comm] using
        (Finset.sum_filter (s := Finset.univ) (p := fun i => hH.eigenvalues i = 2)
          (f := fun _ => (4 : ℝ)))
    have hneg5sum :
        25 * (cneg5 : ℝ) = ∑ i, if hH.eigenvalues i = -5 then (25 : ℝ) else 0 := by
      simpa [cneg5, mul_comm] using
        (Finset.sum_filter (s := Finset.univ) (p := fun i => hH.eigenvalues i = -5)
          (f := fun _ => (25 : ℝ)))
    calc
      484 * (c22 : ℝ) + 4 * (c2 : ℝ) + 25 * (cneg5 : ℝ)
          = (∑ i, if hH.eigenvalues i = 22 then (484 : ℝ) else 0) +
              (∑ i, if hH.eigenvalues i = 2 then (4 : ℝ) else 0) +
              ∑ i, if hH.eigenvalues i = -5 then (25 : ℝ) else 0 := by
                rw [h22sum, h2sum, hneg5sum]
      _ = ∑ i, (484 * (if hH.eigenvalues i = 22 then (1 : ℝ) else 0) +
              4 * (if hH.eigenvalues i = 2 then 1 else 0) +
              25 * (if hH.eigenvalues i = -5 then 1 else 0)) := by
            simp [Finset.sum_add_distrib, add_assoc]
      _ = ∑ i, (hH.eigenvalues i) ^ 2 := by
            refine Finset.sum_congr rfl ?_
            intro i hi
            symm
            exact htraceSq_point i
      _ = 990 := hsum
  have hcardInt : (c22 : Int) + (c2 : Int) + (cneg5 : Int) = 45 := by
    exact_mod_cast hcard
  have htraceInt : 22 * (c22 : Int) + 2 * (c2 : Int) - 5 * (cneg5 : Int) = 0 := by
    exact_mod_cast htrace
  have htraceSqInt : 484 * (c22 : Int) + 4 * (c2 : Int) + 25 * (cneg5 : Int) = 990 := by
    exact_mod_cast htraceSq
  exact spectral_counts_impossible hcardInt htraceInt htraceSqInt

theorem srg_45_22_9_12_nonexistence : intendedStatement := by
  intro V _ _ G _ hG
  exact no_srg_45_22_9_12 (G := G) hG

/--
Packet-facing exact theorem slice.

Once the counting argument forces the equality regime

* `|V| = 45`,
* `G` is `22`-regular,
* every edge has exactly `9` common neighbors,
* every nonedge has exactly `12` common neighbors,

the remaining contradiction is fully formal: those hypotheses imply `G.IsSRGWith 45 22 9 12`,
which is impossible by `no_srg_45_22_9_12`.
-/
theorem equality_profile_isSRGWith
    (hcard : Fintype.card V = 45)
    (hreg : G.IsRegularOfDegree 22)
    (hedge : ∀ v w, G.Adj v w → Fintype.card (G.commonNeighbors v w) = 9)
    (hnonedge :
      Pairwise fun v w ↦ ¬ G.Adj v w → Fintype.card (G.commonNeighbors v w) = 12) :
    G.IsSRGWith 45 22 9 12 where
    card := hcard
    regular := hreg
    of_adj := hedge
    of_not_adj := hnonedge

/--
Lean-complete obstruction for the exact equality regime forced at the end of the prose packet.

This theorem does not yet formalize the earlier Goodman/convexity squeeze, nor the conversion from
`11` common nonneighbors on nonedges to `12` common neighbors. It seals the downstream bridge only:
once the packet reaches the exact `(45,22,9,12)` profile, the impossible SRG obstruction is fully
checked.
-/
theorem no_equality_profile_counterexample
    (hcard : Fintype.card V = 45)
    (hreg : G.IsRegularOfDegree 22)
    (hedge : ∀ v w, G.Adj v w → Fintype.card (G.commonNeighbors v w) = 9)
    (hnonedge :
      Pairwise fun v w ↦ ¬ G.Adj v w → Fintype.card (G.commonNeighbors v w) = 12) :
    False := by
  let hSRG : G.IsSRGWith 45 22 9 12 :=
    equality_profile_isSRGWith (G := G) hcard hreg hedge hnonedge
  exact no_srg_45_22_9_12 (G := G) hSRG

end Obstruction

/--
Final arithmetic contradiction once the spectral bridge supplies the multiplicity equations for the
nontrivial eigenvalues `2` and `-5`.
-/
theorem spectral_multiplicities_impossible
    {f g : Int}
    (hcard : f + g = 44)
    (htrace : 22 + 2 * f - 5 * g = 0) : False := by
  omega

/--
Alternative arithmetic contradiction using the squared-trace identity
`trace(A^2) = 22^2 + 2^2 f + (-5)^2 g = 990`.
-/
theorem spectral_square_multiplicities_impossible
    {f g : Int}
    (hcard : f + g = 44)
    (htraceSq : 484 + 4 * f + 25 * g = 990) : False := by
  omega

/--
Proof skeleton for the packet-sealing theorem slice.

To finish the full slice formalization, the remaining Lean work is:

1. transfer the cubic matrix annihilator into a polynomial annihilator of the adjacency linear map,
2. show every adjacency eigenvalue lies in `{22, 2, -5}`,
3. derive the multiplicity equations `f + g = 44` and `22 + 2 f - 5 g = 0`,
4. invoke `spectral_multiplicities_impossible`.
-/
theorem srg_45_22_9_12_nonexistence_skeleton
    (h_spectral :
      ∀ {V : Type} [Fintype V] [DecidableEq V] (G : SimpleGraph V) [DecidableRel G.Adj],
        G.IsSRGWith 45 22 9 12 →
          ∃ f g : Int, f + g = 44 ∧ 22 + 2 * f - 5 * g = 0) :
    intendedStatement := by
  intro V _ _ G _instAdj hG
  obtain ⟨f, g, hcard, htrace⟩ := h_spectral (G := G) hG
  exact spectral_multiplicities_impossible hcard htrace

/--
Variant of the proof skeleton that uses the checked `trace(A^2) = 990` endpoint directly.

This leaves only the spectral extraction step: prove that the nontrivial spectrum consists of
`2` and `-5`, counted with multiplicities `f` and `g`, and that their squared-eigenvalue sum is
captured by `trace(A^2)`.
-/
theorem srg_45_22_9_12_nonexistence_skeleton_via_traceSq
    (h_spectralSq :
      ∀ {V : Type} [Fintype V] [DecidableEq V] (G : SimpleGraph V) [DecidableRel G.Adj],
        G.IsSRGWith 45 22 9 12 →
          ∃ f g : Int, f + g = 44 ∧ 484 + 4 * f + 25 * g = 990) :
    intendedStatement := by
  intro V _ _ G _instAdj hG
  obtain ⟨f, g, hcard, htraceSq⟩ := h_spectralSq (G := G) hG
  exact spectral_square_multiplicities_impossible hcard htraceSq

end RB10B12BookRamsey
end AutoMath
