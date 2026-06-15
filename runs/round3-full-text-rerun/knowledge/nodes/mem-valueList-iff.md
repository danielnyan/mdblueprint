---
id: mem-valueList-iff
title: mem_valueList_iff
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.BackwardInduction
  declarations:
    - mem_valueList_iff
uses:
  - valueList_eq_map
---

# mem_valueList_iff

## Lean type

```lean
theorem mem_valueList_iff {v : N → U} {l : List (GameTree N U)} : v ∈ valueList l ↔ ∃ c ∈ l, value c = v
```

## Dependencies

- valueList_eq_map
