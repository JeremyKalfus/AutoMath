import Mathlib

namespace AutoMath
namespace RB8B10BookRamsey

open SimpleGraph
open scoped BigOperators Polynomial

set_option linter.unusedSectionVars false

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

/-- Faithfulness check: the Lean target is exactly the nonexistence of `srg(37,18,7,10)`. -/
theorem rb8b10_book_ramsey_statement :
    intendedStatement ↔
      ∀ {V : Type} [Fintype V] [DecidableEq V] (G : SimpleGraph V) [DecidableRel G.Adj],
        ¬ G.IsSRGWith 37 18 7 10 := by
  rfl

/-- The tuple `(37,18,7,10)` passes the basic strongly-regular parameter identity. -/
theorem parameters_satisfy_basic_srg_identity :
    18 * (18 - 7 - 1) = (37 - 18 - 1) * 10 := by
  norm_num

section Obstruction

variable {V : Type} [Fintype V] [DecidableEq V]
variable (G : SimpleGraph V) [DecidableRel G.Adj]

local notation "A" => G.adjMatrix ℝ
local notation "J" => (Matrix.of fun _ _ : V => (1 : ℝ))
local notation "rPos" => (((-3 : ℝ) + Real.sqrt 41) / 2)
local notation "rNeg" => (((-3 : ℝ) - Real.sqrt 41) / 2)
local notation "rPosSq" => (((25 : ℝ) - 3 * Real.sqrt 41) / 2)
local notation "rNegSq" => (((25 : ℝ) + 3 * Real.sqrt 41) / 2)

private theorem sqrt41_sq : (Real.sqrt 41) ^ 2 = 41 := by
  nlinarith [Real.sq_sqrt (show (0 : ℝ) ≤ 41 by positivity)]

private theorem rPos_ne_18 : rPos ≠ 18 := by
  intro h
  nlinarith [h, sqrt41_sq]

private theorem rNeg_ne_18 : rNeg ≠ 18 := by
  intro h
  nlinarith [h, sqrt41_sq]

private theorem rPos_ne_rNeg : rPos ≠ rNeg := by
  intro h
  nlinarith [h, sqrt41_sq]

private theorem quad_factor (x : ℝ) :
    x ^ 2 + 3 * x - 8 = (x - rPos) * (x - rNeg) := by
  nlinarith [sqrt41_sq]

private theorem rPos_sq : rPos ^ 2 = rPosSq := by
  nlinarith [sqrt41_sq]

private theorem rNeg_sq : rNeg ^ 2 = rNegSq := by
  nlinarith [sqrt41_sq]

/-- In an `srg(37,18,7,10)`, the all-ones vector is an eigenvector with eigenvalue `18`. -/
theorem adjMatrix_mul_allOnes (hG : G.IsSRGWith 37 18 7 10) :
    A * J = 18 • J := by
  ext v w
  simp [SimpleGraph.adjMatrix_mul_apply, hG.regular.degree_eq]

/--
Specialized SRG matrix identity for the forced parameter set.

Once the combinatorial proof collapses a counterexample to `srg(37,18,7,10)`, the adjacency
matrix satisfies `A^2 + 3A - 8I = 10J`.
-/
theorem quadratic_matrix_identity (hG : G.IsSRGWith 37 18 7 10) :
    A ^ 2 + 3 • A - 8 • (1 : Matrix V V ℝ) = 10 • J := by
  have hA2 : A ^ 2 = 18 • (1 : Matrix V V ℝ) + 7 • A + 10 • Gᶜ.adjMatrix ℝ := by
    simpa using (SimpleGraph.IsSRGWith.matrix_eq (α := ℝ) hG)
  have hJ : (1 : Matrix V V ℝ) + A + Gᶜ.adjMatrix ℝ = J := by
    simpa [SimpleGraph.compl_adjMatrix_eq_adjMatrix_compl] using
      (SimpleGraph.one_add_adjMatrix_add_compl_adjMatrix_eq_of_one
        (G := G) (α := ℝ))
  calc
    A ^ 2 + 3 • A - 8 • (1 : Matrix V V ℝ)
        = (18 • (1 : Matrix V V ℝ) + 7 • A + 10 • Gᶜ.adjMatrix ℝ) + 3 • A -
            8 • (1 : Matrix V V ℝ) := by
              rw [hA2]
    _ = 10 • ((1 : Matrix V V ℝ) + A + Gᶜ.adjMatrix ℝ) := by
      ext v w
      simp only [Matrix.add_apply, Matrix.sub_apply, Matrix.smul_apply, Matrix.one_apply]
      ring
    _ = 10 • J := by
      rw [hJ]

