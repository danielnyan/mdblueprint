# EconCSLib Full Export Structural Diff

This report compares:

- source tree: [`/home/azureuser/EconCSLib/docs/knowledge`](\/home\/azureuser\/EconCSLib\/docs\/knowledge)
- Lean-backed export tree: `/tmp/econcslib-blueprint-full-export`

The export was produced with the already-existing Lean-backed pipeline in [`tools/knowledge/lean_blueprint_export.py`](\/home\/azureuser\/mdblueprint\/tools\/knowledge\/lean_blueprint_export.py). In this project, the authored Markdown node tree and `mdblueprint.yml` remain the primordial source; Lean is the formal evidence layer used to project or validate dependencies, not the durable truth store for the graph.

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

### 1a. Authored graph vs Lean-derived graph shape

The Lean-derived graph is substantially sparser than the authored graph.

| graph | nodes | edges | nodes with `uses` | isolated nodes | average out-degree |
|---|---:|---:|---:|---:|---:|
| authored source | `535` | `840` | `503` | `3` | `1.57` |
| Lean-derived export | `535` | `270` | `181` | `298` | `0.50` |

At the top-level topic boundary:

| graph | cross-topic edges | top-level topic pairs |
|---|---:|---:|
| authored source | `49` | `4` |
| Lean-derived export | `35` | `6` |

The authored graph is denser overall and keeps almost every node attached to the dependency graph. Its cross-topic edges are concentrated in a few high-level flows, especially between `math` and `game_theory`.

The Lean-derived graph is more tree-like because it keeps only edges that survive Lean-backed inference, transitive pruning, and cycle breaking. That makes it better as a minimal formal dependency skeleton, but worse as a human-readable proof roadmap.

The two graphs therefore represent different structures:

- authored source graph: blueprint, pedagogy, and proof narrative
- Lean-derived export graph: conservative formal dependency skeleton

Neither graph should be treated as automatically superior. The authored graph may contain non-mechanical or redundant edges. The Lean-derived graph may drop proof-stage continuation edges that are mathematically important for exposition.

### 1b. Loomis weak-duality failure case

The clearest observed failure is the relationship between:

- `math.minimax.loomis_induction_proof.value_existence`
- `math.minimax.loomis_induction_proof.weak_duality`

In the authored source tree, `weak_duality` correctly uses `value_existence`:

```yaml
uses:
  - math.minimax.loomis_induction_proof.positive_aggregate
  - math.minimax.loomis_induction_proof.value_existence
```

The node body also explicitly depends on value existence:

- the statement defines `lambda_0` and `mu_0` through `value_existence`
- the proof chooses optimizers supplied by `value_existence`

The Lean source supports this relationship. In `Loomis.lamB0_le_muB0`, the proof directly obtains the optimizers:

```lean
obtain ⟨xx, Hxx⟩ := exists_xx_lamB0 A B hB
obtain ⟨yy, Hyy⟩ := exists_yy_muB0 A B hB
```

Those declarations are part of the `value_existence` node.

However, the generated export currently records:

```yaml
uses:
  - math.simplex.wsum_comm
```

This is the wrong abstraction level for the blueprint graph. It keeps a low-level Lean implementation lemma while dropping the proof-stage continuation edge to `value_existence`.

The raw inference pass did find the authored body references:

- `weak_duality -> value_existence` with evidence `body_node_ref`
- `weak_duality -> positive_aggregate` with evidence `body_node_ref`

The final pruning pass then dropped all `body_node_ref` edges from final `uses`, keeping only Lean declaration references. As a result, the generated graph overprivileged `wsum_wsum_comm` and lost the proof narrative.

This exposes two failure modes:

- body-explicit proof references are too aggressively excluded from final `uses`
- Lean leaf-name matching can be noisy and may surface low-level or unrelated declarations such as generic `trans` lemmas

For this case, the authored edge `weak_duality -> value_existence` should survive because it is both body-explicit and Lean-supported through `exists_xx_lamB0` and `exists_yy_muB0`.

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

The differences cluster into seven failure modes:

1. **Curated `uses` vs Lean-derived `uses`**
   - authored source uses pedagogy and exposition
   - the export uses Lean-backed theorem references and then prunes redundancies

2. **Narrative proof-stage edges removed**
   - body-explicit `[[node:...]]` proof references are currently collected but excluded from final `uses`
   - this can remove real proof continuations, as in `weak_duality -> value_existence`

