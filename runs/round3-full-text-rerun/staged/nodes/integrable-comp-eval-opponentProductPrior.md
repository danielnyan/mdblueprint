---
id: integrable-comp-eval-opponentProductPrior
title: integrable_comp_eval_opponentProductPrior
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - integrable_comp_eval_opponentProductPrior
uses:
  - OpponentTypeProfile
---

# integrable_comp_eval_opponentProductPrior

## Lean type

```lean
theorem integrable_comp_eval_opponentProductPrior [Fintype I] [DecidableEq I] (A : BayesianSingleItemAuction I) [∀ i : I, IsProbabilityMeasure (A.typeMeasure i)] {i : I} {j : {j // j ≠ i}} {E : Type*} [NormedAddCommGroup E] {f : ℝ → E} (hf : Integrable f (A.typeMeasure j)) : Integrable (fun t : OpponentTypeProfile I i => f (t j)) (A.opponentProductPrior i)
```

## Dependencies

- OpponentTypeProfile
