import Mathlib

namespace AutoMath
namespace RB9B11BookRamsey

open SimpleGraph
open scoped BigOperators Polynomial

/--
Lean target for the current packet-sealing attempt:
the verified `R(B9, B11)` packet forces any `41`-vertex counterexample into the strongly regular
parameter set `(41,20,8,11)`, and this file now closes that terminal obstruction completely.
-/
def intendedStatement : Prop :=
  ∀ {V : Type} [Fintype V] [DecidableEq V] (G : SimpleGraph V) [DecidableRel G.Adj],
    ¬ G.IsSRGWith 41 20 8 11

/-- Faithfulness check: the Lean target is exactly the nonexistence of `srg(41,20,8,11)`. -/
theorem rb9b11_book_ramsey_statement :
    intendedStatement ↔
      ∀ {V : Type} [Fintype V] [DecidableEq V] (G : SimpleGraph V) [DecidableRel G.Adj],
        ¬ G.IsSRGWith 41 20 8 11 := by
  rfl

/-- The parameter tuple passes the basic strongly regular parameter identity. -/
theorem parameters_satisfy_basic_srg_identity :
    20 * (20 - 8 - 1) = (41 - 20 - 1) * 11 := by
  norm_num

section ForcedSRG

variable {V : Type} [Fintype V] [DecidableEq V]
variable (G : SimpleGraph V) [DecidableRel G.Adj]

local notation "A" => G.adjMatrix ℝ
local notation "J" => (Matrix.of fun _ _ : V => (1 : ℝ))
local notation "rPos" => (((-3 : ℝ) + 3 * Real.sqrt 5) / 2)
local notation "rNeg" => (((-3 : ℝ) - 3 * Real.sqrt 5) / 2)
local notation "rPosSq" => (((27 : ℝ) - 9 * Real.sqrt 5) / 2)
local notation "rNegSq" => (((27 : ℝ) + 9 * Real.sqrt 5) / 2)

private theorem sqrt5_sq : (Real.sqrt 5) ^ 2 = 5 := by
  nlinarith [Real.sq_sqrt (show (0 : ℝ) ≤ 5 by positivity)]

private theorem rPos_ne_20 : rPos ≠ 20 := by
  intro h
  nlinarith [h, sqrt5_sq]

private theorem rNeg_ne_20 : rNeg ≠ 20 := by
  intro h
  nlinarith [h, sqrt5_sq]

private theorem rPos_ne_rNeg : rPos ≠ rNeg := by
  intro h
  nlinarith [h, sqrt5_sq]

private theorem quad_factor (x : ℝ) :
    x ^ 2 + 3 * x - 9 = (x - rPos) * (x - rNeg) := by
  nlinarith [sqrt5_sq]

private theorem rPos_sq : rPos ^ 2 = rPosSq := by
  nlinarith [sqrt5_sq]

private theorem rNeg_sq : rNeg ^ 2 = rNegSq := by
  nlinarith [sqrt5_sq]

/-- In an `srg(41,20,8,11)`, the all-ones vector is an eigenvector with eigenvalue `20`. -/
theorem adjMatrix_mul_allOnes (hG : G.IsSRGWith 41 20 8 11) :
    A * J = 20 • J := by
  ext v w
  simp [SimpleGraph.adjMatrix_mul_apply, hG.regular.degree_eq]

/--
Specialized SRG matrix identity for the forced parameter set.

This is the checked algebraic core of the packet: once the combinatorial argument collapses a
counterexample to `srg(41,20,8,11)`, the adjacency matrix satisfies
`A^2 + 3A - 9I = 11J`.
-/
theorem quadratic_matrix_identity (hG : G.IsSRGWith 41 20 8 11) :
    A ^ 2 + 3 • A - 9 • (1 : Matrix V V ℝ) = 11 • J := by
  have hA2 : A ^ 2 = 20 • (1 : Matrix V V ℝ) + 8 • A + 11 • Gᶜ.adjMatrix ℝ := by
    simpa using (SimpleGraph.IsSRGWith.matrix_eq (α := ℝ) hG)
  have hJ : (1 : Matrix V V ℝ) + A + Gᶜ.adjMatrix ℝ = J := by
    simpa [SimpleGraph.compl_adjMatrix_eq_adjMatrix_compl] using
      (SimpleGraph.one_add_adjMatrix_add_compl_adjMatrix_eq_of_one
        (G := G) (α := ℝ))
  calc
    A ^ 2 + 3 • A - 9 • (1 : Matrix V V ℝ)
        = (20 • (1 : Matrix V V ℝ) + 8 • A + 11 • Gᶜ.adjMatrix ℝ) + 3 • A -
            9 • (1 : Matrix V V ℝ) := by
              rw [hA2]
    _ = 11 • ((1 : Matrix V V ℝ) + A + Gᶜ.adjMatrix ℝ) := by
      ext v w
      simp only [Matrix.add_apply, Matrix.sub_apply, Matrix.smul_apply, Matrix.one_apply]
      ring
    _ = 11 • J := by
      rw [hJ]

