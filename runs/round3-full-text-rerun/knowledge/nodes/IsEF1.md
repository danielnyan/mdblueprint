---
id: IsEF1
title: IsEF1
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.Instance
  declarations:
    - IsEF1
uses:
  - Valuation
  - Allocation
  - Allocation
  - IsEFX.isEF1
  - toValuation
---

# IsEF1

## Lean type

```lean
def IsEF1 {N G : Type*} [DecidableEq G] (I : AdditiveInstance N G) (A : Allocation N G) : Prop
```

## Dependencies

- Valuation
- Allocation
- Allocation
- IsEFX.isEF1
- toValuation
