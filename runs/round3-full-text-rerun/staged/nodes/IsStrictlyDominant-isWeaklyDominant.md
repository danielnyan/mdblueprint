---
id: IsStrictlyDominant-isWeaklyDominant
title: IsStrictlyDominant.isWeaklyDominant
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.Dominance
  declarations:
    - IsStrictlyDominant.isWeaklyDominant
uses:
  - Strategy
  - IsStrictlyDominant
  - IsWeaklyDominant
  - StrictlyDominates.weakly
---

# IsStrictlyDominant.isWeaklyDominant

## Lean type

```lean
theorem IsStrictlyDominant.isWeaklyDominant {G : StrategicGame N U} {i : N} {s : G.strategy i} [DecidableEq (G.strategy i)] (h : IsStrictlyDominant G i s) : IsWeaklyDominant G i s
```

## Dependencies

- Strategy
- IsStrictlyDominant
- IsWeaklyDominant
- StrictlyDominates.weakly
