---
id: naiveReverse-cost-le
title: naiveReverse_cost_le
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.CostM.ReverseSpace
  declarations:
    - naiveReverse_cost_le
uses:
  - naiveReverse
---

# naiveReverse_cost_le

## Lean type

```lean
theorem naiveReverse_cost_le {A : Type} (l : List A) : (naiveReverse l).cost ≤ l.length * l.length
```

## Dependencies

- naiveReverse
