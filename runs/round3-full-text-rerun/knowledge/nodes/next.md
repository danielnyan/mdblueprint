---
id: next
title: next
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.CentipedeGame
  declarations:
    - next
uses:
---

# next

## Lean type

```lean
def next : (s : PrefixState) → PrefixAction s → PrefixState | root, stopRoot => stop0 | root, continueRoot => afterContinue | afterContinue, stopP1 => stop1 | afterContinue, continueP1 => continue1
```

## Dependencies

- none
