---
id: fib-cost
title: fib_cost
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.CostM.MemoFib
  declarations:
    - fib_cost
uses:
  - toFinset
  - fibAux
  - Visited
  - fibAux_cost
---

# fib_cost

## Lean type

```lean
theorem fib_cost (n : ℕ) : (fib n).cost.toFinset = Finset.range (n + 1)
```

## Dependencies

- toFinset
- fibAux
- Visited
- fibAux_cost
