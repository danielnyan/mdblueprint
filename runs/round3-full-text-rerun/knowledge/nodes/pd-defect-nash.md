---
id: pd-defect-nash
title: pd_defect_nash
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.PrisonersDilemma
  declarations:
    - pd_defect_nash
uses:
  - IsNashEquilibrium
  - PD
  - of_dominant
  - pd_defect_weakly_dominant
---

# pd_defect_nash

## Lean type

```lean
theorem pd_defect_nash : IsNashEquilibrium PD (fun _ => Defect)
```

## Dependencies

- IsNashEquilibrium
- PD
- of_dominant
- pd_defect_weakly_dominant
