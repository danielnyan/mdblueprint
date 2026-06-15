---
id: coalitionPayoff
title: coalitionPayoff
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.CoalitionalGame.Basic
  declarations:
    - coalitionPayoff
uses:
  - PayoffVector
---

# coalitionPayoff

## Lean type

```lean
def coalitionPayoff [AddCommMonoid U] (x : PayoffVector N U) (S : Finset N) : U
```

## Dependencies

- PayoffVector
