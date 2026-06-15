---
id: parMap-unit-cost-le
title: parMap_unit_cost_le
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.CostM.ParAll
  declarations:
    - parMap_unit_cost_le
uses:
  - parList
  - stdSimplex.pure
  - Lottery.pure
---

# parMap_unit_cost_le

## Lean type

```lean
theorem parMap_unit_cost_le (xs : List ℕ) : (parList (xs.map (fun _ => (do ✓ pure 0 : CostM ℕ ℕ)))).cost ≤ 1
```

## Dependencies

- parList
- stdSimplex.pure
- Lottery.pure
