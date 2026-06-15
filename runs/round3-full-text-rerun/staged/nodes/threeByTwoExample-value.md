---
id: threeByTwoExample-value
title: threeByTwoExample_value
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.StrategicGame.ThreeByTwo
  declarations:
    - threeByTwoExample_value
uses:
  - threeByTwoExample
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - common_guarantee_eq_value
  - threeByTwo_row_guarantee
  - threeByTwo_column_guarantee
---

# threeByTwoExample_value

## Lean type

```lean
theorem threeByTwoExample_value : threeByTwoExample.value = 1 / 7
```

## Dependencies

- threeByTwoExample
- IsPositiveAffineOf.symm
- Indifferent.symm
- common_guarantee_eq_value
- threeByTwo_row_guarantee
- threeByTwo_column_guarantee
