---
id: empty-Dominant
title: empty_Dominant
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - empty_Dominant
uses:
  - isDominant
---

# empty_Dominant

## Lean type

```lean
lemma empty_Dominant (h : D.Nonempty) : IST.isDominant Finset.empty D
```

## Dependencies

- isDominant
