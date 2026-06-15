---
id: payoff-nonpos-iff
title: payoff_nonpos_iff
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.OrderedGroup
  declarations:
    - payoff_nonpos_iff
uses:
---

# payoff_nonpos_iff

## Lean type

```lean
theorem payoff_nonpos_iff {value price : U} : value - price ≤ 0 ↔ value ≤ price
```

## Dependencies

- none