/--
Multiplying by `A - 18I` kills the right-hand side of the quadratic identity because `AJ = 18J`.

This yields the cubic annihilator used by the spectral obstruction.
-/
theorem cubic_annihilates_adjMatrix (hG : G.IsSRGWith 37 18 7 10) :
    (A - 18 • (1 : Matrix V V ℝ)) * (A ^ 2 + 3 • A - 8 • (1 : Matrix V V ℝ)) = 0 := by
  rw [quadratic_matrix_identity (G := G) hG]
  calc
    (A - 18 • (1 : Matrix V V ℝ)) * (10 • J)
        = 10 • ((A - 18 • (1 : Matrix V V ℝ)) * J) := by
            rw [Matrix.mul_smul]
    _ = 0 := by
      rw [sub_mul, adjMatrix_mul_allOnes (G := G) hG, smul_mul_assoc, one_mul]
      ext v w
      simp only [Matrix.sub_apply, Matrix.smul_apply, Matrix.zero_apply]
      ring

/-- The adjacency matrix of a simple graph has trace zero. -/
theorem trace_adjMatrix :
    Matrix.trace A = 0 := by
  simp [SimpleGraph.trace_adjMatrix]

/--
For `srg(37,18,7,10)`, the trace of `A^2` is forced to be `37 * 18 = 666`.
-/
theorem trace_adjMatrix_sq (hG : G.IsSRGWith 37 18 7 10) :
    Matrix.trace (A ^ 2) = 666 := by
  calc
    Matrix.trace (A ^ 2)
        = Matrix.trace
            (18 • (1 : Matrix V V ℝ) + 7 • A + 10 • Gᶜ.adjMatrix ℝ) := by
              rw [SimpleGraph.IsSRGWith.matrix_eq (α := ℝ) hG]
    _ = 18 * 37 + 7 * 0 + 10 * 0 := by
      rw [Matrix.trace_add, Matrix.trace_add, Matrix.trace_smul, Matrix.trace_smul,
        Matrix.trace_smul, Matrix.trace_one, SimpleGraph.trace_adjMatrix,
        SimpleGraph.trace_adjMatrix]
      norm_num [hG.card]
    _ = 666 := by norm_num

/--
For a real Hermitian matrix, `trace(A^2)` is the sum of the squared eigenvalues.
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
Every adjacency eigenvalue of a hypothetical `srg(37,18,7,10)` lies in
`{18, (-3 + sqrt 41) / 2, (-3 - sqrt 41) / 2}`.
-/
theorem adjacency_eigenvalue_cases
    (hG : G.IsSRGWith 37 18 7 10) (i : V) :
    let hH : (G.adjMatrix ℝ).IsHermitian := G.isHermitian_adjMatrix (R := ℝ)
    let lam := hH.eigenvalues i
    lam = 18 ∨ lam = rPos ∨ lam = rNeg := by
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
      (G.adjMatrix ℝ ^ 2 + 3 • G.adjMatrix ℝ - 8 • 1).mulVec v =
        (lam ^ 2 + 3 * lam - 8) • v := by
    rw [Matrix.sub_mulVec, Matrix.add_mulVec, Matrix.smul_mulVec, Matrix.smul_mulVec, hA2v, hAv]
    simp [Matrix.one_mulVec]
    ext x
    simp [Pi.mul_def, smul_eq_mul]
    ring
  have hzero :
      ((G.adjMatrix ℝ - 18 • 1) * (G.adjMatrix ℝ ^ 2 + 3 • G.adjMatrix ℝ - 8 • 1)).mulVec v = 0 := by
    simpa using congrArg (fun M => M.mulVec v) (cubic_annihilates_adjMatrix (G := G) hG)
  have hzero' := hzero
  rw [← Matrix.mulVec_mulVec] at hzero'
  rw [hqv] at hzero'
  rw [Matrix.sub_mulVec, Matrix.mulVec_smul, Matrix.smul_mulVec, hAv] at hzero'
  simp [Matrix.one_mulVec] at hzero'
  have hcoord : ∀ x, ((lam - 18) * (lam ^ 2 + 3 * lam - 8)) * v x = 0 := by
    intro x
    have hx := congrFun hzero' x
    simp [Pi.mul_def, smul_eq_mul] at hx
    nlinarith
  have hscalar : ((lam - 18) * (lam ^ 2 + 3 * lam - 8)) • v = 0 := by
    ext x
    simpa [smul_eq_mul] using hcoord x
  have hprod : (lam - 18) * (lam ^ 2 + 3 * lam - 8) = 0 := by
    exact smul_eq_zero.mp hscalar |>.resolve_right hv_nonzero
  have hfac : (lam - 18) * ((lam - rPos) * (lam - rNeg)) = 0 := by
    rw [← quad_factor]
    exact hprod
  rcases mul_eq_zero.mp hfac with h18 | hrest
  · left
    linarith
  · rcases mul_eq_zero.mp hrest with hPos | hNeg
    · right
      left
      linarith
    · right
      right
      linarith

