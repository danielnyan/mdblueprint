---
id: IsEFX-isEF1
title: IsEFX.isEF1
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.Fairness
  declarations:
    - IsEFX.isEF1
uses:
  - Valuation
  - Allocation
  - IsEFX
  - IsEF1
---

# IsEFX.isEF1

## Lean type

```lean
theorem IsEFX.isEF1 (v : Valuation N G) (A : Allocation N G) (h : IsEFX v A) : IsEF1 v A
```

## Dependencies

- Valuation
- Allocation
- IsEFX
- IsEF1
