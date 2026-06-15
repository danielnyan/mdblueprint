---
id: IsUtilitarianOptimal
title: IsUtilitarianOptimal
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Welfare
  declarations:
    - IsUtilitarianOptimal
uses:
  - Allocation
  - Allocation
  - toValuation
  - Valuation
  - Allocation
  - Allocation
---

# IsUtilitarianOptimal

## Lean type

```lean
def IsUtilitarianOptimal [Fintype N] (feasible : Allocation N S → Prop) (u : N → S → ℝ) (A : Allocation N S) : Prop
```

## Dependencies

- Allocation
- Allocation
- toValuation
- Valuation
- Allocation
- Allocation
