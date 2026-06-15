---
id: IsEquitable
title: IsEquitable
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.Instance
  declarations:
    - IsEquitable
uses:
  - Allocation
  - Allocation
  - Allocation
  - toCakeValuation
  - Allocation
  - Valuation
  - Allocation
  - Allocation
  - toValuation
---

# IsEquitable

## Lean type

```lean
def IsEquitable {N G : Type*} (I : AdditiveInstance N G) (A : Allocation N G) : Prop
```

## Dependencies

- Allocation
- Allocation
- Allocation
- toCakeValuation
- Allocation
- Valuation
- Allocation
- Allocation
- toValuation
