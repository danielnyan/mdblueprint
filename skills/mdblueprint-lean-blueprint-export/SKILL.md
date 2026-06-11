---
name: mdblueprint-lean-blueprint-export
description: Use when you need to materialize a full docs/knowledge blueprint tree from an existing Lean-backed node set and inferred DAG edges, including a generated mdblueprint.yml, so a fresh agent can run the core export pipeline end-to-end and compare it against a reference snapshot. This is the downstream export step, not the Lean-first node-generation add-on.
---

# mdblueprint-lean-blueprint-export

Export a Lean-backed knowledge tree into a runnable mdblueprint repository.

## When to use

Use this skill when you already have a node set derived from Lean or a comparable authored source and want to:

- infer and review `uses` into a DAG or proposal artifact, depending on the current exporter mode;
- generate or refresh `docs/knowledge/mdblueprint.yml`;
- materialize a full output tree that `mdblueprint-check` and `mdblueprint-publish` can consume;
- compare the exported tree against a reference snapshot;
- leave node canonicalization and duplicate retirement to the node-maintenance agent before export when the source tree has overlap clusters; this exporter is downstream and must not delete upstream authored files.

## Inputs

- `lean_root`: the Lean repository to index;
- `source_root`: a docs/knowledge-style tree containing the node drafts to export;
- `output_root`: a fresh directory for the generated blueprint tree;
- optional `--verify-against`: a reference tree to compare after export.

## Workflow

1. Run `mdblueprint-lean-blueprint-export <lean_root> <source_root> <output_root>`.
2. Inspect the generated `mdblueprint.yml`, node files, and inferred `uses` edges.
3. If you need a structural comparison, rerun with `--verify-against <reference_root>`.
4. Validate the output with `mdblueprint-check <output_root> --lean-root <lean_root>`.
5. Publish or render-check the exported tree only after the structural check passes.

## Rules

- Keep `source_root` immutable; write only to `output_root`.
- Treat `uses` as Lean-backed graph edges after proposal and pruning.
- Preserve the repository’s graph semantics: export should keep the graph human-readable and semantically faithful, not flatten it into a pure import projection. The export should be judged on the entire graph, not a subset, and stray nodes or weakly attached islands should be treated as quality regressions. If uses review surfaces problematic edges, emit the proposal artifact and let the agent decide whether to keep or fix the edge.
- Do not use export as a node-deduplication or canonicalization step; if the source tree has duplicate clusters, resolve them first through the node-maintenance agent and its subagents.
- Preserve copied topic catalogs and other non-node files from the source tree.
- Do not hand-edit generated `graph.json` or published site artifacts.
- If the source tree lacks `mdblueprint.yml`, let the exporter synthesize a minimal config from the Lean repo and node topics.

## Expected Output

The exporter should produce a tree containing at least:

- `mdblueprint.yml`
- node files under `nodes/` and/or `staged/`
- copied topic catalogs (`topics.md`) if they were present in the source tree

The exporter is a build step, not an admission step: it materializes the current node draft set into a form suitable for downstream mdblueprint validation and publication.
