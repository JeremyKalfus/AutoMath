# Salvage: r-b10-b12-book-ramsey

- stage: `publication_audit`
- failure_reason: `publication_audit_nonzero_exit`
- timed_out: `False`
- timeout_secs: `1200`
- salvaged_on: `2026-04-14T02:01:07.871414-04:00`
- stdout_log: `artifacts/_logs/20260414T015845_publication_audit.stdout.log`
- last_message_path: `artifacts/_logs/20260414T015845_publication_audit.last.txt`

## strongest_recoverable_status
{
  "stage": "verify",
  "classification": "CANDIDATE",
  "verify_verdict": "SURVIVES_SKEPTICAL_CHECK",
  "publication_status": "SLICE_CANDIDATE",
  "publication_confidence": 0.83,
  "lean_ready": true,
  "lean_complete": false,
  "next_action": "Formalize only the two remaining upstream proof bridges, rerun the Lean build in a dependency-ready environment, and then wrap the checked slice into the exact theorem R(B10, B12) = 45 without broadening scope."
}

## partial_artifacts
- artifacts/r-b10-b12-book-ramsey/attempts/solver-A.selection.md
- artifacts/r-b10-b12-book-ramsey/lean/AutoMath/RB10B12BookRamsey.lean
- artifacts/r-b10-b12-book-ramsey/record.md
- artifacts/r-b10-b12-book-ramsey/status.json
- artifacts/r-b10-b12-book-ramsey/working_packet.md

## stdout_tail
/bin/zsh -lc "sed -n '1,260p' artifacts/r-b10-b12-book-ramsey/status.json" in /Users/jeremykalfus/CodingProjects/AutoMath
 succeeded in 0ms:
{
  "slug": "r-b10-b12-book-ramsey",
  "title": "Determine the exact value of R(B10, B12)",
  "stage": "verify",
  "verify_verdict": "SURVIVES_SKEPTICAL_CHECK",
  "classification": "CANDIDATE",
  "confidence": 0.79,
  "lean_ready": true,
  "lean_packet_seal": true,
  "lean_gate_reason": "The verify pass did not find a mathematical flaw in the prose proof, and the remaining gap is tightly scoped formal sealing of the two upstream bridges: the Goodman/convexity reduction to the exact equality profile and the local conversion from 11 common nonneighbors on a nonedge to 12 common neighbors in the forced 22-regular regime. The existing Lean artifact already handles the terminal SRG obstruction slice, so Lean is the shortest remaining path to a sealed packet. This verify environment could not rerun the build because Lake attempted a dependency download under network restriction.",
  "lean_complete": false,
  "publication_status": "SLICE_CANDIDATE",
  "publication_confidence": 0.83,
  "single_solve_to_paper_fraction": 0.85,
  "title_theorem_strength": "strong",
  "publication_narrative_strength": "strong",
  "micro_paper_assessment": "Pass, but not sealed. If the current prose proof is fully formalized, the result already looks like most of a short exact-value note on the almost-diagonal book Ramsey line. The remaining gap is proof sealing and reproducible formal checking, not publication narrative. Until that full wrapper is checked, the honest state is CANDIDATE / SLICE_CANDIDATE rather than EXACT or PAPER_READY.",
  "strongest_honest_claim": "The strongest honest claim after verify is a candidate theorem-proof packet that any 45-vertex counterexample to R(B10, B12) = 45 would be forced into the impossible strongly regular parameter set (45,22,9,12). The terminal SRG obstruction has a Lean artifact, but the full Ramsey theorem and the upstream counting reduction remain prose-only.",
  "paper_title_hint": "The Exact Value of R(B10, B12)",
  "candidate_theorem_slice": "Candidate slice: there is no graph on 45 vertices whose every edge has at most 9 common neighbors and whose every nonedge has at most 11 common nonneighbors; equivalently, any such graph would have to be an impossible srg(45,22,9,12).",
  "publication_packet_quality": "strong",
  "next_action": "Formalize only the two remaining upstream proof bridges, rerun the Lean build in a dependency-ready environment, and then wrap the checked slice into the exact theorem R(B10, B12) = 45 without broadening scope.",
  "proof_artifacts_preserved": true
}

exec
/bin/zsh -lc 'rg --files artifacts/r-b10-b12-book-ramsey' in /Users/jeremykalfus/CodingProjects/AutoMath
 succeeded in 0ms:
