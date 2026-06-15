---
id: matchingPennies-uniform-column-guarantee
title: matchingPennies_uniform_column_guarantee
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.StrategicGame.MatchingPennies
  declarations:
    - matchingPennies_uniform_column_guarantee
uses:
  - matchingPennies
---

# matchingPennies_uniform_column_guarantee

## Lean type

```lean
theorem matchingPennies_uniform_column_guarantee (i : Fin 2) : matchingPennies.Ei i matchingPenniesUniform ≤ 0
```

## Dependencies

- matchingPennies
