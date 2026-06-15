---
id: wsum-pos
title: wsum_pos
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Simplex
  declarations:
    - wsum_pos
uses:
  - IsPositiveAffineOf.trans
  - StrictlyPreferred.trans
  - Arena.Reachable.trans
  - Indifferent.trans
  - Subtree.trans
---

# wsum_pos

## Lean type

```lean
theorem wsum_pos (x : stdSimplex 𝕜 I) {f : I → 𝕜} (hf : ∀ i, 0 < f i) : 0 < wsum x f
```

## Dependencies

- IsPositiveAffineOf.trans
- StrictlyPreferred.trans
- Arena.Reachable.trans
- Indifferent.trans
- Subtree.trans
