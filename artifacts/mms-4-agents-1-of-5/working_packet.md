# Working Packet: The Four-Agent 1-of-5 Maximin-Share Guarantee

- slug: `mms-4-agents-1-of-5`
- title: mms-4-agents-1-of-5
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `73`
- single-solve-to-paper fraction: `0.78`

## statement
For four agents with additive valuations over indivisible goods, determine whether there always exists an allocation giving every agent at least a 1-of-5 maximin-share guarantee.

## novelty_notes
- frontier basis: Surveyed MMS literature bounds the additive ordinal guarantee between n + 1 and 2n - 2 and records n = 4 as the smallest unresolved exact case.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: A yes-or-no answer at n = 4 already has a crisp smallest-open-case narrative and a natural placement between the known impossibility of stronger guarantees and the general 1-of-(2n - 2) bound. After the solve, the remaining work is mostly exposition and a short discussion of how the four-agent result sits inside the broader MMS hierarchy.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: low
- immediate corollary headroom: moderate
- isolated exact-case risk: low
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: high
- exact gap from source: small
- assessment: Lane-eligible. The case has real family anchoring and a clear smallest-open-case story, though the literature audit cost is a bit higher than for the BSHM targets because the fair-division literature is broader.

## likely_paper_shape
- note title: The Four-Agent 1-of-5 Maximin-Share Guarantee
- hypothetical title: A 1-of-5 Maximin-Share Guarantee for Four Additive Agents
- paper shape: A short fair-division note settling the smallest unresolved ordinal MMS guarantee for additive valuations.
- publication if solved: A proof or counterexample for the four-agent 1-of-5 MMS guarantee would plausibly be publishable as a short fair-division note closing the smallest open ordinal additive case.
- minimal artifact requirements: Either a four-agent algorithmic proof guaranteeing 1-of-5 MMS for every additive instance, or a concrete additive counterexample instance disproving the guarantee.

## hypothetical_abstract
We settle the smallest unresolved ordinal maximin-share case for additive fair division by determining whether every four-agent instance admits a 1-of-5 MMS allocation. Existing additive results imply a general 1-of-(2n-2) guarantee and show that stronger exact ordinal guarantees can fail, but the four-agent 1-of-5 threshold remains the first open point. Resolving this threshold yields a compact stand-alone note with immediate relevance to the structure of ordinal MMS guarantees.

## single_solve_explanation
The exact four-agent 1-of-5 statement is already a clean title theorem and not just a feeder instance. Once the theorem or counterexample exists, the note only needs a short survey paragraph on known ordinal MMS bounds and a careful presentation of the proof or example. That keeps the solve itself as the overwhelming majority of the paper.

## broader_theorem_nonimplication
Known additive results only force the weaker general bound 1-of-(2n - 2), which is 1-of-6 when n = 4, while known negative examples do not already rule out the 1-of-5 threshold. So the currently surveyed literature brackets but does not determine the four-agent exact answer.

## literature_gap
Current surveyed MMS literature records that for additive valuations the smallest unresolved ordinal case is whether every four-agent instance admits a 1-of-5 maximin-share allocation.

## transfer_kit
- lemma: Surveyed additive MMS literature gives a general 1-of-(2n-2) guarantee, hence 1-of-6 for four agents.
- lemma: The same survey line states that the optimal ordinal guarantee lies between n + 1 and 2n - 2, so the four-agent threshold is bracketed between 5 and 6.
- lemma: PROP* and envy-free-matching implications are cited in the survey as standard tools connecting stronger fairness notions to ordinal MMS guarantees.
- lemma: The surveyed literature records n = 4 as the smallest open additive ordinal MMS case.
- toy example: The neighboring benchmark is the already guaranteed four-agent 1-of-6 bound obtained from the general additive theory.
- known obstruction: General impossibility examples show that the stronger 1-of-4 threshold cannot hold for all additive instances once n > 2, so any positive proof must genuinely land at 5 rather than at a stronger exact guarantee.
- prior-work stop sentence: The current surveyed literature improves general additive ordinal MMS guarantees to 1-of-(2n-2) but still leaves the four-agent 1-of-5 case unresolved.
- recommended first attack: Try a four-agent structural reduction that combines envy-free-matching style decompositions with a careful case split on the top-valued goods, instead of chasing a full all-n ordinal theorem.
- paper if solved: If solved exactly, the paper would be a short fair-division note closing the smallest open ordinal maximin-share case for additive valuations.

## bounded_source_list
- The maximin-share fair-division literature as summarized on the HandWiki "Maximin share" page retrieved on 2026-04-14, citing the additive-valuation MMS line of Budish (2011), Bouveret-Lemaitre (2015), Aigner-Horev-Segal-Halevi (2019), and subsequent approximation papers; the summary states that for additive valuations the smallest unresolved ordinal MMS case is n = 4, namely whether a 1-of-5 MMS allocation always exists.
- The additive maximin-share survey line summarized in the cited HandWiki page and its referenced core papers on MMS, PROP*, and envy-free matching implications.
- artifacts/mms-4-agents-1-of-5/record.md
- artifacts/mms-4-agents-1-of-5/status.json
