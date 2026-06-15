---
id: loomis-value-eq
title: loomis_value_eq
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Minimax.Loomis
  declarations:
    - loomis_value_eq
uses:
  - IsPositive
---

# loomis_value_eq

## Lean type

```lean
theorem loomis_value_eq (A B : I → J → ℝ) (hB : IsPositive B) : lamB0 A B = muB0 A B
```

## Dependencies

- IsPositive
