---
id: Vickrey
title: Vickrey
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.SimpleAuction
  declarations:
    - Vickrey
uses:
  - Strategy
---

# Vickrey

## Lean type

```lean
def Vickrey (v : Fin 2 → Fin n) : StrategicGame (Fin 2) ℤ
```

## Dependencies

- Strategy
