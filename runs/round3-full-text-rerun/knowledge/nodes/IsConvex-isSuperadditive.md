---
id: IsConvex-isSuperadditive
title: IsConvex.isSuperadditive
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.CoalitionalGame.Basic
  declarations:
    - IsConvex.isSuperadditive
uses:
  - IsConvex
  - IsSuperadditive
---

# IsConvex.isSuperadditive

## Lean type

```lean
theorem IsConvex.isSuperadditive [LE U] (hconv : G.IsConvex) : G.IsSuperadditive
```

## Dependencies

- IsConvex
- IsSuperadditive
