---
id: isTerminal-iff-not-isDecision
title: isTerminal_iff_not_isDecision
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.Basic
  declarations:
    - isTerminal_iff_not_isDecision
uses:
  - IsTerminal
  - isTerminal
  - IsDecision
  - ReachedSubgamePayoffTransfer.init
---

# isTerminal_iff_not_isDecision

## Lean type

```lean
theorem isTerminal_iff_not_isDecision (s : A.State) : A.IsTerminal s ↔ ¬ A.IsDecision s
```

## Dependencies

- IsTerminal
- isTerminal
- IsDecision
- ReachedSubgamePayoffTransfer.init
