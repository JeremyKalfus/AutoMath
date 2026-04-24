# Replacement email draft

Hi Bernard,

Noon my time works. Thank you for the Zoom link.

I cleaned up the AutoMath packet before sending this because my earlier draft used old internal terminology that was misleading. The current terms are:

`lean_queue.json` = solve, verification, significance/publication audit, and artifact preservation are done; Lean is the remaining gate.

`lean_complete.json` = AutoMath has definitively proved the publication-significant result in Lean.

By that standard, the live `lean_complete.json` currently has 0 proofs. The old pieces of Lean code you saw are real checked snippets, but they were instance-only / not publication-significant, so I archived them rather than counting them as AutoMath paper results.

On the `<= 38` question: AutoMath got this from Radziszowski's dynamic survey DS1.17, Section 5.3(g), which records the Rousseau-Sheehan book Ramsey upper-bound mechanism. It gives `R(B_m,B_n) <= 2(m+n+1)` when `2(m+n)+1 > (n-m)^2/3`. For `(m,n) = (8,10)`, this is `37 > 4/3`, so `R(B8,B10) <= 2(8+10+1) = 38`. The lower bound `37 <= R(B8,B10)` is from Theorem 1 of your 2025 paper with McKinley, Pfender, and Van Overberghe: `4n-3 <= R(B_{n-2},B_n)` for `4 <= n <= 21`, taking `n = 10`.

For a transcript: I attached a cleaned run transcript for the `R(B8,B10)` packet, plus short normalized solve/verify/Lean stage summaries. The full raw stdout logs exist, but they are about 13k lines, so I did not attach them by default unless you want them.

The core proof route AutoMath found was:

Assume a 37-vertex obstruction exists. The `B8` and complement-`B10` conditions give triangle caps in both colors. Combining those with Goodman's identity forces equality in a degree quadratic, hence the graph must be 18-regular. Equality then forces every edge to have exactly 7 common neighbors and every nonedge exactly 10 common neighbors, so any obstruction would have to be `srg(37,18,7,10)`. The SRG matrix identity gives nontrivial eigenvalues satisfying `x^2 + 3x - 8 = 0`; the irrational conjugates would have equal multiplicity, forcing trace contribution `-54`, but the trace requirement for an 18-regular graph requires `-18`. Contradiction, so no 37-vertex obstruction exists.

On other problems: yes, there are 8 other current publication-significant packets in `lean_queue.json`, but none are Lean-complete. The current crude snapshot success rate is 9 publication-significant packets out of 151 archived attempts, about 6%. The live Lean-complete publication-significant success count is 0.

I attached:

- a README explaining the files and terminology;
- the clean `R(B8,B10)` transcript;
- the current results snapshot;
- the current `lean_queue.json` and empty `lean_complete.json`;
- the `R(B8,B10)` Lean skeleton.

I also put the source/provenance links in the README: DS1.17, the EJC paper/DOI, and the AutoMath repo snapshot/commit. That should be cleaner than leaving "AutoMath" as a vague uncited name.

Best,
Jeremy