artifacts/r-b10-b12-book-ramsey/status.json
artifacts/r-b10-b12-book-ramsey/attempts/solver-A.selection.md
artifacts/r-b10-b12-book-ramsey/working_packet.md
artifacts/r-b10-b12-book-ramsey/record.md
artifacts/r-b10-b12-book-ramsey/lean/AutoMath/RB10B12BookRamsey.lean

2026-04-14T05:59:13.195298Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmpisyejbs8/.codex/.tmp/plugins/plugins/build-ios-apps/.codex-plugin/plugin.json
2026-04-14T05:59:13.195629Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmpisyejbs8/.codex/.tmp/plugins/plugins/life-science-research/.codex-plugin/plugin.json
2026-04-14T05:59:13.197277Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmpisyejbs8/.codex/.tmp/plugins/plugins/build-ios-apps/.codex-plugin/plugin.json
2026-04-14T05:59:13.197521Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmpisyejbs8/.codex/.tmp/plugins/plugins/life-science-research/.codex-plugin/plugin.json
2026-04-14T05:59:13.199634Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmpisyejbs8/.codex/.tmp/plugins/plugins/build-ios-apps/.codex-plugin/plugin.json
2026-04-14T05:59:13.199878Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmpisyejbs8/.codex/.tmp/plugins/plugins/life-science-research/.codex-plugin/plugin.json
2026-04-14T05:59:13.202834Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmpisyejbs8/.codex/.tmp/plugins/plugins/build-ios-apps/.codex-plugin/plugin.json
2026-04-14T05:59:13.203053Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmpisyejbs8/.codex/.tmp/plugins/plugins/life-science-research/.codex-plugin/plugin.json
2026-04-14T05:59:13.205174Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmpisyejbs8/.codex/.tmp/plugins/plugins/build-ios-apps/.codex-plugin/plugin.json
2026-04-14T05:59:13.205388Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmpisyejbs8/.codex/.tmp/plugins/plugins/life-science-research/.codex-plugin/plugin.json
2026-04-14T05:59:13.208325Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmpisyejbs8/.codex/.tmp/plugins/plugins/build-ios-apps/.codex-plugin/plugin.json
2026-04-14T05:59:13.208549Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmpisyejbs8/.codex/.tmp/plugins/plugins/life-science-research/.codex-plugin/plugin.json
2026-04-14T05:59:13.211690Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmpisyejbs8/.codex/.tmp/plugins/plugins/build-ios-apps/.codex-plugin/plugin.json
2026-04-14T05:59:13.211892Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmpisyejbs8/.codex/.tmp/plugins/plugins/life-science-research/.codex-plugin/plugin.json
2026-04-14T05:59:13.214270Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmpisyejbs8/.codex/.tmp/plugins/plugins/build-ios-apps/.codex-plugin/plugin.json
2026-04-14T05:59:13.214456Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmpisyejbs8/.codex/.tmp/plugins/plugins/life-science-research/.codex-plugin/plugin.json
2026-04-14T05:59:13.218199Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmpisyejbs8/.codex/.tmp/plugins/plugins/build-ios-apps/.codex-plugin/plugin.json
2026-04-14T05:59:13.218383Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmpisyejbs8/.codex/.tmp/plugins/plugins/life-science-research/.codex-plugin/plugin.json
web search: 
web search: "R(B10, B12)"
web search: 
web search: "Small Ramsey Numbers" DS1.17 book Ramsey 5.3 g B10 B12
web search: 
web search: "R(B10, B12)" "Small Ramsey Numbers for Books, Wheels, and Generalizations"
web search: 
web search: "Lower bounds for book Ramsey numbers" pdf
web search: 
web search: https://www.cs.rit.edu/~spr/ElJC/ejcram17.pdf
web search: 
web search: 'R (B 10, B 12)' in https://www.cs.rit.edu/~spr/ElJC/ejcram17.pdf
web search: 
web search: https://www.cs.rit.edu/~spr/ElJC/ejcram17.pdf
web search: 
web search: https://lidicky.name/pub/Ramsey_BWG.pdf
web search: 
web search: https://www.combinatorics.org/ojs/index.php/eljc/article/view/v32i4p64/pdf
web search: 
web search: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v32i4p64/pdf/
web search: 
ERROR: Selected model is at capacity. Please try a different model.
2026-04-14T06:01:07.225840Z  WARN codex_exec: thread/read failed while backfilling turn items for turn completion: thread/read: thread/read failed: ephemeral threads do not support includeTurns
ERROR: Selected model is at capacity. Please try a different model.
tokens used
22,219
