---
id: completeness-independent
title: completeness_independent
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.Utility.VNMAxioms
  declarations:
    - completeness_independent
uses:
  - Lottery
  - Completeness
  - Transitivity
  - Independence
  - Continuity
  - colRatio.continuous
  - lamB.aux.continuous
  - rowRatio.continuous
  - lam.aux.continuous
  - muB.aux.continuous
  - mu.aux.continuous
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - stdSimplex.mix
  - Lottery.mix
  - stdSimplex.pure
  - Lottery.pure
---

# completeness_independent

## Lean type

```lean
theorem completeness_independent : ∃ pref : Lottery ℚ (Fin 3) → Lottery ℚ (Fin 3) → Prop, ¬ Completeness pref ∧ Transitivity pref ∧ Independence pref ∧ Continuity pref
```

## Dependencies

- Lottery
- Completeness
- Transitivity
- Independence
- Continuity
- colRatio.continuous
- lamB.aux.continuous
- rowRatio.continuous
- lam.aux.continuous
- muB.aux.continuous
- mu.aux.continuous
- IsPositiveAffineOf.symm
- Indifferent.symm
- stdSimplex.mix
- Lottery.mix
- stdSimplex.pure
- Lottery.pure
