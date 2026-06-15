---
id: propTarget-lt
title: propTarget_lt
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.GaleShapley
  declarations:
    - propTarget_lt
uses:
  - propTarget
  - isFree
---

# propTarget_lt

## Lean type

```lean
lemma propTarget_lt {n : ℕ} (m : Preferences n) (i : Fin n) {k : ℕ} (hk : k < n) : ∃ j, propTarget m i k = some j
```

## Dependencies

- propTarget
- isFree
