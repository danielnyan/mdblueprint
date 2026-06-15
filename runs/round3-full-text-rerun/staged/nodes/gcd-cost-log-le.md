---
id: gcd-cost-log-le
title: gcd_cost_log_le
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.CostM.GCD
  declarations:
    - gcd_cost_log_le
uses:
---

# gcd_cost_log_le

## Lean type

```lean
theorem gcd_cost_log_le (a b : ℕ) : (gcd a b).cost ≤ 2 * Nat.log 2 b + 1
```

## Dependencies

- none