/--
Pure arithmetic contradiction from the three possible eigenvalue counts.

The cubic annihilator leaves only the values `18`, `rPos`, and `rNeg`; combining their count,
trace, and squared-trace equations forces `sqrt(41)` times an integer to be `72`, which is
impossible after squaring.
-/
theorem spectral_counts_impossible
    {c18 cPos cNeg : ℕ}
    (hcard : c18 + cPos + cNeg = 37)
    (htrace :
      18 * (c18 : ℝ) + rPos * (cPos : ℝ) + rNeg * (cNeg : ℝ) = 0)
    (htraceSq :
      324 * (c18 : ℝ) + rPosSq * (cPos : ℝ) + rNegSq * (cNeg : ℝ) = 666) :
    False := by
  have hcardR : (c18 : ℝ) + (cPos : ℝ) + (cNeg : ℝ) = 37 := by
    exact_mod_cast hcard
  have hc18 : (c18 : ℝ) = 1 := by
    nlinarith [hcardR, htrace, htraceSq]
  have hsum36 : (cPos : ℝ) + (cNeg : ℝ) = 36 := by
    nlinarith [hcardR, hc18]
  have hdiff :
      Real.sqrt 41 * ((cPos : ℝ) - (cNeg : ℝ)) = 72 := by
    nlinarith [htrace, hsum36, hc18]
  have hz :
      ((((cPos : Int) - cNeg : Int) : ℝ)) = (cPos : ℝ) - (cNeg : ℝ) := by
    norm_num
  have hdiffInt :
      Real.sqrt 41 * ((((cPos : Int) - cNeg : Int) : ℝ)) = 72 := by
    rw [hz]
    exact hdiff
  have hsquare :
      41 * ((((cPos : Int) - cNeg : Int) : ℝ)) ^ 2 = 5184 := by
    nlinarith [hdiffInt, sqrt41_sq]
  have hsquareInt :
      41 * (((cPos : Int) - cNeg : Int) ^ 2) = 5184 := by
    exact_mod_cast hsquare
  have hdiv41lhs : (41 : Int) ∣ 41 * (((cPos : Int) - cNeg : Int) ^ 2) := by
    refine ⟨(((cPos : Int) - cNeg : Int) ^ 2), by ring⟩
  have hdiv41rhs : (41 : Int) ∣ 5184 := hsquareInt ▸ hdiv41lhs
  norm_num at hdiv41rhs

