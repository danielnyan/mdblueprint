---
id: play
title: play
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.Play
  declarations:
    - play
uses:
  - ReachedSubgamePayoffTransfer.init
---

# play

## Lean type

```lean
def play (choose : (s : G.State) → G.Action s) (fuel : ℕ) : List G.State
```

## Dependencies

- ReachedSubgamePayoffTransfer.init
