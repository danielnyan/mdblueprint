---
id: Lottery-expectedValue-const
title: Lottery.expectedValue_const
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.Utility.Lottery
  declarations:
    - Lottery.expectedValue_const
uses:
  - Lottery
  - Lottery.expectedValue
  - wsum_const
---

# Lottery.expectedValue_const

## Lean type

```lean
theorem Lottery.expectedValue_const (L : Lottery 𝕜 O) (c : 𝕜) : Lottery.expectedValue L (fun _ => c) = c
```

## Dependencies

- Lottery
- Lottery.expectedValue
- wsum_const
