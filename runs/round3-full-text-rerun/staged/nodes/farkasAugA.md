---
id: farkasAugA
title: farkasAugA
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.LinearAlgebra.Farkas
  declarations:
    - farkasAugA
uses:
  - FarkasAugRow
---

# farkasAugA

## Lean type

```lean
def farkasAugA (A : I → Fin n → 𝕜) (b : I → 𝕜) (c : Fin n → 𝕜) (d : 𝕜) : FarkasAugRow I → Fin (n+1) → 𝕜 | Sum.inl i, j => Fin.lastCases (-b i) (fun j' => A i j') j | Sum.inr false, j => Fin.lastCases 1 (fun _ => (0 : 𝕜)) j | Sum.inr true, j => Fin.lastCases d (fun j' => -c j') j /-- Augmented RHS `b_aug : FarkasAugRow I → 𝕜`. -/
```

## Dependencies

- FarkasAugRow
