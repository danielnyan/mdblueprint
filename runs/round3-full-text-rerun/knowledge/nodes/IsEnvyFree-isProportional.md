---
id: IsEnvyFree-isProportional
title: IsEnvyFree.isProportional
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Divisible.Instance
  declarations:
    - IsEnvyFree.isProportional
uses:
  - Allocation
  - IsEnvyFree
  - MeasureValuation
  - IsProportional
  - Allocation
  - IsEnvyFree
  - IsProportional
---

# IsEnvyFree.isProportional

## Lean type

```lean
theorem IsEnvyFree.isProportional {N Ω : Type*} [MeasurableSpace Ω] [Fintype N] (I : MeasureInstance N Ω) (A : Allocation N Ω) (ha : IsAllocation A) (hef : I.IsEnvyFree A) : I.IsProportional (Fintype.card N) A
```

## Dependencies

- Allocation
- IsEnvyFree
- MeasureValuation
- IsProportional
- Allocation
- IsEnvyFree
- IsProportional
