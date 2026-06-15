---
id: IsMaxmin
title: IsMaxmin
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Welfare
  declarations:
    - IsMaxmin
uses:
  - Allocation
  - Allocation
  - toValuation
  - Valuation
  - Allocation
  - Allocation
---

# IsMaxmin

## Lean type

```lean
def IsMaxmin [Fintype N] [Nonempty N] (feasible : Allocation N S → Prop) (u : N → S → ℝ) (A : Allocation N S) : Prop
```

## Dependencies

- Allocation
- Allocation
- toValuation
- Valuation
- Allocation
- Allocation
