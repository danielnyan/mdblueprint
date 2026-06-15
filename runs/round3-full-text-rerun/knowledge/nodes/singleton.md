---
id: singleton
title: singleton
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.CostM.Visited
  declarations:
    - singleton
uses:
  - Visited
  - toFinset
  - ofFinset
  - Profile.ext
---

# singleton

## Lean type

```lean
def singleton (a : A) : Visited A
```

## Dependencies

- Visited
- toFinset
- ofFinset
- Profile.ext
