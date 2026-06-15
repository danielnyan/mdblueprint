---
agent: lean-countercheck
node_id: foundation.cost.examples.par_all
created_at: "2026-06-15T13:22:21+00:00"
---

# Lean Countercheck: Worked Example: N-ary parList Depth Bound

## Inputs

- node file: `/home/azureuser/EconCSLib/docs/knowledge/nodes/foundation/cost/examples/par_all.md`
- lean file: `/home/azureuser/EconCSLib/EconCSLib/Examples/CostM/ParAll.lean`
- corpus root: `/home/azureuser/EconCSLib`

## Method Status

- heuristic: used

## Matched Declarations

- `(none)`

## Missing Declarations

- `ParAll.parMap_unit_cost_le`

## Extra Declarations

- `parMap_unit_cost_le`

## Node Uses vs Extracted Dependencies

- node uses: `foundation.cost.costm`, `foundation.cost.parallel`
- missing uses: (none)
- extra uses: (none)

## Raw Snapshot

```json
{
  "corpus_root": "/home/azureuser/EconCSLib",
  "dependencies": [],
  "lean_file": "/home/azureuser/EconCSLib/EconCSLib/Examples/CostM/ParAll.lean",
  "method_status": {
    "heuristic": "used"
  },
  "node": {
    "body": "# Worked Example: N-ary parList Depth Bound\n\nThe n-ary `parList` combinator ([[node:foundation.cost.parallel]]) applied to a\nlist of independent unit-cost operations. Because the costs are folded with\n`\u2294` from `\u22a5`, running `n` operations that each charge one unit in parallel has\ndepth-1 cost:\n$$\n  (\\operatorname{parList}\\,ms).\\mathrm{cost}\n    \\;=\\; \\bigsqcup_i (m_i).\\mathrm{cost} \\;\\le\\; 1,\n$$\nproved as `parMap_unit_cost_le`. This is the flat fan-out / fan-in schedule:\narbitrarily many independent unit tasks cost the same as one, the defining\nproperty distinguishing the parallel `\u2294` cost from the sequential `+` cost\n([[node:foundation.cost.costm]]). The empty-list base case (`parList [] `has\ncost `\u22a5 = 0`) is exercised by the accompanying examples in the source file.\n\n## Lean declarations\n\n- `ParAll.parMap_unit_cost_le` \u2014 the `parList`-of-unit-tasks depth bound `\u2264 1`,\n  alongside two `example`s pinning the empty and singleton cases.\n\n## References\n\n- [Danielsson 2008] Nils Anders Danielsson, POPL 2008. The underlying cost\n  monad ([[node:foundation.cost.costm]]).",
    "file_path": "/home/azureuser/EconCSLib/docs/knowledge/nodes/foundation/cost/examples/par_all.md",
    "id": "foundation.cost.examples.par_all",
    "kind": "example",
    "lean": {
      "declarations": [
        "ParAll.parMap_unit_cost_le"
      ],
      "modules": [
        "EconCSLib.Examples.CostM.ParAll"
      ],
      "repository": null
    },
    "status": "formalized",
    "tags": [
      "cost",
      "example",
      "parallel"
    ],
    "title": "Worked Example: N-ary parList Depth Bound",
    "uses": [
      "foundation.cost.costm",
      "foundation.cost.parallel"
    ]
  },
  "source_root": "/home/azureuser/EconCSLib",
  "theorems": [
    {
      "body": "theorem parMap_unit_cost_le (xs : List \u2115) :\n    (parList (xs.map (fun _ => (do \u2713 pure 0 : CostM \u2115 \u2115)))).cost \u2264 1 := by\n  induction xs with\n  | nil => simp [parList]\n  | cons x xs ih =>\n    simp only [List.map_cons, cost_parList_cons]\n    show max (do \u2713 pure 0 : CostM \u2115 \u2115).cost _ \u2264 1\n    have h : ((do \u2713 pure 0 : CostM \u2115 \u2115)).cost = 1 := by\n      simp [CostM.cost_bind, CostM.cost_tick, CostM.cost_pure]\n    rw [h]\n    omega\n\nend ParAll\n",
      "column": 1,
      "end": 1958,
      "kind": "theorem",
      "line": 51,
      "module": "EconCSLib.Examples.CostM.ParAll",
      "name": "parMap_unit_cost_le",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Examples/CostM/ParAll.lean",
      "start": 1522
    }
  ]
}
```

## Intent

- Lean is acting as a counterchecker only.
- Blank or flawed proofs are recorded as incompleteness, not inconsistency.
- Any new lemmata discovered here are proposals for review, not automatic edits.