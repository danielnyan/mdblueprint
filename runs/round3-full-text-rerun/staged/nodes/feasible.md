---
id: feasible
title: feasible
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.Instance
  declarations:
    - feasible
uses:
  - Allocation
  - toGenericCardinalInstance
  - toShareInstance
  - Allocation
---

# feasible

## Lean type

```lean
def feasible {N G : Type*} [Fintype N] [DecidableEq G] (I : AdditiveInstance N G) (A : Allocation N G) : Prop
```

## Dependencies

- Allocation
- toGenericCardinalInstance
- toShareInstance
- Allocation
