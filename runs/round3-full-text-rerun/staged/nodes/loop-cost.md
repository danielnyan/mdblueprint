---
id: loop-cost
title: loop_cost
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.CostM.BoyerMoore
  declarations:
    - loop_cost
uses:
---

# loop_cost

## Lean type

```lean
theorem loop_cost (cand : A) (cnt : ℕ) (xs : List A) : (majority.loop cand cnt xs).cost = 0
```

## Dependencies

- none
