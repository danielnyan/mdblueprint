---
id: pd-defect-weakly-dominant
title: pd_defect_weakly_dominant
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.PrisonersDilemma
  declarations:
    - pd_defect_weakly_dominant
uses:
  - IsStrictlyDominant.isWeaklyDominant
  - IsWeaklyDominant
  - PD
---

# pd_defect_weakly_dominant

## Lean type

```lean
theorem pd_defect_weakly_dominant : ∀ i : Fin 2, IsWeaklyDominant PD i Defect
```

## Dependencies

- IsStrictlyDominant.isWeaklyDominant
- IsWeaklyDominant
- PD
