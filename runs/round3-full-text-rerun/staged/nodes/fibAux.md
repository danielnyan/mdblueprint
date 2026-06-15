---
id: fibAux
title: fibAux
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.CostM.MemoFib
  declarations:
    - fibAux
uses:
  - Visited
  - stdSimplex.pure
  - Lottery.pure
---

# fibAux

## Lean type

```lean
def fibAux : ℕ → CostM (Visited ℕ) (ℕ × ℕ) | 0 => do ✓[singleton 0] pure (0, 1) | k + 1 => do let p ← fibAux k ✓[singleton (k + 1)] pure (p.2, p.1 + p.2) /-- Bottom-up Fibonacci. Visits each sub-problem in `{0, …, n}` exactly once. -/
```

## Dependencies

- Visited
- stdSimplex.pure
- Lottery.pure
