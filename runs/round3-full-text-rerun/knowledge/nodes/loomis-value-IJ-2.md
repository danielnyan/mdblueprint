---
id: loomis-value-IJ-2
title: loomis_value_IJ_2
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Minimax.Loomis
  declarations:
    - loomis_value_IJ_2
uses:
  - IsPositive
  - singleton_of_card_one
  - stdSimplex.mix
  - Lottery.mix
  - wsum_mix
  - lamB.aux_gt_iff_gt
  - lam.aux_gt_iff_gt
  - xB_pos
  - muB.aux_lt_iff_lt
  - mu.aux_lt_iff_lt
  - By_pos
  - wsum_extendDropColumn
  - wsum_extendDropRow
  - lamB0_le_muB0
  - exists_xx_lamB0
  - exists_yy_muB0
  - xBy_pos
  - wsum_wsum_comm
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - lamB.aux.le_lamB0
  - Profile.ext
  - muB.aux.ge_muB0
  - mix_gt_of_gt_nbh
  - linear_comb_gt_of_ge_gt
---

# loomis_value_IJ_2

## Lean type

```lean
theorem loomis_value_IJ_2 (Hn : 2 = Fintype.card I + Fintype.card J) {A B : I → J → ℝ} (_hB : IsPositive B) : lamB0 A B = muB0 A B
```

## Dependencies

- IsPositive
- singleton_of_card_one
- stdSimplex.mix
- Lottery.mix
- wsum_mix
- lamB.aux_gt_iff_gt
- lam.aux_gt_iff_gt
- xB_pos
- muB.aux_lt_iff_lt
- mu.aux_lt_iff_lt
- By_pos
- wsum_extendDropColumn
- wsum_extendDropRow
- lamB0_le_muB0
- exists_xx_lamB0
- exists_yy_muB0
- xBy_pos
- wsum_wsum_comm
- IsPositiveAffineOf.symm
- Indifferent.symm
- lamB.aux.le_lamB0
- Profile.ext
- muB.aux.ge_muB0
- mix_gt_of_gt_nbh
- linear_comb_gt_of_ge_gt
