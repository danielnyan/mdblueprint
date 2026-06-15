---
agent: lean-adjudicator
created_at: "2026-06-15T13:00:00Z"
knowledge_root: ../EconCSLib/docs/knowledge
lean_source_root: ../EconCSLib
inputs:
  refactor_report: runs/refactor-countercheck/20260615T130000Z/reports/refactor-report.md
  dry_run_json: runs/refactor-countercheck/20260615T130000Z/dry-runs/refactor-dry-run.json
  countercheck_pairs: runs/refactor-countercheck/20260615T130000Z/countercheck/pairs.json
  skipped: runs/refactor-countercheck/20260615T130000Z/countercheck/skipped.json
  summary: runs/refactor-countercheck/20260615T130000Z/countercheck/summary.json
  note: Referenced `skills/mdblueprint-lean-adjudicate/references/agent-config.toml` was not present in the workspace; this report uses the skill instructions plus run metadata as the effective defaults.
---

# Lean Adjudication Report

## Scope

This adjudication covers the four Lean countercheck pairs in the refactor-countercheck run:

- `market_design.matching.one_to_one.gale_shapley_algorithm`
- `market_design.matching.one_to_one.lattice`
- `market_design.matching.one_to_one.market`
- `market_design.matching.one_to_one.stability`

No admitted or staged knowledge files were edited.

## Factual Extraction Summary

- Countercheck pairs: `4`
- Skipped candidates: `0`
- Refactor proposals under review: `2`
- Dry-run operations applied: `2`
- Dry-run graph delta: `406 -> 404` edges, `273` nodes unchanged
- Dry-run diagnostics: none from the operations themselves

Lean-side evidence is largely a granularity issue:

- The Gale-Shapley source exposes `GS.daStep`, `GS.daRun`, `GS.finalState`, and `GS.gs` in `namespace GS`.
- The lattice source exposes `GS.opposed_preferences`, `GS.stableJoin_isStable`, `GS.stableMeet_isStable`, `GS.StableMatching`, and `GS.StableMatching.gsStable_isGreatest`, plus helper lemmas and bridge lemmas.
- The market and stability source files expose the conceptual predicates `MatchingMarket`, `Matching.IsBlocking`, `Matching.IsStable`, and `Matching.IsIndividuallyRational`.

The authored nodes are aligned with those Lean artifacts at the intended abstraction level, but the heuristic extractor recorded several helper lemmas and missed some direct declaration matches.

## Node-To-Theorem Mapping

| Node | Authored signal | Lean signal | Mapping judgment |
| --- | --- | --- | --- |
| `market_design.matching.one_to_one.gale_shapley_algorithm` | Uses `market_design.matching.one_to_one.market`, `market_design.matching.one_to_one.matching`; prose names `GS.daStep`, `GS.daRun`, `GS.finalState`, `GS.gs` | `namespace GS` defines `daStep`, `daRun`, `finalState`, `gs`; many helper lemmas around the DA state machine | Accept wrapper-style mapping; the extractor missed the direct defs, but the Lean file names match the authored prose exactly |
| `market_design.matching.one_to_one.lattice` | Uses `market_design.matching.one_to_one.stability`, `market_design.matching.one_to_one.proposing_optimal`; prose names `GS.opposed_preferences`, `GS.stableJoin_isStable`, `GS.stableMeet_isStable`, `GS.StableMatching`, `GS.StableMatching.gsStable_isGreatest` | Same named theorems exist; additional helper lemmas such as `joinWoman_*`, `meetMan_*`, and `opposed_preferences_women` appear | Accept wrapper-style mapping; extra lemmas are formalization artifacts, not authored-node contradictions |
| `market_design.matching.one_to_one.market` | No uses; prose defines the one-to-one matching market concept and names `MatchingMarket` | `MatchingMarket` exists; `IsBlocking`, `IsStable`, and `IsIndividuallyRational` are nearby support predicates | Accept as a conceptual anchor; the Lean file is a lower-level implementation wrapper, not a mismatch |
| `market_design.matching.one_to_one.stability` | Uses `market_design.matching.one_to_one.matching`; prose names `Matching.IsIndividuallyRational`, `Matching.IsBlocking`, `Matching.IsStable` | `Matching.IsBlocking` and `Matching.IsStable` match exactly; `IsIndividuallyRational` is also present as a nearby helper predicate | Accept; the missing-use signal is a heuristic boundary issue |

