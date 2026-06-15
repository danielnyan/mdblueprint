---
id: cutAndChoose-exists-envyFree-allocation
title: cutAndChoose_exists_envyFree_allocation
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Divisible.CutAndChoose
  declarations:
    - cutAndChoose_exists_envyFree_allocation
uses:
  - Allocation
  - IsEnvyFree
  - cutAndChoose_ef_exists
  - fairCutPoint_exists
  - cutAndChooseAlloc_isAllocation
---

# cutAndChoose_exists_envyFree_allocation

## Lean type

```lean
theorem cutAndChoose_exists_envyFree_allocation (M : MeasureInstance (Fin 2) I) [IsFiniteMeasure (M.measure 0)] [NoAtoms (M.measure 0)] : ∃ A : Allocation (Fin 2) I, IsAllocation A ∧ M.IsEnvyFree A
```

## Dependencies

- Allocation
- IsEnvyFree
- cutAndChoose_ef_exists
- fairCutPoint_exists
- cutAndChooseAlloc_isAllocation
