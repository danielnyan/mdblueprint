---
id: wPartner-stableJoin
title: wPartner_stableJoin
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.Lattice
  declarations:
    - wPartner_stableJoin
uses:
  - stableJoin_isStable
---

# wPartner_stableJoin

## Lean type

```lean
lemma wPartner_stableJoin (j : Fin n) : wPartner (stableJoin μ ν hμ hν) (stableJoin_isStable μ ν hμ hν) j = joinWoman μ ν hμ hν j
```

## Dependencies

- stableJoin_isStable
