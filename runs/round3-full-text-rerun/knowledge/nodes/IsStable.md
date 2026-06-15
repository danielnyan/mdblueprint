---
id: IsStable
title: IsStable
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.Basic
  declarations:
    - IsStable
uses:
  - IsBlocking
---

# IsStable

## Lean type

```lean
def IsStable (market : MatchingMarket M W) (μ : Matching M W) : Prop
```

## Dependencies

- IsBlocking
