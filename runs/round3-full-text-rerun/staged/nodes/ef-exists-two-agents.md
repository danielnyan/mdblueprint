---
id: ef-exists-two-agents
title: ef_exists_two_agents
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Divisible.EnvyFree
  declarations:
    - ef_exists_two_agents
uses:
  - Allocation
  - IsEnvyFree
  - MeasureValuation
  - cutAndChoose_ef_exists
---

# ef_exists_two_agents

## Lean type

```lean
theorem ef_exists_two_agents (μ : Fin 2 → Measure I) [IsFiniteMeasure (μ 0)] [IsFiniteMeasure (μ 1)] [NoAtoms (μ 0)] : ∃ A : Allocation (Fin 2) I, IsAllocation A ∧ IsEnvyFree (MeasureValuation μ) A
```

## Dependencies

- Allocation
- IsEnvyFree
- MeasureValuation
- cutAndChoose_ef_exists
