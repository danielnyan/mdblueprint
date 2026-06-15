---
id: twoByTwo-row-guarantee
title: twoByTwo_row_guarantee
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.StrategicGame.TwoByTwo
  declarations:
    - twoByTwo_row_guarantee
uses:
  - twoByTwo
---

# twoByTwo_row_guarantee

## Lean type

```lean
theorem twoByTwo_row_guarantee (a b c d : ℝ) (hdenom : 0 < a + d - b - c) (hab : b ≤ a) (hdc : c ≤ d) : ∀ j, twoByTwoMixedValue a b c d ≤ (twoByTwo a b c d).Ej (twoByTwoRowMixed a b c d hdenom hab hdc) j
```

## Dependencies

- twoByTwo
