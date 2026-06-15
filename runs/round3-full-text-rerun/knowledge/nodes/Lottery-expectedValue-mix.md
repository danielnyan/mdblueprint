---
id: Lottery-expectedValue-mix
title: Lottery.expectedValue_mix
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.Utility.Lottery
  declarations:
    - Lottery.expectedValue_mix
uses:
  - Lottery
  - Lottery.expectedValue
  - stdSimplex.mix
  - Lottery.mix
  - wsum_mix
---

# Lottery.expectedValue_mix

## Lean type

```lean
theorem Lottery.expectedValue_mix (α : 𝕜) (hα₀ : 0 ≤ α) (hα₁ : α ≤ 1) (L₁ L₂ : Lottery 𝕜 O) (f : O → 𝕜) : Lottery.expectedValue (Lottery.mix α hα₀ hα₁ L₁ L₂) f = α * Lottery.expectedValue L₁ f + (1 - α) * Lottery.expectedValue L₂ f
```

## Dependencies

- Lottery
- Lottery.expectedValue
- stdSimplex.mix
- Lottery.mix
- wsum_mix
