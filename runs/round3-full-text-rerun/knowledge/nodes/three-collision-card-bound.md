---
id: three-collision-card-bound
title: three_collision_card_bound
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - three_collision_card_bound
uses:
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - Profile.ext
  - IsPositiveAffineOf.trans
  - StrictlyPreferred.trans
  - Arena.Reachable.trans
  - Indifferent.trans
  - Subtree.trans
---

# three_collision_card_bound

## Lean type

```lean
lemma three_collision_card_bound [DecidableEq T] (σ : Finset T) (c : T → I) (a b z : T) (ha_in_σ : a ∈ σ) (hb_in_σ : b ∈ σ) (hz_in_σ : z ∈ σ) (hab_ne : a ≠ b) (haz_ne : a ≠ z) (hbz_ne : b ≠ z) (hc_eq : c a = c b) (hcz_eq : c b = c z) : σ.card ≥ (σ.image c).card + 2
```

## Dependencies

- IsPositiveAffineOf.symm
- Indifferent.symm
- Profile.ext
- IsPositiveAffineOf.trans
- StrictlyPreferred.trans
- Arena.Reachable.trans
- Indifferent.trans
- Subtree.trans
