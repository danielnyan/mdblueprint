---
id: daStep-nc-held
title: daStep_nc_held
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.GaleShapley
  declarations:
    - daStep_nc_held
uses:
  - isFree
---

# daStep_nc_held

## Lean type

```lean
lemma daStep_nc_held {n : ℕ} {w m : Preferences n} {s : DAState n} {i : Fin n} (hi : isFree s i = false) : (daStep w m s).nextChoice i = s.nextChoice i
```

## Dependencies

- isFree
