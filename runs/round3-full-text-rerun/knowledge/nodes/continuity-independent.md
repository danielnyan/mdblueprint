---
id: continuity-independent
title: continuity_independent
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.Utility.VNMAxioms
  declarations:
    - continuity_independent
uses:
  - Lottery
  - Continuity
  - Completeness
  - Transitivity
  - Independence
  - stdSimplex.mix
  - Lottery.mix
  - colRatio.continuous
  - lamB.aux.continuous
  - rowRatio.continuous
  - lam.aux.continuous
  - muB.aux.continuous
  - mu.aux.continuous
---

# continuity_independent

## Lean type

```lean
theorem continuity_independent : ∃ pref : Lottery ℚ (Fin 3) → Lottery ℚ (Fin 3) → Prop, ¬ Continuity pref ∧ Completeness pref ∧ Transitivity pref ∧ Independence pref
```

## Dependencies

- Lottery
- Continuity
- Completeness
- Transitivity
- Independence
- stdSimplex.mix
- Lottery.mix
- colRatio.continuous
- lamB.aux.continuous
- rowRatio.continuous
- lam.aux.continuous
- muB.aux.continuous
- mu.aux.continuous
