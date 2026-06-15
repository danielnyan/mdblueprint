---
id: farkasAugB
title: farkasAugB
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.LinearAlgebra.Farkas
  declarations:
    - farkasAugB
uses:
  - FarkasAugRow
  - farkasAugA
  - rowEval
---

# farkasAugB

## Lean type

```lean
def farkasAugB (b : I → 𝕜) : FarkasAugRow I → 𝕜 | Sum.inl _ => 0 | Sum.inr false => 0 | Sum.inr true => 1 /-! ### Simp lemmas for `farkasAugA` and `farkasAugB` -/ @[simp] theorem farkasAugA_inl_castSucc (A : I → Fin n → 𝕜) (b : I → 𝕜) (c : Fin n → 𝕜) (d : 𝕜) (i : I) (j' : Fin n) : farkasAugA A b c d (Sum.inl i) j'.castSucc = A i j'
```

## Dependencies

- FarkasAugRow
- farkasAugA
- rowEval
