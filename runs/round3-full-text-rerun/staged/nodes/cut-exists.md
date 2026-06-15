---
id: cut-exists
title: cut_exists
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Divisible.DubinsSpanier
  declarations:
    - cut_exists
uses:
  - Profile.ext
  - IsSingleItemAllocationRule.le_one
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - Allocation
  - IsEnvyFree.isProportional
  - IsProportional
  - MeasureValuation
  - IsPositiveAffineOf.trans
  - StrictlyPreferred.trans
  - Arena.Reachable.trans
  - Indifferent.trans
  - Subtree.trans
  - mem_iUnion
---

# cut_exists

## Lean type

```lean
lemma cut_exists (μ : Measure I) [IsFiniteMeasure μ] [NoAtoms μ] (c : ℝ) (hc_pos : 0 < c) (hc_lt : c < (μ Set.univ).toReal) : ∃ t : I, (μ (Set.Iic t)).toReal = c
```

## Dependencies

- Profile.ext
- IsSingleItemAllocationRule.le_one
- IsPositiveAffineOf.symm
- Indifferent.symm
- Allocation
- IsEnvyFree.isProportional
- IsProportional
- MeasureValuation
- IsPositiveAffineOf.trans
- StrictlyPreferred.trans
- Arena.Reachable.trans
- Indifferent.trans
- Subtree.trans
- mem_iUnion
