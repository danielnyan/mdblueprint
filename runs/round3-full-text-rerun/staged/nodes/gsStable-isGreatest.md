---
id: gsStable-isGreatest
title: gsStable_isGreatest
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.Lattice
  declarations:
    - gsStable_isGreatest
uses:
  - StableMatching
  - gsStable_greatest
---

# gsStable_isGreatest

## Lean type

```lean
theorem gsStable_isGreatest [NeZero n] : IsGreatest (Set.univ : Set (StableMatching w m)) (gsStable w m)
```

## Dependencies

- StableMatching
- gsStable_greatest
