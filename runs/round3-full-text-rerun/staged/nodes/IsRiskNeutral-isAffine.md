---
id: IsRiskNeutral-isAffine
title: IsRiskNeutral.isAffine
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.Utility.Basic
  declarations:
    - IsRiskNeutral.isAffine
uses:
  - IsAffineUtility.isRiskNeutral
  - IsRiskNeutral
  - IsAffineUtility
  - stdSimplex.mix
  - Lottery.mix
  - Lottery
  - stdSimplex.pure
  - Lottery.pure
  - Lottery.expectedValue
  - Lottery.expectedValue_mix
  - Lottery.expectedValue_pure
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# IsRiskNeutral.isAffine

## Lean type

```lean
theorem IsRiskNeutral.isAffine {I : Type*} [Fintype I] [Nontrivial I] {u : 𝕜 → 𝕜} (h : IsRiskNeutral (I
```

## Dependencies

- IsAffineUtility.isRiskNeutral
- IsRiskNeutral
- IsAffineUtility
- stdSimplex.mix
- Lottery.mix
- Lottery
- stdSimplex.pure
- Lottery.pure
- Lottery.expectedValue
- Lottery.expectedValue_mix
- Lottery.expectedValue_pure
- IsPositiveAffineOf.symm
- Indifferent.symm
