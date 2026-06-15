---
id: mem-freeMenSet
title: mem_freeMenSet
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.GaleShapley
  declarations:
    - mem_freeMenSet
uses:
  - freeMenSet
  - isFree
---

# mem_freeMenSet

## Lean type

```lean
lemma mem_freeMenSet {n : ℕ} {s : DAState n} {i : Fin n} : i ∈ freeMenSet s ↔ isFree s i = true
```

## Dependencies

- freeMenSet
- isFree
