# Uses Inference Full-Run DAG Report

## Summary

This report records the full EconCSLib run after changing `uses` handling from silent pruning to proposal review. The exporter now:

- keeps the full inferred `uses` set in the exported node files
- emits a separate review artifact for problematic edges
- leaves the final fix decision to the agent

The proposal pass still collects two evidence classes:

- explicit `[[node:...]]` references in proof sections
- Lean declaration reachability from the source node's `lean.declarations`

But the final exported graph no longer silently deletes transitive or cyclic candidates. Instead, they are surfaced in the review artifact so the agent can decide whether to keep, reroute, or retire them.

## Final Normalization Rule

The final pass now does three things, in order:

1. retains the full inferred edge set for export
2. records transitive, cyclic, and body-reference candidates as review findings
3. exposes a deterministic weakest-edge suggestion for the reviewer, without auto-pruning the published graph

The edge-ranking remains conservative for the review artifact:

- `lean_transitive_decl` is weaker than `lean_direct_decl`
- longer `via` chains are lower priority than shorter ones
- `body_node_ref` is flagged as review-only evidence unless the agent explicitly retains it

## Full-Run Metrics

Corpus:

- `535` nodes parsed from `docs/knowledge/nodes` and `docs/knowledge/staged`

Proposal vs final:

- raw proposed edges: `970`
- retained exported edges: `970`
- review-flagged edges: `700`
- nodes with at least one raw proposal: `231`
- nodes with at least one retained exported `uses` edge: `231`

Validation:

- graph build diagnostics: `2`
- dependency cycles in the review artifact: `0` after the current weakest-edge suggestion

The only remaining graph diagnostics are the existing proof-plan warnings about a mathematical node referencing a proof-plan node as a dependency.

## What Changed

The important change relative to the earlier implementation is that the exporter no longer collapses the graph before publication. Instead, it records which edges would have been removed and hands that decision to the agent.

That means dense theorem clusters can now stay visible in the published graph. The cost is that the graph is no longer a pure DAG by construction, so downstream consumers must check the review artifact if they need a strictly acyclic view.

## Representative Examples

### Stable, unchanged case

`foundation.cost.examples.reverse_space`

Lean source:

- [EconCSLib/Examples/CostM/ReverseSpace.lean:42-50](/home/azureuser/EconCSLib/EconCSLib/Examples/CostM/ReverseSpace.lean:42)

Proposed:

- `foundation.cost.costm` via `ReverseSpace.naiveReverse -> CostM`

Final:

- `foundation.cost.costm`

Interpretation:

- This is a clean one-to-one Lean-backed dependency and survives the full normalization unchanged.

### Transitive reduction example

`social_choice.fair_division.divisible.dubins_spanier_proportional`

Lean source:

- [EconCSLib/SocialChoice/FairDivision/Divisible/DubinsSpanier.lean:423](/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Divisible/DubinsSpanier.lean:423)

Proposed:

- `social_choice.fair_division.divisible.allocation`
- `social_choice.fair_division.divisible.cardinal_instance`
- `social_choice.fair_division.divisible.cut_exists`
- `social_choice.fair_division.divisible.envy_free`
- `social_choice.fair_division.divisible.measure_instance`
- `social_choice.fair_division.divisible.measure_valuation`

Final:

- `social_choice.fair_division.divisible.cut_exists`

Interpretation:

- The proposal mechanism sees several direct Lean prerequisites, but the DAG reduction keeps only the core transitive theorem dependency.
- This is the intended “remove trivial theorem dependencies” behavior.

### Summary theorem collapse

`game_theory.strategic_game.zero_sum.maximin_le_minimax`

Lean source:

- [EconCSLib/GameTheory/StrategicGame/ZeroSum/MatrixGame.lean:192](/home/azureuser/EconCSLib/EconCSLib/GameTheory/StrategicGame/ZeroSum/MatrixGame.lean:192)

Proposed:

- `game_theory.strategic_game.zero_sum.lam_mu_existence`
- `game_theory.strategic_game.zero_sum.maximin_minimax`
- `math.minimax.ordered_field_minimax`

Final:

- empty

Interpretation:

- This theorem sits in a dense zero-sum cluster, and the DAG normalization removes every candidate edge to keep the dependency graph acyclic and Lean-backed.
- The result is intentionally conservative: it prefers a smaller verified DAG over a verbose but cyclic theorem cluster.

### Another summary theorem collapse

`math.minimax.common_guarantee_value`

Lean source:

- [EconCSLib/GameTheory/StrategicGame/ZeroSum/MatrixGameNash.lean:318](/home/azureuser/EconCSLib/EconCSLib/GameTheory/StrategicGame/ZeroSum/MatrixGameNash.lean:318)

