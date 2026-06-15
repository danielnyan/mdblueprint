---
id: Nonempty-of-Dominant
title: Nonempty_of_Dominant
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - Nonempty_of_Dominant
uses:
  - isDominant
---

# Nonempty_of_Dominant

## Lean type

```lean
lemma Nonempty_of_Dominant (h : IST.isDominant σ C) : C.Nonempty
```

## Dependencies

- isDominant
