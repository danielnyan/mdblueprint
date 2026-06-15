---
id: twoByTwo-value
title: twoByTwo_value
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.StrategicGame.TwoByTwo
  declarations:
    - twoByTwo_value
uses:
  - twoByTwo
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - common_guarantee_eq_value
  - twoByTwo_row_guarantee
  - twoByTwo_column_guarantee
---

# twoByTwo_value

## Lean type

```lean
theorem twoByTwo_value (a b c d : ℝ) (hdenom : 0 < a + d - b - c) (hab : b ≤ a) (hac : c ≤ a) (hdb : b ≤ d) (hdc : c ≤ d) : (twoByTwo a b c d).value = twoByTwoMixedValue a b c d
```

## Dependencies

- twoByTwo
- IsPositiveAffineOf.symm
- Indifferent.symm
- common_guarantee_eq_value
- twoByTwo_row_guarantee
- twoByTwo_column_guarantee