3. **Low-level Lean implementation edges retained**
   - declaration matching may retain helper lemmas such as `wsum_wsum_comm`
   - these are formally relevant but often too low-level for the blueprint graph
   - leaf-name matching can also surface unrelated generic declarations when names are too broad

4. **Proof-plan handling**
   - the exporter includes proof-plan-like nodes from the source tree
   - the checker requires proof-plan targets to be explicit and prohibits some role-mismatched dependencies

5. **Config normalization**
   - the exporter synthesizes a more complete `mdblueprint.yml`
   - this introduces config differences even when the source tree is otherwise copied verbatim

6. **Theorem-name dependence**
   - the current Lean reference matcher benefits from well-named declarations
   - if theorem names become opaque, abbreviated, or mechanically generated, low-level NLP and leaf-name rules become less reliable
   - a future theorem-renamer should be treated as an upstream semantic signal, not as a replacement for Lean-backed evidence

7. **Multiple proof routes**
   - some theorems have more than one legitimate proof route
   - a flat `uses` DAG can express one selected route, but it cannot faithfully represent candidate, alternative, or parallel proofs without edge or route annotations
   - collapsing all routes into one `uses` list risks creating a graph that is formally true but misleading about the library's chosen proof architecture

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

## Proposed Remediation Plan

This section lists implementation choices to approve, revise, or veto before the next round. It now reflects the current proposal-review mode for `uses`, where the exporter flags problematic edges instead of silently pruning them.

### Prompt and skill changes

1. **Require a two-layer interpretation of `uses`**
   - Prompt agents to distinguish formal proof dependencies from blueprint proof-stage dependencies.
   - Formal proof dependencies come from Lean declaration references.
   - Blueprint proof-stage dependencies come from node-body references, proof-plan structure, and same-proof-family continuation.
   - The generated node should record the strongest explanation available for each edge, not just the final target list.

2. **Tell agents not to overvalue low-level helper lemmas**
   - Add prompt examples where `wsum_wsum_comm`, `wsum`, `trans`, or similar implementation lemmas are valid Lean evidence but poor blueprint-level `uses` targets.
   - Require promotion from low-level Lean declarations to the nearest meaningful node when such a node exists.

3. **Add positive and negative examples**
   - Positive example: `math.minimax.loomis_induction_proof.weak_duality -> math.minimax.loomis_induction_proof.value_existence`, because the proof text names it and the Lean proof obtains `exists_xx_lamB0` and `exists_yy_muB0`.
   - Positive example: a theorem using a prior theorem declaration directly should usually keep that prior theorem node.
   - Negative example: a theorem should not prefer `math.simplex.wsum_comm` over a same-proof-family optimizer-existence node when the latter explains the proof step.
   - Negative example: generic declarations reached by leaf-name matching, such as unrelated `trans` lemmas, should not create edges without stronger namespace or file evidence.

### Python and tool changes

0. **Add a theorem-renamer extension point**
   - The scaffolding now lives in [`mdblueprint/theorem_renaming.py`](/home/azureuser/mdblueprint/mdblueprint/theorem_renaming.py).
   - `TheoremRenamer.rename(declaration)` can return a canonical semantic name and aliases with confidence scores.
   - `build_uses_inference_context(..., theorem_renamer=...)` threads those aliases into the Lean reference index.
   - The default `IdentityTheoremRenamer` is a no-op, so current behavior is deterministic and unchanged unless a contributor explicitly supplies a renamer.
   - Future contributors should plug the colleague's theorem-renamer into this interface rather than editing the core `uses` pruning code first.

1. **Treat body references as review evidence, not automatic truth**
   - Keep `body_node_ref` proposals visible in the review artifact.
   - Let the agent decide whether a body reference should be retained, rerouted, or retired.
   - Use Lean reachability, proof-family prefixes, and same-proof-section evidence to rank the proposal, but do not let the exporter silently collapse it.

2. **Add edge evidence ranking**
   - Replace the current coarse evidence handling with explicit scores.
   - Proposed ranking from strongest to weakest:
     - `body_ref_and_lean_direct`
     - `body_ref_and_lean_transitive`
     - `same_family_body_ref`
     - `lean_direct_decl_to_node`
     - `lean_transitive_decl_to_node`
     - `low_level_helper_decl`
   - Use this ranking to score the proposal artifact and to explain suggested fixes, not to auto-delete edges from the published graph.

