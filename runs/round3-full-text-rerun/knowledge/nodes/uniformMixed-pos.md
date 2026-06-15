---
id: uniformMixed-pos
title: uniformMixed_pos
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.MixedStrategy
  declarations:
    - uniformMixed_pos
uses:
  - Strategy
  - uniformMixed
  - uniformMixed_apply
---

# uniformMixed_pos

## Lean type

```lean
theorem uniformMixed_pos {G : StrategicGame N ℚ} {i : N} [Fintype (G.strategy i)] [Nonempty (G.strategy i)] (s : G.strategy i) : 0 < (uniformMixed (G
```

## Dependencies

- Strategy
- uniformMixed
- uniformMixed_apply
