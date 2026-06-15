---
id: majorityOutcome-pairwise-distinct
title: majorityOutcome_pairwise_distinct
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.CandidateChoice
  declarations:
    - majorityOutcome_pairwise_distinct
uses:
  - majorityOutcome
---

# majorityOutcome_pairwise_distinct

## Lean type

```lean
theorem majorityOutcome_pairwise_distinct {a b c : Candidate} (hab : a ≠ b) (hac : a ≠ c) (hbc : b ≠ c) : majorityOutcome a b c = Rejected
```

## Dependencies

- majorityOutcome
