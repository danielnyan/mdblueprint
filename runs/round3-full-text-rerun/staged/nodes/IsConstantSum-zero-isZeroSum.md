---
id: IsConstantSum-zero-isZeroSum
title: IsConstantSum.zero_isZeroSum
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.Basic
  declarations:
    - IsConstantSum.zero_isZeroSum
uses:
  - IsConstantSum
  - IsZeroSum
---

# IsConstantSum.zero_isZeroSum

## Lean type

```lean
theorem IsConstantSum.zero_isZeroSum [Add U] [Zero U] {G : StrategicGame (Fin 2) U} (h : IsConstantSum G 0) : IsZeroSum G
```

## Dependencies

- IsConstantSum
- IsZeroSum
