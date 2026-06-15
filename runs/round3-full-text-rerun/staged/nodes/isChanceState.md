---
id: isChanceState
title: isChanceState
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.Basic
  declarations:
    - isChanceState
uses:
  - IsTerminal
  - isTerminal
---

# isChanceState

## Lean type

```lean
def isChanceState (G : ExtensiveGame N U) (s : G.State) : Prop
```

## Dependencies

- IsTerminal
- isTerminal
