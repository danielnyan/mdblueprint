---
id: integral-typeMeasure-eq-intervalIntegral-mul
title: integral_typeMeasure_eq_intervalIntegral_mul
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - integral_typeMeasure_eq_intervalIntegral_mul
uses:
  - integral_typeMeasure_eq_intervalIntegral_smul
  - OpponentTypeProfile
  - Profile.ext
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# integral_typeMeasure_eq_intervalIntegral_mul

## Lean type

```lean
theorem integral_typeMeasure_eq_intervalIntegral_mul (A : BayesianSingleItemAuction I) (i : I) (g : ℝ → ℝ) (hmeas : AEMeasurable (fun v => ENNReal.ofReal (A.typeDensity i v)) (volume.restrict (Set.Ioc 0 (A.typeData.omega i)))) (hnonneg : ∀ᵐ v ∂(volume.restrict (Set.Ioc 0 (A.typeData.omega i))), 0 ≤ A.typeDensity i v) : (∫ v, g v ∂A.typeMeasure i) = ∫ v in 0..A.typeData.omega i, g v * A.typeDensity i v
```

## Dependencies

- integral_typeMeasure_eq_intervalIntegral_smul
- OpponentTypeProfile
- Profile.ext
- IsPositiveAffineOf.symm
- Indifferent.symm
