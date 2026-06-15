---
id: IsZeroSum-child-mem
title: IsZeroSum.child_mem
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.Zermelo
  declarations:
    - IsZeroSum.child_mem
uses:
  - IsZeroSum
  - IsZeroSum.head
  - Subtree.head
  - IsZeroSum.tail_mem
  - Subtree.tail_mem
---

# IsZeroSum.child_mem

## Lean type

```lean
theorem IsZeroSum.child_mem {m : Fin 2} {h : GameTree (Fin 2) ℚ} {t : List (GameTree (Fin 2) ℚ)} {c : GameTree (Fin 2) ℚ} (hzs : IsZeroSum (Node m h t)) (hmem : c ∈ h :: t) : IsZeroSum c
```

## Dependencies

- IsZeroSum
- IsZeroSum.head
- Subtree.head
- IsZeroSum.tail_mem
- Subtree.tail_mem
