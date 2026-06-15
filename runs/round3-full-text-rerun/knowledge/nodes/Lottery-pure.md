---
id: Lottery-pure
title: Lottery.pure
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.Utility.Lottery
  declarations:
    - Lottery.pure
uses:
  - Lottery
  - stdSimplex.pure
---

# Lottery.pure

## Lean type

```lean
abbrev Lottery.pure {O : Type*} [Fintype O] [DecidableEq O] (o₀ : O) : Lottery 𝕜 O
```

## Dependencies

- Lottery
- stdSimplex.pure
