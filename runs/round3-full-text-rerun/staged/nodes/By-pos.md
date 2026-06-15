---
id: By-pos
title: By_pos
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Minimax.Loomis
  declarations:
    - By_pos
uses:
  - IsPositive
  - wsum_pos
---

# By_pos

## Lean type

```lean
theorem By_pos {B : I → J → ℝ} (hB : IsPositive B) (y : stdSimplex ℝ J) (i : I) : 0 < By B y i
```

## Dependencies

- IsPositive
- wsum_pos
