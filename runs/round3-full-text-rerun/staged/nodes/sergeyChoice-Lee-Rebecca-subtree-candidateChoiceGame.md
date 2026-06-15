---
id: sergeyChoice-Lee-Rebecca-subtree-candidateChoiceGame
title: sergeyChoice_Lee_Rebecca_subtree_candidateChoiceGame
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.CandidateChoice
  declarations:
    - sergeyChoice_Lee_Rebecca_subtree_candidateChoiceGame
uses:
  - sergeyChoice
  - candidateChoiceGame
  - larryChoice
  - IsZeroSum.tail_mem
  - Subtree.tail_mem
  - IsZeroSum.head
  - Subtree.head
  - IsPositiveAffineOf.trans
  - StrictlyPreferred.trans
  - Arena.Reachable.trans
  - Indifferent.trans
  - Subtree.trans
---

# sergeyChoice_Lee_Rebecca_subtree_candidateChoiceGame

## Lean type

```lean
theorem sergeyChoice_Lee_Rebecca_subtree_candidateChoiceGame : Subtree (sergeyChoice Lee Rebecca) candidateChoiceGame
```

## Dependencies

- sergeyChoice
- candidateChoiceGame
- larryChoice
- IsZeroSum.tail_mem
- Subtree.tail_mem
- IsZeroSum.head
- Subtree.head
- IsPositiveAffineOf.trans
- StrictlyPreferred.trans
- Arena.Reachable.trans
- Indifferent.trans
- Subtree.trans
