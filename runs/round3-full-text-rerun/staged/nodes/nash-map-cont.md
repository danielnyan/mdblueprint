---
id: nash-map-cont
title: nash_map_cont
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.Nash
  declarations:
    - nash_map_cont
uses:
  - colRatio.continuous
  - lamB.aux.continuous
  - rowRatio.continuous
  - lam.aux.continuous
  - muB.aux.continuous
  - mu.aux.continuous
  - nash_map
  - one_le_sum_g
---

# nash_map_cont

## Lean type

```lean
theorem nash_map_cont : Continuous (nash_map G)
```

## Dependencies

- colRatio.continuous
- lamB.aux.continuous
- rowRatio.continuous
- lam.aux.continuous
- muB.aux.continuous
- mu.aux.continuous
- nash_map
- one_le_sum_g
