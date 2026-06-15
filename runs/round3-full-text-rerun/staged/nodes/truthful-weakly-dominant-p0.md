---
id: truthful-weakly-dominant-p0
title: truthful_weakly_dominant_p0
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.SimpleAuction
  declarations:
    - truthful_weakly_dominant_p0
uses:
  - IsStrictlyDominant.isWeaklyDominant
  - IsWeaklyDominant
  - Vickrey
---

# truthful_weakly_dominant_p0

## Lean type

```lean
theorem truthful_weakly_dominant_p0 (v : Fin 2 → Fin n) : IsWeaklyDominant (Vickrey n v) 0 (v 0)
```

## Dependencies

- IsStrictlyDominant.isWeaklyDominant
- IsWeaklyDominant
- Vickrey
