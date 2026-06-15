---
id: parSum
title: parSum
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.CostM.ParSum
  declarations:
    - parSum
uses:
  - stdSimplex.pure
  - Lottery.pure
  - IsZeroSum.head
  - Subtree.head
---

# parSum

## Lean type

```lean
def parSum (xs : List ℕ) : CostM ℕ ℕ
```

## Dependencies

- stdSimplex.pure
- Lottery.pure
- IsZeroSum.head
- Subtree.head
