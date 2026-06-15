---
id: holding-rank-mono-run
title: holding_rank_mono_run
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.GaleShapley
  declarations:
    - holding_rank_mono_run
uses:
  - holding_rank_mono_step
---

# holding_rank_mono_run

## Lean type

```lean
lemma holding_rank_mono_run (fuel : ℕ) (s : DAState n) (j : Fin n) {hval : Fin n} (hh : s.holding j = some hval) : ∃ h' : Fin n, (daRun w m fuel s).holding j = some h' ∧ (w.prefs j).idxOf h' ≤ (w.prefs j).idxOf hval
```

## Dependencies

- holding_rank_mono_step
