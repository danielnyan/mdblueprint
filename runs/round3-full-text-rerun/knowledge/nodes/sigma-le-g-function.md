---
id: sigma-le-g-function
title: sigma_le_g_function
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.Nash
  declarations:
    - sigma_le_g_function
uses:
  - MixedS
  - Strategy
  - g_function
---

# sigma_le_g_function

## Lean type

```lean
lemma sigma_le_g_function (i : N) (σ : MixedS G) (a : G.strategy i) : (σ i).val a ≤ g_function G i σ a
```

## Dependencies

- MixedS
- Strategy
- g_function
