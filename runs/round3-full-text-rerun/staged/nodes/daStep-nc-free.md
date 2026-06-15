---
id: daStep-nc-free
title: daStep_nc_free
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.GaleShapley
  declarations:
    - daStep_nc_free
uses:
  - isFree
---

# daStep_nc_free

## Lean type

```lean
lemma daStep_nc_free {n : ℕ} {w m : Preferences n} {s : DAState n} {i : Fin n} (hi : isFree s i = true) : (daStep w m s).nextChoice i = s.nextChoice i + 1
```

## Dependencies

- isFree
