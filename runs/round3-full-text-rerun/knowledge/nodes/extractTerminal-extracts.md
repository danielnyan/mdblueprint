---
id: extractTerminal-extracts
title: extractTerminal_extracts
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.FiniteArenaExtraction
  declarations:
    - extractTerminal_extracts
uses:
  - IsTerminal
  - isTerminal
  - extractTerminalGameTree
  - extractTerminal_payoff
---

# extractTerminal_extracts

## Lean type

```lean
theorem extractTerminal_extracts (s : G.State) (hs : G.isTerminal s) : ExtractsGameTree G s (G.extractTerminalGameTree s hs)
```

## Dependencies

- IsTerminal
- isTerminal
- extractTerminalGameTree
- extractTerminal_payoff
