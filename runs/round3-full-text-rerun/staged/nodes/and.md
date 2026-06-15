---
id: and
title: and
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.MatrixGame
  declarations:
    - and
uses:
  - Continuity
---

# and

## Lean type

```lean
theorem and are proved by aliasing the simplified-Loomis development in [`MinimaxLoomis`](MinimaxLoomis.lean). The Loomis proof uses ℝ-specific compactness / continuity, so the theorems are pinned to ℝ even though their statements (via `maximin` / `minimax` above) make sense over any order-complete linearly ordered field. -/ section LayerThree variable (A : MatrixGame I J ℝ) /-- Maximin ≤ minimax (always holds, for any matrix game). This is the finite weak-duality inequality. -/
```

## Dependencies

- Continuity
