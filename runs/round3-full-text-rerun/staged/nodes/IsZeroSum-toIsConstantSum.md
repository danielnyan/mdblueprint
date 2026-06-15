---
id: IsZeroSum-toIsConstantSum
title: IsZeroSum.toIsConstantSum
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.Basic
  declarations:
    - IsZeroSum.toIsConstantSum
uses:
  - IsZeroSum
  - IsConstantSum
---

# IsZeroSum.toIsConstantSum

## Lean type

```lean
theorem IsZeroSum.toIsConstantSum [Add U] [Zero U] {G : StrategicGame (Fin 2) U} (hzs : IsZeroSum G) : IsConstantSum G 0
```

## Dependencies

- IsZeroSum
- IsConstantSum
