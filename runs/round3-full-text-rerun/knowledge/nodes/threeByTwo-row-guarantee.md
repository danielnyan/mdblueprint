---
id: threeByTwo-row-guarantee
title: threeByTwo_row_guarantee
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.StrategicGame.ThreeByTwo
  declarations:
    - threeByTwo_row_guarantee
uses:
  - threeByTwoExample
---

# threeByTwo_row_guarantee

## Lean type

```lean
theorem threeByTwo_row_guarantee : ∀ j, (1 : ℝ) / 7 ≤ threeByTwoExample.Ej threeByTwoRowOpt j
```

## Dependencies

- threeByTwoExample
