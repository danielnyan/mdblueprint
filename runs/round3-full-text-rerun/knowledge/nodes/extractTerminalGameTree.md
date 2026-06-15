---
id: extractTerminalGameTree
title: extractTerminalGameTree
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.FiniteArenaExtraction
  declarations:
    - extractTerminalGameTree
uses:
  - IsTerminal
  - isTerminal
---

# extractTerminalGameTree

## Lean type

```lean
def extractTerminalGameTree (s : G.State) (_hs : G.isTerminal s) : GameTree N U
```

## Dependencies

- IsTerminal
- isTerminal
