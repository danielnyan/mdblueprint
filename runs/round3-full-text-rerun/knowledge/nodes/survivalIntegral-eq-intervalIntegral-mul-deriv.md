---
id: survivalIntegral-eq-intervalIntegral-mul-deriv
title: survivalIntegral_eq_intervalIntegral_mul_deriv
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - survivalIntegral_eq_intervalIntegral_mul_deriv
uses:
  - IsPositiveAffineOf.trans
  - StrictlyPreferred.trans
  - Arena.Reachable.trans
  - Indifferent.trans
  - Subtree.trans
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - HasPositiveDensityOnSupport
---

# survivalIntegral_eq_intervalIntegral_mul_deriv

## Lean type

```lean
theorem survivalIntegral_eq_intervalIntegral_mul_deriv {F Q : ℝ → ℝ} {ω : ℝ} (hω : 0 ≤ ω) (hF : AbsolutelyContinuousOnInterval F 0 ω) (hF0 : F 0 = 0) (hFω : F ω = 1) (hQ : IntervalIntegrable Q volume 0 ω) : (∫ v in 0..ω, Q v * (1 - F v)) = ∫ v in 0..ω, (∫ z in 0..v, Q z) * deriv F v
```

## Dependencies

- IsPositiveAffineOf.trans
- StrictlyPreferred.trans
- Arena.Reachable.trans
- Indifferent.trans
- Subtree.trans
- IsPositiveAffineOf.symm
- Indifferent.symm
- HasPositiveDensityOnSupport
