# Lean Node Generation Prompt and Study Notes

This file documents a Lean-first node-generation prompt for the EconCSLib
knowledge blueprint, plus a small empirical study on how much node metadata
is recoverable from Lean source alone.

## Goal

Generate `docs/knowledge` nodes from the Lean files in `EconCSLib/EconCSLib`
without relying on the existing Markdown nodes as the source of truth.

The generator should treat Lean as the primary input and only use the current
knowledge tree as a verification baseline.

## What Lean Can Usually Provide

From the Lean files, the generator can usually recover:

- module path
- public declaration names
- declaration kind (`def`, `theorem`, `lemma`, `structure`, etc.)
- whether a declaration has a proof gap (`sorry` / `admit`)
- a rough topic root from the Lean file path
- module docstring summaries
- declaration docstrings

## What Lean Usually Cannot Provide By Itself

Lean source usually does not determine:

- the final human-facing node title
- the exact `uses` graph
- the full `topics` membership list
- `verification` fields in their final editorial form
- `generality` metadata
- source-book citations and other bibliography fields

## Random-Sample Study

I sampled 20 EconCSLib nodes with Lean metadata and compared their authored
node records to the Lean declarations they expose.

Summary:

- 10 / 20 sampled nodes were backed by a single public Lean declaration.
- 18 / 20 sampled nodes had at least one exact Lean declaration match in the
  index.
- 2 / 20 sampled nodes had a title that appeared verbatim in a Lean docstring.
- 1 / 20 sampled nodes had a title that was recoverable by simple leaf-name
  titleization.
- 0 / 20 sampled Lean files exposed explicit `Blueprint:` markers in the Lean
  index.

Interpretation:

- Lean is good at giving the formal spine of the node.
- Lean is not enough to reconstruct the final editorial phrasing.
- Composite nodes are common: one Markdown node can correspond to several Lean
  declarations.
- Some node ids are concept labels rather than direct declaration names, so the
  generator must infer the node boundary from module structure and surrounding
  docstrings.

Representative cases from the sample:

- `social_choice.fair_division.divisible.proportional_exists`
  - one Lean theorem
  - title is descriptive, not a literal declaration-name transform
- `social_choice.fair_division.indivisible.round_robin_alloc`
  - one node, three Lean declarations
  - shows that a node can aggregate a small cluster of related declarations
- `mechanism_design.auction.knapsack.relaxations_dynamic_programming`
  - many Lean declarations, but no direct one-to-one node declaration name
  - illustrates a node that is more of a concept bundle than a single theorem
- `game_theory.extensive_game.perfect_information.kuhn_spe_existence_no_chance`
  - node metadata names the theorem in a human-friendly way
  - Lean exports names that do not line up directly with the node id

## Prompt

Use this prompt for a generation agent.

```text
You are generating EconCSLib blueprint nodes from Lean source files.

Input:
- a Lean project root, containing modules under `EconCSLib/`
- the existing `docs/knowledge/mdblueprint.yml` only as a topic registry and
  verification baseline

Output:
- Markdown node files under `docs/knowledge/staged/` or `docs/knowledge/nodes/`
- `mdblueprint.yml` updates only when topic registry or Lean repository wiring
  must change

Rules:
1. Treat Lean source as the primary source of truth.
2. Derive one node per coherent mathematical concept, not one node per Lean
   declaration.
3. Use the Lean module path, declaration names, and docstrings to infer the
   node's scope.
4. Prefer a public theorem/definition cluster that matches the concept exposed
   by the module.
5. Set:
   - `id` from the concept slug
   - `title` from the mathematical concept, not the raw declaration name
   - `kind` from the Lean declaration family
   - `status` from proof completeness (`admitted` / `formalized` / `proved`)
   - `primary_topic` and `topics` from the Lean module subtree and the topic
     registry
   - `lean.modules` and `lean.declarations` from the exact Lean symbols that
     support the node
6. If a node contains several public declarations, list them all in
   `lean.declarations`.
7. If the Lean proof is incomplete, mark the node as staged and set proof
   verification to a gap-like value rather than inventing a proof.
8. Never fabricate `uses`. Only add a dependency if it is justified by the
   local Lean structure or by an explicit cross-reference in the source.
9. Do not invent citations. Only add `source` or `verification` details when
   they are explicitly justified by the source material.
10. When the right node boundary is uncertain, emit a staged node and leave a
    note for human review.
11. Keep the output deterministic and re-runnable on the same Lean checkout.

Suggested generation workflow:
1. Index the Lean project.
2. Group declarations by module and docstring context.
3. Find candidate concept clusters with shared terms, names, and module scope.
4. Draft node metadata for each cluster.
5. Verify the draft against the existing knowledge tree and record any
   mismatches.
6. Escalate uncertain clusters to staged status.
```

