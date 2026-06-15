---
id: ParetoEfficiency
title: ParetoEfficiency
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Basic
  declarations:
    - ParetoEfficiency
uses:
  - VotingRule
  - Unanimity
---

# ParetoEfficiency

## Lean type

```lean
abbrev ParetoEfficiency (f : VotingRule N A) : Prop
```

## Dependencies

- VotingRule
- Unanimity
