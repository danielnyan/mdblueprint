---
id: IsZeroSum-tail-mem
title: IsZeroSum.tail_mem
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.Zermelo
  declarations:
    - IsZeroSum.tail_mem
uses:
  - IsZeroSum
---

# IsZeroSum.tail_mem

## Lean type

```lean
theorem IsZeroSum.tail_mem {m : Fin 2} {h : GameTree (Fin 2) ℚ} {t : List (GameTree (Fin 2) ℚ)} {c : GameTree (Fin 2) ℚ} (hzs : IsZeroSum (Node m h t)) (hmem : c ∈ t) : IsZeroSum c
```

## Dependencies

- IsZeroSum
