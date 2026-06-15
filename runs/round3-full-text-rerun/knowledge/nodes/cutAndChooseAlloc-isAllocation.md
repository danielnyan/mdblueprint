---
id: cutAndChooseAlloc-isAllocation
title: cutAndChooseAlloc_isAllocation
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Divisible.CutAndChoose
  declarations:
    - cutAndChooseAlloc_isAllocation
uses:
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - Profile.ext
  - mem_iUnion
  - cutAndChooseAlloc_one
  - cutAndChooseAlloc_zero
---

# cutAndChooseAlloc_isAllocation

## Lean type

```lean
theorem cutAndChooseAlloc_isAllocation (μ : Fin 2 → Measure I) (t : I) : IsAllocation (cutAndChooseAlloc μ t)
```

## Dependencies

- IsPositiveAffineOf.symm
- Indifferent.symm
- Profile.ext
- mem_iUnion
- cutAndChooseAlloc_one
- cutAndChooseAlloc_zero
