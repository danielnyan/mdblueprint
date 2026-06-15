---
id: egalitarianWelfare-le
title: egalitarianWelfare_le
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Welfare
  declarations:
    - egalitarianWelfare_le
uses:
  - Valuation
  - Allocation
  - Allocation
---

# egalitarianWelfare_le

## Lean type

```lean
lemma egalitarianWelfare_le [Nonempty N] (u : N → S → ℝ) (A : Allocation N S) (i : N) : egalitarianWelfare u A ≤ u i (A i)
```

## Dependencies

- Valuation
- Allocation
- Allocation
