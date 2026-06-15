---
id: StrictlyDominates-weakly
title: StrictlyDominates.weakly
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.Dominance
  declarations:
    - StrictlyDominates.weakly
uses:
  - Strategy
  - StrictlyDominates
  - WeaklyDominates
---

# StrictlyDominates.weakly

## Lean type

```lean
theorem StrictlyDominates.weakly {G : StrategicGame N U} {i : N} {s s' : G.strategy i} (h : StrictlyDominates G i s s') : WeaklyDominates G i s s'
```

## Dependencies

- Strategy
- StrictlyDominates
- WeaklyDominates
