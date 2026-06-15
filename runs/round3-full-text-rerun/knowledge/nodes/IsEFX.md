---
id: IsEFX
title: IsEFX
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.Instance
  declarations:
    - IsEFX
uses:
  - Valuation
  - Allocation
  - Allocation
  - toValuation
---

# IsEFX

## Lean type

```lean
def IsEFX {N G : Type*} [DecidableEq G] (I : AdditiveInstance N G) (A : Allocation N G) : Prop
```

## Dependencies

- Valuation
- Allocation
- Allocation
- toValuation
