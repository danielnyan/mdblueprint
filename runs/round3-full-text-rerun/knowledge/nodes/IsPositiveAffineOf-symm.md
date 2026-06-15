---
id: IsPositiveAffineOf-symm
title: IsPositiveAffineOf.symm
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.Utility.AffineTransform
  declarations:
    - IsPositiveAffineOf.symm
uses:
  - IsPositiveAffineOf
---

# IsPositiveAffineOf.symm

## Lean type

```lean
theorem IsPositiveAffineOf.symm {u v : X → 𝕜} (h : IsPositiveAffineOf u v) : IsPositiveAffineOf v u
```

## Dependencies

- IsPositiveAffineOf
