# Working Packet: On F(2,2) in Digraph Splitting

- slug: `digraph-splitting-f22`
- title: Determine F(2,2) in Thomassen's digraph partition problem
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `69`
- single-solve-to-paper fraction: `0.69`

## statement
Either prove that F(2,2) exists and determine its exact value or construct arbitrarily large counterexamples showing that no finite threshold exists.

## novelty_notes
- frontier basis: West's page highlights F(2,2) as a central open parameter, records the lower bound F(2,2) > 5, and later work still uses the parameter only conditionally.
- why still open: (not recorded)
- attempted conflict check: The exclusion sweep found no prior AutoMath mathematical attempt, slug conflict, or near-duplicate for the exact F(2,2) digraph splitting parameter.
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The note would have a clear central theorem if solved, but the current frontier packet is weaker than a true micro-paper because the theorem slice is not robust under proof broadening.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: moderate
- immediate corollary headroom: moderate
- isolated exact-case risk: low
- broader-theorem implication risk: unresolved
- theorem-slice stability: fragile
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: small
- assessment: Fail for the strict lane: exact parameter, but theorem-slice stability is fragile and broader-theorem implication risk remains unresolved.

## likely_paper_shape
- note title: On F(2,2) in Digraph Splitting
- hypothetical title: On F(2,2) in Digraph Splitting
- paper shape: A small-parameter threshold note in digraph splitting, likely with one sharp lower-bound construction and one finite upper-bound theorem or impossibility family.
- publication if solved: A resolution of F(2,2) would be publishable, but it sits too close to the broader F(s,t) program to count as a stable micro-paper slice.
- minimal artifact requirements: Either a finite sharp threshold proof or an explicit infinite counterexample family, together with small extremal examples showing why 5 does not suffice.

## hypothetical_abstract
We determine the small parameter F(2,2) in Thomassen's digraph partition problem. We either prove a finite threshold for splitting into two minimum-outdegree-2 parts or construct arbitrarily large counterexamples showing that no such finite threshold exists. Although that would produce a publishable note, the honest theorem is too exposed to broader-program drift to qualify as a strict micro-paper target today.

## single_solve_explanation
A clean F(2,2) resolution would certainly be note-shaped, since the parameter is standard and the lower-bound obstruction F(2,2) > 5 is already recorded. The issue is theorem stability: a successful proof is quite likely to arise from a more general splitting framework, making the exact F(2,2) title theorem look secondary. That risk pushes it below the current lane even though the problem is mathematically attractive.

## broader_theorem_nonimplication
The existing literature does not imply F(2,2), and the page explicitly records only a small lower bound; however, the most plausible successful proof routes appear generic enough that the exact branded slice may not remain the honest paper title.

## literature_gap
The available record shows F(2,2) > 5 and stops before proving finiteness, sharpness, or nonexistence.

## transfer_kit
- lemma: West's problem page records the explicit lower bound F(2,2) > 5 via an example of Andre Kezdy.
- lemma: The same page explains that the general F(s,t) existence problem already reduces much of the surrounding theory to the two-part case.
- lemma: A 2024 note still treats consequences of finite F(2,2) conditionally, so the parameter remains open rather than merely unoptimized.
- toy example: The recorded lower-bound construction showing F(2,2) > 5 is the basic worked example for how the threshold can fail at the first naive guess.
- known obstruction: Even the first optimistic bound fails, and any proof that F(2,2) is finite may naturally expand into a wider theorem about F(s,t).
- prior-work stop sentence: The literature gives F(2,2) > 5 and then stops short of determining whether a finite sharp threshold exists.
- recommended first attack: Separate the task into two stages: sharpen the extremal lower-bound family first, then attack upper bounds through structural decompositions of minimal counterexamples.
- paper if solved: The paper would be a threshold note for one named small digraph partition parameter, provided the proof does not immediately subsume a larger family.

## bounded_source_list
- Douglas West's "Splitting digraphs" problem page, summarizing Alon, Thomassen, and Stiebitz, together with the recorded lower bound F(2,2) > 5 and a 2024 note using F(2,2) conditionally.
- West's splitting page, parameter-specific exact searches around F(2,2), and the 2024 conditional follow-up note.
- artifacts/digraph-splitting-f22/record.md
- artifacts/digraph-splitting-f22/status.json
