---
id: val-empty
title: val_empty
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Divisible.Valuation
  declarations:
    - val_empty
uses:
  - MeasureValuation
---

# val_empty

## Lean type

```lean
@[simp] lemma val_empty (i : N) : (MeasureValuation μ).val i ∅ = 0
```

## Dependencies

- MeasureValuation
