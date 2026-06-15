---
id: IsEnvyFree
title: IsEnvyFree
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.Instance
  declarations:
    - IsEnvyFree
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

# IsEnvyFree

## Lean type

```lean
def IsEnvyFree {N G : Type*} (I : AdditiveInstance N G) (A : Allocation N G) : Prop
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
