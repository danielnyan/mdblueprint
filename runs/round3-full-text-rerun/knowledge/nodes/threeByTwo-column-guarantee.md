---
id: threeByTwo-column-guarantee
title: threeByTwo_column_guarantee
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.StrategicGame.ThreeByTwo
  declarations:
    - threeByTwo_column_guarantee
uses:
  - threeByTwoExample
---

# threeByTwo_column_guarantee

## Lean type

```lean
theorem threeByTwo_column_guarantee : ∀ i, threeByTwoExample.Ei i threeByTwoColOpt ≤ (1 : ℝ) / 7
```

## Dependencies

- threeByTwoExample
