---
id: payoff-nonneg-iff
title: payoff_nonneg_iff
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.OrderedGroup
  declarations:
    - payoff_nonneg_iff
uses:
---

# payoff_nonneg_iff

## Lean type

```lean
theorem payoff_nonneg_iff {value price : U} : 0 ≤ value - price ↔ price ≤ value
```

## Dependencies

- none
