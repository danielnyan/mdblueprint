---
id: isEnvyFree-iff-toCardinalInstance-isEnvyFree
title: isEnvyFree_iff_toCardinalInstance_isEnvyFree
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Divisible.Instance
  declarations:
    - isEnvyFree_iff_toCardinalInstance_isEnvyFree
uses:
  - Allocation
  - IsEnvyFree
---

# isEnvyFree_iff_toCardinalInstance_isEnvyFree

## Lean type

```lean
theorem isEnvyFree_iff_toCardinalInstance_isEnvyFree {N Ω : Type*} [MeasurableSpace Ω] [Fintype N] (I : MeasureInstance N Ω) [∀ i, IsFiniteMeasure (I.measure i)] (A : Allocation N Ω) : I.IsEnvyFree A ↔ I.toCardinalInstance.IsEnvyFree A
```

## Dependencies

- Allocation
- IsEnvyFree
