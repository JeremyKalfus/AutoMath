# Working Packet: An Abelian (64681,441,3)-Difference Set

- slug: `abelian-difference-set-64681-441-3`
- title: abelian-difference-set-64681-441-3
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `73`
- single-solve-to-paper fraction: `0.74`

## statement
Determine whether any abelian group of order 64681 admits a (64681,441,3)-difference set.

## novelty_notes
- frontier basis: Table 4 isolates (64681,441,3) as one of only six remaining abelian lambda = 3 cases after the source's multiplier-orbit, cyclic-multiplier, contracted-multiplier, Lander, and Mann eliminations.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If this exact tuple is settled, the paper is already mostly determined: restate the Table 4 frontier, recall the source's elimination machinery, and present the construction or obstruction. Little remains beyond concise framing and certificate checking.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: tiny
- assessment: Lane-eligible and retained as the top queue slot because it has the shortest honest solve-to-publication distance among the locally unattempted Gordon Table 4 survivors, while keeping a stable theorem slice and bounded post-solve writeup. A construction or uniform obstruction here would already read like the title theorem of a short residual-case note. The larger surviving Table 4 and Table 3 tuples carry heavier certificate or closability burdens, so they remain behind this case.

## likely_paper_shape
- note title: An Abelian (64681,441,3)-Difference Set
- hypothetical title: On Abelian (64681,441,3)-Difference Sets
- paper shape: A one-theorem note resolving one residual abelian lambda = 3 difference-set parameter from Table 4.
- publication if solved: A construction or nonexistence proof for an abelian (64681,441,3)-difference set would support a short note resolving one of the six residual lambda = 3 abelian difference-set cases isolated by Gordon.
- minimal artifact requirements: Either an explicit abelian group of order 64681 carrying a (64681,441,3)-difference set, or a compact group-uniform nonexistence proof.

## hypothetical_abstract
We determine the existence status of abelian difference sets with parameters (64681,441,3). Gordon's 2022 reduction leaves this tuple in the six-case residual list for lambda = 3 after multiplier-orbit, contracted-multiplier, Lander, and Mann eliminations. Resolving this parameter therefore yields a compact stand-alone note with a fully source-anchored frontier statement.

## single_solve_explanation
This tuple already has a plausible short-note shape because the source compresses the broader lambda = 3 landscape down to a six-case residual list. Once the exact existence status is known, the paper mainly needs a short recap of Gordon's elimination framework and the final certificate. That puts the solve itself in the 70-90% range of the finished note.

## broader_theorem_nonimplication
The source explicitly says that Table 4 contains the remaining open lambda = 3 cases after Theorems 2, 3, 4, the Lander tests, and the Mann test have been applied. This tuple therefore lies in the residual frontier rather than being implied by the broader published reductions.

## literature_gap
Gordon's Table 4 leaves exactly six open abelian (v,k,3)-difference-set parameter sets, including (64681,441,3).

## transfer_kit
- lemma: Theorem 2 gives the orbit-count obstruction over G = Z_p x H and rules out a parameter set when the integer system k = ao + b, b(b - 1) <= lambda(|H| - 1), and a o(o - 1) <= lambda(p - 1) has no positive solution.
- lemma: Theorem 3 bounds the multiplier group size in the cyclic case by |M| <= k.
- lemma: Theorem 4 gives the analogous contracted-multiplier bound for quotient groups G/H in the cyclic case.
- lemma: Table 4 records the six lambda = 3 parameter sets that survive the source's eliminations.
- toy example: The source's opening example re-proves nonexistence of a (352,27,2)-difference set by a short multiplier-orbit contradiction, illustrating the exact obstruction style the current tuple may still admit.
- known obstruction: This tuple already survives Theorems 2, 3, 4, the Lander tests, and the Mann test, so any proof must find a sharper multiplier, character, or group-structure obstruction than the source currently provides.
- prior-work stop sentence: After applying Theorems 2, 3, 4, the Lander tests, and the Mann test, Gordon's Table 4 still lists (64681,441,3) among the six remaining open abelian lambda = 3 cases.
- recommended first attack: Work prime-by-prime through divisors of n = 438 to force a stronger multiplier-orbit contradiction in candidate abelian groups of order 64681, and only if that fails analyze whether cyclic or quotient-multiplier bounds can be sharpened for the surviving group types.
- paper if solved: If solved exactly, the paper would be a short note removing one residual lambda = 3 entry from Gordon's finite abelian difference-set frontier.

## bounded_source_list
- Daniel M. Gordon, "On difference sets with small lambda," Journal of Algebraic Combinatorics 55 (2022), especially Theorem 2, Theorems 3 and 4, and Table 4 on page 6, which lists the six remaining open abelian (v,k,3)-difference-set parameter sets after the source's eliminations.
- Gordon (2022) for the residual Table 4 frontier, together with the cited Lander tests and Mann test background already folded into the source's elimination narrative.
- artifacts/abelian-difference-set-64681-441-3/record.md
- artifacts/abelian-difference-set-64681-441-3/status.json
