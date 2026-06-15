---
id: isEFX-iff
title: isEFX_iff
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.Checker
  declarations:
    - isEFX_iff
uses:
  - Valuation
  - Allocation
  - IsEFX
  - IsEnvyFree.isProportional
  - IsProportional
---

# isEFX_iff

## Lean type

```lean
theorem isEFX_iff [Fintype N] [DecidableEq N] [DecidableEq G] (v : Valuation N G) (A : Allocation N G) : isEFX v A = true ↔ IsEFX v A
```

## Dependencies

- Valuation
- Allocation
- IsEFX
- IsEnvyFree.isProportional
- IsProportional
