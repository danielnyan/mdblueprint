---
id: integral-typeMeasure-eq-intervalIntegral-smul
title: integral_typeMeasure_eq_intervalIntegral_smul
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - integral_typeMeasure_eq_intervalIntegral_smul
uses:
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# integral_typeMeasure_eq_intervalIntegral_smul

## Lean type

```lean
theorem integral_typeMeasure_eq_intervalIntegral_smul (A : BayesianSingleItemAuction I) (i : I) {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] (g : ℝ → E) (hmeas : AEMeasurable (fun v => ENNReal.ofReal (A.typeDensity i v)) (volume.restrict (Set.Ioc 0 (A.typeData.omega i)))) (hnonneg : ∀ᵐ v ∂(volume.restrict (Set.Ioc 0 (A.typeData.omega i))), 0 ≤ A.typeDensity i v) : (∫ v, g v ∂A.typeMeasure i) = ∫ v in 0..A.typeData.omega i, A.typeDensity i v • g v
```

## Dependencies

- IsPositiveAffineOf.symm
- Indifferent.symm
