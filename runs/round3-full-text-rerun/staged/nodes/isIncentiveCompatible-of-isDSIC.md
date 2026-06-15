---
id: isIncentiveCompatible-of-isDSIC
title: isIncentiveCompatible_of_isDSIC
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - isIncentiveCompatible_of_isDSIC
uses:
  - HasIntegrableInterimObjects
  - IsDSIC
  - isDSIC
  - IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
  - IsIncentiveCompatible
  - integral_interimQuasiLinearUtilityIntegrand_eq
  - integrable_interimQuasiLinearUtilityIntegrand
  - interimQuasiLinearUtilityIntegrand_le_of_isDSIC
---

# isIncentiveCompatible_of_isDSIC

## Lean type

```lean
theorem isIncentiveCompatible_of_isDSIC [DecidableEq I] (A : BayesianSingleItemAuction I) (hint : A.HasIntegrableInterimObjects) (hdsic : A.IsDSIC) : A.IsIncentiveCompatible
```

## Dependencies

- HasIntegrableInterimObjects
- IsDSIC
- isDSIC
- IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
- IsIncentiveCompatible
- integral_interimQuasiLinearUtilityIntegrand_eq
- integrable_interimQuasiLinearUtilityIntegrand
- interimQuasiLinearUtilityIntegrand_le_of_isDSIC
