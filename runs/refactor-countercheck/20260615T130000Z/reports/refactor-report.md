---
agent: graph-refactor-proposer
target:
  knowledge_root: ../EconCSLib/docs/knowledge
decision: proposals
created_at: "2026-06-15T12:47:52Z"
inputs:
  - tools.knowledge.check ../EconCSLib/docs/knowledge
  - mdblueprint-lint ../EconCSLib/docs/knowledge --json
  - tools.knowledge.stats ../EconCSLib/docs/knowledge --json
  - tools.knowledge.refactor_pack ../EconCSLib/docs/knowledge --target market_design.matching.one_to_one.gale_shapley_algorithm
  - tools.knowledge.refactor_pack ../EconCSLib/docs/knowledge --target market_design.matching.one_to_one.lattice
summary: Two admitted matching-theory dependency edges are redundant and can be removed mechanically.
baseline:
  check: passed
  lint: findings
  stats: collected
formulation_impact:
  reviewed: true
  reason: The surviving candidates are direct-edge removals only; the target bodies have no cross-links to the removed nodes, and the local packs showed existing transitive paths that preserve the graph reachability needed for the remaining descendants.
---

## Scope

This report covers the admitted knowledge base only.

- Knowledge root: `../EconCSLib/docs/knowledge`
- Scope mode: `admitted`
- Staged nodes included: `false`

The review considered the full admitted graph plus bounded evidence packs for two candidate nodes. Staged overlap findings were recorded as skipped signals because staged content is outside scope in this run.

## Deterministic Baseline

- Structural check passed with `0` errors and `1` warning. The warning came from the Lean repository state: `econcslib` has uncommitted or untracked files.
- Lint returned multiple findings across several classes, including `LINT_FUZZY_DUP`, `LINT_STAGED_OVERLAP`, `LINT_REDUNDANT_DEP`, `LINT_PROSE_DEP`, `LINT_TOPIC_CYCLE`, and `LINT_TOPIC_LEAN_ALIGNMENT`.
- Graph stats reported `535` total nodes, `273` admitted, `262` staged, `12` topics in use, DAG depth `14`, and `3` orphans.
- The highest in-degree hot spots were in `game_theory.strategic_game.*` and related minimax nodes; the highest out-degree hot spots were in `mechanism_design` and `math.minimax`.

The baseline does not justify any bulk structural rewrite. The only concrete operations that survived refinement are two low-risk redundant-dependency removals in the admitted matching subgraph.

## Proposals

| proposal_id | kind | classification | targets | action | evidence | risk | validation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| refactor-001 | remove-redundant-dependency | mechanical-safe | `market_design.matching.one_to_one.gale_shapley_algorithm`, `market_design.matching.one_to_one.market` | Remove `market_design.matching.one_to_one.market` from `uses` in `gale_shapley_algorithm`. | `LINT_REDUNDANT_DEP` on `market_design.matching.one_to_one.gale_shapley_algorithm`; refactor pack shows direct dependencies `{market, matching}`, no body refs, and a transitive path to `market` through `matching`. | Minimal. The node body does not cross-link `market`, so there is no prose dependency to reconcile. The only risk is an unintended loss of explicit bookkeeping for a prerequisite already implied by the graph. | Dry-run: `uv --cache-dir /tmp/uv-cache run python -m tools.knowledge.refactor_dry_run ../EconCSLib/docs/knowledge runs/refactor-countercheck/20260615T124240Z/dry-runs/refactor-plan.yml --json`. After applying, rerun `tools.knowledge.check` and `mdblueprint-lint`. |
| refactor-002 | remove-redundant-dependency | mechanical-safe | `market_design.matching.one_to_one.lattice`, `market_design.matching.one_to_one.stability` | Remove `market_design.matching.one_to_one.stability` from `uses` in `lattice`. | `LINT_REDUNDANT_DEP` on `market_design.matching.one_to_one.lattice`; refactor pack shows direct dependencies `{stability, proposing_optimal}`, no body refs to `stability`, and a transitive path to `stability` via `proposing_optimal -> gale_shapley_stable -> stability`. | Low. The node body still names stable matchings, but only expositoryly; the graph evidence indicates the direct edge is bookkeeping only. | Dry-run: `uv --cache-dir /tmp/uv-cache run python -m tools.knowledge.refactor_dry_run ../EconCSLib/docs/knowledge runs/refactor-countercheck/20260615T124240Z/dry-runs/refactor-plan.yml --json`. After applying, rerun `tools.knowledge.check` and `mdblueprint-lint`. |

## Refinement Pass

I ranked semantic candidates ahead of lint-hygiene candidates and then filtered out anything that needed body rewrites, topic policy, or staged-node involvement. That left only the two direct-edge removals above.

Reclassifications:

