---
id: cutAndChoose-ef-exists
title: cutAndChoose_ef_exists
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Divisible.CutAndChoose
  declarations:
    - cutAndChoose_ef_exists
uses:
  - Allocation
  - IsEnvyFree
  - MeasureValuation
  - fairCutPoint_exists
  - cutAndChooseAlloc_isAllocation
  - cutAndChoose_isEnvyFree
---

# cutAndChoose_ef_exists

## Lean type

```lean
theorem cutAndChoose_ef_exists (μ : Fin 2 → Measure I) [IsFiniteMeasure (μ 0)] [NoAtoms (μ 0)] : ∃ A : Allocation (Fin 2) I, IsAllocation A ∧ IsEnvyFree (MeasureValuation μ) A
```

## Dependencies

- Allocation
- IsEnvyFree
- MeasureValuation
- fairCutPoint_exists
- cutAndChooseAlloc_isAllocation
- cutAndChoose_isEnvyFree
