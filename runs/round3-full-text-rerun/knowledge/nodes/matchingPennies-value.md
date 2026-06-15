---
id: matchingPennies-value
title: matchingPennies_value
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.StrategicGame.MatchingPennies
  declarations:
    - matchingPennies_value
uses:
  - matchingPennies
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - common_guarantee_eq_value
  - matchingPennies_uniform_row_guarantee
  - matchingPennies_uniform_column_guarantee
---

# matchingPennies_value

## Lean type

```lean
theorem matchingPennies_value : matchingPennies.value = 0
```

## Dependencies

- matchingPennies
- IsPositiveAffineOf.symm
- Indifferent.symm
- common_guarantee_eq_value
- matchingPennies_uniform_row_guarantee
- matchingPennies_uniform_column_guarantee