/--
Multiplying by `A - 20I` kills the right-hand side of the quadratic identity because `A J = 20 J`.

This yields the exact cubic annihilator that drives the terminal spectral obstruction.
-/
theorem cubic_annihilates_adjMatrix (hG : G.IsSRGWith 41 20 8 11) :
    (A - 20 • (1 : Matrix V V ℝ)) * (A ^ 2 + 3 • A - 9 • (1 : Matrix V V ℝ)) = 0 := by
  rw [quadratic_matrix_identity (G := G) hG]
  calc
    (A - 20 • (1 : Matrix V V ℝ)) * (11 • J)
        = 11 • ((A - 20 • (1 : Matrix V V ℝ)) * J) := by
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
For `srg(41,20,8,11)`, the trace of `A^2` is forced to be `41 * 20 = 820`.

This is the second checked spectral invariant preserved from the verification packet.
-/
theorem trace_adjMatrix_sq (hG : G.IsSRGWith 41 20 8 11) :
    Matrix.trace (A ^ 2) = 820 := by
  calc
    Matrix.trace (A ^ 2)
        = Matrix.trace
            (20 • (1 : Matrix V V ℝ) + 8 • A + 11 • Gᶜ.adjMatrix ℝ) := by
              rw [SimpleGraph.IsSRGWith.matrix_eq (α := ℝ) hG]
    _ = 20 * 41 + 8 * 0 + 11 * 0 := by
      rw [Matrix.trace_add, Matrix.trace_add, Matrix.trace_smul, Matrix.trace_smul,
        Matrix.trace_smul, Matrix.trace_one, SimpleGraph.trace_adjMatrix,
        SimpleGraph.trace_adjMatrix]
      norm_num [hG.card]
    _ = 820 := by norm_num

/--
For a real Hermitian matrix, `trace(A^2)` is the sum of the squared eigenvalues.

This packages the only spectral bridge needed in the final `R(B9,B11)` contradiction.
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
Every adjacency eigenvalue of a hypothetical `srg(41,20,8,11)` lies in
`{20, (-3 + 3 * sqrt 5) / 2, (-3 - 3 * sqrt 5) / 2}`.
-/
theorem adjacency_eigenvalue_cases
    (hG : G.IsSRGWith 41 20 8 11) (i : V) :
    let hH : (G.adjMatrix ℝ).IsHermitian := G.isHermitian_adjMatrix (R := ℝ)
    let lam := hH.eigenvalues i
    lam = 20 ∨ lam = rPos ∨ lam = rNeg := by
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
      (G.adjMatrix ℝ ^ 2 + 3 • G.adjMatrix ℝ - 9 • 1).mulVec v =
        (lam ^ 2 + 3 * lam - 9) • v := by
    rw [Matrix.sub_mulVec, Matrix.add_mulVec, Matrix.smul_mulVec, Matrix.smul_mulVec, hA2v, hAv]
    simp [Matrix.one_mulVec]
    ext x
    simp [Pi.mul_def, smul_eq_mul]
    ring
  have hzero :
      ((G.adjMatrix ℝ - 20 • 1) * (G.adjMatrix ℝ ^ 2 + 3 • G.adjMatrix ℝ - 9 • 1)).mulVec v = 0 := by
    simpa using congrArg (fun M => M.mulVec v) (cubic_annihilates_adjMatrix (G := G) hG)
  have hzero' := hzero
  rw [← Matrix.mulVec_mulVec] at hzero'
  rw [hqv] at hzero'
  rw [Matrix.sub_mulVec, Matrix.mulVec_smul, Matrix.smul_mulVec, hAv] at hzero'
  simp [Matrix.one_mulVec] at hzero'
  have hcoord : ∀ x, ((lam - 20) * (lam ^ 2 + 3 * lam - 9)) * v x = 0 := by
    intro x
    have hx := congrFun hzero' x
    simp [Pi.mul_def, smul_eq_mul] at hx
    nlinarith
  have hscalar : ((lam - 20) * (lam ^ 2 + 3 * lam - 9)) • v = 0 := by
    ext x
    simpa [smul_eq_mul] using hcoord x
  have hprod : (lam - 20) * (lam ^ 2 + 3 * lam - 9) = 0 := by
    exact smul_eq_zero.mp hscalar |>.resolve_right hv_nonzero
  have hfac : (lam - 20) * ((lam - rPos) * (lam - rNeg)) = 0 := by
    rw [← quad_factor]
    exact hprod
  rcases mul_eq_zero.mp hfac with h20 | hrest
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

