---
id: value-eq-minimax
title: value_eq_minimax
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.MatrixGameNash
  declarations:
    - value_eq_minimax
uses:
  - minimax_theorem
---

# value_eq_minimax

## Lean type

```lean
theorem value_eq_minimax : A.value = A.minimax
```

## Dependencies

- minimax_theorem
