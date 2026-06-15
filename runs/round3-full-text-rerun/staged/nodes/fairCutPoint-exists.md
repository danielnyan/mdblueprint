---
id: fairCutPoint-exists
title: fairCutPoint_exists
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Divisible.CutAndChoose
  declarations:
    - fairCutPoint_exists
uses:
  - IsFairCutPoint
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - cut_exists
---

# fairCutPoint_exists

## Lean type

```lean
theorem fairCutPoint_exists (μ : Fin 2 → Measure I) [IsFiniteMeasure (μ 0)] [NoAtoms (μ 0)] : ∃ t : I, IsFairCutPoint μ t
```

## Dependencies

- IsFairCutPoint
- IsPositiveAffineOf.symm
- Indifferent.symm
- cut_exists
