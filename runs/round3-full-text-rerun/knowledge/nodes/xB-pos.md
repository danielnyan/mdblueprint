---
id: xB-pos
title: xB_pos
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Minimax.Loomis
  declarations:
    - xB_pos
uses:
  - IsPositive
  - wsum_pos
---

# xB_pos

## Lean type

```lean
theorem xB_pos {B : I → J → ℝ} (hB : IsPositive B) (x : stdSimplex ℝ I) (j : J) : 0 < xB B x j
```

## Dependencies

- IsPositive
- wsum_pos
