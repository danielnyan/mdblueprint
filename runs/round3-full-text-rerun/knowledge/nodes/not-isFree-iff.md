---
id: not-isFree-iff
title: not_isFree_iff
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.GaleShapley
  declarations:
    - not_isFree_iff
uses:
  - isFree
---

# not_isFree_iff

## Lean type

```lean
lemma not_isFree_iff {n : ℕ} (s : DAState n) (i : Fin n) : isFree s i = false ↔ ∃ j : Fin n, s.holding j = some i
```

## Dependencies

- isFree
