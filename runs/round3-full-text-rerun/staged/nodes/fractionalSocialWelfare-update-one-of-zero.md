---
id: fractionalSocialWelfare-update-one-of-zero
title: fractionalSocialWelfare_update_one_of_zero
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Knapsack
  declarations:
    - fractionalSocialWelfare_update_one_of_zero
uses:
  - fractionalSocialWelfare
---

# fractionalSocialWelfare_update_one_of_zero

## Lean type

```lean
lemma fractionalSocialWelfare_update_one_of_zero (b : I → ℝ) {x : I → ℝ} {i : I} (hxi : x i = 0) : fractionalSocialWelfare b (Function.update x i 1) = b i + fractionalSocialWelfare b x
```

## Dependencies

- fractionalSocialWelfare
