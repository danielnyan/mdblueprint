---
id: isZeroSum-iff-isConstantSum-zero
title: isZeroSum_iff_isConstantSum_zero
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.Basic
  declarations:
    - isZeroSum_iff_isConstantSum_zero
uses:
  - IsZeroSum
  - IsConstantSum
---

# isZeroSum_iff_isConstantSum_zero

## Lean type

```lean
theorem isZeroSum_iff_isConstantSum_zero [Add U] [Zero U] {G : StrategicGame (Fin 2) U} : IsZeroSum G ↔ IsConstantSum G 0
```

## Dependencies

- IsZeroSum
- IsConstantSum
