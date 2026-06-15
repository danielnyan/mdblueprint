# Graph Refactor Agent Run

Use `skills/mdblueprint-graph-refactor-review/SKILL.md`.
Knowledge root: `../EconCSLib/docs/knowledge`
Scope mode: `admitted`.
Pass `--include-staged`: `false`.

Write the refactor report to `runs/refactor-countercheck/20260615T130000Z/reports/refactor-report.md`.
Write the dry-run plan to `runs/refactor-countercheck/20260615T130000Z/dry-runs/refactor-plan.yml`.
If no concrete operation survives refinement, write a valid dry-run plan with `operations: []`.
Do not edit admitted or staged knowledge files.
