---
id: cutAndChooseAlloc-zero
title: cutAndChooseAlloc_zero
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Divisible.CutAndChoose
  declarations:
    - cutAndChooseAlloc_zero
uses:
---

# cutAndChooseAlloc_zero

## Lean type

```lean
@[simp] lemma cutAndChooseAlloc_zero (μ : Fin 2 → Measure I) (t : I) : cutAndChooseAlloc μ t 0 = if μ 1 (Iic t) ≥ μ 1 (Ioi t) then Ioi t else Iic t
```

## Dependencies

- none
