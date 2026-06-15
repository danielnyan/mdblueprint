---
id: holding-injective-run
title: holding_injective_run
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.GaleShapley
  declarations:
    - holding_injective_run
uses:
  - holding_injective_step
---

# holding_injective_run

## Lean type

```lean
lemma holding_injective_run (fuel : ℕ) (s : DAState n) (hinj : ∀ j1 j2 : Fin n, ∀ i : Fin n, s.holding j1 = some i → s.holding j2 = some i → j1 = j2) : ∀ j1 j2 : Fin n, ∀ i : Fin n, (daRun w m fuel s).holding j1 = some i → (daRun w m fuel s).holding j2 = some i → j1 = j2
```

## Dependencies

- holding_injective_step
