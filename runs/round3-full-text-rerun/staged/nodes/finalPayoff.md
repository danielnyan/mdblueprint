---
id: finalPayoff
title: finalPayoff
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.Play
  declarations:
    - finalPayoff
uses:
  - finalState
---

# finalPayoff

## Lean type

```lean
def finalPayoff (choose : (s : G.State) → G.Action s) (fuel : ℕ) (i : N) : U
```

## Dependencies

- finalState
