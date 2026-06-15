---
id: lamB0-one
title: lamB0_one
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Minimax.Loomis
  declarations:
    - lamB0_one
uses:
---

# lamB0_one

## Lean type

```lean
theorem lamB0_one (A : I → J → ℝ) : lamB0 A (fun _ _ => 1) = MinimaxLoomis.lam0 A
```

## Dependencies

- none
