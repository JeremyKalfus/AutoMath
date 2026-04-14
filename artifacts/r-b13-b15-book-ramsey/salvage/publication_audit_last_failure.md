# Salvage: r-b13-b15-book-ramsey

- stage: `publication_audit`
- failure_reason: `publication_audit_nonzero_exit`
- timed_out: `False`
- timeout_secs: `1200`
- salvaged_on: `2026-04-14T02:22:23.348477-04:00`
- stdout_log: `artifacts/_logs/20260414T022135_publication_audit.stdout.log`
- last_message_path: `artifacts/_logs/20260414T022135_publication_audit.last.txt`

## strongest_recoverable_status
{
  "stage": "verify",
  "classification": "CANDIDATE",
  "verify_verdict": "VERIFIED",
  "publication_status": "SLICE_CANDIDATE",
  "publication_confidence": 0.84,
  "lean_ready": true,
  "lean_complete": false,
  "next_action": "Advance to publication_audit with the verified candidate theorem packet, then formalize in Lean unless publication audit uncovers bounded-scope rediscovery."
}

## partial_artifacts
- artifacts/r-b13-b15-book-ramsey/attempts/solver-A.selection.md
- artifacts/r-b13-b15-book-ramsey/record.md
- artifacts/r-b13-b15-book-ramsey/status.json
- artifacts/r-b13-b15-book-ramsey/working_packet.md

## stdout_tail
# why_this_is_or_is_not_publishable

If the proof verifies, this is publishable in the strict micro-paper lane.

Why:

- the exact title theorem is already crisp: `R(B13, B15) = 57`
- the solve would already be roughly `85%` to `90%` of the paper
- the remaining work is cheap exposition, verification, and possibly Lean formal packaging

What still has to happen before calling it paper-ready:

- verify the Goodman arithmetic line by line
- verify the strongly regular multiplicity contradiction cleanly
- run the bounded prior-art audit in the later stage
- optionally formalize the short counting chain if the manager wants Lean closure

# paper_shape_support

What makes this paper-shaped beyond a bare exact value:

- the title theorem is exact and family-anchored
- the proof has a compact named mechanism: Goodman squeeze plus infeasible strongly regular extremal case
- the boundary remark is immediate and clean
- the post-solve editorial overhead is low

Minimal remaining packaging work:

- a 1-2 paragraph setup explaining the one-gap literature window
- one polished theorem-proof section
- one short comparison remark with the adjacent `R(B14, B15) = 59` benchmark already noted in the packet

# boundary_remark

Boundary remark:

This argument appears tuned to exact one-gap cases. If the literature window were wider than `1`, the same Goodman squeeze would likely leave too much degree variance and would no longer force a unique extremal configuration.

# likely_failure_points

- The biggest technical risk is a sign or constant slip in the Goodman-to-`sum d_i^2` calculation.
- The second risk is the strongly regular multiplicity algebra; it should be written explicitly in verify rather than left implicit.
- A softer risk is notation mismatch if some source uses a different indexing convention for `B_k`.
- A publication-stage risk remains that the exact value could already be known despite the packet's bounded novelty check, but solve itself is not the stage to clear that.

# what_verify_should_check

- Recheck the book translation: `B13` means edge codegree at least `13`, `B15` means edge codegree at least `15`.
- Recompute `\binom{57}{2} = 1596` and `\binom{57}{3} = 29260`.
- Re-derive Goodman exactly:
  `t + \bar t = 29260 - 56m + (1/2)\sum d_i^2`.
- Re-derive inequality `(1)` and the window `779 <= m <= 798`.
- Re-derive the integer convexity lower bound `(2)` and the conclusion `m = 798`.
- Confirm that equality forces `28`-regularity and exact codegrees `(12, 15)`.
- Write the strongly regular multiplicity computation explicitly and confirm the nonintegrality.
- Then perform the bounded rediscovery search and only after that decide whether to promote toward publication audit and Lean.

2026-04-14T06:22:15.516758Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp50353zdv/.codex/.tmp/plugins/plugins/build-ios-apps/.codex-plugin/plugin.json
2026-04-14T06:22:15.517064Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp50353zdv/.codex/.tmp/plugins/plugins/life-science-research/.codex-plugin/plugin.json
2026-04-14T06:22:15.518641Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp50353zdv/.codex/.tmp/plugins/plugins/build-ios-apps/.codex-plugin/plugin.json
2026-04-14T06:22:15.518888Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp50353zdv/.codex/.tmp/plugins/plugins/life-science-research/.codex-plugin/plugin.json
2026-04-14T06:22:15.521003Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp50353zdv/.codex/.tmp/plugins/plugins/build-ios-apps/.codex-plugin/plugin.json
2026-04-14T06:22:15.521220Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp50353zdv/.codex/.tmp/plugins/plugins/life-science-research/.codex-plugin/plugin.json
2026-04-14T06:22:15.524092Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp50353zdv/.codex/.tmp/plugins/plugins/build-ios-apps/.codex-plugin/plugin.json
2026-04-14T06:22:15.524309Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp50353zdv/.codex/.tmp/plugins/plugins/life-science-research/.codex-plugin/plugin.json
2026-04-14T06:22:15.526418Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp50353zdv/.codex/.tmp/plugins/plugins/build-ios-apps/.codex-plugin/plugin.json
2026-04-14T06:22:15.526634Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp50353zdv/.codex/.tmp/plugins/plugins/life-science-research/.codex-plugin/plugin.json
2026-04-14T06:22:15.529495Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp50353zdv/.codex/.tmp/plugins/plugins/build-ios-apps/.codex-plugin/plugin.json
2026-04-14T06:22:15.529693Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp50353zdv/.codex/.tmp/plugins/plugins/life-science-research/.codex-plugin/plugin.json
2026-04-14T06:22:15.532799Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp50353zdv/.codex/.tmp/plugins/plugins/build-ios-apps/.codex-plugin/plugin.json
2026-04-14T06:22:15.533019Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp50353zdv/.codex/.tmp/plugins/plugins/life-science-research/.codex-plugin/plugin.json
2026-04-14T06:22:15.535332Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp50353zdv/.codex/.tmp/plugins/plugins/build-ios-apps/.codex-plugin/plugin.json
2026-04-14T06:22:15.535515Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp50353zdv/.codex/.tmp/plugins/plugins/life-science-research/.codex-plugin/plugin.json
2026-04-14T06:22:15.539210Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp50353zdv/.codex/.tmp/plugins/plugins/build-ios-apps/.codex-plugin/plugin.json
2026-04-14T06:22:15.539393Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp50353zdv/.codex/.tmp/plugins/plugins/life-science-research/.codex-plugin/plugin.json
ERROR: Selected model is at capacity. Please try a different model.
2026-04-14T06:22:21.901095Z  WARN codex_exec: thread/read failed while backfilling turn items for turn completion: thread/read: thread/read failed: ephemeral threads do not support includeTurns
ERROR: Selected model is at capacity. Please try a different model.
tokens used
48,464
