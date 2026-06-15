---
id: isEnvyFree-iff
title: isEnvyFree_iff
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.Checker
  declarations:
    - isEnvyFree_iff
uses:
  - Valuation
  - Allocation
  - IsEnvyFree
  - IsEFX.isEF1
  - IsEF1
---

# isEnvyFree_iff

## Lean type

```lean
theorem isEnvyFree_iff [Fintype N] (v : Valuation N G) (A : Allocation N G) : isEnvyFree v A = true ↔ IsEnvyFree v A
```

## Dependencies

- Valuation
- Allocation
- IsEnvyFree
- IsEFX.isEF1
- IsEF1
