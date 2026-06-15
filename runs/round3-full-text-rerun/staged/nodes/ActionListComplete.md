---
id: ActionListComplete
title: ActionListComplete
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.FiniteArenaExtraction
  declarations:
    - ActionListComplete
uses:
  - IsZeroSum.head
  - Subtree.head
  - IsTerminal
  - isTerminal
  - IsReachable.next
---

# ActionListComplete

## Lean type

```lean
def ActionListComplete (s : G.State) (head : G.Action s) (tail : List (G.Action s)) : Prop
```

## Dependencies

- IsZeroSum.head
- Subtree.head
- IsTerminal
- isTerminal
- IsReachable.next
