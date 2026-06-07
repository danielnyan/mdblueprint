# Uses Inference Implementation Report

## Summary

This pass implements a conservative `uses` inference module for Lean-backed
nodes and wires it into the Lean node sample generator.

The generated `uses` field is no longer always blank when the generator is
given a knowledge tree as a node/declaration index.

## Implementation

New module:

- `mdblueprint/knowledge_uses.py`

Generator update:

- `skills/mdblueprint-lean-node-generation/scripts/generate_sample_node_drafts.py`

Test coverage:

- `tests/test_knowledge_uses.py`

The inference pass uses two evidence sources:

- explicit `[[node:...]]` references in theorem proof sections
- Lean declaration references reachable from the source node's
  `lean.declarations`

For Lean evidence, the pass builds a declaration-reference graph from Lean
source text. It strips comments before extracting symbols, then follows direct
references and narrow transitive references through helper declarations.

It maps declaration references back to node ids using the existing knowledge
tree's `lean.declarations`.

## Guardrails

The first implementation was too broad: it scanned every declaration against
every other declaration and emitted many false positives. The current version
hardens that in several ways:

- symbol lookup is token-indexed rather than all-pairs regex matching
- generic leaf names such as `allocation`, `value`, `winner`, `pure`, and
  `bind` are ignored as standalone evidence
- Lean comments and docstrings are stripped before reference extraction
- markdown node refs are considered only in theorem proof sections
- dependencies must pass a topic-compatibility filter
- transitive Lean dependencies are emitted only when the intermediate
  declarations are not already represented by other nodes

These rules are still heuristic, but they make the output usable for an
ablation study instead of leaving `uses` blank.

## Validation

Compile check:

- `uv run python -m py_compile mdblueprint/knowledge_uses.py skills/mdblueprint-lean-node-generation/scripts/generate_sample_node_drafts.py tests/test_knowledge_uses.py`

Focused checks:

- direct theorem proof reference via `[[node:...]]`
- transitive Lean reference through a private helper declaration

`pytest` is still unavailable in the VM, so the focused checks were executed
directly with `uv run python`.

## Sample Results

The generator was run with:

```bash
uv run python skills/mdblueprint-lean-node-generation/scripts/generate_sample_node_drafts.py \
  --lean-root /home/azureuser/EconCSLib \
  --knowledge-root /home/azureuser/EconCSLib/docs/knowledge \
  --output /tmp/mdblueprint-inferred-uses-sample
```

### Original Six-Node Sample

| node | authored count | inferred count | true positives | missing | extras |
| --- | ---: | ---: | ---: | ---: | ---: |
| `foundation.cost.examples.reverse_space` | 1 | 1 | 1 | 0 | 0 |
| `game_theory.strategic_game.equilibrium.nash_existence_finite_games` | 2 | 8 | 0 | 2 | 8 |
| `math.minimax.common_guarantee_value` | 4 | 6 | 2 | 2 | 4 |
| `social_choice.fair_division.divisible.proportional_exists` | 1 | 8 | 1 | 0 | 7 |
| `social_choice.fair_division.indivisible.maximin_share` | 2 | 4 | 2 | 0 | 2 |
| `social_choice.fair_division.indivisible.round_robin_alloc` | 2 | 4 | 1 | 1 | 3 |

### Round-2 Five-Node Sample

| node | authored count | inferred count | true positives | missing | extras |
| --- | ---: | ---: | ---: | ---: | ---: |
| `social_choice.fair_division.divisible.dubins_spanier_proportional` | 1 | 6 | 0 | 1 | 6 |
| `game_theory.strategic_game.zero_sum.maximin_le_minimax` | 1 | 3 | 1 | 0 | 2 |
| `social_choice.fair_division.indivisible.best_good` | 1 | 2 | 0 | 1 | 2 |
| `foundation.cost.costm` | 0 | 0 | 0 | 0 | 0 |
| `game_theory.strategic_game.zero_sum.von_neumann_minimax` | 0 | 7 | 0 | 0 | 7 |

## Findings

The implementation succeeds at the basic requirement: generated `uses` are no
longer blank when there is Lean-backed or proof-section evidence.

It performs best on nodes where the authored edge is close to a concrete Lean
declaration:

- `foundation.cost.examples.reverse_space -> foundation.cost.costm`
- `social_choice.fair_division.indivisible.maximin_share -> allocation`
- `social_choice.fair_division.indivisible.maximin_share -> valuation`
- `game_theory.strategic_game.zero_sum.maximin_le_minimax -> maximin_minimax`

It misses authored edges when the target node is a wrapper concept rather than
the exact declaration reached by Lean:

- `round_robin_alloc -> best_good`
- `best_good -> additive_valuation`
- `nash_existence_finite_games -> mixed_nash_equilibrium`
- `nash_existence_finite_games -> brouwer_compact_convex`

It emits extra edges when the Lean proof exposes immediate formal prerequisites
that the authored blueprint omits for readability:

- low-level simplex facts
- bundled cardinal/instance structures
- measure/allocation definitions
- Loomis/minimax intermediate lemmas

One important metadata issue was found:

- `social_choice.fair_division.divisible.ds_step` currently lists
  `SocialChoice.FairDivision.Divisible.dubinsSpanierProportional` in
  `lean.declarations`, not the private `ds_step` declaration. That prevents
  the inference pass from mapping the Lean `ds_step` reference back to the
  authored `ds_step` node.

## Interpretation

This pass should be treated as a candidate generator, not a final authority.

The hard rule that `uses` should be Lean-backed is now implementable, but
Lean-backed evidence is broader than authored `uses`. The code can identify
formal dependencies; it still needs a ranking/minimality layer to decide which
formal dependencies should become direct blueprint edges.

The remaining work is to classify inferred edges into:

- direct authored-style dependencies
- low-level formal prerequisites
- wrapper-node misses
- metadata mismatches in `lean.declarations`

That classification can drive a verifier that reports candidate edges and
missing wrapper nodes without automatically overwriting the curated graph.

