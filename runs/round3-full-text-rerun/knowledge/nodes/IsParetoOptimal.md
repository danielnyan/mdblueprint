---
id: IsParetoOptimal
title: IsParetoOptimal
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.Instance
  declarations:
    - IsParetoOptimal
uses:
  - Allocation
  - Allocation
  - toGenericCardinalInstance
  - Allocation
  - Valuation
  - Allocation
  - Allocation
  - toValuation
---

# IsParetoOptimal

## Lean type

```lean
def IsParetoOptimal {N G : Type*} [Fintype N] [DecidableEq G] (I : AdditiveInstance N G) (A : Allocation N G) : Prop
```

## Dependencies

- Allocation
- Allocation
- toGenericCardinalInstance
- Allocation
- Valuation
- Allocation
- Allocation
- toValuation
