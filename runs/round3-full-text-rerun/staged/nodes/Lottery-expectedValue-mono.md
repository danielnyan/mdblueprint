---
id: Lottery-expectedValue-mono
title: Lottery.expectedValue_mono
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.Utility.Lottery
  declarations:
    - Lottery.expectedValue_mono
uses:
  - Lottery
  - Lottery.expectedValue
  - wsum_le_wsum
---

# Lottery.expectedValue_mono

## Lean type

```lean
theorem Lottery.expectedValue_mono {L : Lottery 𝕜 O} {f g : O → 𝕜} (h : ∀ o, f o ≤ g o) : Lottery.expectedValue L f ≤ Lottery.expectedValue L g
```

## Dependencies

- Lottery
- Lottery.expectedValue
- wsum_le_wsum
