---
id: bestGood-le
title: bestGood_le
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.RoundRobin
  declarations:
    - bestGood_le
uses:
  - toAdditiveValuation
  - Allocation
  - Pos
---

# bestGood_le

## Lean type

```lean
lemma bestGood_le [DecidableEq G] (I : AdditiveInstance (Fin n) G) (i : Fin n) (s : Finset G) (hs : s.Nonempty) {g : G} (hg : g ∈ s) : I.weight i g ≤ I.weight i (bestGood I i s hs)
```

## Dependencies

- toAdditiveValuation
- Allocation
- Pos
