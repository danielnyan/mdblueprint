---
id: rotateBundles-mem
title: rotateBundles_mem
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.EnvyCycle
  declarations:
    - rotateBundles_mem
uses:
  - Allocation
  - Pos
  - IsZeroSum.head
  - Subtree.head
---

# rotateBundles_mem

## Lean type

```lean
lemma rotateBundles_mem (A : Allocation N G) (l : List N) (i : N) (h : i ∈ l) : ∃ k : Fin l.length, l.get k = i ∧ ∃ k' : Fin l.length, (k'.val = (k.val + 1) % l.length) ∧ rotateBundles A l i = A (l.get k')
```

## Dependencies

- Allocation
- Pos
- IsZeroSum.head
- Subtree.head
