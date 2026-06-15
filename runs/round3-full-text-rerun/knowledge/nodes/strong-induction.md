---
id: strong-induction
title: strong_induction
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.GameTree
  declarations:
    - strong_induction
uses:
  - Arena.Reachable.step
  - CPState.step
  - size_pos
  - size_head_lt
  - size_mem_tail_lt
---

# strong_induction

## Lean type

```lean
theorem strong_induction {motive : GameTree N U → Prop} (base : ∀ p, motive (Leaf p)) (step : ∀ (m : N) (h : GameTree N U) (t : List (GameTree N U)), (∀ c ∈ h :: t, motive c) → motive (Node m h t)) (g : GameTree N U) : motive g
```

## Dependencies

- Arena.Reachable.step
- CPState.step
- size_pos
- size_head_lt
- size_mem_tail_lt
