---
id: cutAndChooseRule-isEnvyFree
title: cutAndChooseRule_isEnvyFree
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Divisible.CutAndChoose
  declarations:
    - cutAndChooseRule_isEnvyFree
uses:
  - IsEnvyFree
  - cutAndChoose_isEnvyFree
  - fairCutPoint_exists
---

# cutAndChooseRule_isEnvyFree

## Lean type

```lean
theorem cutAndChooseRule_isEnvyFree (M : MeasureInstance (Fin 2) I) [IsFiniteMeasure (M.measure 0)] [NoAtoms (M.measure 0)] : M.IsEnvyFree (cutAndChooseRule M).1
```

## Dependencies

- IsEnvyFree
- cutAndChoose_isEnvyFree
- fairCutPoint_exists
