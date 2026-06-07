# EconCSLib Full Export Structural Diff

This report compares:

- source tree: [`/home/azureuser/EconCSLib/docs/knowledge`](\/home\/azureuser\/EconCSLib\/docs\/knowledge)
- Lean-backed export tree: `/tmp/econcslib-blueprint-full-export`

The export was produced with the already-existing Lean-backed pipeline in [`tools/knowledge/lean_blueprint_export.py`](\/home\/azureuser\/mdblueprint\/tools\/knowledge\/lean_blueprint_export.py).

## Export Summary

- nodes: `535`
- topics in generated `mdblueprint.yml`: `112`
- final inferred `uses` edges after DAG pruning: `270`
- file set diff: none
  - no missing files
  - no extra files

The export is structurally aligned with the source tree at the file level, but not at the metadata level.

## Verification Result

The tree comparison is not clean.

- `mdblueprint.yml` differs
- `473` node metadata differences were detected by the tree verifier
- the repo checker reports:
  - `20` errors
  - `384` warnings

## What Stayed The Same

The following remained stable across the source tree and the exported tree:

- file layout
- node count
- topic count in the source tree is preserved as a topic projection in the export
- Lean declaration coverage for the nodes that existed in the source tree
- the underlying node bodies were copied, not regenerated

## What Changed

### 1. `uses` changed in `472` nodes

This is the main structural delta.

The exported tree replaces authored `uses` values with Lean-inferred, DAG-pruned dependencies.

Examples:

- `foundation.cost.cells`
  - source `uses`: `["foundation.cost.costm"]`
  - exported `uses`: `[]`
- `foundation.cost.examples.boyer_moore`
  - source `uses`: `["foundation.cost.costm", "foundation.cost.cells"]`
  - exported `uses`: `["foundation.cost.cells", "foundation.cost.costm"]`
- `foundation.cost.examples.par_all`
  - source `uses`: `["foundation.cost.costm", "foundation.cost.parallel"]`
  - exported `uses`: `["foundation.cost.parallel"]`
- `foundation.cost.examples.par_sum`
  - source `uses`: `["foundation.cost.costm", "foundation.cost.parallel"]`
  - exported `uses`: `["foundation.cost.parallel"]`
- `foundation.preference.abstract_relation`
  - source `uses`: `[]`
  - exported `uses`: `["foundation.utility.lottery"]`
- `foundation.preference.indifferent`
  - source `uses`: `[]`
  - exported `uses`: `["foundation.preference.strictly_preferred", "foundation.preference.total_preorder"]`
- `foundation.preference.relation`
  - source `uses`: `["foundation.preference.indifferent", "foundation.preference.strictly_preferred", "foundation.preference.total_preorder", "foundation.preference.abstract_relation"]`
  - exported `uses`: `[]`

Interpretation:

- some authored `uses` edges are pruned away because the Lean-backed DAG pass treats them as redundant or transitive
- some authored edges are replaced by finer-grained Lean-backed dependencies
- some source edges are not recoverable from Lean alone because they encode pedagogical or conceptual prerequisites rather than exact theorem references

### 2. `mdblueprint.yml` differs

The source and generated configs are not identical.

The meaningful config deltas are:

- `graph`
  - source: only `max_visible_nodes`, `max_expand_nodes`, `proof_plans`
  - export adds:
    - `max_page_total`
    - `inline_child_max_size`
- `lean`
  - source uses a relative placeholder path and `"revision": "auto"`
  - export rewrites the Lean repository payload with:
    - an output-relative `local_path`
    - the concrete Lean repo revision
- `lint`
  - source omits this section
  - export materializes the default lint config
- `math`
  - source omits explicit delimiter settings
  - export writes the default delimiter configuration
- `sources`
  - source omits `require_source_spans`
  - export writes `require_source_spans: false`

So the config mismatch is partly a normalization effect and partly a synthesis effect.

## Checker Diagnostics

The repo checker reports two classes of structural problems in the exported tree.

### Errors

There are `20` errors total.

- `18` are proof-plan structural errors of the form `proof-plan target is required`
- `2` are dependency-shape errors where a mathematical node uses a proof-plan node as a dependency

Representative errors:

- `math.linear_programming.minimax_bridge.zero_sum_lp_bridge`
  - `proof-plan target is required`
- `math.minimax.kakutani_minimax_proof`
  - `proof-plan target is required`
- `math.minimax.loomis_induction_proof`
  - `proof-plan target is required`
- `math.minimax.minimax_from_loomis`
  - `proof-plan target is required`
