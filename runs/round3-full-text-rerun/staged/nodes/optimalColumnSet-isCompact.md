---
id: optimalColumnSet-isCompact
title: optimalColumnSet_isCompact
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.OptimalStrategySetPolytope
  declarations:
    - optimalColumnSet_isCompact
uses:
  - optimalColumnSet
  - optimalColumnSet_isClosed
---

# optimalColumnSet_isCompact

## Lean type

```lean
theorem optimalColumnSet_isCompact : IsCompact A.optimalColumnSet
```

## Dependencies

- optimalColumnSet
- optimalColumnSet_isClosed