3. **Classify low-level helper declarations**
   - Add a helper-declaration filter for common infrastructure names and broad leaves.
   - Initial candidates: `wsum`, `wsum_wsum_comm`, generic `trans`, generic `map`, generic `mem`, and similarly common leaves.
   - Do not discard them entirely; demote them unless no stronger node-level explanation exists.

4. **Tighten Lean declaration matching**
   - Stop treating every sufficiently long leaf name as globally meaningful.
   - Require at least one of:
     - exact qualified-name match;
     - same module or imported module family;
     - compatible namespace prefix;
     - explicit body reference to the target node.
   - This should reduce unrelated edges such as `GameTree.Subtree.trans` appearing in a minimax proof.

5. **Use theorem-renamer output as a controlled matching signal**
   - Allow semantic aliases from the renamer to supplement exact Lean declaration names.
   - Do not let aliases create final `uses` edges by themselves unless they are supported by Lean reachability, body references, same-proof-family evidence, or manual review.
   - Emit alias provenance in the evidence report so reviewers can distinguish exact-name matches from renamer-assisted matches.

6. **Emit an edge evidence report**
   - Extend the export tool to write a machine-readable artifact, for example `uses_review.json`.
   - Each proposed edge should include:
     - source node;
     - target node;
     - review status: keep, reroute, retire, or needs-review;
     - evidence type;
     - Lean declaration path if present;
     - theorem-renamer alias used, if any;
     - body reference locations if present;
     - reviewer rationale or fix recommendation.
   - This would make future graph disagreements auditable instead of purely visual.

7. **Add a structural comparison command**
   - Add a CLI command that compares an authored tree and a generated tree.
   - It should report:
     - direct edge precision and recall;
     - transitive-closure overlap;
     - isolated-node counts;
     - per-topic edge deltas;
     - examples of lost proof-stage edges;
     - examples of low-level helper edges introduced by inference.

8. **Keep proof-plan handling explicit**
   - Preserve proof-plan nodes as first-class graph objects.
   - If a proof-plan node is missing `target`, surface that as a reviewer action item instead of hiding the node.
   - If a theorem points at a proof-plan node directly, report it as a routing issue and let the agent decide whether to repair the route or exclude the plan from the comparison tree.

9. **Represent proof routes separately from ordinary theorem dependencies**
   - Preserve `plan_status: selected` vs `candidate`.
   - Avoid flattening candidate routes into the selected theorem's ordinary `uses`.
   - Add route-level artifacts, for example `routes.json` or `uses_evidence.json` route groups, so the UI can show alternatives without changing the selected proof DAG.

## Multiple Proof Routes Observed In EconCSLib

This issue does appear in the main EconCSLib knowledge tree.

Representative cases:

- `game_theory.strategic_game.zero_sum.von_neumann_minimax`
  - selected route: `math.minimax.minimax_from_loomis`
  - additional proved route mentioned in the theorem body: `math.minimax.ordered_field_minimax`
- `math.minimax.minimax_from_loomis`
  - `plan_status: selected`
  - records the library's chosen route through the all-ones specialization of Loomis
  - explicitly mentions an alternative ordered-field-generic route
- `math.minimax.lp_duality_minimax_proof`
  - `plan_status: candidate`
  - viable via LP strong duality, but not the selected Lean proof of von Neumann minimax
- `math.minimax.kakutani_minimax_proof`
  - `plan_status: candidate`
  - records a different mathematical route to the same target
- `math.minimax.minimax_from_antisymmetric_games`
  - `plan_status: candidate`
  - records another route to the same target
- `math.minimax.minimax_from_deterministic_approachability`
  - `plan_status: candidate`
  - records another route to the same target
- `math.fixed_point.scarf_lemma`
  - records a Lean-route note indicating that the formal route differs from the source exposition route

Implication:

- the public theorem graph needs a selected proof route for normal dependency navigation
- the ablation tooling should keep candidate routes as reviewable alternatives
- graph-distance metrics should not automatically penalize a generated graph for discovering a valid alternative route, but they should distinguish "selected route mismatch" from "formal dependency error"

### Proposed tests

1. **Loomis regression test**
   - Assert that `weak_duality -> value_existence` survives final inference.
   - Assert that `weak_duality -> math.simplex.wsum_comm` is not preferred over the same-proof-family edge.

