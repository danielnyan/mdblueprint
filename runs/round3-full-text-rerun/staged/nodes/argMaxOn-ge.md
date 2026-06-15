---
id: argMaxOn-ge
title: argMaxOn_ge
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.Argmax
  declarations:
    - argMaxOn_ge
uses:
  - IsZeroSum.head
  - Subtree.head
  - argMaxOn
---

# argMaxOn_ge

## Lean type

```lean
theorem argMaxOn_ge [TotalPreorder Y] [DecidableLE Y] (f : X → Y) (head : X) (tail : List X) : ∀ x ∈ head :: tail, f x ≤ f (argMaxOn f head tail)
```

## Dependencies

- IsZeroSum.head
- Subtree.head
- argMaxOn
