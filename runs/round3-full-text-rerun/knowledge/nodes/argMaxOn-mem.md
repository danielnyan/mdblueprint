---
id: argMaxOn-mem
title: argMaxOn_mem
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.Argmax
  declarations:
    - argMaxOn_mem
uses:
  - IsZeroSum.head
  - Subtree.head
  - argMaxOn
---

# argMaxOn_mem

## Lean type

```lean
theorem argMaxOn_mem [TotalPreorder Y] [DecidableLE Y] (f : X → Y) (head : X) (tail : List X) : argMaxOn f head tail ∈ head :: tail
```

## Dependencies

- IsZeroSum.head
- Subtree.head
- argMaxOn
