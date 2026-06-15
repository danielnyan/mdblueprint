---
id: size-mem-children-lt
title: size_mem_children_lt
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.GameTree
  declarations:
    - size_mem_children_lt
uses:
  - size_head_lt
  - size_mem_tail_lt
  - IsPositiveAffineOf.refl
  - Indifferent.refl
  - IVariant.refl
---

# size_mem_children_lt

## Lean type

```lean
theorem size_mem_children_lt (m : N) (h : GameTree N U) (t : List (GameTree N U)) {c : GameTree N U} (hmem : c ∈ children (Node m h t)) : c.size < (Node m h t).size
```

## Dependencies

- size_head_lt
- size_mem_tail_lt
- IsPositiveAffineOf.refl
- Indifferent.refl
- IVariant.refl
