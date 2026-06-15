---
id: freeMenSet
title: freeMenSet
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.GaleShapley
  declarations:
    - freeMenSet
uses:
  - isFree
---

# freeMenSet

## Lean type

```lean
def freeMenSet {n : ℕ} (s : DAState n) : Finset (Fin n)
```

## Dependencies

- isFree
