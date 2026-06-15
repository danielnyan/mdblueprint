---
id: IsESS-nash-condition
title: IsESS.nash_condition
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ESS
  declarations:
    - IsESS.nash_condition
uses:
  - IsESS
---

# IsESS.nash_condition

## Lean type

```lean
theorem IsESS.nash_condition {s : S} (h : IsESS u s) : ∀ t, u s s ≥ u t s
```

## Dependencies

- IsESS
