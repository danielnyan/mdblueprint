---
id: Lottery-expectedValue-pure
title: Lottery.expectedValue_pure
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.Utility.Lottery
  declarations:
    - Lottery.expectedValue_pure
uses:
  - Lottery.expectedValue
  - Lottery
  - stdSimplex.pure
  - Lottery.pure
  - wsum_pure_apply
---

# Lottery.expectedValue_pure

## Lean type

```lean
theorem Lottery.expectedValue_pure [DecidableEq O] (o₀ : O) (f : O → 𝕜) : Lottery.expectedValue (Lottery.pure (𝕜
```

## Dependencies

- Lottery.expectedValue
- Lottery
- stdSimplex.pure
- Lottery.pure
- wsum_pure_apply
