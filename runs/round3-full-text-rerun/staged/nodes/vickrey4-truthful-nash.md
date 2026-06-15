---
id: vickrey4-truthful-nash
title: vickrey4_truthful_nash
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.SimpleAuction
  declarations:
    - vickrey4_truthful_nash
uses:
  - IsNashEquilibrium
  - Vickrey
  - of_dominant
  - vickrey4_p0_dominant
  - vickrey4_p1_dominant
---

# vickrey4_truthful_nash

## Lean type

```lean
theorem vickrey4_truthful_nash : IsNashEquilibrium (Vickrey 4 v4) v4
```

## Dependencies

- IsNashEquilibrium
- Vickrey
- of_dominant
- vickrey4_p0_dominant
- vickrey4_p1_dominant
