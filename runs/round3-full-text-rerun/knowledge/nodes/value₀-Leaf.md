---
id: value₀-Leaf
title: value₀_Leaf
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.Zermelo
  declarations:
    - value₀_Leaf
uses:
  - IsZeroSum
---

# value₀_Leaf

## Lean type

```lean
theorem value₀_Leaf (p : Fin 2 → ℚ) (_h : IsZeroSum (Leaf p)) : value₀ (Leaf p) = p 0
```

## Dependencies

- IsZeroSum
