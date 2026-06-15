---
id: FMRowIndex
title: FMRowIndex
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.LinearAlgebra.FourierMotzkin
  declarations:
    - FMRowIndex
uses:
  - ZeroRows
  - PosRows
  - NegRows
---

# FMRowIndex

## Lean type

```lean
abbrev FMRowIndex (A : I → Fin (n+1) → 𝕜) : Type _
```

## Dependencies

- ZeroRows
- PosRows
- NegRows