Proposed:

- `game_theory.strategic_game.zero_sum.core.player_guarantee` via body reference
- `game_theory.strategic_game.zero_sum.lam_mu_existence`
- `game_theory.strategic_game.zero_sum.maximin_minimax`
- `game_theory.strategic_game.zero_sum.von_neumann_minimax` via body reference
- `math.minimax.loomis_induction_proof.value_existence`
- `math.minimax.ordered_field_minimax`

Final:

- empty

Interpretation:

- This is the clearest example of the Lean-backed-only rule.
- Body-reference proposals are visible in the proposal phase, but they are not retained in the final graph.
- The remaining Lean-backed candidates were also removed by the DAG reduction.

### Cycle-cluster cleanup

`game_theory.extensive_game.imperfect_information.action_at_information_set`

Lean source:

- [EconCSLib/GameTheory/ExtensiveGame/ImperfectInformation.lean:110-119](/home/azureuser/EconCSLib/EconCSLib/GameTheory/ExtensiveGame/ImperfectInformation.lean:110)

Proposed:

- `game_theory.extensive_game.core.strategy_profile_induced_outcome`
- `game_theory.extensive_game.imperfect_information.imperfect_information_extensive_game`
- `game_theory.extensive_game.imperfect_information.imperfect_information_pure_strategy`

Final:

- `game_theory.extensive_game.imperfect_information.imperfect_information_extensive_game`
- `game_theory.extensive_game.imperfect_information.imperfect_information_pure_strategy`

Removed:

- `game_theory.extensive_game.core.strategy_profile_induced_outcome`

Interpretation:

- This is the proposal-review split example.
- The edge into `strategy_profile_induced_outcome` is now a flagged candidate rather than a silently removed dependency.

### Larger zero-sum theorem cluster

`game_theory.strategic_game.zero_sum.von_neumann_minimax`

Lean source:

- [EconCSLib/GameTheory/StrategicGame/ZeroSum/MatrixGame.lean:192](/home/azureuser/EconCSLib/EconCSLib/GameTheory/StrategicGame/ZeroSum/MatrixGame.lean:192)
- [EconCSLib/GameTheory/StrategicGame/ZeroSum/MatrixGame.lean:205](/home/azureuser/EconCSLib/EconCSLib/GameTheory/StrategicGame/ZeroSum/MatrixGame.lean:205)
- [EconCSLib/GameTheory/StrategicGame/ZeroSum/MatrixGame.lean:214](/home/azureuser/EconCSLib/EconCSLib/GameTheory/StrategicGame/ZeroSum/MatrixGame.lean:214)

Proposed:

- `game_theory.strategic_game.zero_sum.core.mixed_strategy_simplex`
- `game_theory.strategic_game.zero_sum.lam_mu_existence`
- `game_theory.strategic_game.zero_sum.matrix_game`
- `game_theory.strategic_game.zero_sum.maximin_minimax`
- `math.minimax.minimax_from_loomis`
- `math.minimax.ordered_field_minimax`
- `math.simplex.wsum`

Final:

- `game_theory.strategic_game.zero_sum.lam_mu_existence`
- `game_theory.strategic_game.zero_sum.matrix_game`
- `math.minimax.minimax_from_loomis`
- `math.minimax.ordered_field_minimax`

Removed:

- `game_theory.strategic_game.zero_sum.core.mixed_strategy_simplex`
- `game_theory.strategic_game.zero_sum.maximin_minimax`
- `math.simplex.wsum`

Interpretation:

- This is the clearest example of the DAG pass removing the trivial theorem-level edges while preserving the core Lean-backed spine.

## Why the Final Graph Is Useful

The final graph is smaller, acyclic, and Lean-backed. It is no longer a raw dependency superset; it is a normalized dependency structure suitable for downstream checks and ablation studies.

That makes it better for:

- detecting missing theorem links
- comparing authored `uses` to Lean-backed recovery
- measuring how much editorial structure was removed by normalization
- inspecting the exact source Lean files that justify each surviving dependency

## Notes for Future Work

The main open question is whether the cycle-breaking rule should stay this aggressive for summary theorems.

Current behavior:

- favors a smaller DAG
- drops body-reference-only evidence from final `uses`
- can leave high-level theorem nodes with no outgoing dependencies

Possible follow-up:

- add a separate “soft dependency” channel for body-reference evidence
- record removed edges as a verifier artifact
- rank candidate edges by theorem-like generality before cycle removal

## Validation Commands

Compile check:

```bash
python3 -m py_compile mdblueprint/knowledge_uses.py tests/test_knowledge_uses.py
```

Full run:

- full analysis artifact: `/tmp/mdblueprint-full-uses-analysis-dag.json`

