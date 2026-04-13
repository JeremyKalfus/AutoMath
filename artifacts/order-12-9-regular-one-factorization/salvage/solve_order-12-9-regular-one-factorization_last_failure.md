# Salvage: order-12-9-regular-one-factorization

- stage: `solve_order-12-9-regular-one-factorization`
- failure_reason: `solve_timeout`
- timed_out: `True`
- timeout_secs: `1200`
- salvaged_on: `2026-04-12T22:30:23.031601-04:00`
- stdout_log: `artifacts/_logs/20260412T195319_solve_order-12-9-regular-one-factorization.stdout.log`
- last_message_path: `artifacts/_logs/20260412T195319_solve_order-12-9-regular-one-factorization.last.txt`

## strongest_recoverable_status
{}

## partial_artifacts
- artifacts/order-12-9-regular-one-factorization/working_packet.md

## stdout_tail
exec
/bin/zsh -lc "mkdir -p artifacts/order-12-9-regular-one-factorization && sed -n '1,260p' artifacts/order-12-9-regular-one-factorization/working_packet.md" in /Users/jeremykalfus/CodingProjects/AutoMath
 succeeded in 0ms:
 succeeded in 0ms:
# Working Packet: One-factorizations of 9-regular graphs of order 12

- slug: `order-12-9-regular-one-factorization`
- title: Is every 9-regular graph on 12 vertices one-factorizable?
- publication status: `SLICE_CANDIDATE`
- packet quality: `strong`

## statement
Settle the smallest high-degree unresolved slice by classifying the nine nonisomorphic 9-regular graphs on 12 vertices with respect to one-factorizability, ideally proving all are one-factorizable or isolating minimal exceptions.

## novelty_notes
- frontier basis: The canonical 2005 classification paper leaves the degree-9 order-12 slice explicitly unresolved and records that only nine nonisomorphic base graphs remain in this slice.
- why still open: The canonical 2005 paper explicitly leaves degrees 7, 8, and 9 open for order 12, and the bounded later-status search surfaced no later paper resolving the degree-9 slice.
- attempted conflict check: The repo memory sweep found no earlier AutoMath attempt or near-duplicate on order-12 one-factorizations or degree-9 regular graph factorizations.
- rediscovery risk: medium

## proof_sketch
- attack style: near-complete-graph case split using perfect-matching structure, complement heuristics, and tiny exact verification on the nine degree-9 graphs
- likely route: A complete verdict on those nine graphs is already a finite exact-classification note with the statement, table, and verification format essentially predetermined.
- verifier focus: For a positive solve, store each factorization explicitly as nine perfect matchings; for a negative solve, preserve the complete obstruction search or structural proof for every one of the nine graphs.

## likely_paper_shape
- note title: One-factorizations of 9-regular graphs of order 12
- paper shape: A fixed-order exact classification note with a table of the nine graphs, factorization verdicts, and a short structural discussion.
- publication if solved: A complete degree-9 classification on order 12 is already a short exact-classification paper because the source explicitly leaves that slice open.
- minimal artifact requirements: An explicit factorization table or a complete obstruction argument for each of the nine graphs, together with a small perfect-matching decomposition checker.

## bounded_source_list
- Petteri Kaski and Patric R. J. Ostergard, "One-Factorizations of Regular Graphs of Order 12" (Electronic Journal of Combinatorics 12, 2005).
- Canonical 2005 order-12 one-factorization paper plus one bounded later-status search for a quiet degree-9 resolution.
- artifacts/order-12-9-regular-one-factorization/record.md
- artifacts/order-12-9-regular-one-factorization/status.json

