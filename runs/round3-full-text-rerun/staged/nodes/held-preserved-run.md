---
id: held-preserved-run
title: held_preserved_run
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.GaleShapley
  declarations:
    - held_preserved_run
uses:
  - holding_rank_mono_run
  - isFree
  - propTarget
---

# held_preserved_run

## Lean type

```lean
lemma held_preserved_run (fuel : ℕ) (s : DAState n) (j : Fin n) {hval : Fin n} (hh : s.holding j = some hval) : ∃ h', (daRun w m fuel s).holding j = some h'
```

## Dependencies

- holding_rank_mono_run
- isFree
- propTarget
