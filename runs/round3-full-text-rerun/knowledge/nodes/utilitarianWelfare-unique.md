---
id: utilitarianWelfare-unique
title: utilitarianWelfare_unique
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Welfare
  declarations:
    - utilitarianWelfare_unique
uses:
  - Valuation
  - Allocation
  - Allocation
---

# utilitarianWelfare_unique

## Lean type

```lean
@[simp] lemma utilitarianWelfare_unique [Unique N] (u : N → S → ℝ) (A : Allocation N S) : utilitarianWelfare u A = u default (A default)
```

## Dependencies

- Valuation
- Allocation
- Allocation
