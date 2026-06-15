---
id: size-bound-out
title: size_bound_out
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Brouwer
  declarations:
    - size_bound_out
uses:
  - TT
  - isDominant
  - size_bound_key
  - IsPositiveAffineOf.trans
  - StrictlyPreferred.trans
  - Arena.Reachable.trans
  - Indifferent.trans
  - Subtree.trans
  - Brouwer
  - isEmpty
---

# size_bound_out

## Lean type

```lean
theorem size_bound_out (σ : Finset (TT n l)) (C : Finset (Fin n)) (h : TT.ILO.isDominant σ C): ∀ x ∈ σ, ∀ i ∉ C, (x i : ℤ) < n + 1
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
- Brouwer
- isEmpty
