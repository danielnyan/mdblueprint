---
id: gs-partner-isAchievable
title: gs_partner_isAchievable
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.Optimal
  declarations:
    - gs_partner_isAchievable
uses:
  - IsAchievable
  - gs_bijective
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - galeShapley_isStable
---

# gs_partner_isAchievable

## Lean type

```lean
lemma gs_partner_isAchievable (j : Fin n) : IsAchievable w m j ((Equiv.ofBijective (gs w m) (gs_bijective w m)).symm j)
```

## Dependencies

- IsAchievable
- gs_bijective
- IsPositiveAffineOf.symm
- Indifferent.symm
- galeShapley_isStable
