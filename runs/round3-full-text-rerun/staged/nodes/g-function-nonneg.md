---
id: g-function-nonneg
title: g_function_nonneg
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.Nash
  declarations:
    - g_function_nonneg
uses:
  - MixedS
  - Strategy
  - g_function
  - sigma_le_g_function
---

# g_function_nonneg

## Lean type

```lean
lemma g_function_nonneg (i : N) (σ : MixedS G) (a : G.strategy i) : 0 ≤ g_function G i σ a
```

## Dependencies

- MixedS
- Strategy
- g_function
- sigma_le_g_function
