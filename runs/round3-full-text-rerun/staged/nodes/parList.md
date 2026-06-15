---
id: parList
title: parList
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.CostM
  declarations:
    - parList
uses:
---

# parList

## Lean type

```lean
def parList [SemilatticeSup C] [OrderBot C] (ms : List (CostM C A)) : CostM C (List A)
```

## Dependencies

- none
