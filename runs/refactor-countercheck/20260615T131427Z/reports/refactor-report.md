---
agent: graph-refactor-proposer
target:
  knowledge_root: ../EconCSLib/docs/knowledge
decision: needs_human_decision
created_at: "2026-06-15T13:14:27Z"
inputs:
  - "uv --cache-dir /tmp/uv-cache run python -m tools.knowledge.check ../EconCSLib/docs/knowledge"
  - "uv --cache-dir /tmp/uv-cache run mdblueprint-lint ../EconCSLib/docs/knowledge --json"
  - "uv --cache-dir /tmp/uv-cache run python -m tools.knowledge.stats ../EconCSLib/docs/knowledge --json"
  - "../EconCSLib/docs/knowledge/nodes/zero_sum/core/strong_complementarity.md"
  - "../EconCSLib/docs/knowledge/nodes/math/minimax/strong_complementarity.md"
  - "../EconCSLib/docs/knowledge/staged/extensive_game/spe_imperfect_information.md"
  - "../EconCSLib/docs/knowledge/nodes/foundation/cost/examples/boyer_moore.md"
summary: Whole-KB admitted+staged refactor review found strong semantic overlap and topic-policy decisions, but no mechanically safe graph edit survived refinement.
baseline:
  check: passed
  lint: findings
  stats: collected
formulation_impact:
  reviewed: true
  reason: Merge/overlap/topic-policy changes can alter descendant validity or ownership, so the review treated those signals as semantic decisions rather than bulk cleanup.
---

## Scope

This report covers the whole knowledge base in `admitted+staged` mode.
Staged nodes were included as graph evidence for dependency existence,
reachability, duplicate/overlap, topic, and formulation-impact analysis, but
they were not treated as admitted truth.

The review concentrated on the highest-signal areas surfaced by the baseline:
`game_theory.strategic_game.zero_sum`, `math.minimax`,
`game_theory.extensive_game`, `foundation.cost`, and the Lean/topic alignment
cluster spanning `foundation`, `game_theory`, `math`, and `social_choice`.

## Deterministic Baseline

- Structural check: passed, with one warning from the Lean repository gate about
  uncommitted or untracked files in `econcslib`.
- Graph stats: 535 total nodes, 273 admitted, 262 staged, 12 topics in use,
  DAG depth 14, and 3 orphans.
- High-degree hotspots: `game_theory.strategic_game.nash_equilibrium` (23
  inbound), `game_theory.strategic_game.strategic_game` (20), and
  `game_theory.strategic_game.zero_sum.core.value` (20) were the main
  dependency hubs.
- Lint summary: 405 findings total, 323 warnings and 82 info findings.
- Lint codes of interest:
  - `LINT_FUZZY_DUP`: 7
  - `LINT_STAGED_OVERLAP`: 3
  - `LINT_REDUNDANT_DEP`: 74
  - `LINT_PROSE_DEP`: 50
  - `LINT_TOPIC_CYCLE`: 2
  - `LINT_TOPIC_LEAN_ALIGNMENT`: 26
  - `LINT_LEAN_KIND`: 237
  - `LINT_ORPHAN`: 2
  - `LINT_LEAN_MODULE_FRAGMENTED`: 4

The baseline points to three broad classes of work:

- semantic duplication or near-duplication;
- staged nodes that overlap admitted content;
- editorial topic/Lean divergence that needs human policy, not blind rewriting.

## Proposals

| proposal_id | kind | classification | targets | action | evidence | risk | validation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| refactor-001 | merge-duplicate | semantic-review | `game_theory.strategic_game.zero_sum.core.strong_complementarity`, `math.minimax.strong_complementarity` | Treat the pair as a canonical-content decision before any merge. They share title, source span, Lean declaration, and proof shape, but they live in different topic homes and the math node carries extra LP context. | `LINT_FUZZY_DUP` between the two nodes; inspected both node bodies and frontmatter. | Deleting one node without a canonical-choice review could discard intended topic ownership or reverse-dependency visibility. | Review both nodes side by side, then run a focused refactor dry-run only if a survivor and migration path are agreed. |
| refactor-002 | needs-human-review | semantic-review | `game_theory.extensive_game.imperfect_information.spe_imperfect_information`, `game_theory.extensive_game.perfect_information.kuhn_spe_existence_with_chance`, `game_theory.extensive_game.perfect_information.zero_sum_perfect_information_value_with_chance` | Decide whether the staged nodes are genuinely distinct chance/no-chance or imperfect-information variants, or whether one or more should be generalized/reframed before admission. | `LINT_STAGED_OVERLAP` against the admitted SPE and no-chance nodes; all three candidates are still staged. | Premature collapse would erase mathematically relevant distinctions; premature admission would duplicate content. | Admission-referee review with formulation-sensitive comparison against the admitted counterparts. |
| refactor-003 | mark-lean-topic-divergent | semantic-review | `foundation.cost.examples.boyer_moore`, `foundation.cost.examples.gcd`, `foundation.cost.examples.lcs`, `foundation.cost.examples.memo_fib`, `foundation.cost.examples.par_all`, `foundation.cost.examples.par_sum`, `foundation.cost.examples.reverse_space`, `game_theory.extensive_game.perfect_information.simple_perfect_information_game`, `game_theory.strategic_game.prisoners_dilemma`, `game_theory.strategic_game.zero_sum.applications.perron_frobenius_positive_matrix`, `game_theory.strategic_game.zero_sum.core.mixed_extension`, `game_theory.strategic_game.zero_sum.core.mixed_strategy_simplex`, `game_theory.strategic_game.zero_sum.examples.computation_three_by_two_example`, `game_theory.strategic_game.zero_sum.examples.diagonal_matrix_game_value`, `game_theory.strategic_game.zero_sum.examples.matching_pennies`, `game_theory.strategic_game.zero_sum.examples.three_player_minimax_failure`, `game_theory.strategic_game.zero_sum.examples.two_by_two_value_formula`, `game_theory.strategic_game.zero_sum.lam_mu_existence`, `math.minimax.antisymmetric_matrix_game_value`, `math.minimax.common_guarantee_value`, `math.minimax.strong_complementarity`, `math.minimax.value_predicates`, `math.minimax.zero_sum_nash_saddle`, `social_choice.preference`, `social_choice.preference_profile`, `social_choice.strict_preference` | Treat the Lean/topic mismatch cluster as an editorial policy issue. Do not bulk-apply topic rewrites from the lint alone; decide per cluster whether the Lean root or the blueprint root is the intended home. | `LINT_TOPIC_LEAN_ALIGNMENT` across 26 nodes, spanning several unrelated topic roots and both example-heavy and theory-heavy areas. | A blanket rewrite would move content away from its conceptual home and could make the graph harder to navigate. | Human policy review, then local node edits or `topic_lean_alignment: divergent` only where the divergence is intentional. |

