---
id: holding-rank-mono-step
title: holding_rank_mono_step
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.GaleShapley
  declarations:
    - holding_rank_mono_step
uses:
  - isFree
  - propTarget
---

# holding_rank_mono_step

## Lean type

```lean
lemma holding_rank_mono_step (s : DAState n) (j : Fin n) {hval : Fin n} (hh : s.holding j = some hval) : ∃ h' : Fin n, (daStep w m s).holding j = some h' ∧ (w.prefs j).idxOf h' ≤ (w.prefs j).idxOf hval
```

## Dependencies

- isFree
- propTarget
