---
id: fib-cost-card
title: fib_cost_card
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.CostM.MemoFib
  declarations:
    - fib_cost_card
uses:
  - fib_cost
---

# fib_cost_card

## Lean type

```lean
theorem fib_cost_card (n : ℕ) : (fib n).cost.toFinset.card = n + 1
```

## Dependencies

- fib_cost
