---
id: IsESS-strict-against-other
title: IsESS.strict_against_other
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ESS
  declarations:
    - IsESS.strict_against_other
uses:
  - IsESS
---

# IsESS.strict_against_other

## Lean type

```lean
theorem IsESS.strict_against_other {s t : S} (hs : IsESS u s) (ht : IsESS u t) (hne : s ≠ t) : u s s > u t s
```

## Dependencies

- IsESS
