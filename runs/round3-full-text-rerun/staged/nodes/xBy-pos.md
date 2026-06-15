---
id: xBy-pos
title: xBy_pos
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Minimax.Loomis
  declarations:
    - xBy_pos
uses:
  - IsPositive
  - wsum_pos
  - By_pos
---

# xBy_pos

## Lean type

```lean
theorem xBy_pos {B : I → J → ℝ} (hB : IsPositive B) (x : stdSimplex ℝ I) (y : stdSimplex ℝ J) : 0 < wsum x (fun i => By B y i)
```

## Dependencies

- IsPositive
- wsum_pos
- By_pos
