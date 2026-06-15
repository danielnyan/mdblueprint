---
id: IsLinearUtility
title: IsLinearUtility
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.Utility.Lottery
  declarations:
    - IsLinearUtility
uses:
  - Lottery
  - stdSimplex.mix
  - Lottery.mix
---

# IsLinearUtility

## Lean type

```lean
def IsLinearUtility {O : Type*} [Fintype O] (u : Lottery 𝕜 O → 𝕜) : Prop
```

## Dependencies

- Lottery
- stdSimplex.mix
- Lottery.mix
