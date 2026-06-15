---
id: IsPositiveAffineOf-preserves-representation
title: IsPositiveAffineOf.preserves_representation
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.Utility.AffineTransform
  declarations:
    - IsPositiveAffineOf.preserves_representation
uses:
  - IsPositiveAffineOf
  - IsPositiveAffineOf.preserves_le
---

# IsPositiveAffineOf.preserves_representation

## Lean type

```lean
theorem IsPositiveAffineOf.preserves_representation [Preorder X] {u v : X → 𝕜} (h : IsPositiveAffineOf u v) (hrep : RepresentsPreference u) : RepresentsPreference v
```

## Dependencies

- IsPositiveAffineOf
- IsPositiveAffineOf.preserves_le
