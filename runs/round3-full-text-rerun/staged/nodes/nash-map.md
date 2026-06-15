---
id: nash-map
title: nash_map
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.Nash
  declarations:
    - nash_map
uses:
  - MixedS
  - nash_map_cert
  - colRatio.continuous
  - lamB.aux.continuous
  - rowRatio.continuous
  - lam.aux.continuous
  - muB.aux.continuous
  - mu.aux.continuous
  - evaluate_at_mixed
  - Strategy
  - stdSimplex.pure
  - Lottery.pure
  - g_function
---

# nash_map

## Lean type

```lean
def nash_map (σ : MixedS G) : MixedS G
```

## Dependencies

- MixedS
- nash_map_cert
- colRatio.continuous
- lamB.aux.continuous
- rowRatio.continuous
- lam.aux.continuous
- muB.aux.continuous
- mu.aux.continuous
- evaluate_at_mixed
- Strategy
- stdSimplex.pure
- Lottery.pure
- g_function
