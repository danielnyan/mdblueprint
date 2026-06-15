---
id: symMat
title: symMat
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Minimax.Minimax
  declarations:
    - symMat
uses:
---

# symMat

## Lean type

```lean
def symMat (A : I → J → 𝕜) : (I ⊕ J ⊕ Unit) → (I ⊕ J ⊕ Unit) → 𝕜 | Sum.inl _, Sum.inl _ => 0 | Sum.inl i, Sum.inr (Sum.inl j) => A i j | Sum.inl _, Sum.inr (Sum.inr _) => -1 | Sum.inr (Sum.inl j), Sum.inl i => -A i j | Sum.inr (Sum.inl _), Sum.inr (Sum.inl _) => 0 | Sum.inr (Sum.inl _), Sum.inr (Sum.inr _) => 1 | Sum.inr (Sum.inr _), Sum.inl _ => 1 | Sum.inr (Sum.inr _), Sum.inr (Sum.inl _) => -1 | Sum.inr (Sum.inr _), Sum.inr (Sum.inr _) => 0
```

## Dependencies

- none
