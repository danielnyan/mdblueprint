---
id: truthful-weakly-dominant-p1
title: truthful_weakly_dominant_p1
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.SimpleAuction
  declarations:
    - truthful_weakly_dominant_p1
uses:
  - IsStrictlyDominant.isWeaklyDominant
  - IsWeaklyDominant
  - Vickrey
  - Strategy
---

# truthful_weakly_dominant_p1

## Lean type

```lean
theorem truthful_weakly_dominant_p1 (v : Fin 2 → Fin n) : IsWeaklyDominant (Vickrey n v) 1 (v 1)
```

## Dependencies

- IsStrictlyDominant.isWeaklyDominant
- IsWeaklyDominant
- Vickrey
- Strategy
