---
id: IsAffineUtility-isRiskNeutral
title: IsAffineUtility.isRiskNeutral
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.Utility.Basic
  declarations:
    - IsAffineUtility.isRiskNeutral
uses:
  - IsAffineUtility
  - IsRiskNeutral
  - wsum_add
  - wsum_smul
  - wsum_const
---

# IsAffineUtility.isRiskNeutral

## Lean type

```lean
theorem IsAffineUtility.isRiskNeutral {I : Type*} [Fintype I] {u : 𝕜 → 𝕜} (h : IsAffineUtility u) : IsRiskNeutral (I
```

## Dependencies

- IsAffineUtility
- IsRiskNeutral
- wsum_add
- wsum_smul
- wsum_const
