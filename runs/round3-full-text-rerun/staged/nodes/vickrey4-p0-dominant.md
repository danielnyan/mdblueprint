---
id: vickrey4-p0-dominant
title: vickrey4_p0_dominant
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.SimpleAuction
  declarations:
    - vickrey4_p0_dominant
uses:
  - IsStrictlyDominant.isWeaklyDominant
  - IsWeaklyDominant
  - Vickrey
---

# vickrey4_p0_dominant

## Lean type

```lean
theorem vickrey4_p0_dominant : IsWeaklyDominant (Vickrey 4 v4) 0 (v4 0)
```

## Dependencies

- IsStrictlyDominant.isWeaklyDominant
- IsWeaklyDominant
- Vickrey
