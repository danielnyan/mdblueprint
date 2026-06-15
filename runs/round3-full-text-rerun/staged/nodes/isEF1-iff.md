---
id: isEF1-iff
title: isEF1_iff
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.Checker
  declarations:
    - isEF1_iff
uses:
  - Valuation
  - Allocation
  - IsEFX.isEF1
  - IsEF1
  - IsEFX
---

# isEF1_iff

## Lean type

```lean
theorem isEF1_iff [Fintype N] [DecidableEq N] [DecidableEq G] (v : Valuation N G) (A : Allocation N G) : isEF1 v A = true ↔ IsEF1 v A
```

## Dependencies

- Valuation
- Allocation
- IsEFX.isEF1
- IsEF1
- IsEFX
