# Working Packet: A Residual Abelian Lambda = 3 Difference-Set Case

- slug: `abelian-difference-set-182733434811-740406-3`
- title: abelian-difference-set-182733434811-740406-3
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `76`
- single-solve-to-paper fraction: `0.76`

## statement
Determine whether any abelian group of order 182733434811 admits a (182733434811,740406,3)-difference set.

## novelty_notes
- frontier basis: Gordon's Table 4 identifies (182733434811,740406,3) as one of the six remaining abelian lambda = 3 cases after Theorem 2, Theorems 3 and 4, Lander, and Mann eliminations.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The source already supplies the cleanup narrative and the elimination framework, so an exact solve would only need the decisive existence or nonexistence argument for this one tuple plus a short recap of why it escaped the previous tests.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: small
- assessment: This is lane-eligible, though less crisp than the selected [3,9,9] case: the frontier basis is strong, the exact gap is explicit, and one decisive solve would already look like the core of a short cleanup note.

## likely_paper_shape
- note title: A Residual Abelian Lambda = 3 Difference-Set Case
- hypothetical title: On an Open Abelian (182733434811,740406,3)-Difference Set Case
- paper shape: A one-theorem cleanup note removing one of the six residual abelian lambda = 3 parameter sets in Gordon's 2022 table.
- publication if solved: A proof of existence or nonexistence would remove one of the six residual abelian lambda = 3 cases isolated by Gordon's 2022 elimination up to k <= 10^10.
- minimal artifact requirements: Either a compact nonexistence argument using multiplier or contracted-multiplier structure, or an explicit abelian difference-set certificate with a short verification packet.

## hypothetical_abstract
We determine whether any abelian group of order 182733434811 admits a (182733434811,740406,3)-difference set. Gordon's 2022 analysis leaves this tuple as one of only six residual abelian lambda = 3 cases with k <= 10^10 after the standard elimination theorems are applied. The result therefore closes a named residual table entry with only light exposition beyond the decisive proof.

## single_solve_explanation
Because the tuple already appears in an explicit residual table, an exact solve would immediately be the main theorem of a short note. The paper would not need a feeder ladder: the literature context is just the elimination pipeline and the fact that this tuple survived it. Remaining work after the solve is mostly a concise recap of the known filters and the final argument.

## broader_theorem_nonimplication
The canonical source explicitly says that Theorem 2, Theorems 3 and 4, Lander, and Mann do not settle this tuple, so no broader published elimination uncovered in the bounded audit already disposes of it.

## literature_gap
Prior work stops at listing (182733434811,740406,3) in Table 4 as one of the six remaining abelian lambda = 3 cases for k <= 10^10.

## transfer_kit
- lemma: Gordon's Lemma 1 gives the orbit structure of G under a multiplier after isolating a prime divisor p of v.
- lemma: Theorem 2 converts the orbit decomposition into the inequalities k = ao + b, b(b - 1) <= lambda(|H| - 1), and a o(o - 1) <= lambda(p - 1).
- lemma: Theorem 3 bounds the multiplier group size in cyclic groups by |M| <= k.
- lemma: Theorem 4 extends the same style of bound to contracted multipliers over quotient groups.
- toy example: Use Gordon's smaller Table 4 entries (4761,120,3) or (64681,441,3) as the worked model for how a residual lambda = 3 case is packaged in the source literature.
- known obstruction: This tuple already survives the standard fast eliminations, so any proof must use structure not captured by Gordon's existing Theorem 2, cyclic multiplier bounds, Lander, or Mann filters.
- prior-work stop sentence: Table 4 of Gordon (2022) still lists (182733434811,740406,3) as an open abelian lambda = 3 case.
- recommended first attack: Factor the ambient abelian group through a large prime divisor p of v, force multiplier or contracted-multiplier orbits, and try to contradict the orbit-count inequalities or quotient character data.
- paper if solved: If solved exactly, the paper would be a one-theorem note deleting one row from Gordon's residual abelian lambda = 3 table.

## bounded_source_list
- Daniel M. Gordon, "On difference sets with small lambda" (Journal of Algebraic Combinatorics 55, 2022), especially Theorem 2, Theorems 3 and 4, and Table 4 listing the six remaining abelian (v,k,3)-difference-set cases for k <= 10^10.
- Gordon 2022, especially the orbit-counting elimination Theorem 2, the cyclic and contracted multiplier bounds in Theorems 3 and 4, and Table 4.
- artifacts/abelian-difference-set-182733434811-740406-3/record.md
- artifacts/abelian-difference-set-182733434811-740406-3/status.json
