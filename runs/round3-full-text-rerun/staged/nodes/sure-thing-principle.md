---
id: sure-thing-principle
title: sure_thing_principle
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.Utility.VNMAxioms
  declarations:
    - sure_thing_principle
uses:
  - Lottery
  - Independence
  - stdSimplex.mix
  - Lottery.mix
  - Profile.ext
  - Completeness
  - stdSimplex.pure
  - Lottery.pure
  - Transitivity
  - IsPositiveAffineOf.trans
  - StrictlyPreferred.trans
  - Arena.Reachable.trans
  - Indifferent.trans
  - Subtree.trans
  - colRatio.continuous
  - lamB.aux.continuous
  - rowRatio.continuous
  - lam.aux.continuous
  - muB.aux.continuous
  - mu.aux.continuous
  - Continuity
---

# sure_thing_principle

## Lean type

```lean
theorem sure_thing_principle {pref : Lottery 𝕜 O → Lottery 𝕜 O → Prop} (hind : Independence pref) (L₁ L₂ L₃ L₄ : Lottery 𝕜 O) (α : 𝕜) (hα₀ : 0 ≤ α) (hα₁ : α ≤ 1) : strict pref (Lottery.mix α hα₀ hα₁ L₁ L₃) (Lottery.mix α hα₀ hα₁ L₂ L₃) ↔ strict pref (Lottery.mix α hα₀ hα₁ L₁ L₄) (Lottery.mix α hα₀ hα₁ L₂ L₄)
```

## Dependencies

- Lottery
- Independence
- stdSimplex.mix
- Lottery.mix
- Profile.ext
- Completeness
- stdSimplex.pure
- Lottery.pure
- Transitivity
- IsPositiveAffineOf.trans
- StrictlyPreferred.trans
- Arena.Reachable.trans
- Indifferent.trans
- Subtree.trans
- colRatio.continuous
- lamB.aux.continuous
- rowRatio.continuous
- lam.aux.continuous
- muB.aux.continuous
- mu.aux.continuous
- Continuity
