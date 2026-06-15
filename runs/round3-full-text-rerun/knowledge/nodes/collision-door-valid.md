---
id: collision-door-valid
title: collision_door_valid
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - collision_door_valid
uses:
  - isCell
  - Dominant_of_subset
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# collision_door_valid

## Lean type

```lean
lemma collision_door_valid [DecidableEq T] (σ : Finset T) (C : Finset I) (_ : T → I) (x : T) (h_cell : isCell σ C) (hx_in_σ : x ∈ σ) (h_card_eq : C.card = σ.card) : isDoorof (σ.erase x) C σ C
```

## Dependencies

- isCell
- Dominant_of_subset
- IsPositiveAffineOf.symm
- Indifferent.symm
