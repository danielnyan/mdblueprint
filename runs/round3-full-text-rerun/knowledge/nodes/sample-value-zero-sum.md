---
id: sample-value-zero-sum
title: sample_value_zero_sum
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.SimpleGameTree
  declarations:
    - sample_value_zero_sum
uses:
  - value_zero_sum
  - sample_zero_sum
---

# sample_value_zero_sum

## Lean type

```lean
theorem sample_value_zero_sum : (value sample) 0 + (value sample) 1 = 0
```

## Dependencies

- value_zero_sum
- sample_zero_sum
