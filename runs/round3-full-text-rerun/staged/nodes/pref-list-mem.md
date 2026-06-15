---
id: pref-list-mem
title: pref_list_mem
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.GaleShapley
  declarations:
    - pref_list_mem
uses:
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# pref_list_mem

## Lean type

```lean
lemma pref_list_mem {n : ℕ} (l : List (Fin n)) (hnd : l.Nodup) (hlen : l.length = n) (x : Fin n) : x ∈ l
```

## Dependencies

- IsPositiveAffineOf.symm
- Indifferent.symm
