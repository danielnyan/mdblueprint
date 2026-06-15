---
id: IsImputation
title: IsImputation
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.CoalitionalGame.Basic
  declarations:
    - IsImputation
uses:
  - PayoffVector
  - IsEfficient
  - IsIndividuallyRational
---

# IsImputation

## Lean type

```lean
def IsImputation [Fintype N] [AddCommMonoid U] [LE U] (x : PayoffVector N U) : Prop
```

## Dependencies

- PayoffVector
- IsEfficient
- IsIndividuallyRational
