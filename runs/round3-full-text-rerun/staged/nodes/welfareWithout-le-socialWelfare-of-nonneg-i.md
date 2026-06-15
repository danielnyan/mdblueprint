---
id: welfareWithout-le-socialWelfare-of-nonneg-i
title: welfareWithout_le_socialWelfare_of_nonneg_i
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.VCG
  declarations:
    - welfareWithout_le_socialWelfare_of_nonneg_i
uses:
  - Valuation
  - welfareWithout
  - socialWelfare
  - socialWelfare_eq_value_add_welfareWithout
---

# welfareWithout_le_socialWelfare_of_nonneg_i

## Lean type

```lean
lemma welfareWithout_le_socialWelfare_of_nonneg_i (v : ∀ _ : I, Valuation A ℝ) (i : I) (hi_nonneg : ∀ a : A, 0 ≤ v i a) (a : A) : welfareWithout v i a ≤ socialWelfare v a
```

## Dependencies

- Valuation
- welfareWithout
- socialWelfare
- socialWelfare_eq_value_add_welfareWithout
