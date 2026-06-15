---
id: IsEfficient
title: IsEfficient
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.CoalitionalGame.Basic
  declarations:
    - IsEfficient
uses:
  - PayoffVector
  - coalitionPayoff
---

# IsEfficient

## Lean type

```lean
def IsEfficient [Fintype N] [AddCommMonoid U] (x : PayoffVector N U) : Prop
```

## Dependencies

- PayoffVector
- coalitionPayoff
