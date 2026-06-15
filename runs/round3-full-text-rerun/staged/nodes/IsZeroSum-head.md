---
id: IsZeroSum-head
title: IsZeroSum.head
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.Zermelo
  declarations:
    - IsZeroSum.head
uses:
  - IsZeroSum
---

# IsZeroSum.head

## Lean type

```lean
theorem IsZeroSum.head {m : Fin 2} {h : GameTree (Fin 2) ℚ} {t : List (GameTree (Fin 2) ℚ)} (hzs : IsZeroSum (Node m h t)) : IsZeroSum h
```

## Dependencies

- IsZeroSum
