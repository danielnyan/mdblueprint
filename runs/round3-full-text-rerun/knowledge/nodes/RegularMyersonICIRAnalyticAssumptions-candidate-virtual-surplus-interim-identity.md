---
id: RegularMyersonICIRAnalyticAssumptions-candidate-virtual-surplus-interim-identity
title: RegularMyersonICIRAnalyticAssumptions.candidate_virtual_surplus_interim_identity
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - RegularMyersonICIRAnalyticAssumptions.candidate_virtual_surplus_interim_identity
uses:
  - HasSameSellingEnvironment
  - IsRegularMyersonOptimalICIRAuction.isFeasible
  - IsFeasible
  - IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
  - IsIncentiveCompatible
  - IsRegularMyersonOptimalICIRAuction.isIndividuallyRationalOnSupport
  - IsIndividuallyRationalOnSupport
  - InterimFubiniAnalyticAssumptions.hasExpectedVirtualSurplusInterimIdentity
  - HasExpectedVirtualSurplusInterimIdentity
  - RegularMyersonICIRAnalyticAssumptions.candidate_interim_fubini
---

# RegularMyersonICIRAnalyticAssumptions.candidate_virtual_surplus_interim_identity

## Lean type

```lean
theorem RegularMyersonICIRAnalyticAssumptions.candidate_virtual_surplus_interim_identity [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] {A B : BayesianSingleItemAuction I} (h : A.RegularMyersonICIRAnalyticAssumptions) (henv : A.HasSameSellingEnvironment B) (hfeas : B.IsFeasible) (hIC : B.IsIncentiveCompatible) (hIR : B.IsIndividuallyRationalOnSupport) : A.HasExpectedVirtualSurplusInterimIdentity B
```

## Dependencies

- HasSameSellingEnvironment
- IsRegularMyersonOptimalICIRAuction.isFeasible
- IsFeasible
- IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
- IsIncentiveCompatible
- IsRegularMyersonOptimalICIRAuction.isIndividuallyRationalOnSupport
- IsIndividuallyRationalOnSupport
- InterimFubiniAnalyticAssumptions.hasExpectedVirtualSurplusInterimIdentity
- HasExpectedVirtualSurplusInterimIdentity
- RegularMyersonICIRAnalyticAssumptions.candidate_interim_fubini
