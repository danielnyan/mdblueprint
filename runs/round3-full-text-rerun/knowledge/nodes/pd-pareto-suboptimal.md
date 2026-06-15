---
id: pd-pareto-suboptimal
title: pd_pareto_suboptimal
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.PrisonersDilemma
  declarations:
    - pd_pareto_suboptimal
uses:
  - PD
---

# pd_pareto_suboptimal

## Lean type

```lean
theorem pd_pareto_suboptimal : PD.payoff (fun _ => Cooperate) 0 > PD.payoff (fun _ => Defect) 0
```

## Dependencies

- PD
