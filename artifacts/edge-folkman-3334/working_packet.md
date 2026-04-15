# Working Packet: The Edge Folkman Number F_e(3,3;4)

- slug: `edge-folkman-3334`
- title: edge-folkman-3334
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `35`
- single-solve-to-paper fraction: `0.42`

## statement
Determine the smallest n for which there exists a K4-free graph on n vertices such that every 2-edge-coloring contains a monochromatic triangle.

## novelty_notes
- frontier basis: The source history treats F_e(3,3;4) as the bizarre remaining exact case after the smaller adjacent case F_e(3,3;5)=15 was settled.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The theorem would be important, but the required artifact package is too large for a short note. The result is paper-worthy, just not in the repo's preferred 70-90% micro-paper lane.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: high
- immediate corollary headroom: moderate
- isolated exact-case risk: low
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: True
- certificate compactness: low
- exact gap from source: small
- assessment: Not lane-eligible. The theorem is important, but the solve-to-publication distance is too large and the certificate burden is too heavy.

## likely_paper_shape
- note title: The Edge Folkman Number F_e(3,3;4)
- hypothetical title: The Edge Folkman Number F_e(3,3;4)
- paper shape: A substantial computational Folkman-number paper, not a micro-paper.
- publication if solved: An exact value of F_e(3,3;4) would certainly be publishable, but likely as a substantial computational paper rather than a micro-paper note.
- minimal artifact requirements: A full extremal graph search or equally strong structural proof, with certifiable lower and upper bound artifacts.

## hypothetical_abstract
We determine the exact value of the edge Folkman number F_e(3,3;4). Earlier work settled the adjacent case F_e(3,3;5)=15 and left F_e(3,3;4) as an anomalously difficult remaining exact problem. Any exact solution would be significant, but it would almost certainly require a heavy computational certificate package.

## single_solve_explanation
If solved, the exact theorem would indeed be the title result. But the work remaining after a raw solve would still be large: certify both bounds, document large extremal constructions or proof logs, and manage a substantial verification packet. That places it well outside the target micro-paper band.

## broader_theorem_nonimplication
The nearby exact value F_e(3,3;5)=15 does not force the K4-free case. The open case persists precisely because the easier adjacent parameter does not generalize down to m=4.

## literature_gap
Current checked sources settle F_e(3,3;5)=15 and raise the lower bound for F_e(3,3;4) to at least 21, but do not determine the exact K4-free edge-Folkman value.

## transfer_kit
- lemma: The adjacent exact value F_e(3,3;5)=15 was solved and presented as the smallest open solved case of a broader Folkman-number program.
- lemma: The source explicitly flags F_e(3,3;4) as a bizarre remaining open case.
- lemma: The 2020 Bikov-Nenov paper improves the lower bound to F_e(3,3;4) >= 21 without closing the exact value.
- toy example: The neighboring solved benchmark is F_e(3,3;5)=15.
- known obstruction: The open case is famous precisely because naive extrapolation from the solved m=5 case fails and the certificate burden for m=4 is very large.
- prior-work stop sentence: Current checked sources settle F_e(3,3;5) and improve the lower bound for F_e(3,3;4) to 21, but still leave F_e(3,3;4) without an exact value.
- recommended first attack: Do not enter this lane unless a radically smaller certifiable upper-bound or obstruction mechanism appears before any heavy search.
- paper if solved: If solved exactly, the paper would be a major computational Folkman-number article rather than a micro-paper.

## bounded_source_list
- Stanisław P. Radziszowski's abstract announcing F_e(3,3;5)=15 as the smallest open solved case of a general Folkman-number problem and explicitly flagging F_e(3,3;4) as a bizarre open case, together with a 2020 Australasian Journal of Combinatorics paper by Bikov and Nenov improving the lower bound to F_e(3,3;4) >= 21 while still leaving the exact value open.
- Radziszowski's abstract, the 2020 Bikov-Nenov lower-bound paper, and the survey-style history snippet surfaced in this curation run.
- artifacts/edge-folkman-3334/record.md
- artifacts/edge-folkman-3334/status.json
