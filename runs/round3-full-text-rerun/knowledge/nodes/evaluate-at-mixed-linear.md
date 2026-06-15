---
id: evaluate-at-mixed-linear
title: evaluate_at_mixed_linear
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.Nash
  declarations:
    - evaluate_at_mixed_linear
uses:
  - MixedS
  - Strategy
  - evaluate_at_mixed
  - stdSimplex.pure
  - Lottery.pure
  - Profile.ext
  - stdSimplex.pure_apply
---

# evaluate_at_mixed_linear

## Lean type

```lean
lemma evaluate_at_mixed_linear (i : N) (σ : MixedS G) (τ : stdSimplex ℝ (G.strategy i)) : evaluate_at_mixed G i (update σ i τ) = ∑ a : G.strategy i, (τ.val a) * evaluate_at_mixed G i (update σ i (stdSimplex.pure a))
```

## Dependencies

- MixedS
- Strategy
- evaluate_at_mixed
- stdSimplex.pure
- Lottery.pure
- Profile.ext
- stdSimplex.pure_apply
