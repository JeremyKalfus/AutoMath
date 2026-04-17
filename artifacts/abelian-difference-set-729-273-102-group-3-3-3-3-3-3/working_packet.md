# Working Packet: The Elementary Abelian (729,273,102)-Difference-Set Problem

- slug: `abelian-difference-set-729-273-102-group-3-3-3-3-3-3`
- title: abelian-difference-set-729-273-102-group-3-3-3-3-3-3
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `86`
- single-solve-to-paper fraction: `0.84`

## statement
Determine whether the elementary abelian group C_3^6 admits a (729,273,102)-difference set.

## novelty_notes
- frontier basis: Gordon's 2019 LJDSR slides single out 729 273 102 in [3,3,3,3,3,3] as the smallest open elementary-abelian case, while local attempt and source memory show no cooled-down or duplicate run on this exact group statement.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: One exact solve would already answer the stated smallest-open-case question, so the remaining work would be limited to short family context and clean proof exposition.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: low
- immediate corollary headroom: moderate
- isolated exact-case risk: low
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: tiny
- assessment: Lane-eligible. The candidate is an exact smallest-open-case theorem with a clean family anchor, low feeder risk, and a paper packet that is already close to title-and-abstract form.

## likely_paper_shape
- note title: The Elementary Abelian (729,273,102)-Difference-Set Problem
- hypothetical title: The Elementary Abelian (729,273,102)-Difference-Set Problem
- paper shape: A short note settling the smallest open elementary-abelian difference-set case.
- publication if solved: A proof of existence or nonexistence would settle Gordon's named smallest open elementary-abelian case at parameters (729,273,102) in C_3^6.
- minimal artifact requirements: A source-faithful proof or disproof in C_3^6, the decisive character-orbit or quotient argument, and a brief explanation of how this resolves the smallest open elementary-abelian case.

## hypothetical_abstract
We determine whether the elementary abelian group C_3^6 admits a (729,273,102)-difference set. Gordon's La Jolla Difference Set Repository slides identify this exact group as the smallest open elementary-abelian case outside the settled Hadamard and Paley families. Our result therefore closes a named residual case and yields a short self-contained note with only light family framing beyond the core proof.

## single_solve_explanation
The source already supplies both the exact statement and the publication narrative: this is the smallest open elementary-abelian case. A single exact solve would therefore provide almost all of the paper's mathematical content. What remains after the solve is mostly expository packaging, not additional theorem development.

## broader_theorem_nonimplication
The later source does not claim a general classification of elementary-abelian difference sets beyond the settled Hadamard and Paley families; instead it isolates C_3^6 at (729,273,102) as an unresolved residue, so no broader published theorem surfaced here that already forces the answer.

## literature_gap
Prior work surfaced in this curation stops at Gordon 2019 identifying (729,273,102) in C_3^6 as the smallest open elementary-abelian case; the bounded exact and alternate-notation web sweeps on 2026-04-15 found no direct later settlement.

## transfer_kit
- lemma: Gordon 2019 explicitly labels (729,273,102) in [3,3,3,3,3,3] as the smallest open elementary-abelian case, fixing the theorem slice.
- lemma: For any abelian difference set D, the group-ring equation D D^(-1) = n + lambda G and its character form constrain all nontrivial character values to modulus sqrt(n); here n = 171.
- lemma: The source discussion on known gcd(v,n) > 1 cases highlights the character-divisibility viewpoint as a natural obstruction framework for noncyclic abelian groups.
- toy example: Work in F_3^2 first: inspect how character values and multiplier-fixed orbit unions behave in a small elementary-abelian model before lifting the bookkeeping pattern to F_3^6.
- known obstruction: The family is already settled in the obvious Hadamard and Paley directions, so any proof must address the genuinely residual elementary-abelian case rather than inherit an infinite-family construction.
- prior-work stop sentence: Gordon 2019 lists 729 273 102 in [3,3,3,3,3,3] as the smallest open elementary-abelian case.
- recommended first attack: Translate the problem into character-value constraints on F_3^6 and test whether the 19-part of n = 171 forces an impossible orbit or divisibility pattern for a putative difference set.
- paper if solved: If solved exactly, the paper would be a short note settling the smallest open elementary-abelian difference-set case.

## bounded_source_list
- Daniel M. Gordon, "The La Jolla Difference Set Repository" (ArasuFest talk slides, August 3, 2019), especially slide 46 listing the smallest open elementary-abelian case 729 273 102 [3,3,3,3,3,3].
- Gordon 2019 slide 46, Gordon-Schmidt 2015/2016 multiplier-survey table context, bounded exact-statement and alternate-notation web sweeps on 2026-04-15, and local attempt/source registry checks.
- artifacts/abelian-difference-set-729-273-102-group-3-3-3-3-3-3/record.md
- artifacts/abelian-difference-set-729-273-102-group-3-3-3-3-3-3/status.json
