---
id: fmB
title: fmB
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.LinearAlgebra.FourierMotzkin
  declarations:
    - fmB
uses:
  - FMRowIndex
  - ZeroRows
  - fmA
  - PosRows
  - NegRows
  - rowEval
---

# fmB

## Lean type

```lean
def fmB (A : I → Fin (n+1) → 𝕜) (b : I → 𝕜) (idx : FMRowIndex A) : 𝕜
```

## Dependencies

- FMRowIndex
- ZeroRows
- fmA
- PosRows
- NegRows
- rowEval
