---
id: toValuation-empty
title: toValuation_empty
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.Valuation
  declarations:
    - toValuation_empty
uses:
  - toValuation
---

# toValuation_empty

## Lean type

```lean
@[simp] lemma toValuation_empty (w : AdditiveValuation N G) (i : N) : w.toValuation.val i ∅ = 0
```

## Dependencies

- toValuation
