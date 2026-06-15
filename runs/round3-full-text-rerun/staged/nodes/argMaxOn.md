---
id: argMaxOn
title: argMaxOn
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.Argmax
  declarations:
    - argMaxOn
uses:
  - IsZeroSum.head
  - Subtree.head
---

# argMaxOn

## Lean type

```lean
def argMaxOn [TotalPreorder Y] [DecidableLE Y] (f : X → Y) (head : X) (tail : List X) : X
```

## Dependencies

- IsZeroSum.head
- Subtree.head
