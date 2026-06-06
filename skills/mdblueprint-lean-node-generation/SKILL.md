---
name: mdblueprint-lean-node-generation
description: Use when generating or refreshing mdblueprint node drafts from Lean source alone, especially for ablation studies that compare Lean-derived drafts against an existing docs/knowledge baseline.
---

# mdblueprint-lean-node-generation

Generate staged mdblueprint nodes from Lean source.

## When to use

Use this skill when the user wants Lean-driven node drafts, especially when
testing how much node metadata can be recovered without treating the existing
`docs/knowledge` tree as source input.

## Workflow

1. Read `references/lean-node-generation-prompt.md`.
2. If you need a reproducible sample run, use `scripts/generate_sample_node_drafts.py`.
3. Index the Lean project and select a bounded sample of concept clusters.
4. Draft one Markdown node per concept, not one node per declaration.
5. Use Lean modules, declaration names, docstrings, and proof state as the
   primary evidence.
6. Verify the draft against the authored blueprint only after drafting.
7. Report exact matches, approximations, and missing fields.

## Rules

- Lean source is the primary source of truth for formal content.
- Existing `docs/knowledge` content is verifier-only unless the task explicitly
  asks for reproduction.
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
