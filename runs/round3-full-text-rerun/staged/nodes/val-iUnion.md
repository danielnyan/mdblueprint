---
id: val-iUnion
title: val_iUnion
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Divisible.Valuation
  declarations:
    - val_iUnion
uses:
  - Allocation
  - MeasureValuation
---

# val_iUnion

## Lean type

```lean
lemma val_iUnion [Countable N] (i : N) (A : Allocation N Ω) (hdisj : ∀ j k : N, j ≠ k → Disjoint (A j) (A k)) (hmeas : ∀ j, MeasurableSet (A j)) : (MeasureValuation μ).val i (⋃ j, A j) = ∑' j, (MeasureValuation μ).val i (A j)
```

## Dependencies

- Allocation
- MeasureValuation
