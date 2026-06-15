---
id: optimalRowSet-isCompact
title: optimalRowSet_isCompact
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.OptimalStrategySetPolytope
  declarations:
    - optimalRowSet_isCompact
uses:
  - optimalRowSet
  - optimalRowSet_isClosed
---

# optimalRowSet_isCompact

## Lean type

```lean
theorem optimalRowSet_isCompact : IsCompact A.optimalRowSet
```

## Dependencies

- optimalRowSet
- optimalRowSet_isClosed
