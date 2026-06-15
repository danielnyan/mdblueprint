---
id: uniformMixed-apply
title: uniformMixed_apply
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.MixedStrategy
  declarations:
    - uniformMixed_apply
uses:
  - Strategy
  - uniformMixed
---

# uniformMixed_apply

## Lean type

```lean
theorem uniformMixed_apply {G : StrategicGame N ℚ} {i : N} [Fintype (G.strategy i)] [Nonempty (G.strategy i)] (s : G.strategy i) : (uniformMixed (G
```

## Dependencies

- Strategy
- uniformMixed
