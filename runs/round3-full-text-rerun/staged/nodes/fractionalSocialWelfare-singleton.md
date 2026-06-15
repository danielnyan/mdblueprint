---
id: fractionalSocialWelfare-singleton
title: fractionalSocialWelfare_singleton
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Knapsack
  declarations:
    - fractionalSocialWelfare_singleton
uses:
  - fractionalSocialWelfare
---

# fractionalSocialWelfare_singleton

## Lean type

```lean
lemma fractionalSocialWelfare_singleton (b : I → ℝ) (i : I) (α : ℝ) : fractionalSocialWelfare b (fun j => if j = i then α else 0) = b i * α
```

## Dependencies

- fractionalSocialWelfare
