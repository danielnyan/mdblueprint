---
id: profileStrategy
title: profileStrategy
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.GameTreeStrategicForm
  declarations:
    - profileStrategy
uses:
  - PlayerStrategy
  - Strategy
  - toStrategicGame
---

# profileStrategy

## Lean type

```lean
def profileStrategy (σ : N → PlayerStrategy N U) : Strategy N U
```

## Dependencies

- PlayerStrategy
- Strategy
- toStrategicGame
