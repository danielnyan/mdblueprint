---
id: size-bound-in
title: size_bound_in
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Brouwer
  declarations:
    - size_bound_in
uses:
  - TT
  - isDominant
  - size_bound_key
  - IsPositiveAffineOf.trans
  - StrictlyPreferred.trans
  - Arena.Reachable.trans
  - Indifferent.trans
  - Subtree.trans
---

# size_bound_in

## Lean type

```lean
theorem size_bound_in (σ : Finset (TT n l)) (C : Finset (Fin n)) (h : TT.ILO.isDominant σ C): ∀ x ∈ σ, ∀ y ∈ σ, ∀ i : Fin n, abs ((x i : ℤ) - (y i : ℤ)) < 2 * (n + 1)
```

## Dependencies

- TT
- isDominant
- size_bound_key
- IsPositiveAffineOf.trans
- StrictlyPreferred.trans
- Arena.Reachable.trans
- Indifferent.trans
- Subtree.trans
