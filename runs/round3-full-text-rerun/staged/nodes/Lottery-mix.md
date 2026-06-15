---
id: Lottery-mix
title: Lottery.mix
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.Utility.Lottery
  declarations:
    - Lottery.mix
uses:
  - Lottery
  - stdSimplex.mix
---

# Lottery.mix

## Lean type

```lean
abbrev Lottery.mix {O : Type*} [Fintype O] (α : 𝕜) (hα₀ : 0 ≤ α) (hα₁ : α ≤ 1) (L₁ L₂ : Lottery 𝕜 O) : Lottery 𝕜 O
```

## Dependencies

- Lottery
- stdSimplex.mix
