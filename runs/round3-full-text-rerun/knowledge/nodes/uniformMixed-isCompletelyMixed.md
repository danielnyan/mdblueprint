---
id: uniformMixed-isCompletelyMixed
title: uniformMixed_isCompletelyMixed
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.MixedStrategy
  declarations:
    - uniformMixed_isCompletelyMixed
uses:
  - Strategy
  - IsCompletelyMixed
  - uniformMixed
  - uniformMixed_pos
---

# uniformMixed_isCompletelyMixed

## Lean type

```lean
theorem uniformMixed_isCompletelyMixed {G : StrategicGame N ℚ} {i : N} [Fintype (G.strategy i)] [Nonempty (G.strategy i)] : IsCompletelyMixed G (uniformMixed (G
```

## Dependencies

- Strategy
- IsCompletelyMixed
- uniformMixed
- uniformMixed_pos
