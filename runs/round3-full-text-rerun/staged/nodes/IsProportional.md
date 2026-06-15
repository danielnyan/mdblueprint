---
id: IsProportional
title: IsProportional
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.Instance
  declarations:
    - IsProportional
uses:
  - Allocation
  - IsEnvyFree.isProportional
  - Allocation
  - Allocation
  - IsEnvyFree.isProportional
  - toCakeValuation
  - Allocation
  - Valuation
  - Allocation
  - IsEnvyFree.isProportional
  - Allocation
  - IsEnvyFree.isProportional
  - toValuation
---

# IsProportional

## Lean type

```lean
def IsProportional {N G : Type*} (I : AdditiveInstance N G) (n : ℕ) (A : Allocation N G) : Prop
```

## Dependencies

- Allocation
- IsEnvyFree.isProportional
- Allocation
- Allocation
- IsEnvyFree.isProportional
- toCakeValuation
- Allocation
- Valuation
- Allocation
- IsEnvyFree.isProportional
- Allocation
- IsEnvyFree.isProportional
- toValuation
