---
id: mixedNashEquilibrium
title: mixedNashEquilibrium
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.Nash
  declarations:
    - mixedNashEquilibrium
uses:
  - Strategy
  - MixedS
  - evaluate_at_mixed
---

# mixedNashEquilibrium

## Lean type

```lean
def mixedNashEquilibrium (G : StrategicGame N ℝ) [Fintype N] [∀ i, Fintype (G.strategy i)] : MixedS G → Prop
```

## Dependencies

- Strategy
- MixedS
- evaluate_at_mixed
