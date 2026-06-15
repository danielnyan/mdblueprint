---
id: val-union
title: val_union
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Divisible.Valuation
  declarations:
    - val_union
uses:
  - MeasureValuation
---

# val_union

## Lean type

```lean
lemma val_union (i : N) (S T : Set Ω) (hdisj : Disjoint S T) (ht : MeasurableSet T) : (MeasureValuation μ).val i (S ∪ T) = (MeasureValuation μ).val i S + (MeasureValuation μ).val i T
```

## Dependencies

- MeasureValuation
