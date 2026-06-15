---
id: Survives
title: Survives
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.IESDS
  declarations:
    - Survives
uses:
  - Strategy
  - IsNashEquilibrium.survives
  - Profile
---

# Survives

## Lean type

```lean
def Survives (G : StrategicGame N U) : ℕ → (i : N) → G.strategy i → Prop | 0 => fun _ _ => True | n + 1 => fun i s => G.Survives n i s ∧ ¬ ∃ t : G.strategy i, G.Survives n i t ∧ ∀ σ : G.Profile, (∀ j, G.Survives n j (σ j)) → G.payoff (deviate σ i s) i < G.payoff (deviate σ i t) i /-- Survival at round n+1 implies survival at round n. -/
```

## Dependencies

- Strategy
- IsNashEquilibrium.survives
- Profile
