---
id: outsidedoor-is-singleton
title: outsidedoor_is_singleton
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - outsidedoor_is_singleton
uses:
  - isOutsideDoor
---

# outsidedoor_is_singleton

## Lean type

```lean
lemma outsidedoor_is_singleton (h : IST.isOutsideDoor τ D) : τ = Finset.empty ∧ ∃ i, D = {i}
```

## Dependencies

- isOutsideDoor
