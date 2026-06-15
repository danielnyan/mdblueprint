---
id: IsPositiveAffineOf-preserves-le
title: IsPositiveAffineOf.preserves_le
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.Utility.AffineTransform
  declarations:
    - IsPositiveAffineOf.preserves_le
uses:
  - IsPositiveAffineOf
---

# IsPositiveAffineOf.preserves_le

## Lean type

```lean
theorem IsPositiveAffineOf.preserves_le {u v : X → 𝕜} (h : IsPositiveAffineOf u v) (x y : X) : u x ≤ u y ↔ v x ≤ v y
```

## Dependencies

- IsPositiveAffineOf
