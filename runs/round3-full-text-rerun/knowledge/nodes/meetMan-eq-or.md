---
id: meetMan-eq-or
title: meetMan_eq_or
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.Lattice
  declarations:
    - meetMan_eq_or
uses:
---

# meetMan_eq_or

## Lean type

```lean
lemma meetMan_eq_or (i : Fin n) : meetMan μ ν hμ hν i = mPartner μ hμ i ∨ meetMan μ ν hμ hν i = mPartner ν hν i
```

## Dependencies

- none