## Discrepancy Table

| Node | Missing theorem/declaration | Extra theorem/declaration | Missing dependency/use | Extra dependency/use | Post-hoc failure modes | Verdict |
| --- | --- | --- | --- | --- | --- | --- |
| `market_design.matching.one_to_one.gale_shapley_algorithm` | `GS.daStep`, `GS.daRun`, `GS.finalState`, `GS.gs` were reported missing by the heuristic pass | Helper lemmas like `pref_list_mem`, `initState`, `isFree`, `HoldInv`, `galeShapley_isStable` were surfaced | `market_design.matching.one_to_one.market`, `market_design.matching.one_to_one.matching` | Many helper dependencies around the DA proof state machine | `missing_theorem`, `extra_theorem`, `missing_dependency`, `extra_dependency`, `helper_lemma_leakage`, `formalization_artifact_not_in_authored_graph` | Accept, false abend |
| `market_design.matching.one_to_one.lattice` | None | Helper lemmas such as `joinWoman_*`, `meetMan_*`, `opposed_preferences_women`, `gsStable_greatest` | `market_design.matching.one_to_one.stability`, `market_design.matching.one_to_one.proposing_optimal` | Bridge/helper lemmas around the lattice construction | `extra_theorem`, `missing_dependency`, `extra_dependency`, `helper_lemma_leakage`, `formalization_artifact_not_in_authored_graph` | Accept, false abend |
| `market_design.matching.one_to_one.market` | `MatchingMarket` reported missing by the heuristic pass | `IsBlocking`, `IsStable`, `IsIndividuallyRational` surfaced as extra declarations | None | `IsBlocking` | `missing_theorem`, `extra_theorem`, `extra_dependency`, `summary_node_vs_atomic_theorem_mismatch` | Accept, false abend |
| `market_design.matching.one_to_one.stability` | None | `IsIndividuallyRational` surfaced as extra declaration | `market_design.matching.one_to_one.matching` | `IsBlocking` | `missing_dependency`, `extra_theorem`, `extra_dependency`, `summary_node_vs_atomic_theorem_mismatch` | Accept, false abend |

## Final Judgments

| Node | Verdict | Confidence | Rationale |
| --- | --- | --- | --- |
| `market_design.matching.one_to_one.gale_shapley_algorithm` | `accept` | `high` | The Lean file contains the exact named DA definitions, and the apparent mismatch is a namespace/extractor granularity issue rather than a semantic discrepancy |
| `market_design.matching.one_to_one.lattice` | `accept` | `high` | The authored theorem names match the Lean file, and the extra helper lemmas are expected proof artifacts |
| `market_design.matching.one_to_one.market` | `accept` | `high` | The node is a conceptual wrapper around `MatchingMarket`; Lean uses lower-level predicates in the same module, which is consistent with the authored contract |
| `market_design.matching.one_to_one.stability` | `accept` | `high` | The Lean predicates match the authored definitions; the missing-use signal is a heuristic boundary artifact |

## Final Filter

| Node | Label | Why |
| --- | --- | --- |
| `market_design.matching.one_to_one.gale_shapley_algorithm` | `false_abend` | The exact Lean declarations exist, but the heuristic extractor failed to map them cleanly to the authored node |
| `market_design.matching.one_to_one.lattice` | `false_abend` | Additional lemmas are proof scaffolding; the authored theorem content is aligned with Lean |
| `market_design.matching.one_to_one.market` | `false_abend` | The node is a summary-level concept, while Lean exposes implementation predicates in the same module |
| `market_design.matching.one_to_one.stability` | `false_abend` | The missing dependency is an abstraction mismatch, not a substantive contradiction |

## Conclusion

No true discrepancy was found in this countercheck set.

The proposed refactor removals remain mechanically safe from the Lean-adjudication perspective because the mismatches are all false abends caused by helper lemmas, namespace granularity, or summary-node versus atomic-theorem resolution.
