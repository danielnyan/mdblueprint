---
id: naiveReverse
title: naiveReverse
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.CostM.ReverseSpace
  declarations:
    - naiveReverse
uses:
  - stdSimplex.pure
  - Lottery.pure
---

# naiveReverse

## Lean type

```lean
def naiveReverse {A : Type} : List A → CostM ℕ (List A) | [] => pure [] | a :: as => do ✓[as.length + 1] do let rest ← naiveReverse as pure (rest ++ [a]) /-- Cumulative `++` allocation is quadratic in input length. -/
```

## Dependencies

- stdSimplex.pure
- Lottery.pure
