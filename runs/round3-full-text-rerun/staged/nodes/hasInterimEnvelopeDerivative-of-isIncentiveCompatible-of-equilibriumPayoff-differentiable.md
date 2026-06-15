---
id: hasInterimEnvelopeDerivative-of-isIncentiveCompatible-of-equilibriumPayoff-differentiable
title: hasInterimEnvelopeDerivative_of_isIncentiveCompatible_of_equilibriumPayoff_differentiable
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - hasInterimEnvelopeDerivative_of_isIncentiveCompatible_of_equilibriumPayoff_differentiable
uses:
  - IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
  - IsIncentiveCompatible
  - HasInterimEnvelopeDerivative
  - deriv_equilibriumPayoff_eq_interimAllocProb_of_isIncentiveCompatible
---

# hasInterimEnvelopeDerivative_of_isIncentiveCompatible_of_equilibriumPayoff_differentiable

## Lean type

```lean
theorem hasInterimEnvelopeDerivative_of_isIncentiveCompatible_of_equilibriumPayoff_differentiable (A : BayesianSingleItemAuction I) (hIC : A.IsIncentiveCompatible) (hdiff : ∀ (i : I) (v_i : ℝ), DifferentiableAt ℝ (A.equilibriumPayoff i) v_i) : A.HasInterimEnvelopeDerivative
```

## Dependencies

- IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
- IsIncentiveCompatible
- HasInterimEnvelopeDerivative
- deriv_equilibriumPayoff_eq_interimAllocProb_of_isIncentiveCompatible
