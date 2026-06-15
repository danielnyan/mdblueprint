---
id: cdfRealContinuous
title: cdfRealContinuous
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Divisible.UnitInterval
  declarations:
    - cdfRealContinuous
uses:
  - colRatio.continuous
  - lamB.aux.continuous
  - rowRatio.continuous
  - lam.aux.continuous
  - muB.aux.continuous
  - mu.aux.continuous
  - Profile.ext
---

# cdfRealContinuous

## Lean type

```lean
lemma cdfRealContinuous (ν : Measure ℝ) [IsFiniteMeasure ν] [NoAtoms ν] : Continuous (fun t : ℝ => (ν (Set.Iic t)).toReal)
```

## Dependencies

- colRatio.continuous
- lamB.aux.continuous
- rowRatio.continuous
- lam.aux.continuous
- muB.aux.continuous
- mu.aux.continuous
- Profile.ext
