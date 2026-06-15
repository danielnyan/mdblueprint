---
id: finalState-NoAchievableRejection
title: finalState_NoAchievableRejection
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.Optimal
  declarations:
    - finalState_NoAchievableRejection
uses:
  - NoAchievableRejection
  - finalState
  - daRun_NoAchievableRejection
  - initState
  - holdinv_init
  - initState_injective
  - initState_NoAchievableRejection
---

# finalState_NoAchievableRejection

## Lean type

```lean
lemma finalState_NoAchievableRejection : NoAchievableRejection w m (finalState w m)
```

## Dependencies

- NoAchievableRejection
- finalState
- daRun_NoAchievableRejection
- initState
- holdinv_init
- initState_injective
- initState_NoAchievableRejection
