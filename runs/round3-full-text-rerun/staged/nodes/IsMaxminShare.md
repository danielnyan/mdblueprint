---
id: IsMaxminShare
title: IsMaxminShare
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.Instance
  declarations:
    - IsMaxminShare
uses:
  - Valuation
  - Allocation
  - Allocation
  - IsProportional.isMaxminShare
  - toValuation
---

# IsMaxminShare

## Lean type

```lean
def IsMaxminShare {N G : Type*} [Fintype N] [DecidableEq G] (I : AdditiveInstance N G) (A : Allocation N G) : Prop
```

## Dependencies

- Valuation
- Allocation
- Allocation
- IsProportional.isMaxminShare
- toValuation