- `LINT_TOPIC_LEAN_ALIGNMENT` findings were not promoted. They require a topic/Lean hierarchy decision, not a mechanical graph cleanup.
- `LINT_STAGED_OVERLAP` findings were not promoted. This run is `admitted` only, so staged nodes are outside the reviewed graph.
- `LINT_PROSE_DEP` findings were not promoted. Removing those edges cleanly would require prose/body rewrites or explicit expository exceptions, which is not a safe mechanical operation here.
- `LINT_FUZZY_DUP` findings were not promoted. They need canonical-survivor decisions and, in some cases, merge or deletion semantics rather than dependency pruning.
- `LINT_TOPIC_CYCLE` was not promoted. It is a topic-taxonomy projection issue, not a local dependency refactor.

Important signals considered but not promoted:

| signal | targets | why_not_proposed | follow_up |
| --- | --- | --- | --- |
| `LINT_FUZZY_DUP` | `game_theory.strategic_game.zero_sum.core.strong_complementarity`, `math.linear_programming.minimax_bridge.player_1_lp`, `social_choice.fair_division.divisible.allocation`, others | Needs canonical-node selection and, for some pairs, semantic merge or deletion judgment. | Open a duplicate/merge review with a named survivor. |
| `LINT_STAGED_OVERLAP` | `game_theory.extensive_game.imperfect_information.spe_imperfect_information`, `game_theory.extensive_game.perfect_information.kuhn_spe_existence_with_chance`, `game_theory.extensive_game.perfect_information.zero_sum_perfect_information_value_with_chance` | Staged nodes are outside `admitted` scope. | Re-run in `admitted+staged` or hand off to admission review. |
| `LINT_PROSE_DEP` | `math.minimax.lp_duality_minimax_proof`, `math.minimax.minimax_from_loomis`, `math.minimax.value_predicates` | These would need prose rewrites or a deliberate expository exception, not a pure dependency cleanup. | Resolve with body edits and a semantic pass. |
| `LINT_TOPIC_LEAN_ALIGNMENT` | `foundation.cost.examples.*`, `game_theory.strategic_game.*`, `math.minimax.*`, `social_choice.*` | Requires topic/Lean policy, possibly `topic_lean_alignment: divergent` or a topic move. | Escalate to alignment review or topic-maintenance work. |
| `LINT_TOPIC_CYCLE` | `game_theory.strategic_game`, `game_theory.extensive_game`, `game_theory.zero_sum` | Topic-browser projection issue, not a node-edge refactor. | Address in topic taxonomy / navigation maintenance. |
| high-degree hot spots | `game_theory.strategic_game.nash_equilibrium`, `game_theory.strategic_game.strategic_game`, `game_theory.strategic_game.zero_sum.core.value`, `mechanism_design.myerson.optimal_auction`, `math.minimax.loomis_theorem` | No local refactor evidence from the bounded packs for a topology or formulation change. | Inspect in a dedicated topic- or node-focused pass if they become the target of a future review. |

## Human Decisions

- No human decision is needed for the two mechanical removals once the dry-run validates.
- Duplicate, staged-overlap, and Lean/topic-alignment findings remain human decisions for a separate pass.

## Formulation-Sensitive Impact

These are dependency-only changes, so the impact is limited to graph bookkeeping rather than theorem text or node semantics.

- `market_design.matching.one_to_one.gale_shapley_algorithm`
  - Reviewed descendants: `market_design.matching.one_to_one.gale_shapley_stable`, `market_design.matching.one_to_one.proposing_optimal`.
  - Role of the changed edge: `market_design.matching.one_to_one.market` is a direct prerequisite of the algorithm node but is already supplied transitively through `market_design.matching.one_to_one.matching`.
  - Preservation check: the descendants do not lose any prerequisite path because the retained `matching` edge still carries the market dependency.
  - Result: safe to remove as redundant bookkeeping.

- `market_design.matching.one_to_one.lattice`
  - Reviewed descendants: none.
  - Role of the changed edge: `market_design.matching.one_to_one.stability` is present as a direct edge but already flows through `market_design.matching.one_to_one.proposing_optimal -> market_design.matching.one_to_one.gale_shapley_stable -> market_design.matching.one_to_one.stability`.
  - Preservation check: no loaded descendant depends on the removed edge directly, and the body only mentions `[[proposing_optimal]]` and `[[rural_hospitals]]`.
  - Result: safe to remove as redundant bookkeeping.

## Generality Gate

The generality question is not driving any structural refactor here. Both proposals are narrow graph cleanups, not node generalizations, splits, or merges.

- Most general useful form: not applicable to the chosen operations.
- Whether the current node already has that form: not applicable.
- Whether a narrower form is deliberate: yes, the current nodes are intentionally specific matching-theory statements and algorithm descriptions.
- Assumptions removable: only the duplicated dependency edges identified by the DAG.
- Hypotheses that may be artifacts of current placement: none that require a request or a body rewrite for this review.

## Request Files

No request files are needed for this report.

- No node additions were proposed.
- No split/generalize/merge action was selected.
- The scope is `admitted`, so staged-node requests were intentionally excluded.