## Refinement Pass

Semantic candidates were ranked above mechanical hygiene because the baseline
contains stronger signals about duplicate content, staged/admitted overlap, and
topic ownership than about simple redundant edges.

I did not promote `LINT_REDUNDANT_DEP` into the dry-run plan even though it is
the largest mechanical bucket. The reason is that the same baseline also shows
high-value semantic work:

- fuzzy duplicates where canonical survivor choice matters;
- staged overlaps that may be separate mathematical variants;
- broad Lean/topic divergence spanning multiple topic families.

The following signals were considered but not promoted into concrete operations:

| signal | targets | why_not_proposed | follow_up |
| --- | --- | --- | --- |
| `LINT_REDUNDANT_DEP` | Many nodes across `foundation.cost`, `game_theory.cooperative_game`, `game_theory.extensive_game`, `game_theory.strategic_game.zero_sum`, `market_design.matching.one_to_one`, and `math.minimax` | Low-risk hygiene, but not the best use of the proposal budget while merge/overlap/topic-policy questions remain unresolved. | After semantic decisions settle, rerun a focused dependency-cleanup pass on the surviving canonical nodes. |
| `LINT_PROSE_DEP` | Especially `math.minimax.*`, `foundation.cost.*`, and related proof-heavy nodes | Several of these are proof-route or exposition cross-links that need local body inspection; the lint alone does not prove a structural dependency bug. | Review only the nodes whose prose links are believed to be accidental structural edges. |
| `LINT_TOPIC_CYCLE` | `game_theory.extensive_game` ↔ `game_theory.strategic_game` and `game_theory.strategic_game` ↔ `game_theory.zero_sum` | The detector explicitly notes that the underlying node-level DAG remains acyclic; this is a topic-projection artifact, not a node refactor target. | Handle only if topic navigation policy changes. |
| `LINT_FUZZY_DUP` | `game_theory.strategic_game.zero_sum.core.strong_complementarity` vs `math.minimax.strong_complementarity`; `math.linear_programming.minimax_bridge.player_1_lp` vs `player_2_lp`; fair-division instance nodes | Some are exact or near-exact duplicates, but the right canonical survivor depends on topic ownership and reverse-dependency intent. | Resolve canonicals one pair at a time, then write the corresponding merge or deprecation plan. |
| High-degree hot spots | `game_theory.strategic_game.nash_equilibrium`, `game_theory.strategic_game.strategic_game`, `game_theory.strategic_game.zero_sum.core.value` | These are shared hubs, not obvious refactor defects. | Only revisit if a specific dependency or topic change touches one of these hubs. |

## Generality Gate

The only plausible generalization-style questions were the staged extensive-game
overlaps. Their chance/no-chance and imperfect-information distinctions are
mathematically meaningful, but the baseline did not provide enough evidence to
collapse them into a single generalized node or to split them into separate
survivors mechanically.

For the strong-complementarity duplicate pair, the issue is not generality but
canonical content ownership: both nodes state the same theorem with different
topic homes, so the question is which home should survive, not which statement
is more general.

## Formulation-Sensitive Impact

The proposal space was checked for descendant impact, but no dependency rewrite
was promoted to a concrete operation.

- `game_theory.strategic_game.zero_sum.core.strong_complementarity` and
  `math.minimax.strong_complementarity` share the same statement, proof source,
  and Lean declaration. The risk is not theorem invalidation but duplicate
  ownership and reverse-dependency ambiguity if one node is deleted without a
  canonical decision.
- The staged extensive-game overlap nodes are formulation-sensitive because the
  chance/no-chance and imperfect-information distinctions can change the exact
  statement family. A naive collapse could erase a genuinely different theorem
  shape.

## Request Files

No request files were written. The review did not identify a new node, split,
or generalized statement with enough certainty to justify a
`docs/knowledge/requests/` artifact.

## Human Decisions

- Pick the canonical survivor for the `strong_complementarity` pair.
- Decide whether the staged extensive-game overlap nodes are separate variants
  or should be generalized/rewritten before admission.
- Decide whether the `LINT_TOPIC_LEAN_ALIGNMENT` cluster should be marked as
  intentional divergence or whether any subtree should be moved to match Lean
  module roots.

## Conclusion

No concrete operation survived refinement. The correct output of this run is a
human-decision report plus an empty dry-run plan, not a mechanical edit plan.
