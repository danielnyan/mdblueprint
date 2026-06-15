---
id: minimax-theorem
title: minimax_theorem
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.MatrixGame
  declarations:
    - minimax_theorem
uses:
  - minmax_from_general
---

# minimax_theorem

## Lean type

```lean
theorem minimax_theorem : A.maximin = A.minimax
```

## Dependencies

- minmax_from_general
