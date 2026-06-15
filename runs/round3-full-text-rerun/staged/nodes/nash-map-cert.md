---
id: nash-map-cert
title: nash_map_cert
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.Nash
  declarations:
    - nash_map_cert
uses:
  - MixedS
  - Strategy
  - g_function
  - one_le_sum_g
  - g_function_nonneg
---

# nash_map_cert

## Lean type

```lean
lemma nash_map_cert (σ : MixedS G) (i : N) : nash_map_aux G σ i ∈ stdSimplex ℝ (G.strategy i)
```

## Dependencies

- MixedS
- Strategy
- g_function
- one_le_sum_g
- g_function_nonneg
