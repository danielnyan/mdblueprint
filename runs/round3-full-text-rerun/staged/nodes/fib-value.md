---
id: fib-value
title: fib_value
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.CostM.MemoFib
  declarations:
    - fib_value
uses:
  - fibAux
  - fibAux_ret
---

# fib_value

## Lean type

```lean
theorem fib_value (n : ℕ) : (fib n).ret = Nat.fib n
```

## Dependencies

- fibAux
- fibAux_ret
