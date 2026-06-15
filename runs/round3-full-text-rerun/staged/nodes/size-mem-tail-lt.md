---
id: size-mem-tail-lt
title: size_mem_tail_lt
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.GameTree
  declarations:
    - size_mem_tail_lt
uses:
  - size_pos
---

# size_mem_tail_lt

## Lean type

```lean
theorem size_mem_tail_lt (m : N) (h : GameTree N U) (t : List (GameTree N U)) {c : GameTree N U} (hmem : c ∈ t) : c.size < (Node m h t).size
```

## Dependencies

- size_pos
