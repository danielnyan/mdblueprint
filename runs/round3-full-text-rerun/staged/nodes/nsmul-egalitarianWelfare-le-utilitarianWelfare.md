---
id: nsmul-egalitarianWelfare-le-utilitarianWelfare
title: nsmul_egalitarianWelfare_le_utilitarianWelfare
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Welfare
  declarations:
    - nsmul_egalitarianWelfare_le_utilitarianWelfare
uses:
  - Valuation
  - Allocation
  - Allocation
---

# nsmul_egalitarianWelfare_le_utilitarianWelfare

## Lean type

```lean
lemma nsmul_egalitarianWelfare_le_utilitarianWelfare [Nonempty N] (u : N → S → ℝ) (A : Allocation N S) (hle : ∀ i : N, egalitarianWelfare u A ≤ u i (A i)) : Fintype.card N • egalitarianWelfare u A ≤ utilitarianWelfare u A
```

## Dependencies

- Valuation
- Allocation
- Allocation
