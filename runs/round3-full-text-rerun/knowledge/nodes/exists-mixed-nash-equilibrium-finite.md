---
id: exists-mixed-nash-equilibrium-finite
title: exists_mixed_nash_equilibrium_finite
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.Nash
  declarations:
    - exists_mixed_nash_equilibrium_finite
uses:
  - Strategy
  - MixedS
  - mixedNashEquilibrium
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - Profile.ext
  - ProductSimplices
  - nash_map
  - colRatio.continuous
  - lamB.aux.continuous
  - rowRatio.continuous
  - lam.aux.continuous
  - muB.aux.continuous
  - mu.aux.continuous
  - nash_map_cont
  - Brouwer_Product
  - g_function
  - one_le_sum_g
  - evaluate_at_mixed
  - stdSimplex.pure
  - Lottery.pure
  - evaluate_at_mixed_linear
---

# exists_mixed_nash_equilibrium_finite

## Lean type

```lean
theorem exists_mixed_nash_equilibrium_finite (G : StrategicGame N ℝ) [Fintype N] [DecidableEq N] [∀ i, Fintype (G.strategy i)] [∀ i, DecidableEq (G.strategy i)] [∀ i, Inhabited (G.strategy i)] [Inhabited N] : ∃ σ : MixedS G, mixedNashEquilibrium G σ
```

## Dependencies

- Strategy
- MixedS
- mixedNashEquilibrium
- IsPositiveAffineOf.symm
- Indifferent.symm
- Profile.ext
- ProductSimplices
- nash_map
- colRatio.continuous
- lamB.aux.continuous
- rowRatio.continuous
- lam.aux.continuous
- muB.aux.continuous
- mu.aux.continuous
- nash_map_cont
- Brouwer_Product
- g_function
- one_le_sum_g
- evaluate_at_mixed
- stdSimplex.pure
- Lottery.pure
- evaluate_at_mixed_linear
