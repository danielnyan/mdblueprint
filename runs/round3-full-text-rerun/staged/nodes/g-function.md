---
id: g-function
title: g_function
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.Nash
  declarations:
    - g_function
uses:
  - MixedS
  - Strategy
  - evaluate_at_mixed
  - stdSimplex.pure
  - Lottery.pure
---

# g_function

## Lean type

```lean
def g_function (i : N) (σ : MixedS G) (a : G.strategy i) : ℝ
```

## Dependencies

- MixedS
- Strategy
- evaluate_at_mixed
- stdSimplex.pure
- Lottery.pure
