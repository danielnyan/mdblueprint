---
id: mover
title: mover
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.CentipedeGame
  declarations:
    - mover
uses:
---

# mover

## Lean type

```lean
def mover : PrefixState → Option (Fin 2) | root => some 0 | afterContinue => some 1 | stop0 => none | stop1 => none | continue1 => none
```

## Dependencies

- none