The cubic annihilator leaves only the values `20`, `rPos`, and `rNeg`; combining their count,
trace, and squared-trace equations forces the impossible relation `161 * c20 = 41`.
-/
theorem spectral_counts_impossible
    {c20 cPos cNeg : ℕ}
    (hcard : c20 + cPos + cNeg = 41)
    (htrace :
      20 * (c20 : ℝ) + rPos * (cPos : ℝ) + rNeg * (cNeg : ℝ) = 0)
    (htraceSq :
      400 * (c20 : ℝ) + rPosSq * (cPos : ℝ) + rNegSq * (cNeg : ℝ) = 820) :
    False := by
  have hcardR : (c20 : ℝ) + (cPos : ℝ) + (cNeg : ℝ) = 41 := by
    exact_mod_cast hcard
  have hc20 : (c20 : ℝ) = 1 := by
    nlinarith [hcardR, htrace, htraceSq]
  have hsum40 : (cPos : ℝ) + (cNeg : ℝ) = 40 := by
    nlinarith [hcardR, hc20]
  have hdiff :
      3 * Real.sqrt 5 * ((cPos : ℝ) - (cNeg : ℝ)) = 80 := by
    nlinarith [htrace, hsum40, hc20]
  have hz :
      ((((cPos : Int) - cNeg : Int) : ℝ)) = (cPos : ℝ) - (cNeg : ℝ) := by
    norm_num
  have hdiffInt :
      3 * Real.sqrt 5 * ((((cPos : Int) - cNeg : Int) : ℝ)) = 80 := by
    rw [hz]
    exact hdiff
  have hsquare :
      45 * ((((cPos : Int) - cNeg : Int) : ℝ)) ^ 2 = 6400 := by
    nlinarith [hdiffInt, sqrt5_sq]
  have hsquareInt :
      45 * (((cPos : Int) - cNeg : Int) ^ 2) = 6400 := by
    exact_mod_cast hsquare
  have hdiv9lhs : (9 : Int) ∣ 45 * (((cPos : Int) - cNeg : Int) ^ 2) := by
    refine ⟨5 * (((cPos : Int) - cNeg : Int) ^ 2), by ring⟩
  have hdiv9rhs : (9 : Int) ∣ 6400 := hsquareInt ▸ hdiv9lhs
  norm_num at hdiv9rhs

