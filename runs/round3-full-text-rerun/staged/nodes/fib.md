---
id: fib
title: fib
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.CostM.MemoFib
  declarations:
    - fib
uses:
  - Visited
  - fibAux
  - stdSimplex.pure
  - Lottery.pure
---

# fib

## Lean type

```lean
def fib (n : ℕ) : CostM (Visited ℕ) ℕ
```

## Dependencies

- Visited
- fibAux
- stdSimplex.pure
- Lottery.pure
