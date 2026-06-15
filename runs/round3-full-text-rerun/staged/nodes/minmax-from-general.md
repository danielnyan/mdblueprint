---
id: minmax-from-general
title: minmax_from_general
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Minimax.Loomis
  declarations:
    - minmax_from_general
uses:
  - loomis_value_eq
  - IsPositive
  - lamB0_one
  - muB0_one
---

# minmax_from_general

## Lean type

```lean
theorem minmax_from_general (A : I → J → ℝ) : MinimaxLoomis.lam0 A = MinimaxLoomis.mu0 A
```

## Dependencies

- loomis_value_eq
- IsPositive
- lamB0_one
- muB0_one
