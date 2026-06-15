---
id: integral-comp-eval-opponentProductPrior
title: integral_comp_eval_opponentProductPrior
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - integral_comp_eval_opponentProductPrior
uses:
  - OpponentTypeProfile
---

# integral_comp_eval_opponentProductPrior

## Lean type

```lean
theorem integral_comp_eval_opponentProductPrior [Fintype I] [DecidableEq I] (A : BayesianSingleItemAuction I) [∀ i : I, IsProbabilityMeasure (A.typeMeasure i)] {i : I} {j : {j // j ≠ i}} {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] {f : ℝ → E} (hf : AEStronglyMeasurable f (A.typeMeasure j)) : (∫ t : OpponentTypeProfile I i, f (t j) ∂A.opponentProductPrior i) = ∫ v, f v ∂A.typeMeasure j
```

## Dependencies

- OpponentTypeProfile
