---
id: vickrey4-p1-dominant
title: vickrey4_p1_dominant
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.SimpleAuction
  declarations:
    - vickrey4_p1_dominant
uses:
  - IsStrictlyDominant.isWeaklyDominant
  - IsWeaklyDominant
  - Vickrey
---

# vickrey4_p1_dominant

## Lean type

```lean
theorem vickrey4_p1_dominant : IsWeaklyDominant (Vickrey 4 v4) 1 (v4 1)
```

## Dependencies

- IsStrictlyDominant.isWeaklyDominant
- IsWeaklyDominant
- Vickrey
