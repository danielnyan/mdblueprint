---
id: finalState
title: finalState
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.Play
  declarations:
    - finalState
uses:
  - playMoves
  - sampleGame
  - isWinner
  - Board
  - TTTState.isOver
  - CPState.isOver
  - tttGame
  - ReachedSubgamePayoffTransfer.init
---

# finalState

## Lean type

```lean
def finalState (choose : (s : G.State) → G.Action s) (fuel : ℕ) : G.State
```

## Dependencies

- playMoves
- sampleGame
- isWinner
- Board
- TTTState.isOver
- CPState.isOver
- tttGame
- ReachedSubgamePayoffTransfer.init