## Verification Rubric

Use the following checks when evaluating a generated node set:

- declaration coverage: does every referenced Lean declaration exist?
- granularity: does one node correspond to one concept, not a random file
  boundary?
- title quality: does the title read like a mathematical concept rather than a
  raw Lean identifier?
- topic placement: is `primary_topic` plausible and are `topics` minimal?
- dependency discipline: are `uses` edges real and non-hallucinatory?
- proof status: do the `verification` fields reflect the Lean proof state?
- reproducibility: does a second run on the same Lean checkout give the same
  node metadata?

## Practical Conclusion

Lean alone is sufficient to generate a useful first draft of the knowledge
nodes, but not a final canonical node set.

The stable strategy is:

- generate from Lean
- stage uncertain nodes
- verify against the baseline `docs/knowledge`
- only promote after human review
## Skill Trial

I also turned this into a repo-local Codex skill:

- [`skills/mdblueprint-lean-node-generation/SKILL.md`](skills/mdblueprint-lean-node-generation/SKILL.md)

I then used the skill workflow on six representative nodes with direct Lean
hits and generated Lean-only drafts. The drafts reproduced:

- `id` in all 6 / 6 cases
- exact `lean.declarations` in all 6 / 6 cases
- `kind` in 4 / 6 cases
- `status` in 4 / 6 cases
- `primary_topic` in 5 / 6 cases

The drafts did not reproduce well:

- `title` in 0 / 6 cases
- `topics` in 1 / 6 cases
- `uses` in 0 / 6 cases
- `lean.modules` in 0 / 6 cases

The strongest result is that Lean is enough to anchor the node identity and the
formal declaration list. The weakest result is the final editorial framing.
That means the skill is useful as a draft generator, but the authored blueprint
still supplies the final naming, topic placement, and dependency curation.

## Discrepancy Analysis: `uses` and `lean.modules`

I inspected the mismatches by hand on the representative sample.

### `uses`

The `uses` field did not reproduce from Lean-only generation, and that is not a bug in the script. The missing edges are a different kind of information:

- `social_choice.fair_division.divisible.proportional_exists` needs `dubins_spanier_proportional` because the theorem is a proof-route dependency.
- `social_choice.fair_division.indivisible.round_robin_alloc` depends on `best_good` and `allocation` because the node is a curated concept bundle.
- `game_theory.strategic_game.equilibrium.nash_existence_finite_games` uses Brouwer and the mixed-Nash theorem because the node is a higher-level theorem statement, not a direct Lean declaration wrapper.
- `foundation.cost.examples.reverse_space` uses `foundation.cost.costm` because the example is situated in the cost-monad framework.

Conclusion: `uses` is a curated logical graph, not a direct Lean export. Lean source can support it, but only with statement/proof semantic analysis, not just declaration indexing.

### `lean.modules`

The new script now prefixes the repo namespace (`EconCSLib.`), which fixes the simple namespace mismatch between Lean's file-derived module names and the authored metadata.

Most sample nodes line up after that normalization. The remaining mismatch is conceptual, not syntactic:

- `math.minimax.common_guarantee_value` is authored with `lean.modules: [EconCSLib.GameTheory.StrategicGame.ZeroSum.MatrixGame]`, but the Lean declaration lives in `GameTheory.StrategicGame.ZeroSum.MatrixGameNash`.

That is a deliberate human choice: the node belongs to the conceptual `MatrixGame` theory family even though the theorem is implemented in a later refinement file.

Conclusion: `lean.modules` is mostly recoverable from Lean, but the authored node sometimes points at a broader conceptual home module instead of the exact definition site.
