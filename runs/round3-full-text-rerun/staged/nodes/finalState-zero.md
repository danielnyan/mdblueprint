---
id: finalState-zero
title: finalState_zero
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.Play
  declarations:
    - finalState_zero
uses:
  - finalState
---

# finalState_zero

## Lean type

```lean
theorem finalState_zero (choose : (s : A.State) → A.Action s) (s : A.State) : A.finalState choose s 0 = s
```

## Dependencies

- finalState
