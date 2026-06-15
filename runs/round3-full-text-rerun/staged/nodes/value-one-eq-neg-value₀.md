---
id: value-one-eq-neg-value₀
title: value_one_eq_neg_value₀
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.Zermelo
  declarations:
    - value_one_eq_neg_value₀
uses:
  - IsZeroSum
  - value_zero_sum
---

# value_one_eq_neg_value₀

## Lean type

```lean
theorem value_one_eq_neg_value₀ (g : GameTree (Fin 2) ℚ) (hzs : IsZeroSum g) : (value g) 1 = -value₀ g
```

## Dependencies

- IsZeroSum
- value_zero_sum
