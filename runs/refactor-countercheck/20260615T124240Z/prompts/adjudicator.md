# Lean Adjudicator Run

Use `skills/mdblueprint-lean-adjudicate/SKILL.md`.
Use `skills/mdblueprint-lean-adjudicate/references/agent-config.toml` for defaults.
Knowledge root: `../EconCSLib/docs/knowledge`
Lean source root: `../EconCSLib`

Inputs, when present:
- refactor report: `runs/refactor-countercheck/20260615T124240Z/reports/refactor-report.md`
- dry-run JSON: `runs/refactor-countercheck/20260615T124240Z/dry-runs/refactor-dry-run.json`
- countercheck pairs: `runs/refactor-countercheck/20260615T124240Z/countercheck/pairs.json`
- skipped candidates: `runs/refactor-countercheck/20260615T124240Z/countercheck/skipped.json`
- countercheck summary: `runs/refactor-countercheck/20260615T124240Z/countercheck/summary.json`

Write the adjudication report to `runs/refactor-countercheck/20260615T124240Z/adjudication/adjudication-report.md`.
Do not edit admitted or staged knowledge files.
