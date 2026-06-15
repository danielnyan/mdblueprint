---
id: IsESS-isNSS
title: IsESS.isNSS
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ESS
  declarations:
    - IsESS.isNSS
uses:
  - IsESS
  - IsNSS
---

# IsESS.isNSS

## Lean type

```lean
theorem IsESS.isNSS {s : S} (h : IsESS u s) : IsNSS u s
```

## Dependencies

- IsESS
- IsNSS
