---
id: isFree-iff
title: isFree_iff
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.GaleShapley
  declarations:
    - isFree_iff
uses:
  - isFree
---

# isFree_iff

## Lean type

```lean
lemma isFree_iff {n : ℕ} (s : DAState n) (i : Fin n) : isFree s i = true ↔ ∀ j : Fin n, s.holding j ≠ some i
```

## Dependencies

- isFree
