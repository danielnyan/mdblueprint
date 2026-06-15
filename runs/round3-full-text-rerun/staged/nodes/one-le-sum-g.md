---
id: one-le-sum-g
title: one_le_sum_g
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.Nash
  declarations:
    - one_le_sum_g
uses:
  - MixedS
  - Strategy
  - g_function
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - sigma_le_g_function
---

# one_le_sum_g

## Lean type

```lean
lemma one_le_sum_g (i : N) (σ : MixedS G) : 1 ≤ ∑ a : G.strategy i, g_function G i σ a
```

## Dependencies

- MixedS
- Strategy
- g_function
- IsPositiveAffineOf.symm
- Indifferent.symm
- sigma_le_g_function
