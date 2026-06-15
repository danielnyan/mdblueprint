---
id: parSum-cost-le-clog
title: parSum_cost_le_clog
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.CostM.ParSum
  declarations:
    - parSum_cost_le_clog
uses:
  - parSum
  - IsPositiveAffineOf.trans
  - StrictlyPreferred.trans
  - Arena.Reachable.trans
  - Indifferent.trans
  - Subtree.trans
---

# parSum_cost_le_clog

## Lean type

```lean
theorem parSum_cost_le_clog (xs : List ℕ) : (parSum xs).cost ≤ Nat.clog 2 xs.length
```

## Dependencies

- parSum
- IsPositiveAffineOf.trans
- StrictlyPreferred.trans
- Arena.Reachable.trans
- Indifferent.trans
- Subtree.trans
