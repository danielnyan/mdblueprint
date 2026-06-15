---
id: size-bound-key
title: size_bound_key
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Brouwer
  declarations:
    - size_bound_key
uses:
  - TT
  - isDominant
  - TT.Ilt_keyprop
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# size_bound_key

## Lean type

```lean
lemma size_bound_key (σ : Finset (TT n l)) (C : Finset (Fin n)) (h : TT.ILO.isDominant σ C) (h2 : σ.Nonempty): l < ∑ k ∈ C, (σ.image (fun x => (x k : ℕ))).min' (h2.image _) + C.card
```

## Dependencies

- TT
- isDominant
- TT.Ilt_keyprop
- IsPositiveAffineOf.symm
- Indifferent.symm
