---
id: bestGood-mem
title: bestGood_mem
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.RoundRobin
  declarations:
    - bestGood_mem
uses:
  - toAdditiveValuation
---

# bestGood_mem

## Lean type

```lean
lemma bestGood_mem [DecidableEq G] (I : AdditiveInstance (Fin n) G) (i : Fin n) (s : Finset G) (hs : s.Nonempty) : bestGood I i s hs ∈ s
```

## Dependencies

- toAdditiveValuation
