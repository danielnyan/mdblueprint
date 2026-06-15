---
id: welfareWithout-le-socialWelfare
title: welfareWithout_le_socialWelfare
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.VCG
  declarations:
    - welfareWithout_le_socialWelfare
uses:
  - Valuation
  - welfareWithout
  - socialWelfare
---

# welfareWithout_le_socialWelfare

## Lean type

```lean
lemma welfareWithout_le_socialWelfare (v : ∀ _ : I, Valuation A ℝ) (hnonneg : ∀ i : I, ∀ a : A, 0 ≤ v i a) (i : I) (a : A) : welfareWithout v i a ≤ socialWelfare v a
```

## Dependencies

- Valuation
- welfareWithout
- socialWelfare
