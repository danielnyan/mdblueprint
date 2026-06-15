---
id: IsDSIC-truthful-isNash
title: IsDSIC.truthful_isNash
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.MechBasic
  declarations:
    - IsDSIC.truthful_isNash
uses:
  - IsDSIC
  - isDSIC
  - IsNashEquilibrium
  - toStrategicGame
  - of_dominant
---

# IsDSIC.truthful_isNash

## Lean type

```lean
theorem IsDSIC.truthful_isNash [Preorder U] (hdsic : M.IsDSIC u) (v : ∀ i, T i) : IsNashEquilibrium (M.toStrategicGame u v) v
```

## Dependencies

- IsDSIC
- isDSIC
- IsNashEquilibrium
- toStrategicGame
- of_dominant
