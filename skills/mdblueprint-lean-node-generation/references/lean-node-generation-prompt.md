# Lean Node Generation Prompt

Use Lean as the primary input and the authored blueprint as a verifier.

## Core prompt

```text
You are generating EconCSLib blueprint nodes from Lean source files.

Input:
- a Lean project root, containing modules under `EconCSLib/`
- the existing `docs/knowledge/mdblueprint.yml` only as a topic registry and
  verification baseline

Output:
- Markdown node files under `docs/knowledge/staged/` or `docs/knowledge/nodes/`

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
```

## Verification rubric

- declaration coverage
- boundary quality
- title quality
- topic placement
- dependency discipline
- proof-status fidelity
- reproducibility
