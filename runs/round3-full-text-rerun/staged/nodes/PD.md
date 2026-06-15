---
id: PD
title: PD
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.PrisonersDilemma
  declarations:
    - PD
uses:
  - Strategy
---

# PD

## Lean type

```lean
def PD : StrategicGame (Fin 2) ℕ
```

## Dependencies

- Strategy
