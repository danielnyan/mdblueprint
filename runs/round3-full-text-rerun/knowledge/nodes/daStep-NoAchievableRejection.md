---
id: daStep-NoAchievableRejection
title: daStep_NoAchievableRejection
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.Optimal
  declarations:
    - daStep_NoAchievableRejection
uses:
  - HoldInv
  - NoAchievableRejection
  - IsAchievable
  - isFree
  - propTarget
  - pref_list_mem
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - isFree_iff
  - daStep_holding
  - daStep_nc_free
  - daStep_nc_held
---

# daStep_NoAchievableRejection

## Lean type

```lean
lemma daStep_NoAchievableRejection (s : DAState n) (hhold : HoldInv m s) (hinj : ∀ j1 j2 i : Fin n, s.holding j1 = some i → s.holding j2 = some i → j1 = j2) (hinv : NoAchievableRejection w m s) : NoAchievableRejection w m (daStep w m s)
```

## Dependencies

- HoldInv
- NoAchievableRejection
- IsAchievable
- isFree
- propTarget
- pref_list_mem
- IsPositiveAffineOf.symm
- Indifferent.symm
- isFree_iff
- daStep_holding
- daStep_nc_free
- daStep_nc_held
