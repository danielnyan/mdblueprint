---
id: socialWelfare-eq-value-add-welfareWithout
title: socialWelfare_eq_value_add_welfareWithout
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.VCG
  declarations:
    - socialWelfare_eq_value_add_welfareWithout
uses:
  - Valuation
  - socialWelfare
  - welfareWithout
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# socialWelfare_eq_value_add_welfareWithout

## Lean type

```lean
lemma socialWelfare_eq_value_add_welfareWithout (v : ∀ _ : I, Valuation A ℝ) (i : I) (a : A) : socialWelfare v a = v i a + welfareWithout v i a
```

## Dependencies

- Valuation
- socialWelfare
- welfareWithout
- IsPositiveAffineOf.symm
- Indifferent.symm
