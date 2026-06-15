---
id: VNM-axioms-independent
title: VNM.axioms_independent
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.Utility.VNMAxioms
  declarations:
    - VNM.axioms_independent
uses:
  - Lottery
  - Completeness
  - Transitivity
  - Independence
  - Continuity
  - completeness_independent
  - transitivity_independent
  - independence_independent
  - continuity_independent
---

# VNM.axioms_independent

## Lean type

```lean
theorem VNM.axioms_independent : -- ¬Complete (∃ pref : Lottery ℚ (Fin 3) → Lottery ℚ (Fin 3) → Prop, ¬ Completeness pref ∧ Transitivity pref ∧ Independence pref ∧ Continuity pref) ∧ -- ¬Transitive (∃ pref : Lottery ℚ (Fin 3) → Lottery ℚ (Fin 3) → Prop, ¬ Transitivity pref ∧ Completeness pref ∧ Independence pref ∧ Continuity pref) ∧ -- ¬Independent (∃ pref : Lottery ℚ (Fin 3) → Lottery ℚ (Fin 3) → Prop, ¬ Independence pref ∧ Completeness pref ∧ Transitivity pref ∧ Continuity pref) ∧ -- ¬Continuous (∃ pref : Lottery ℚ (Fin 3) → Lottery ℚ (Fin 3) → Prop, ¬ Continuity pref ∧ Completeness pref ∧ Transitivity pref ∧ Independence pref)
```

## Dependencies

- Lottery
- Completeness
- Transitivity
- Independence
- Continuity
- completeness_independent
- transitivity_independent
- independence_independent
- continuity_independent
