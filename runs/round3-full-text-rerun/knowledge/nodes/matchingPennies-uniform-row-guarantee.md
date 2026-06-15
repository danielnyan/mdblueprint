---
id: matchingPennies-uniform-row-guarantee
title: matchingPennies_uniform_row_guarantee
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.StrategicGame.MatchingPennies
  declarations:
    - matchingPennies_uniform_row_guarantee
uses:
  - matchingPennies
---

# matchingPennies_uniform_row_guarantee

## Lean type

```lean
theorem matchingPennies_uniform_row_guarantee (j : Fin 2) : 0 ≤ matchingPennies.Ej matchingPenniesUniform j
```

## Dependencies

- matchingPennies
