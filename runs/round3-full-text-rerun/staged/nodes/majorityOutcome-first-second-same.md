---
id: majorityOutcome-first-second-same
title: majorityOutcome_first_second_same
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.CandidateChoice
  declarations:
    - majorityOutcome_first_second_same
uses:
  - majorityOutcome
---

# majorityOutcome_first_second_same

## Lean type

```lean
@[simp] theorem majorityOutcome_first_second_same (a c : Candidate) : majorityOutcome a a c = Accepted a
```

## Dependencies

- majorityOutcome
