---
id: matchingPennies-uniform-row-optimal
title: matchingPennies_uniform_row_optimal
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.StrategicGame.MatchingPennies
  declarations:
    - matchingPennies_uniform_row_optimal
uses:
  - optimalRowStrategies
  - matchingPennies
  - mem_optimalRowStrategies_iff_E_ge
  - matchingPennies_value
  - wsum_wsum_comm
  - wsum_const
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - wsum_le_wsum
  - matchingPennies_uniform_row_guarantee
---

# matchingPennies_uniform_row_optimal

## Lean type

```lean
theorem matchingPennies_uniform_row_optimal : matchingPenniesUniform ∈ matchingPennies.optimalRowStrategies
```

## Dependencies

- optimalRowStrategies
- matchingPennies
- mem_optimalRowStrategies_iff_E_ge
- matchingPennies_value
- wsum_wsum_comm
- wsum_const
- IsPositiveAffineOf.symm
- Indifferent.symm
- wsum_le_wsum
- matchingPennies_uniform_row_guarantee
