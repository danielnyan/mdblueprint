---
id: RandomizedSubmodularWelfareAlgorithm-IsPolynomial
title: RandomizedSubmodularWelfareAlgorithm.IsPolynomial
kind: theorem
status: staged
lean:
  module: EconCSLib.OpenProblem.SubmodularWelfareDemandOracle
  declarations:
    - RandomizedSubmodularWelfareAlgorithm.IsPolynomial
uses:
  - BundlePartitionAllocation
  - PolynomialTimeInAgentsItems
  - PolynomialBundleOracleQueryBound
  - Profile
  - Valuation
---

# RandomizedSubmodularWelfareAlgorithm.IsPolynomial

## Lean type

```lean
def RandomizedSubmodularWelfareAlgorithm.IsPolynomial {I Ω G : Type*} [Fintype I] [Fintype Ω] [DecidableEq G] {M : Finset G} [Fintype (BundlePartitionAllocation I M)] [Nonempty (BundlePartitionAllocation I M)] (_alg : RandomizedSubmodularWelfareAlgorithm I Ω M) : Prop
```

## Dependencies

- BundlePartitionAllocation
- PolynomialTimeInAgentsItems
- PolynomialBundleOracleQueryBound
- Profile
- Valuation
