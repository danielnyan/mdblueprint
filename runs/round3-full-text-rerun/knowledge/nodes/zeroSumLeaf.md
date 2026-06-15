---
id: zeroSumLeaf
title: zeroSumLeaf
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.SimpleGameTree
  declarations:
    - zeroSumLeaf
uses:
  - IsCompletelyMixedProfile.player
  - IsCompletelyMixed.player
  - Player
---

# zeroSumLeaf

## Lean type

```lean
def zeroSumLeaf (v : ℚ) : Player → ℚ | ⟨0, _⟩ => v | ⟨1, _⟩ => -v /-- The sample game tree (see module docstring). -/
```

## Dependencies

- IsCompletelyMixedProfile.player
- IsCompletelyMixed.player
- Player
