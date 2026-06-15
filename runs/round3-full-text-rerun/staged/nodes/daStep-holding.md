---
id: daStep-holding
title: daStep_holding
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.GaleShapley
  declarations:
    - daStep_holding
uses:
  - isFree
  - propTarget
  - freeMenSet
  - finalState
  - initState
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# daStep_holding

## Lean type

```lean
lemma daStep_holding {n : ℕ} (w m : Preferences n) (s : DAState n) (p : Fin n) : (daStep w m s).holding p = (match s.holding p, ((Finset.univ.filter (fun i : Fin n => isFree s i && (propTarget m i (s.nextChoice i) == some p))).val.toList).argmin (fun i => (w.prefs p).idxOf i) with | none, none => none | some h, none => some h | none, some q => some q | some h, some q => if (w.prefs p).idxOf q < (w.prefs p).idxOf h then some q else some h)
```

## Dependencies

- isFree
- propTarget
- freeMenSet
- finalState
- initState
- IsPositiveAffineOf.symm
- Indifferent.symm
