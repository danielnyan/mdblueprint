---
id: muB0-one
title: muB0_one
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Minimax.Loomis
  declarations:
    - muB0_one
uses:
---

# muB0_one

## Lean type

```lean
theorem muB0_one (A : I → J → ℝ) : muB0 A (fun _ _ => 1) = MinimaxLoomis.mu0 A
```

## Dependencies

- none
