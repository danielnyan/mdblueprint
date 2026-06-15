---
id: extractTerminal-payoff
title: extractTerminal_payoff
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.FiniteArenaExtraction
  declarations:
    - extractTerminal_payoff
uses:
  - IsTerminal
  - isTerminal
  - extractTerminalGameTree
---

# extractTerminal_payoff

## Lean type

```lean
theorem extractTerminal_payoff (s : G.State) (hs : G.isTerminal s) : G.extractTerminalGameTree s hs = GameTree.Leaf (G.payoff s)
```

## Dependencies

- IsTerminal
- isTerminal
- extractTerminalGameTree
