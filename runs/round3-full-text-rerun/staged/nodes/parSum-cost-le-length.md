---
id: parSum-cost-le-length
title: parSum_cost_le_length
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.CostM.ParSum
  declarations:
    - parSum_cost_le_length
uses:
  - parSum
---

# parSum_cost_le_length

## Lean type

```lean
theorem parSum_cost_le_length (xs : List ℕ) : (parSum xs).cost ≤ xs.length
```

## Dependencies

- parSum
