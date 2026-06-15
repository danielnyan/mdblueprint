---
id: tendsto-diam-to-zero
title: tendsto_diam_to_zero
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Brouwer
  declarations:
    - tendsto_diam_to_zero
uses:
  - room_seq
  - TTtostdSimplex
  - isDominant
  - TT
  - size_bound_in
---

# tendsto_diam_to_zero

## Lean type

```lean
theorem tendsto_diam_to_zero (f : stdSimplex ℝ (Fin n) → stdSimplex ℝ (Fin n)) : Tendsto (fun k => Metric.diam ((((room_seq f (g1 f ((hpkg f).1.2 k))).1.1.image (fun x => TTtostdSimplex x)) : Set (stdSimplex ℝ (Fin n))))) atTop (𝓝 0)
```

## Dependencies

- room_seq
- TTtostdSimplex
- isDominant
- TT
- size_bound_in
