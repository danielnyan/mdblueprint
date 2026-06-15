---
id: lam0-le-mu0
title: lam0_le_mu0
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Minimax.MinimaxLoomis
  declarations:
    - lam0_le_mu0
uses:
  - exists_xx_lam0
  - exists_yy_mu0
  - wsum_wsum_comm
  - ge_iff_simplex_ge
  - le_iff_simplex_le
---

# lam0_le_mu0

## Lean type

```lean
theorem lam0_le_mu0 (A : I → J → ℝ) : lam0 A ≤ mu0 A
```

## Dependencies

- exists_xx_lam0
- exists_yy_mu0
- wsum_wsum_comm
- ge_iff_simplex_ge
- le_iff_simplex_le
