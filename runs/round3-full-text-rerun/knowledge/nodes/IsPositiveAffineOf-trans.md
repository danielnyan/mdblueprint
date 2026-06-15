---
id: IsPositiveAffineOf-trans
title: IsPositiveAffineOf.trans
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.Utility.AffineTransform
  declarations:
    - IsPositiveAffineOf.trans
uses:
  - IsPositiveAffineOf
---

# IsPositiveAffineOf.trans

## Lean type

```lean
theorem IsPositiveAffineOf.trans {u v w : X → 𝕜} (h₁ : IsPositiveAffineOf u v) (h₂ : IsPositiveAffineOf v w) : IsPositiveAffineOf u w
```

## Dependencies

- IsPositiveAffineOf
