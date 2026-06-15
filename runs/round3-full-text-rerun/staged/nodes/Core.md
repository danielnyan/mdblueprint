---
id: Core
title: Core
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.CoalitionalGame.Core
  declarations:
    - Core
uses:
  - PayoffVector
  - IsEfficient
  - coalitionPayoff
---

# Core

## Lean type

```lean
def Core : Set (PayoffVector N ℝ)
```

## Dependencies

- PayoffVector
- IsEfficient
- coalitionPayoff
