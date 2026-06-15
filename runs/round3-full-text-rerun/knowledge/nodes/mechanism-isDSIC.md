---
id: mechanism-isDSIC
title: mechanism_isDSIC
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Vickrey
  declarations:
    - mechanism_isDSIC
uses:
  - IsDSIC
  - isDSIC
  - truthful_weakly_dominant
  - game_eq_toStrategicGame
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - IsDSIC
  - isDSIC
  - truthful_weakly_dominant
  - game_eq_toStrategicGame
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# mechanism_isDSIC

## Lean type

```lean
theorem mechanism_isDSIC : mechanism.isDSIC (fun (w : I) (pay : I → U) (vals : I → U) (i : I) => if i = w then vals i - pay i else 0)
```

## Dependencies

- IsDSIC
- isDSIC
- truthful_weakly_dominant
- game_eq_toStrategicGame
- IsPositiveAffineOf.symm
- Indifferent.symm
- IsDSIC
- isDSIC
- truthful_weakly_dominant
- game_eq_toStrategicGame
- IsPositiveAffineOf.symm
- Indifferent.symm
