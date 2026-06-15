---
id: symMat-skew
title: symMat_skew
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Minimax.Minimax
  declarations:
    - symMat_skew
uses:
  - symMat
---

# symMat_skew

## Lean type

```lean
theorem symMat_skew (A : I → J → 𝕜) : ∀ k l, symMat A k l = - symMat A l k
```

## Dependencies

- symMat
