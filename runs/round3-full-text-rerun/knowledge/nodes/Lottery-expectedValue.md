---
id: Lottery-expectedValue
title: Lottery.expectedValue
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.Utility.Lottery
  declarations:
    - Lottery.expectedValue
uses:
  - Lottery
---

# Lottery.expectedValue

## Lean type

```lean
abbrev Lottery.expectedValue {O : Type*} [Fintype O] (L : Lottery 𝕜 O) (f : O → 𝕜) : 𝕜
```

## Dependencies

- Lottery
