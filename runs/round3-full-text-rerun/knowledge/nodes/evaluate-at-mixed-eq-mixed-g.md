---
id: evaluate-at-mixed-eq-mixed-g
title: evaluate_at_mixed_eq_mixed_g
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.Nash
  declarations:
    - evaluate_at_mixed_eq_mixed_g
uses:
  - MixedS
  - evaluate_at_mixed
  - mixed_g
---

# evaluate_at_mixed_eq_mixed_g

## Lean type

```lean
theorem evaluate_at_mixed_eq_mixed_g (i : N) (σ : MixedS G) : evaluate_at_mixed G i σ = mixed_g G i (fun j => (σ j).val)
```

## Dependencies

- MixedS
- evaluate_at_mixed
- mixed_g