- `math.minimax.loomis_induction_proof.base_case`
  - `mathematical node uses proof-plan node as a dependency; proof-plan nodes must use target instead: 'math.minimax.minimax_from_loomis'`
- `game_theory.strategic_game.zero_sum.von_neumann_minimax`
  - `mathematical node uses proof-plan node as a dependency; proof-plan nodes must use target instead: 'math.minimax.minimax_from_loomis'`

Interpretation:

- the export can materialize a tree and compute a DAG, but proof-plan nodes still require semantic curation
- the checker is enforcing a stronger contract than the exporter currently guarantees
- the problematic edges are not file-layout failures; they are node-role and dependency-role failures

### Warnings

There are `384` warnings total.

The important subgroup is the missing `uses` warnings:

- `40` warnings say that a proof reference appears in the body, but the referenced node is not listed in `uses`

Representative warnings:

- `math.linear_algebra.farkas_lemma`
  - proof references `math.linear_algebra.theorem_of_alternative`
- `math.linear_programming.strong_complementarity`
  - proof references `math.linear_algebra.farkas_lemma`
- `math.minimax.common_guarantee_value`
  - proof references:
    - `game_theory.strategic_game.zero_sum.von_neumann_minimax`
    - `game_theory.strategic_game.zero_sum.core.player_guarantee`
- `math.minimax.loomis_induction_proof.value_existence`
  - proof references:
    - `math.simplex.continuity`
    - `math.simplex.bounded_by_value`
    - `game_theory.strategic_game.zero_sum.lam_mu_existence`

Interpretation:

- the Lean-inferred DAG is conservative and intentionally drops many low-level proof dependencies
- the checker still expects some of those proof references to appear in `uses`
- this means the current `uses` inference is structurally valid as a DAG, but not yet complete as a proof-reference coverage mechanism

## Main Failure Modes

The differences cluster into three failure modes:

1. **Curated `uses` vs Lean-derived `uses`**
   - authored source uses pedagogy and exposition
   - the export uses Lean-backed theorem references and then prunes redundancies

2. **Proof-plan handling**
   - the exporter includes proof-plan-like nodes from the source tree
   - the checker requires proof-plan targets to be explicit and prohibits some role-mismatched dependencies

3. **Config normalization**
   - the exporter synthesizes a more complete `mdblueprint.yml`
   - this introduces config differences even when the source tree is otherwise copied verbatim

## Proof-Plan Contract

The remaining checker failures are not generic graph issues. They come from the repository's proof-plan contract.

The relevant rules are enforced in [`tools/knowledge/validator.py`](/home/azureuser/mdblueprint/tools/knowledge/validator.py) and [`tools/knowledge/graph.py`](/home/azureuser/mdblueprint/tools/knowledge/graph.py):

- a node with `kind: proof-plan` must declare a `target`
- that `target` must point to an existing theorem-like node
- a proof-plan node may not use its own target as a normal `uses` dependency
- a mathematical node may not depend on a proof-plan node directly
  - instead, the theorem node should depend on the theorem that the plan proves
- a theorem node with `proved_via_plan` must point to a real proof-plan node whose `target` is that theorem

The concrete export failures fall into this bucket:

- proof-plan nodes like `math.minimax.loomis_induction_proof` are missing `target`
- theorem nodes like `math.minimax.loomis_induction_proof.base_case` and `game_theory.strategic_game.zero_sum.von_neumann_minimax` still point at proof-plan nodes in `uses`

So the next step is a policy decision:

1. **Normalize proof-plan metadata in the export**
   - add or repair `target` on proof-plan nodes
   - move theorem-to-plan dependencies onto theorem targets
   - preserve proof plans as first-class graph objects

2. **Exclude proof-plan nodes from the exported proposal tree**
   - export only theorem-like nodes and their Lean-derived DAG
   - treat proof plans as an auxiliary review artifact instead of part of the comparison tree

For the current ablation study, option 1 is the stronger test because it preserves more of the source structure while exposing how much of the mismatch is due to proof-plan semantics rather than theorem dependency inference.

## Bottom Line

The export is file-complete and structurally close, but it is not a drop-in equality check against the authored EconCSLib knowledge tree.

The dominant mismatch is `uses`:

- `472` nodes changed
- many changes are intentional DAG reductions
- many others expose the gap between Lean-backed theorem dependencies and the authored blueprint dependency layer

The checker then surfaces the remaining contract violations:

- proof-plan nodes missing targets
- mathematical nodes depending on proof-plan nodes
- proof references that are not promoted into `uses`

This makes the exported tree a useful proposed blueprint, but not yet a fully admitted ground-truth replacement.
