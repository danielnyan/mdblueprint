---
id: RegularMyersonICIRAnalyticAssumptions-candidate-allocation-survival-integrable
title: RegularMyersonICIRAnalyticAssumptions.candidate_allocation_survival_integrable
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - RegularMyersonICIRAnalyticAssumptions.candidate_allocation_survival_integrable
uses:
  - IsRegularMyersonOptimalICIRAuction.isFeasible
  - IsFeasible
  - IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
  - IsIncentiveCompatible
  - IsRegularMyersonOptimalICIRAuction.isIndividuallyRationalOnSupport
  - IsIndividuallyRationalOnSupport
  - hasIntervalIntegrableInterimAllocation_of_isIncentiveCompatible
---

# RegularMyersonICIRAnalyticAssumptions.candidate_allocation_survival_integrable

## Lean type

```lean
theorem RegularMyersonICIRAnalyticAssumptions.candidate_allocation_survival_integrable [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] {A : BayesianSingleItemAuction I} (h : A.RegularMyersonICIRAnalyticAssumptions) (B : BayesianSingleItemAuction I) (_hfeas : B.IsFeasible) (hIC : B.IsIncentiveCompatible) (_hIR : B.IsIndividuallyRationalOnSupport) : ∀ i : I, IntervalIntegrable (fun v => B.interimAllocProb i v * (1 - (A.typeData.cdf i).cdf v)) volume 0 (A.typeData.omega i)
```

## Dependencies

- IsRegularMyersonOptimalICIRAuction.isFeasible
- IsFeasible
- IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
- IsIncentiveCompatible
- IsRegularMyersonOptimalICIRAuction.isIndividuallyRationalOnSupport
- IsIndividuallyRationalOnSupport
- hasIntervalIntegrableInterimAllocation_of_isIncentiveCompatible
