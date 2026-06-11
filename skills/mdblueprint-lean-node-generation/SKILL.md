---
name: mdblueprint-lean-node-generation
description: Optional add-on skill for generating or refreshing mdblueprint node drafts from Lean source alone, especially for ablation studies that compare Lean-derived drafts against an existing docs/knowledge baseline.
---

# mdblueprint-lean-node-generation

Generate staged mdblueprint nodes from Lean source as an optional add-on workflow.

## When to use

Use this skill when the user explicitly wants Lean-driven node drafts, especially
when testing how much node metadata can be recovered without treating the existing
`docs/knowledge` tree as source input. This is not part of the normal
Markdown-first authoring and publishing loop; it is a separate add-on for import,
ablation, and comparison studies.

## Workflow

This skill is best treated as a modular add-on with two phases: upstream preparation and downstream drafting/comparison. Upstream preparation should already exist in the core Markdown-first pipeline; this skill only consumes its output.

### Upstream preparation

1. Confirm the authored baseline exists: staged/admitted nodes, `docs/knowledge/mdblueprint.yml`, and any existing reports needed for comparison.
2. Confirm the baseline tree is not being deleted or rewritten by this add-on.
3. If you need a reproducible sample run, use `scripts/generate_sample_node_drafts.py`.

### Downstream Lean-first drafting

4. Read `references/lean-node-generation-prompt.md`.
5. Index the Lean project and select a bounded sample of concept clusters.
6. Draft one Markdown node per concept, not one node per declaration.
7. Use Lean modules, declaration names, docstrings, and proof state as the
   primary evidence.
8. Verify the draft against the authored blueprint only after drafting.
9. Report exact matches, approximations, and missing fields.

## Rules

- Lean source is the primary source of truth for the Lean-first add-on workflow.
- Existing `docs/knowledge` content is verifier-only unless the task explicitly
  asks for reproduction.
- Do not confuse this add-on with the core Markdown-first knowledge base workflow.
- Do not delete, replace, or rewrite upstream authored files. Write only to the
  add-on's own draft/output path or a separate comparison tree.
- Do not invent `uses` edges, citations, or verification claims.
- Prefer staged nodes for uncertain boundaries.
- If one node spans multiple declarations, list them all in
  `lean.declarations`.

## Output shape

When drafting a node, try to recover:

- `id`
- `title`
- `kind`
- `status`
- `primary_topic`
- `topics`
- `lean.modules`
- `lean.declarations`

If a field cannot be recovered from Lean alone, leave it conservative and note
the uncertainty rather than fabricating a precise value.
