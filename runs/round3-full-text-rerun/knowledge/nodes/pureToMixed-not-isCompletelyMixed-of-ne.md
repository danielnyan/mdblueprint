---
id: pureToMixed-not-isCompletelyMixed-of-ne
title: pureToMixed_not_isCompletelyMixed_of_ne
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.MixedStrategy
  declarations:
    - pureToMixed_not_isCompletelyMixed_of_ne
uses:
  - Strategy
  - IsCompletelyMixed
  - pureToMixed
---

# pureToMixed_not_isCompletelyMixed_of_ne

## Lean type

```lean
theorem pureToMixed_not_isCompletelyMixed_of_ne {G : StrategicGame N ℚ} {i : N} [Fintype (G.strategy i)] [DecidableEq (G.strategy i)] {s₀ s₁ : G.strategy i} (h : s₁ ≠ s₀) : ¬ IsCompletelyMixed G (pureToMixed (G
```

## Dependencies

- Strategy
- IsCompletelyMixed
- pureToMixed
