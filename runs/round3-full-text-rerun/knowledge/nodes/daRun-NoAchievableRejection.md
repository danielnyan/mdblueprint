---
id: daRun-NoAchievableRejection
title: daRun_NoAchievableRejection
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.Optimal
  declarations:
    - daRun_NoAchievableRejection
uses:
  - HoldInv
  - NoAchievableRejection
  - holdinv_step
  - holding_injective_step
  - daStep_NoAchievableRejection
---

# daRun_NoAchievableRejection

## Lean type

```lean
lemma daRun_NoAchievableRejection (fuel : ℕ) (s : DAState n) (hhold : HoldInv m s) (hinj : ∀ j1 j2 i : Fin n, s.holding j1 = some i → s.holding j2 = some i → j1 = j2) (hinv : NoAchievableRejection w m s) : NoAchievableRejection w m (daRun w m fuel s)
```

## Dependencies

- HoldInv
- NoAchievableRejection
- holdinv_step
- holding_injective_step
- daStep_NoAchievableRejection
