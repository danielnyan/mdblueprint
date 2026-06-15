---
id: lamB0-le-muB0
title: lamB0_le_muB0
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Minimax.Loomis
  declarations:
    - lamB0_le_muB0
uses:
  - IsPositive
  - exists_xx_lamB0
  - exists_yy_muB0
  - xBy_pos
  - wsum_wsum_comm
  - wsum_le_wsum
  - IsPositiveAffineOf.trans
  - StrictlyPreferred.trans
  - Arena.Reachable.trans
  - Indifferent.trans
  - Subtree.trans
---

# lamB0_le_muB0

## Lean type

```lean
theorem lamB0_le_muB0 (A B : I → J → ℝ) (hB : IsPositive B) : lamB0 A B ≤ muB0 A B
```

## Dependencies

- IsPositive
- exists_xx_lamB0
- exists_yy_muB0
- xBy_pos
- wsum_wsum_comm
- wsum_le_wsum
- IsPositiveAffineOf.trans
- StrictlyPreferred.trans
- Arena.Reachable.trans
- Indifferent.trans
- Subtree.trans
