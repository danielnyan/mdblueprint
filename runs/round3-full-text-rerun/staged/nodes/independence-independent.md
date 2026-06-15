---
id: independence-independent
title: independence_independent
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.Utility.VNMAxioms
  declarations:
    - independence_independent
uses:
  - Lottery
  - Independence
  - Completeness
  - Transitivity
  - Continuity
  - colRatio.continuous
  - lamB.aux.continuous
  - rowRatio.continuous
  - lam.aux.continuous
  - muB.aux.continuous
  - mu.aux.continuous
---

# independence_independent

## Lean type

```lean
theorem independence_independent : ∃ pref : Lottery ℚ (Fin 3) → Lottery ℚ (Fin 3) → Prop, ¬ Independence pref ∧ Completeness pref ∧ Transitivity pref ∧ Continuity pref
```

## Dependencies

- Lottery
- Independence
- Completeness
- Transitivity
- Continuity
- colRatio.continuous
- lamB.aux.continuous
- rowRatio.continuous
- lam.aux.continuous
- muB.aux.continuous
- mu.aux.continuous
