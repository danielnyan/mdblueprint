---
id: CPState-step
title: CPState.step
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.CentipedeGame
  declarations:
    - CPState.step
uses:
  - TTTState.isOver
  - CPState.isOver
---

# CPState.step

## Lean type

```lean
def CPState.step (s : CPState) (a : CPAct) : CPState
```

## Dependencies

- TTTState.isOver
- CPState.isOver
