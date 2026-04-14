# Working Packet: On F(2,1) in Digraph Splitting

- slug: `digraph-splitting-f21`
- title: Is F(2,1) finite in Thomassen's digraph partition problem?
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `73`
- single-solve-to-paper fraction: `0.71`

## statement
Either prove that F(2,1) exists and give a sharp or near-sharp finite bound, or construct arbitrarily large counterexamples showing that F(2,1) is infinite.

## novelty_notes
- frontier basis: Alon highlighted the finiteness of F(2,1), West's problem page still treats it as unresolved, and a 2024 note still uses F(2,1) only conditionally.
- why still open: (not recorded)
- attempted conflict check: The exclusion sweep found no prior AutoMath mathematical attempt, slug conflict, or near-duplicate for the exact F(2,1) digraph splitting question.
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the exact small parameter were settled, the note would have an obvious theorem and corollary structure, but the current risk is theorem-slice drift rather than paper shape.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: moderate
- immediate corollary headroom: moderate
- isolated exact-case risk: low
- broader-theorem implication risk: unresolved
- theorem-slice stability: unclear
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: small
- assessment: Fail for the strict lane: exact and interesting, but theorem-slice stability is unclear and broader-theorem implication risk remains unresolved.

## likely_paper_shape
- note title: On F(2,1) in Digraph Splitting
- hypothetical title: On F(2,1) in Digraph Splitting
- paper shape: A small-parameter digraph partition note centered on the first still-sensitive asymmetric case.
- publication if solved: A resolution of F(2,1) would be a real digraph-partition note, but the exact title theorem could drift if the proof broadens to a more general F(s,t) statement.
- minimal artifact requirements: Either a finite partition theorem with an explicit bound or an infinite counterexample family demonstrating nonexistence.

## hypothetical_abstract
We settle the smallest asymmetric parameter pair still emphasized in Thomassen's digraph partition problem by determining whether F(2,1) is finite. We either prove a finite threshold forcing a partition into subdigraphs of minimum outdegree at least 2 and 1 or construct arbitrarily large counterexamples. The result would make a legitimate note, but the theorem slice is vulnerable to broadening if the proof naturally resolves more general parameter pairs.

## single_solve_explanation
This target can certainly be paper-shaped, since F(2,1) is a named small parameter in a standard digraph partition problem. The reason it fails the strict lane is not lack of narrative but theorem-slice instability: a convincing proof may well emerge as part of a wider F(s,t) theorem, which would demote the exact branded slice to a corollary. That broader-theorem implication risk makes it weaker than the sharper finite-exception candidates.

## broader_theorem_nonimplication
No published general theorem currently implies F(2,1), and the 2024 literature still phrases consequences conditionally on F(2,1) being finite; however, any successful attack could plausibly settle a broader family at the same time.

## literature_gap
Alon analyzed the finiteness question for F(2,1), and later work still uses the parameter conditionally rather than as a settled theorem.

## transfer_kit
- lemma: Alon's 2006 splitting paper isolates the finiteness of F(2,1) as a particularly interesting small parameter case.
- lemma: West's problem page records Stiebitz's optimistic heuristic and Alon's contrary suggestion that even F(2,1) might fail to be finite.
- lemma: A 2024 follow-up note still treats F(2,1) as conditional input for higher-parameter consequences, confirming that the exact pair remains live.
- toy example: The already understood small baseline F(1,1) = 3 provides the nearest solved toy model for how a two-part minimum-outdegree threshold theorem is supposed to look.
- known obstruction: Extremal digraph constructions can hide the required local outdegree inside one part, and any successful proof may naturally scale to a more general F(s,t) theorem instead of staying parameter-specific.
- prior-work stop sentence: The literature singles out F(2,1) but still stops short of proving finiteness or producing an infinite counterexample family.
- recommended first attack: Work first with a minimal counterexample at fixed minimum outdegree and look for structural reductions that force a good partition before trying to optimize the threshold.
- paper if solved: The paper would be a parameter-specific digraph splitting note, unless the proof immediately broadens into a more general F(s,t) theorem.

## bounded_source_list
- Noga Alon, "Splitting digraphs" (Combinatorics, Probability and Computing 15, 2006), together with Douglas West's "Splitting digraphs" problem page and a 2024 follow-up note using F(2,1) conditionally.
- Alon 2006, West's splitting page, parameter-specific exact searches for F(2,1), and the 2024 conditional follow-up note.
- artifacts/digraph-splitting-f21/record.md
- artifacts/digraph-splitting-f21/status.json
