---
id: valueList-cons
title: valueList_cons
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.BackwardInduction
  declarations:
    - valueList_cons
uses:
---

# valueList_cons

## Lean type

```lean
@[simp] theorem valueList_cons (x : GameTree N U) (xs : List (GameTree N U)) : valueList (x :: xs) = value x :: valueList xs
```

## Dependencies

- none
