---
id: maximin-le-minimax
title: maximin_le_minimax
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.MatrixGame
  declarations:
    - maximin_le_minimax
uses:
  - lam0_le_mu0
---

# maximin_le_minimax

## Lean type

```lean
theorem maximin_le_minimax : A.maximin ≤ A.minimax
```

## Dependencies

- lam0_le_mu0
