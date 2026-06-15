---
id: utilitarianWelfare-mono
title: utilitarianWelfare_mono
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Welfare
  declarations:
    - utilitarianWelfare_mono
uses:
  - Valuation
  - Allocation
  - Allocation
---

# utilitarianWelfare_mono

## Lean type

```lean
lemma utilitarianWelfare_mono (u : N → S → ℝ) (A B : Allocation N S) (h : ∀ i : N, u i (A i) ≤ u i (B i)) : utilitarianWelfare u A ≤ utilitarianWelfare u B
```

## Dependencies

- Valuation
- Allocation
- Allocation
