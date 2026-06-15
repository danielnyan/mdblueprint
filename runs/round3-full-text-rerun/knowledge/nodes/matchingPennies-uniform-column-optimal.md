---
id: matchingPennies-uniform-column-optimal
title: matchingPennies_uniform_column_optimal
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.StrategicGame.MatchingPennies
  declarations:
    - matchingPennies_uniform_column_optimal
uses:
  - optimalColumnStrategies
  - matchingPennies
  - mem_optimalColumnStrategies_iff_E_le
  - matchingPennies_value
  - wsum_le_wsum
  - matchingPennies_uniform_column_guarantee
  - wsum_const
---

# matchingPennies_uniform_column_optimal

## Lean type

```lean
theorem matchingPennies_uniform_column_optimal : matchingPenniesUniform ∈ matchingPennies.optimalColumnStrategies
```

## Dependencies

- optimalColumnStrategies
- matchingPennies
- mem_optimalColumnStrategies_iff_E_le
- matchingPennies_value
- wsum_le_wsum
- matchingPennies_uniform_column_guarantee
- wsum_const
