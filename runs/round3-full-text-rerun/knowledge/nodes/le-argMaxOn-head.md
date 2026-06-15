---
id: le-argMaxOn-head
title: le_argMaxOn_head
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.Argmax
  declarations:
    - le_argMaxOn_head
uses:
  - IsZeroSum.head
  - Subtree.head
  - argMaxOn
  - argMaxOn_ge
---

# le_argMaxOn_head

## Lean type

```lean
theorem le_argMaxOn_head [TotalPreorder Y] [DecidableLE Y] (f : X → Y) (head : X) (tail : List X) : f head ≤ f (argMaxOn f head tail)
```

## Dependencies

- IsZeroSum.head
- Subtree.head
- argMaxOn
- argMaxOn_ge
