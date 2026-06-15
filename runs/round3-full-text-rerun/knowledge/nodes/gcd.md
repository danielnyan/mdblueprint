---
id: gcd
title: gcd
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.CostM.GCD
  declarations:
    - gcd
uses:
  - stdSimplex.pure
  - Lottery.pure
---

# gcd

## Lean type

```lean
def gcd : ℕ → ℕ → CostM ℕ ℕ | a, 0 => pure a | a, b + 1 => do ✓ gcd (b + 1) (a % (b + 1)) termination_by _ b => b decreasing_by exact Nat.mod_lt _ (Nat.succ_pos _) /-- Linear cost bound: `gcd a b` performs at most `b` `mod` operations. -/
```

## Dependencies

- stdSimplex.pure
- Lottery.pure
