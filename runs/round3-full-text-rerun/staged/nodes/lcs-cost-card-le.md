---
id: lcs-cost-card-le
title: lcs_cost_card_le
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.CostM.LCS
  declarations:
    - lcs_cost_card_le
uses:
  - lcs_cost_subset
---

# lcs_cost_card_le

## Lean type

```lean
theorem lcs_cost_card_le (xs ys : List A) : (lcs xs ys).cost.toFinset.card ≤ (xs.length + 1) * (ys.length + 1)
```

## Dependencies

- lcs_cost_subset
