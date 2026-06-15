---
id: fibAux-ret
title: fibAux_ret
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.CostM.MemoFib
  declarations:
    - fibAux_ret
uses:
  - fibAux
---

# fibAux_ret

## Lean type

```lean
theorem fibAux_ret (n : ℕ) : (fibAux n).ret = (Nat.fib n, Nat.fib (n + 1))
```

## Dependencies

- fibAux
