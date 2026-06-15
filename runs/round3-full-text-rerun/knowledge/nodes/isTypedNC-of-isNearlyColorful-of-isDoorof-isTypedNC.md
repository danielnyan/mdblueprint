---
id: isTypedNC-of-isNearlyColorful-of-isDoorof-isTypedNC
title: isTypedNC_of_isNearlyColorful_of_isDoorof_isTypedNC
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - isTypedNC_of_isNearlyColorful_of_isDoorof_isTypedNC
uses:
  - isNearlyColorful
  - isTypedNC
  - Finset.eq_of_mem_of_card_one
---

# isTypedNC_of_isNearlyColorful_of_isDoorof_isTypedNC

## Lean type

```lean
lemma isTypedNC_of_isNearlyColorful_of_isDoorof_isTypedNC (h_nc : isNearlyColorful c τ D) (h_door : isDoorof τ D σ C) (h_room_typed : isTypedNC c i σ C) : isTypedNC c i τ D
```

## Dependencies

- isNearlyColorful
- isTypedNC
- Finset.eq_of_mem_of_card_one
