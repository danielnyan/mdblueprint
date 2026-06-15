---
id: arrow-impossibility
title: arrow_impossibility
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Arrow
  declarations:
    - arrow_impossibility
uses:
  - SWF
  - Unanimity
  - IIA
  - Dictatorial
  - arrow_of_unanimity_iia
---

# arrow_impossibility

## Lean type

```lean
theorem arrow_impossibility [Fintype A] [Fintype N] [Nonempty N] (hA : Fintype.card A ≥ 3) (F : SWF N A) (hU : F.Unanimity) (hIIA : F.IIA) : F.Dictatorial
```

## Dependencies

- SWF
- Unanimity
- IIA
- Dictatorial
- arrow_of_unanimity_iia
