# Round 2 Lean Node Generation Report

## Scope

This round removes the prior report and the previous draft nodes, then re-tests five new EconCSLib nodes against Lean-derived drafts generated with the `mdblueprint-lean-node-generation` workflow. This workflow is an add-on for Lean-first import and ablation studies, not part of the core Markdown-first knowledge base pipeline. It should be run as a modular downstream step after the upstream authored baseline exists, not as a replacement for the core node/blueprint workflow.

The key question is whether the Lean source alone can reconstruct `uses` and the surrounding metadata without falling back to the authored blueprint.

## Sample

- `social_choice.fair_division.divisible.dubins_spanier_proportional`
- `game_theory.strategic_game.zero_sum.maximin_le_minimax`
- `social_choice.fair_division.indivisible.best_good`
- `foundation.cost.costm`
- `game_theory.strategic_game.zero_sum.von_neumann_minimax`

## Summary

| node | title | kind | status | primary_topic | topics | uses | lean.modules | lean.declarations |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `social_choice.fair_division.divisible.dubins_spanier_proportional` | diff | match | diff | match | diff | diff | match | match |
| `game_theory.strategic_game.zero_sum.maximin_le_minimax` | diff | diff | match | diff | diff | diff | match | match |
| `social_choice.fair_division.indivisible.best_good` | diff | match | match | match | diff | diff | match | diff |
| `foundation.cost.costm` | diff | match | match | match | match | match | match | diff |
| `game_theory.strategic_game.zero_sum.von_neumann_minimax` | diff | match | match | diff | diff | match | match | diff |

## Uses-Focused Comparison

### `social_choice.fair_division.divisible.dubins_spanier_proportional`

Authored `uses`: ['social_choice.fair_division.divisible.ds_step']
Generated `uses`: []
Result: `uses` differs.

Failure mode: the Lean theorem is proved by a private induction helper and explicit step/base lemmas, but the authored blueprint points to the semantic step node `ds_step` rather than the private helper name that appears in the Lean file.

### `game_theory.strategic_game.zero_sum.maximin_le_minimax`

Authored `uses`: ['game_theory.strategic_game.zero_sum.maximin_minimax']
Generated `uses`: []
Result: `uses` differs.

Failure mode: Lean proves the inequality by calling `MinimaxLoomis.lam0_le_mu0`, while the authored node links to the conceptual predecessor node `maximin_minimax`. The agent sees a theorem reference, but not the blueprint author's wrapper-level concept choice.

### `social_choice.fair_division.indivisible.best_good`

Authored `uses`: ['social_choice.fair_division.indivisible.additive_valuation']
Generated `uses`: []
Result: `uses` differs.

Failure mode: the Lean declaration is a definition with a docstring, so the source is enough to infer what the function does, but not enough to decide that the author wants the local prerequisite `additive_valuation` as an explicit dependency edge.

### `foundation.cost.costm`

Authored `uses`: []
Generated `uses`: []
Result: `uses` matches exactly.

Failure mode: none for `uses`; this node is a control case and the authored graph intentionally has no prerequisites.

### `game_theory.strategic_game.zero_sum.von_neumann_minimax`

Authored `uses`: []
Generated `uses`: []
Result: `uses` matches exactly.

Failure mode: none for `uses`; the blueprint keeps the theorem node dependency-free because the proof-plan dependencies are modeled elsewhere, not in `uses`.

## Interpretation

The second-round sample confirms the earlier failure mode rather than changing it. It also reinforces the role split: the Lean-first node-generation workflow can draft plausible node objects, but the core repository still treats authored Markdown nodes and `mdblueprint.yml` as the durable source of truth.

- `lean.declarations` are recoverable from Lean with simple indexing.
- `lean.modules` also match once the module path is used as the index reports it, without inventing extra prefixes.
- Some authored nodes bundle helper lemmas or wrapper declarations under one node, while the Lean-first draft keeps only the primary declaration unless the generator is taught to bundle the auxiliaries too.
- `uses` is not a direct Lean export.
- Even when Lean names the proof steps, the blueprint may map them to a different conceptual node, or keep them out of `uses` entirely when the relation lives in a proof-plan layer.
- The agent can infer a plausible prerequisite set only by mixing theorem references, local helper names, docstrings, and conceptual grouping heuristics; that is weaker than the authored semantic graph.

## Failure Pattern

The dominant failure pattern is a mismatch between what Lean exposes and what the blueprint author encodes: Lean shows implementation-level theorem names, while the authored `uses` expresses exposition-level dependency choices.

This matters most when a theorem depends on:

- a private helper inside the same file
- a local theorem with a different concept name than the file-level theorem
- an external theorem that EconCSLib wraps with its own explanatory node
- a proof-plan dependency that is intentionally kept outside `uses`