/--
Final terminal obstruction: no strongly regular graph with parameters `(37,18,7,10)` exists.
-/
theorem no_srg_37_18_7_10 (hG : G.IsSRGWith 37 18 7 10) : False := by
  classical
  let hH : (G.adjMatrix ℝ).IsHermitian := G.isHermitian_adjMatrix (R := ℝ)
  let c18 : ℕ := (Finset.univ.filter fun i => hH.eigenvalues i = 18).card
  let cPos : ℕ := (Finset.univ.filter fun i => hH.eigenvalues i = rPos).card
  let cNeg : ℕ := (Finset.univ.filter fun i => hH.eigenvalues i = rNeg).card
  have hcases : ∀ i : V,
      hH.eigenvalues i = 18 ∨ hH.eigenvalues i = rPos ∨ hH.eigenvalues i = rNeg := by
    intro i
    simpa [hH] using adjacency_eigenvalue_cases (G := G) hG i
  have hcount_point :
      ∀ i : V,
        (if hH.eigenvalues i = 18 then (1 : ℕ) else 0) +
            (if hH.eigenvalues i = rPos then 1 else 0) +
            (if hH.eigenvalues i = rNeg then 1 else 0) = 1 := by
    intro i
    rcases hcases i with h18 | hPos | hNeg
    · have h18Pos : ¬ ((18 : ℝ) = rPos) := rPos_ne_18.symm
      have h18Neg : ¬ ((18 : ℝ) = rNeg) := rNeg_ne_18.symm
      simp [h18, h18Pos, h18Neg]
    · have hPos18 : ¬ (rPos = (18 : ℝ)) := rPos_ne_18
      have hPosNeg : ¬ (rPos = rNeg) := rPos_ne_rNeg
      simp [hPos, hPos18, hPosNeg]
    · have hNeg18 : ¬ (rNeg = (18 : ℝ)) := rNeg_ne_18
      have hNegPos : ¬ (rNeg = rPos) := rPos_ne_rNeg.symm
      simp [hNeg, hNeg18, hNegPos]
  have hcard : c18 + cPos + cNeg = 37 := by
    calc
      c18 + cPos + cNeg
          = ∑ i, ((if hH.eigenvalues i = 18 then (1 : ℕ) else 0) +
              (if hH.eigenvalues i = rPos then 1 else 0) +
              (if hH.eigenvalues i = rNeg then 1 else 0)) := by
                simp [c18, cPos, cNeg, add_assoc, Finset.sum_add_distrib]
      _ = ∑ _i : V, (1 : ℕ) := by
            refine Finset.sum_congr rfl ?_
            intro i hi
            exact hcount_point i
      _ = 37 := by
            simp [hG.card]
  have htrace_point :
      ∀ i : V,
        hH.eigenvalues i =
          18 * (if hH.eigenvalues i = 18 then (1 : ℝ) else 0) +
            rPos * (if hH.eigenvalues i = rPos then 1 else 0) +
            rNeg * (if hH.eigenvalues i = rNeg then 1 else 0) := by
    intro i
    rcases hcases i with h18 | hPos | hNeg
    · have h18Pos : ¬ ((18 : ℝ) = rPos) := rPos_ne_18.symm
      have h18Neg : ¬ ((18 : ℝ) = rNeg) := rNeg_ne_18.symm
      simp [h18, h18Pos, h18Neg]
    · have hPos18 : ¬ (rPos = (18 : ℝ)) := rPos_ne_18
      have hPosNeg : ¬ (rPos = rNeg) := rPos_ne_rNeg
      simp [hPos, hPos18, hPosNeg]
    · have hNeg18 : ¬ (rNeg = (18 : ℝ)) := rNeg_ne_18
      have hNegPos : ¬ (rNeg = rPos) := rPos_ne_rNeg.symm
      simp [hNeg, hNeg18, hNegPos]
  have sum_indicator_const (c : ℝ) (p : V → Prop) [DecidablePred p] :
      (∑ i, if p i then c else 0) = c * ((Finset.univ.filter p).card : ℝ) := by
    rw [← Finset.sum_filter]
    simp [mul_comm]
  have htrace :
      18 * (c18 : ℝ) + rPos * (cPos : ℝ) + rNeg * (cNeg : ℝ) = 0 := by
    have hsum : ∑ i, hH.eigenvalues i = 0 := by
      simpa [hH.trace_eq_sum_eigenvalues] using trace_adjMatrix (G := G)
    have h18sum :
        (∑ i, if hH.eigenvalues i = 18 then (18 : ℝ) else 0) = 18 * (c18 : ℝ) := by
      simpa [c18] using
        (sum_indicator_const (c := 18) (p := fun i => hH.eigenvalues i = 18))
    have hPosSum :
        (∑ i, if hH.eigenvalues i = rPos then rPos else 0) = rPos * (cPos : ℝ) := by
      simpa [cPos] using
        (sum_indicator_const (c := rPos) (p := fun i => hH.eigenvalues i = rPos))
    have hNegSum :
        (∑ i, if hH.eigenvalues i = rNeg then rNeg else 0) = rNeg * (cNeg : ℝ) := by
      simpa [cNeg] using
        (sum_indicator_const (c := rNeg) (p := fun i => hH.eigenvalues i = rNeg))
    calc
      18 * (c18 : ℝ) + rPos * (cPos : ℝ) + rNeg * (cNeg : ℝ)
          = (∑ i, if hH.eigenvalues i = 18 then (18 : ℝ) else 0) +
              (∑ i, if hH.eigenvalues i = rPos then rPos else 0) +
              ∑ i, if hH.eigenvalues i = rNeg then rNeg else 0 := by
                rw [h18sum, hPosSum, hNegSum]
      _ = ∑ i, (18 * (if hH.eigenvalues i = 18 then (1 : ℝ) else 0) +
              rPos * (if hH.eigenvalues i = rPos then 1 else 0) +
              rNeg * (if hH.eigenvalues i = rNeg then 1 else 0)) := by
            simp [Finset.sum_add_distrib, add_assoc]
      _ = ∑ i, hH.eigenvalues i := by
            refine Finset.sum_congr rfl ?_
            intro i hi
            symm
            exact htrace_point i
      _ = 0 := hsum
  have htraceSq_point :
      ∀ i : V,
        (hH.eigenvalues i) ^ 2 =
          324 * (if hH.eigenvalues i = 18 then (1 : ℝ) else 0) +
            rPosSq * (if hH.eigenvalues i = rPos then 1 else 0) +
            rNegSq * (if hH.eigenvalues i = rNeg then 1 else 0) := by
    intro i
    rcases hcases i with h18 | hPos | hNeg
    · have h18Pos : ¬ ((18 : ℝ) = rPos) := rPos_ne_18.symm
      have h18Neg : ¬ ((18 : ℝ) = rNeg) := rNeg_ne_18.symm
      norm_num [h18, h18Pos, h18Neg]
    · have hPos18 : ¬ (rPos = (18 : ℝ)) := rPos_ne_18
      have hPosNeg : ¬ (rPos = rNeg) := rPos_ne_rNeg
      simp [hPos, hPos18, hPosNeg, rPos_sq]
    · have hNeg18 : ¬ (rNeg = (18 : ℝ)) := rNeg_ne_18
      have hNegPos : ¬ (rNeg = rPos) := rPos_ne_rNeg.symm
      simp [hNeg, hNeg18, hNegPos, rNeg_sq]
  have htraceSq :
      324 * (c18 : ℝ) + rPosSq * (cPos : ℝ) + rNegSq * (cNeg : ℝ) = 666 := by
    have hsum :
        ∑ i, (hH.eigenvalues i) ^ 2 = 666 := by
      simpa [trace_sq_eq_sum_sq_eigenvalues (hM := hH)] using trace_adjMatrix_sq (G := G) hG
    have h18sum :
        (∑ i, if hH.eigenvalues i = 18 then (324 : ℝ) else 0) = 324 * (c18 : ℝ) := by
      simpa [c18] using
        (sum_indicator_const (c := 324) (p := fun i => hH.eigenvalues i = 18))
    have hPosSum :
        (∑ i, if hH.eigenvalues i = rPos then rPosSq else 0) = rPosSq * (cPos : ℝ) := by
      simpa [cPos] using
        (sum_indicator_const (c := rPosSq) (p := fun i => hH.eigenvalues i = rPos))
    have hNegSum :
        (∑ i, if hH.eigenvalues i = rNeg then rNegSq else 0) = rNegSq * (cNeg : ℝ) := by
      simpa [cNeg] using
        (sum_indicator_const (c := rNegSq) (p := fun i => hH.eigenvalues i = rNeg))
    calc
      324 * (c18 : ℝ) + rPosSq * (cPos : ℝ) + rNegSq * (cNeg : ℝ)
          = (∑ i, if hH.eigenvalues i = 18 then (324 : ℝ) else 0) +
              (∑ i, if hH.eigenvalues i = rPos then rPosSq else 0) +
              ∑ i, if hH.eigenvalues i = rNeg then rNegSq else 0 := by
                rw [h18sum, hPosSum, hNegSum]
      _ = ∑ i, (324 * (if hH.eigenvalues i = 18 then (1 : ℝ) else 0) +
              rPosSq * (if hH.eigenvalues i = rPos then 1 else 0) +
              rNegSq * (if hH.eigenvalues i = rNeg then 1 else 0)) := by
            simp [Finset.sum_add_distrib, add_assoc]
      _ = ∑ i, (hH.eigenvalues i) ^ 2 := by
            refine Finset.sum_congr rfl ?_
            intro i hi
            symm
            exact htraceSq_point i
      _ = 666 := hsum
  exact spectral_counts_impossible hcard htrace htraceSq

end Obstruction

/--
Completed packet-sealing theorem: the forced strongly regular obstruction is impossible.
-/
theorem srg_37_18_7_10_nonexistence : intendedStatement := by
  intro V _ _ G _ hG
  exact no_srg_37_18_7_10 (G := G) hG

/--
Publication-facing Lean seal for the `R(B8,B10)` packet's terminal obstruction.
-/
theorem rb8b10_book_ramsey_obstruction : intendedStatement :=
  srg_37_18_7_10_nonexistence

end RB8B10BookRamsey
end AutoMath