/--
Final terminal obstruction: no strongly regular graph with parameters `(41,20,8,11)` exists.
-/
theorem no_srg_41_20_8_11 (hG : G.IsSRGWith 41 20 8 11) : False := by
  classical
  let hH : (G.adjMatrix ℝ).IsHermitian := G.isHermitian_adjMatrix (R := ℝ)
  let c20 : ℕ := (Finset.univ.filter fun i => hH.eigenvalues i = 20).card
  let cPos : ℕ := (Finset.univ.filter fun i => hH.eigenvalues i = rPos).card
  let cNeg : ℕ := (Finset.univ.filter fun i => hH.eigenvalues i = rNeg).card
  have hcases : ∀ i : V,
      hH.eigenvalues i = 20 ∨ hH.eigenvalues i = rPos ∨ hH.eigenvalues i = rNeg := by
    intro i
    simpa [hH] using adjacency_eigenvalue_cases (G := G) hG i
  have hcount_point :
      ∀ i : V,
        (if hH.eigenvalues i = 20 then (1 : ℕ) else 0) +
            (if hH.eigenvalues i = rPos then 1 else 0) +
            (if hH.eigenvalues i = rNeg then 1 else 0) = 1 := by
    intro i
    rcases hcases i with h20 | hPos | hNeg
    · have h20Pos : ¬ ((20 : ℝ) = rPos) := rPos_ne_20.symm
      have h20Neg : ¬ ((20 : ℝ) = rNeg) := rNeg_ne_20.symm
      simp [h20, h20Pos, h20Neg]
    · have hPos20 : ¬ (rPos = (20 : ℝ)) := rPos_ne_20
      have hPosNeg : ¬ (rPos = rNeg) := rPos_ne_rNeg
      simp [hPos, hPos20, hPosNeg]
    · have hNeg20 : ¬ (rNeg = (20 : ℝ)) := rNeg_ne_20
      have hNegPos : ¬ (rNeg = rPos) := rPos_ne_rNeg.symm
      simp [hNeg, hNeg20, hNegPos]
  have hcard : c20 + cPos + cNeg = 41 := by
    calc
      c20 + cPos + cNeg
          = ∑ i, ((if hH.eigenvalues i = 20 then (1 : ℕ) else 0) +
              (if hH.eigenvalues i = rPos then 1 else 0) +
              (if hH.eigenvalues i = rNeg then 1 else 0)) := by
                simp [c20, cPos, cNeg, add_assoc, Finset.sum_add_distrib]
      _ = ∑ _i : V, (1 : ℕ) := by
            refine Finset.sum_congr rfl ?_
            intro i hi
            exact hcount_point i
      _ = 41 := by
            simp [hG.card]
  have htrace_point :
      ∀ i : V,
        hH.eigenvalues i =
          20 * (if hH.eigenvalues i = 20 then (1 : ℝ) else 0) +
            rPos * (if hH.eigenvalues i = rPos then 1 else 0) +
            rNeg * (if hH.eigenvalues i = rNeg then 1 else 0) := by
    intro i
    rcases hcases i with h20 | hPos | hNeg
    · have h20Pos : ¬ ((20 : ℝ) = rPos) := rPos_ne_20.symm
      have h20Neg : ¬ ((20 : ℝ) = rNeg) := rNeg_ne_20.symm
      simp [h20, h20Pos, h20Neg]
    · have hPos20 : ¬ (rPos = (20 : ℝ)) := rPos_ne_20
      have hPosNeg : ¬ (rPos = rNeg) := rPos_ne_rNeg
      simp [hPos, hPos20, hPosNeg]
    · have hNeg20 : ¬ (rNeg = (20 : ℝ)) := rNeg_ne_20
      have hNegPos : ¬ (rNeg = rPos) := rPos_ne_rNeg.symm
      simp [hNeg, hNeg20, hNegPos]
  have sum_indicator_const (c : ℝ) (p : V → Prop) [DecidablePred p] :
      (∑ i, if p i then c else 0) = c * ((Finset.univ.filter p).card : ℝ) := by
    rw [← Finset.sum_filter]
    simp [mul_comm]
  have htrace :
      20 * (c20 : ℝ) + rPos * (cPos : ℝ) + rNeg * (cNeg : ℝ) = 0 := by
    have hsum : ∑ i, hH.eigenvalues i = 0 := by
      simpa [hH.trace_eq_sum_eigenvalues] using trace_adjMatrix (G := G)
    have h20sum :
        (∑ i, if hH.eigenvalues i = 20 then (20 : ℝ) else 0) = 20 * (c20 : ℝ) := by
      simpa [c20] using
        (sum_indicator_const (c := 20) (p := fun i => hH.eigenvalues i = 20))
    have hPosSum :
        (∑ i, if hH.eigenvalues i = rPos then rPos else 0) = rPos * (cPos : ℝ) := by
      simpa [cPos] using
        (sum_indicator_const (c := rPos) (p := fun i => hH.eigenvalues i = rPos))
    have hNegSum :
        (∑ i, if hH.eigenvalues i = rNeg then rNeg else 0) = rNeg * (cNeg : ℝ) := by
      simpa [cNeg] using
        (sum_indicator_const (c := rNeg) (p := fun i => hH.eigenvalues i = rNeg))
    calc
      20 * (c20 : ℝ) + rPos * (cPos : ℝ) + rNeg * (cNeg : ℝ)
          = (∑ i, if hH.eigenvalues i = 20 then (20 : ℝ) else 0) +
              (∑ i, if hH.eigenvalues i = rPos then rPos else 0) +
              ∑ i, if hH.eigenvalues i = rNeg then rNeg else 0 := by
                rw [h20sum, hPosSum, hNegSum]
      _ = ∑ i, (20 * (if hH.eigenvalues i = 20 then (1 : ℝ) else 0) +
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
          400 * (if hH.eigenvalues i = 20 then (1 : ℝ) else 0) +
            rPosSq * (if hH.eigenvalues i = rPos then 1 else 0) +
            rNegSq * (if hH.eigenvalues i = rNeg then 1 else 0) := by
    intro i
    rcases hcases i with h20 | hPos | hNeg
    · have h20Pos : ¬ ((20 : ℝ) = rPos) := rPos_ne_20.symm
      have h20Neg : ¬ ((20 : ℝ) = rNeg) := rNeg_ne_20.symm
      norm_num [h20, h20Pos, h20Neg]
    · have hPos20 : ¬ (rPos = (20 : ℝ)) := rPos_ne_20
      have hPosNeg : ¬ (rPos = rNeg) := rPos_ne_rNeg
      simpa [hPos, hPos20, hPosNeg, rPos_sq]
    · have hNeg20 : ¬ (rNeg = (20 : ℝ)) := rNeg_ne_20
      have hNegPos : ¬ (rNeg = rPos) := rPos_ne_rNeg.symm
      simpa [hNeg, hNeg20, hNegPos, rNeg_sq]
  have htraceSq :
      400 * (c20 : ℝ) + rPosSq * (cPos : ℝ) + rNegSq * (cNeg : ℝ) = 820 := by
    have hsum :
        ∑ i, (hH.eigenvalues i) ^ 2 = 820 := by
      simpa [trace_sq_eq_sum_sq_eigenvalues (hM := hH)] using trace_adjMatrix_sq (G := G) hG
    have h20sum :
        (∑ i, if hH.eigenvalues i = 20 then (400 : ℝ) else 0) = 400 * (c20 : ℝ) := by
      simpa [c20] using
        (sum_indicator_const (c := 400) (p := fun i => hH.eigenvalues i = 20))
    have hPosSum :
        (∑ i, if hH.eigenvalues i = rPos then rPosSq else 0) = rPosSq * (cPos : ℝ) := by
      simpa [cPos] using
        (sum_indicator_const (c := rPosSq) (p := fun i => hH.eigenvalues i = rPos))
    have hNegSum :
        (∑ i, if hH.eigenvalues i = rNeg then rNegSq else 0) = rNegSq * (cNeg : ℝ) := by
      simpa [cNeg] using
        (sum_indicator_const (c := rNegSq) (p := fun i => hH.eigenvalues i = rNeg))
    calc
      400 * (c20 : ℝ) + rPosSq * (cPos : ℝ) + rNegSq * (cNeg : ℝ)
          = (∑ i, if hH.eigenvalues i = 20 then (400 : ℝ) else 0) +
              (∑ i, if hH.eigenvalues i = rPos then rPosSq else 0) +
              ∑ i, if hH.eigenvalues i = rNeg then rNegSq else 0 := by
                rw [h20sum, hPosSum, hNegSum]
      _ = ∑ i, (400 * (if hH.eigenvalues i = 20 then (1 : ℝ) else 0) +
              rPosSq * (if hH.eigenvalues i = rPos then 1 else 0) +
              rNegSq * (if hH.eigenvalues i = rNeg then 1 else 0)) := by
            simp [Finset.sum_add_distrib, add_assoc]
      _ = ∑ i, (hH.eigenvalues i) ^ 2 := by
            refine Finset.sum_congr rfl ?_
            intro i hi
            symm
            exact htraceSq_point i
      _ = 820 := hsum
  exact spectral_counts_impossible hcard htrace htraceSq

end ForcedSRG

/--
Completed packet-sealing theorem: the forced strongly regular obstruction is impossible.
-/
theorem rb9b11_book_ramsey_obstruction : intendedStatement := by
  intro V _ _ G _ hG
  exact no_srg_41_20_8_11 (G := G) hG

end RB9B11BookRamsey
end AutoMath
