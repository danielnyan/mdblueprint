---
id: majority-peak-le
title: majority_peak_le
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.CostM.BoyerMoore
  declarations:
    - majority_peak_le
uses:
  - loop_cost
---

# majority_peak_le

## Lean type

```lean
theorem majority_peak_le (xs : List A) : (majority xs).cost.peak ≤ 2
```

## Dependencies

- loop_cost
