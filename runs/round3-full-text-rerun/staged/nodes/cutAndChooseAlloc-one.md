---
id: cutAndChooseAlloc-one
title: cutAndChooseAlloc_one
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Divisible.CutAndChoose
  declarations:
    - cutAndChooseAlloc_one
uses:
---

# cutAndChooseAlloc_one

## Lean type

```lean
@[simp] lemma cutAndChooseAlloc_one (μ : Fin 2 → Measure I) (t : I) : cutAndChooseAlloc μ t 1 = if μ 1 (Iic t) ≥ μ 1 (Ioi t) then Iic t else Ioi t
```

## Dependencies

- none
