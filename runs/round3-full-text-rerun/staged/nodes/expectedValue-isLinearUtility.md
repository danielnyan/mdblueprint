---
id: expectedValue-isLinearUtility
title: expectedValue_isLinearUtility
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.Utility.Lottery
  declarations:
    - expectedValue_isLinearUtility
uses:
  - IsLinearUtility
  - Lottery.expectedValue
  - Lottery
  - Lottery.expectedValue_mix
---

# expectedValue_isLinearUtility

## Lean type

```lean
theorem expectedValue_isLinearUtility {O : Type*} [Fintype O] (f : O → 𝕜) : IsLinearUtility (𝕜
```

## Dependencies

- IsLinearUtility
- Lottery.expectedValue
- Lottery
- Lottery.expectedValue_mix
