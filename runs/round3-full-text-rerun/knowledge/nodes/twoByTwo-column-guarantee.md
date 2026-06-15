---
id: twoByTwo-column-guarantee
title: twoByTwo_column_guarantee
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.StrategicGame.TwoByTwo
  declarations:
    - twoByTwo_column_guarantee
uses:
  - twoByTwo
---

# twoByTwo_column_guarantee

## Lean type

```lean
theorem twoByTwo_column_guarantee (a b c d : ℝ) (hdenom : 0 < a + d - b - c) (hac : c ≤ a) (hdb : b ≤ d) : ∀ i, (twoByTwo a b c d).Ei i (twoByTwoColumnMixed a b c d hdenom hac hdb) ≤ twoByTwoMixedValue a b c d
```

## Dependencies

- twoByTwo