2. **Generic leaf-name noise test**
   - Construct declarations with unrelated `trans` lemmas in different namespaces.
   - Assert that a source theorem does not infer unrelated `trans` nodes without namespace or body evidence.

3. **Body-reference retention test**
   - A theorem body references a prior node in the proof section.
   - The prior node has reachable Lean declarations.
   - Assert the final DAG keeps that edge unless it is truly redundant through another kept blueprint-level path.

4. **Proof-plan normalization test**
   - A proof-plan node without `target` should be repaired or excluded according to the approved policy.
   - A theorem depending on a proof-plan node should be rewritten to the plan target or rejected with a clear diagnostic.

5. **Theorem-renamer integration test**
   - A declaration with an opaque Lean name receives a semantic alias from a fake renamer.
   - The alias appears in the reference index.
   - Low-confidence aliases are ignored.
   - The final edge still requires Lean or node-level evidence before being admitted.

6. **Multiple-route preservation test**
   - A theorem has one selected proof-plan and one candidate proof-plan.
   - The selected route is used for the default graph.
   - The candidate route remains available as an alternative route artifact and is not flattened into ordinary `uses`.

## Open Project Questions

These decisions affect the next implementation round. The questions are now about how far the review-only `uses` mode should go before we reintroduce any hard DAG enforcement.

1. **Should the published `uses` graph be a strict DAG or a reviewable superset?**
   - A strict DAG is easier for downstream tooling.
   - A reviewable superset is better for preserving proof narrative and agent judgment.

2. **Should body references be allowed in the published graph if they are not Lean-backed?**
   - Strict option: no, keep them only in the review artifact.
   - Hybrid option: yes, but mark such edges as `body_only` in a dedicated evidence file.

3. **Should low-level helper nodes appear in the public graph?**
   - Strict Lean option: yes, if they are real formal dependencies.
   - Blueprint option: no, demote them in the review rubric unless no higher-level node explains the proof step.

4. **How should proof-plan nodes be handled in the generated tree?**
   - Repair and preserve them.
   - Exclude them from the comparison export.
   - Keep them as auxiliary artifacts but not as ordinary `uses` nodes.

5. **Should generated `uses` replace authored `uses`, or should they be stored separately?**
   - Replacement is useful for ablation but can destroy editorial structure.
   - Separate storage, such as `inferred_uses` or `uses_review.json`, lets us compare without overwriting the authored blueprint graph.

6. **Should the graph comparison metric compare direct edges or transitive closure?**
   - Direct-edge comparison penalizes proposal retention heavily.
   - Closure comparison better captures whether two graphs imply similar reachability.
   - Both may be needed: direct edges for editorial structure, closure for dependency semantics.

7. **What contract should the theorem-renamer provide?**
   - Minimal option: declaration-to-alias candidates with confidence.
   - Stronger option: declaration-to-node candidates with confidence and rationale.
   - Strongest option: theorem statement normalization plus semantic clustering across declarations and node bodies.

8. **Should theorem-renamer output ever create an edge without Lean reachability?**
   - Conservative option: no; aliases only help match Lean references to node-level targets.
   - Hybrid option: yes, but only as `renamer_only` evidence requiring manual review.

9. **How should multiple proof routes be represented in generated output?**
   - Keep one selected route in `uses`.
   - Store candidate routes separately as proof-plan nodes or route artifacts.
   - Annotate edges with route ids and let the UI decide which route to render.

10. **Should graph-distance metrics treat alternative proof routes as errors?**
   - Strict authored-graph comparison would count them as differences.
   - Proof-aware comparison should separate selected-route mismatch, candidate-route discovery, outright unsupported dependency, and review-only candidates.

## Bottom Line

The export is file-complete and structurally close, but it is not a drop-in equality check against the authored EconCSLib knowledge tree.

The dominant mismatch is now methodological rather than purely structural:

- the exporter keeps the full inferred `uses` set
- the review artifact marks transitive, cyclic, and body-reference candidates
- the agent is responsible for the final fix decision

The checker then surfaces the remaining contract violations:

- proof-plan nodes missing targets
- mathematical nodes depending on proof-plan nodes
- proof references that still need a policy decision

This makes the exported tree a useful proposed blueprint, but not yet a fully admitted ground-truth replacement.
