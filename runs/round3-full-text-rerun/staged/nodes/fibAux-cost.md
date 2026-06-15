---
id: fibAux-cost
title: fibAux_cost
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.CostM.MemoFib
  declarations:
    - fibAux_cost
uses:
  - fibAux
  - toFinset
  - Visited
  - Profile.ext
---

# fibAux_cost

## Lean type

```lean
theorem fibAux_cost (n : ℕ) : (fibAux n).cost.toFinset = Finset.range (n + 1)
```

## Dependencies

- fibAux
- toFinset
- Visited
- Profile.ext
