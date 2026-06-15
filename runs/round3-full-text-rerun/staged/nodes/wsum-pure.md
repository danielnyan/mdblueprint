---
id: wsum-pure
title: wsum_pure
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Simplex
  declarations:
    - wsum_pure
uses:
  - wsum_pure_apply
---

# wsum_pure

## Lean type

```lean
theorem wsum_pure [DecidableEq I] (i₀ : I) (f : I → 𝕜) : wsum ⟨fun i => if i = i₀ then 1 else 0, fun i => by simp only; split_ifs <;> norm_num, by simp [Finset.sum_ite_eq', Finset.mem_univ]⟩ f = f i₀
```

## Dependencies

- wsum_pure_apply
