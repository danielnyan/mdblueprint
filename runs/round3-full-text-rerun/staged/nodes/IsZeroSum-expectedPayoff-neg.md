---
id: IsZeroSum-expectedPayoff-neg
title: IsZeroSum.expectedPayoff_neg
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.Basic
  declarations:
    - IsZeroSum.expectedPayoff_neg
uses:
  - IsZeroSum
  - MixedProfile
  - expectedPayoff
---

# IsZeroSum.expectedPayoff_neg

## Lean type

```lean
theorem IsZeroSum.expectedPayoff_neg' (hzs : IsZeroSum G) (p : StrategicGame.MixedProfile G) : StrategicGame.expectedPayoff G p 0 = -(StrategicGame.expectedPayoff G p 1)
```

## Dependencies

- IsZeroSum
- MixedProfile
- expectedPayoff
