---
id: measurePreserving-profileSplitMeasurableEquiv-productPrior
title: measurePreserving_profileSplitMeasurableEquiv_productPrior
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - measurePreserving_profileSplitMeasurableEquiv_productPrior
uses:
  - Profile.ext
  - IsPositiveAffineOf.trans
  - StrictlyPreferred.trans
  - Arena.Reachable.trans
  - Indifferent.trans
  - Subtree.trans
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - IsPositiveAffineOf.refl
  - Indifferent.refl
  - IVariant.refl
  - OpponentTypeProfile
---

# measurePreserving_profileSplitMeasurableEquiv_productPrior

## Lean type

```lean
theorem measurePreserving_profileSplitMeasurableEquiv_productPrior [Fintype I] [DecidableEq I] (A : BayesianSingleItemAuction I) [∀ i : I, IsProbabilityMeasure (A.typeMeasure i)] (i : I) : MeasurePreserving (profileSplitMeasurableEquiv i) A.productPrior ((A.typeMeasure i).prod (A.opponentProductPrior i))
```

## Dependencies

- Profile.ext
- IsPositiveAffineOf.trans
- StrictlyPreferred.trans
- Arena.Reachable.trans
- Indifferent.trans
- Subtree.trans
- IsPositiveAffineOf.symm
- Indifferent.symm
- IsPositiveAffineOf.refl
- Indifferent.refl
- IVariant.refl
- OpponentTypeProfile
