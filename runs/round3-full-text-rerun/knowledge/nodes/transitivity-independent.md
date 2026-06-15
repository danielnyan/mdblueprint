---
id: transitivity-independent
title: transitivity_independent
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.Utility.VNMAxioms
  declarations:
    - transitivity_independent
uses:
  - Lottery
  - Transitivity
  - Completeness
  - Independence
  - Continuity
  - colRatio.continuous
  - lamB.aux.continuous
  - rowRatio.continuous
  - lam.aux.continuous
  - muB.aux.continuous
  - mu.aux.continuous
  - stdSimplex.mix
  - Lottery.mix
---

# transitivity_independent

## Lean type

```lean
theorem transitivity_independent : ∃ pref : Lottery ℚ (Fin 3) → Lottery ℚ (Fin 3) → Prop, ¬ Transitivity pref ∧ Completeness pref ∧ Independence pref ∧ Continuity pref
```

## Dependencies

- Lottery
- Transitivity
- Completeness
- Independence
- Continuity
- colRatio.continuous
- lamB.aux.continuous
- rowRatio.continuous
- lam.aux.continuous
- muB.aux.continuous
- mu.aux.continuous
- stdSimplex.mix
- Lottery.mix
