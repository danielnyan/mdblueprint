---
id: exists-argMax-on
title: exists_argMax_on
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.Argmax
  declarations:
    - exists_argMax_on
uses:
  - IsZeroSum.head
  - Subtree.head
---

# exists_argMax_on

## Lean type

```lean
theorem exists_argMax_on [TotalPreorder Y] (f : X → Y) (head : X) (tail : List X) : ∃ m, m ∈ head :: tail ∧ ∀ x ∈ head :: tail, f x ≤ f m
```

## Dependencies

- IsZeroSum.head
- Subtree.head