2026-04-12T23:53:43.931704Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp8_uzmq7g/.codex/.tmp/plugins/plugins/build-ios-apps/.codex-plugin/plugin.json
2026-04-12T23:53:43.932387Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp8_uzmq7g/.codex/.tmp/plugins/plugins/life-science-research/.codex-plugin/plugin.json
2026-04-12T23:53:43.934812Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp8_uzmq7g/.codex/.tmp/plugins/plugins/build-ios-apps/.codex-plugin/plugin.json
2026-04-12T23:53:43.935248Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp8_uzmq7g/.codex/.tmp/plugins/plugins/life-science-research/.codex-plugin/plugin.json
2026-04-12T23:53:43.938844Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp8_uzmq7g/.codex/.tmp/plugins/plugins/build-ios-apps/.codex-plugin/plugin.json
2026-04-12T23:53:43.939182Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp8_uzmq7g/.codex/.tmp/plugins/plugins/life-science-research/.codex-plugin/plugin.json
2026-04-12T23:53:43.943739Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp8_uzmq7g/.codex/.tmp/plugins/plugins/build-ios-apps/.codex-plugin/plugin.json
2026-04-12T23:53:43.944020Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp8_uzmq7g/.codex/.tmp/plugins/plugins/life-science-research/.codex-plugin/plugin.json
2026-04-12T23:53:43.946923Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp8_uzmq7g/.codex/.tmp/plugins/plugins/build-ios-apps/.codex-plugin/plugin.json
2026-04-12T23:53:43.947202Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp8_uzmq7g/.codex/.tmp/plugins/plugins/life-science-research/.codex-plugin/plugin.json
2026-04-12T23:53:43.952166Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp8_uzmq7g/.codex/.tmp/plugins/plugins/build-ios-apps/.codex-plugin/plugin.json
2026-04-12T23:53:43.952421Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp8_uzmq7g/.codex/.tmp/plugins/plugins/life-science-research/.codex-plugin/plugin.json
2026-04-12T23:53:43.957646Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp8_uzmq7g/.codex/.tmp/plugins/plugins/build-ios-apps/.codex-plugin/plugin.json
2026-04-12T23:53:43.957867Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp8_uzmq7g/.codex/.tmp/plugins/plugins/life-science-research/.codex-plugin/plugin.json
2026-04-12T23:53:43.961341Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp8_uzmq7g/.codex/.tmp/plugins/plugins/build-ios-apps/.codex-plugin/plugin.json
2026-04-12T23:53:43.961541Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp8_uzmq7g/.codex/.tmp/plugins/plugins/life-science-research/.codex-plugin/plugin.json
2026-04-12T23:53:43.967361Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp8_uzmq7g/.codex/.tmp/plugins/plugins/build-ios-apps/.codex-plugin/plugin.json
2026-04-12T23:53:43.967552Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp8_uzmq7g/.codex/.tmp/plugins/plugins/life-science-research/.codex-plugin/plugin.json
codex
The packet gives the claim and verifier shape, but not the nine graphs themselves. I’m doing one narrow repo search for any local graph data or prior sidecar notes for this slug, then I’ll write the reasoning record around the strongest path available.
exec
/bin/zsh -lc "rg --files . | rg 'order-12|one-factor|factorization'" in /Users/jeremykalfus/CodingProjects/AutoMath
 succeeded in 0ms:
./artifacts/order-12-9-regular-one-factorization/working_packet.md

2026-04-12T23:53:49.323147Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp8_uzmq7g/.codex/.tmp/plugins/plugins/build-ios-apps/.codex-plugin/plugin.json
2026-04-12T23:53:49.323427Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp8_uzmq7g/.codex/.tmp/plugins/plugins/life-science-research/.codex-plugin/plugin.json
2026-04-12T23:53:49.324815Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp8_uzmq7g/.codex/.tmp/plugins/plugins/build-ios-apps/.codex-plugin/plugin.json
2026-04-12T23:53:49.325041Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp8_uzmq7g/.codex/.tmp/plugins/plugins/life-science-research/.codex-plugin/plugin.json
2026-04-12T23:53:49.326912Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp8_uzmq7g/.codex/.tmp/plugins/plugins/build-ios-apps/.codex-plugin/plugin.json
2026-04-12T23:53:49.327134Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp8_uzmq7g/.codex/.tmp/plugins/plugins/life-science-research/.codex-plugin/plugin.json
2026-04-12T23:53:49.329767Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp8_uzmq7g/.codex/.tmp/plugins/plugins/build-ios-apps/.codex-plugin/plugin.json
2026-04-12T23:53:49.329968Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp8_uzmq7g/.codex/.tmp/plugins/plugins/life-science-research/.codex-plugin/plugin.json
2026-04-12T23:53:49.331893Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp8_uzmq7g/.codex/.tmp/plugins/plugins/build-ios-apps/.codex-plugin/plugin.json
2026-04-12T23:53:49.332093Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp8_uzmq7g/.codex/.tmp/plugins/plugins/life-science-research/.codex-plugin/plugin.json
2026-04-12T23:53:49.334793Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp8_uzmq7g/.codex/.tmp/plugins/plugins/build-ios-apps/.codex-plugin/plugin.json
2026-04-12T23:53:49.334977Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp8_uzmq7g/.codex/.tmp/plugins/plugins/life-science-research/.codex-plugin/plugin.json
2026-04-12T23:53:49.337911Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp8_uzmq7g/.codex/.tmp/plugins/plugins/build-ios-apps/.codex-plugin/plugin.json
2026-04-12T23:53:49.338095Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp8_uzmq7g/.codex/.tmp/plugins/plugins/life-science-research/.codex-plugin/plugin.json
2026-04-12T23:53:49.340319Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp8_uzmq7g/.codex/.tmp/plugins/plugins/build-ios-apps/.codex-plugin/plugin.json
2026-04-12T23:53:49.340506Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp8_uzmq7g/.codex/.tmp/plugins/plugins/life-science-research/.codex-plugin/plugin.json
2026-04-12T23:53:49.344042Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp8_uzmq7g/.codex/.tmp/plugins/plugins/build-ios-apps/.codex-plugin/plugin.json
2026-04-12T23:53:49.344215Z  WARN codex_core::plugins::manifest: ignoring interface.defaultPrompt: prompt must be at most 128 characters path=/var/folders/dt/8glc0ycs71n4sb1kzlxncvlc0000gn/T/tmp8_uzmq7g/.codex/.tmp/plugins/plugins/life-science-research/.codex-plugin/plugin.json
