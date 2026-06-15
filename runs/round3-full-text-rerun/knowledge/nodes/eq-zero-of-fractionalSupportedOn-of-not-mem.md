---
id: eq-zero-of-fractionalSupportedOn-of-not-mem
title: eq_zero_of_fractionalSupportedOn_of_not_mem
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Knapsack
  declarations:
    - eq_zero_of_fractionalSupportedOn_of_not_mem
uses:
  - fractionalSupportedOn
---

# eq_zero_of_fractionalSupportedOn_of_not_mem

## Lean type

```lean
lemma eq_zero_of_fractionalSupportedOn_of_not_mem {items : List I} {x : I → ℝ} (hsupp : fractionalSupportedOn items x) {i : I} (hi : i ∉ items) : x i = 0
```

## Dependencies

- fractionalSupportedOn
