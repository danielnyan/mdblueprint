---
id: lcs-cost-subset
title: lcs_cost_subset
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.CostM.LCS
  declarations:
    - lcs_cost_subset
uses:
  - toFinset
  - Visited
  - IsPositiveAffineOf.trans
  - StrictlyPreferred.trans
  - Arena.Reachable.trans
  - Indifferent.trans
  - Subtree.trans
---

# lcs_cost_subset

## Lean type

```lean
theorem lcs_cost_subset (xs : List A) : ∀ (ys : List A), (lcs xs ys).cost.toFinset ⊆ Finset.range (xs.length + 1) ×ˢ Finset.range (ys.length + 1)
```

## Dependencies

- toFinset
- Visited
- IsPositiveAffineOf.trans
- StrictlyPreferred.trans
- Arena.Reachable.trans
- Indifferent.trans
- Subtree.trans
