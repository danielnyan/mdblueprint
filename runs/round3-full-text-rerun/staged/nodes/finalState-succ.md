---
id: finalState-succ
title: finalState_succ
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.Play
  declarations:
    - finalState_succ
uses:
  - finalState
  - IsReachable.next
---

# finalState_succ

## Lean type

```lean
theorem finalState_succ (choose : (s : A.State) → A.Action s) (s : A.State) (n : ℕ) : A.finalState choose s (n + 1) = A.finalState choose (A.next s (choose s)) n
```

## Dependencies

- finalState
- IsReachable.next
