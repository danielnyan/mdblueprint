---
id: Arena-ofFin
title: Arena.ofFin
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.Basic
  declarations:
    - Arena.ofFin
uses:
  - IsReachable.next
---

# Arena.ofFin

## Lean type

```lean
def Arena.ofFin (n : ℕ) (nActions : Fin n → ℕ) (next : (s : Fin n) → Fin (nActions s) → Fin n) : Arena
```

## Dependencies

- IsReachable.next
