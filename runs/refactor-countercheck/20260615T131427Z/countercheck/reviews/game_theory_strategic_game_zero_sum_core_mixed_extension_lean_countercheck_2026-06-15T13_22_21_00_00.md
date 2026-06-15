---
agent: lean-countercheck
node_id: game_theory.strategic_game.zero_sum.core.mixed_extension
created_at: "2026-06-15T13:22:21+00:00"
---

# Lean Countercheck: Mixed Extension Of A Matrix Game

## Inputs

- node file: `/home/azureuser/EconCSLib/docs/knowledge/nodes/zero_sum/core/mixed_extension.md`
- lean file: `/home/azureuser/EconCSLib/EconCSLib/Math/Simplex.lean`
- corpus root: `/home/azureuser/EconCSLib`

## Method Status

- heuristic: used

## Matched Declarations

- `expectedPayoffMatrix`

## Missing Declarations

- `(none)`

## Extra Declarations

- `affineCombination_eq_linearCombination`
- `wsum`
- `wsum_const`
- `wsum_le_wsum`
- `wsum_nonneg`
- `wsum_pos`
- `wsum_ge_wsum`
- `wsum_add`
- `wsum_smul`
- `stdSimplex.mix`
- `stdSimplex.mix_apply`
- `wsum_mix`
- `linear_comb_gt_left`
- `linear_comb_gt_right`
- `linear_comb_gt_of_ge_gt`
- `linear_comb_lt_of_le_lt`
- `wsum_mix_gt_of_ge_gt`
- `wsum_mix_lt_of_le_lt`
- `mix_gt_of_gt_nbh`
- `mix_lt_of_lt_nbh`
- `wsum_wsum_comm`
- `stdSimplex.pure`
- `stdSimplex.pure_apply`
- `wsum_pure_apply`
- `wsum_pure`
- `ge_iff_simplex_ge`
- `le_iff_simplex_le`
- `stdSimplex.continuous_coord`
- `wsum_continuous`
- `expectedPayoffMatrix_comm`

## Node Uses vs Extracted Dependencies

- node uses: `game_theory.strategic_game.zero_sum.core.mixed_strategy_simplex`
- missing uses: `game_theory.strategic_game.zero_sum.core.mixed_strategy_simplex`
- extra uses: `expectedPayoffMatrix`, `linear_comb_gt_of_ge_gt`, `linear_comb_lt_of_le_lt`, `mix_gt_of_gt_nbh`, `stdSimplex.continuous_coord`, `stdSimplex.mix`, `stdSimplex.pure`, `wsum_const`, `wsum_le_wsum`, `wsum_mix`, `wsum_nonneg`, `wsum_pure`, `wsum_pure_apply`, `wsum_wsum_comm`

## Raw Snapshot

```json
{
  "corpus_root": "/home/azureuser/EconCSLib",
  "dependencies": [
    {
      "kind": "hard",
      "module": "EconCSLib.Math.Simplex",
      "source": "affineCombination_eq_linearCombination",
      "target": "wsum_le_wsum"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Math.Simplex",
      "source": "affineCombination_eq_linearCombination",
      "target": "wsum_nonneg"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Math.Simplex",
      "source": "affineCombination_eq_linearCombination",
      "target": "wsum_const"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Math.Simplex",
      "source": "affineCombination_eq_linearCombination",
      "target": "wsum_pure"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Math.Simplex",
      "source": "wsum_nonneg",
      "target": "wsum_le_wsum"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Math.Simplex",
      "source": "wsum_nonneg",
      "target": "wsum_const"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Math.Simplex",
      "source": "wsum_ge_wsum",
      "target": "wsum_le_wsum"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Math.Simplex",
      "source": "stdSimplex.mix_apply",
      "target": "stdSimplex.mix"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Math.Simplex",
      "source": "wsum_mix",
      "target": "stdSimplex.mix"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Math.Simplex",
      "source": "linear_comb_lt_of_le_lt",
      "target": "linear_comb_gt_of_ge_gt"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Math.Simplex",
      "source": "linear_comb_lt_of_le_lt",
      "target": "wsum_mix"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Math.Simplex",
      "source": "wsum_mix_gt_of_ge_gt",
      "target": "linear_comb_gt_of_ge_gt"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Math.Simplex",
      "source": "wsum_mix_gt_of_ge_gt",
      "target": "linear_comb_lt_of_le_lt"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Math.Simplex",
      "source": "wsum_mix_gt_of_ge_gt",
      "target": "stdSimplex.mix"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Math.Simplex",
      "source": "wsum_mix_gt_of_ge_gt",
      "target": "wsum_mix"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Math.Simplex",
      "source": "wsum_mix_lt_of_le_lt",
      "target": "linear_comb_lt_of_le_lt"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Math.Simplex",
      "source": "wsum_mix_lt_of_le_lt",
      "target": "stdSimplex.mix"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Math.Simplex",
      "source": "wsum_mix_lt_of_le_lt",
      "target": "wsum_mix"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Math.Simplex",
      "source": "mix_lt_of_lt_nbh",
      "target": "mix_gt_of_gt_nbh"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Math.Simplex",
      "source": "stdSimplex.pure_apply",
      "target": "stdSimplex.pure"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Math.Simplex",
      "source": "wsum_pure_apply",
      "target": "stdSimplex.pure"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Math.Simplex",
      "source": "wsum_pure",
      "target": "wsum_pure_apply"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Math.Simplex",
      "source": "ge_iff_simplex_ge",
      "target": "stdSimplex.pure"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Math.Simplex",
      "source": "ge_iff_simplex_ge",
      "target": "wsum_le_wsum"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Math.Simplex",
      "source": "ge_iff_simplex_ge",
      "target": "wsum_const"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Math.Simplex",
      "source": "le_iff_simplex_le",
      "target": "stdSimplex.pure"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Math.Simplex",
      "source": "le_iff_simplex_le",
      "target": "wsum_le_wsum"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Math.Simplex",
      "source": "le_iff_simplex_le",
      "target": "wsum_const"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Math.Simplex",
      "source": "wsum_continuous",
      "target": "stdSimplex.continuous_coord"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Math.Simplex",
      "source": "wsum_continuous",
      "target": "expectedPayoffMatrix"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Math.Simplex",
      "source": "expectedPayoffMatrix_comm",
      "target": "expectedPayoffMatrix"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Math.Simplex",
      "source": "expectedPayoffMatrix_comm",
      "target": "wsum_wsum_comm"
    }
  ],
  "lean_file": "/home/azureuser/EconCSLib/EconCSLib/Math/Simplex.lean",
  "method_status": {
    "heuristic": "used"
  },
  "node": {
    "body": "# Mixed Extension Of A Matrix Game\n\nFor a finite matrix game $A : I \\times J \\to \\mathbb{R}$, the mixed extension\nhas strategy spaces $\\Delta(I)$ and $\\Delta(J)$.  Its payoff is the bilinear\nextension\n$$\n  g(x,y)=\\sum_{i \\in I}\\sum_{j \\in J} x_i y_j A_{ij}.\n$$\nPure strategies are identified with Dirac measures in the corresponding\nsimplex.\n\n## References\n\n- [MFoGT, Chapter 2, Section 2.3] Laraki, Renault, and Sorin, *Mathematical Foundations of Game Theory*. Mixed extension and multilinear payoff.",
    "file_path": "/home/azureuser/EconCSLib/docs/knowledge/nodes/zero_sum/core/mixed_extension.md",
    "id": "game_theory.strategic_game.zero_sum.core.mixed_extension",
    "kind": "definition",
    "lean": {
      "declarations": [
        "expectedPayoffMatrix"
      ],
      "modules": [
        "EconCSLib.Math.Simplex"
      ],
      "repository": null
    },
    "status": "formalized",
    "tags": [
      "zero-sum",
      "mixed-strategy",
      "expected-payoff"
    ],
    "title": "Mixed Extension Of A Matrix Game",
    "uses": [
      "game_theory.strategic_game.zero_sum.core.mixed_strategy_simplex"
    ]
  },
  "source_root": "/home/azureuser/EconCSLib",
  "theorems": [
    {
      "body": "@[simp]\ntheorem affineCombination_eq_linearCombination {k V I : Type*}\n    [Ring k] [PartialOrder k] [Fintype I]\n    [AddCommGroup V] [Module k V]\n    (x : stdSimplex k I) (p : I \u2192 V) :\n    affineCombination x p = Fintype.linearCombination k p x := by\n  simp [affineCombination, Fintype.linearCombination_apply,\n    Finset.affineCombination_eq_linear_combination, stdSimplex.sum_eq_one x]\n\nend stdSimplex\n\n/-- Weighted sum of `f` with weights from a simplex element `x`.\n    Thin `abbrev` over Mathlib's finite dot product `\u2b1d\u1d65`: definitionally equal,\n    so `simp [wsum]` (or no unfold at all) switches between the two forms.\n    Kept as a named concept because the simplex-specific lemmas below\n    (`wsum_const`, `wsum_le_wsum`, `wsum_nonneg`, `wsum_pure`) depend on\n    `\u2211 x = 1` or `x \u2265 0` and have no generic `dotProduct` analogue. -/\n",
      "column": 1,
      "end": 3292,
      "kind": "theorem",
      "line": 70,
      "module": "EconCSLib.Math.Simplex",
      "name": "affineCombination_eq_linearCombination",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Math/Simplex.lean",
      "start": 2452
    },
    {
      "body": "abbrev wsum (x : stdSimplex \ud835\udd5c I) (f : I \u2192 \ud835\udd5c) : \ud835\udd5c :=\n  x \u2b1d\u1d65 f\n\n/-- Weighted sum of a constant equals the constant. -/\n",
      "column": 1,
      "end": 3409,
      "kind": "abbrev",
      "line": 87,
      "module": "EconCSLib.Math.Simplex",
      "name": "wsum",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Math/Simplex.lean",
      "start": 3292
    },
    {
      "body": "theorem wsum_const (x : stdSimplex \ud835\udd5c I) (c : \ud835\udd5c) :\n    wsum x (fun _ => c) = c := by\n  simp [wsum, dotProduct, \u2190 Finset.sum_mul]\n\n/-- Weighted sum is monotone: pointwise `\u2264` implies `wsum \u2264`. -/\n",
      "column": 1,
      "end": 3603,
      "kind": "theorem",
      "line": 91,
      "module": "EconCSLib.Math.Simplex",
      "name": "wsum_const",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Math/Simplex.lean",
      "start": 3409
    },
    {
      "body": "theorem wsum_le_wsum (x : stdSimplex \ud835\udd5c I) {f g : I \u2192 \ud835\udd5c}\n    (h : \u2200 i, f i \u2264 g i) : wsum x f \u2264 wsum x g := by\n  apply Finset.sum_le_sum\n  intro i _\n  exact mul_le_mul_of_nonneg_left (h i) (x.property.1 i)\n\n/-- Weighted sum of non-negative values is non-negative. -/\n",
      "column": 1,
      "end": 3868,
      "kind": "theorem",
      "line": 96,
      "module": "EconCSLib.Math.Simplex",
      "name": "wsum_le_wsum",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Math/Simplex.lean",
      "start": 3603
    },
    {
      "body": "theorem wsum_nonneg (x : stdSimplex \ud835\udd5c I) {f : I \u2192 \ud835\udd5c}\n    (h : \u2200 i, 0 \u2264 f i) : 0 \u2264 wsum x f := by\n  calc 0 = wsum x (fun _ => (0 : \ud835\udd5c)) := (wsum_const x 0).symm\n    _ \u2264 wsum x f := wsum_le_wsum x (fun i => by linarith [h i])\n\n/-- Weighted sum of strictly-positive values is strictly positive.\n\n    Some coordinate `a` of any simplex point is strictly positive (since\n    `\u2211 x = 1`), and the corresponding `x_a \u00b7 f a` summand is strictly\n    positive while every other summand is non-negative. -/\n",
      "column": 1,
      "end": 4362,
      "kind": "theorem",
      "line": 103,
      "module": "EconCSLib.Math.Simplex",
      "name": "wsum_nonneg",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Math/Simplex.lean",
      "start": 3868
    },
    {
      "body": "theorem wsum_pos (x : stdSimplex \ud835\udd5c I) {f : I \u2192 \ud835\udd5c}\n    (hf : \u2200 i, 0 < f i) : 0 < wsum x f := by\n  classical\n  obtain \u27e8a, ha\u27e9 : \u2203 a, 0 < x.val a := by\n    by_contra hAll\n    push_neg at hAll\n    have hzero : \u2200 i, x.val i = 0 :=\n      fun i => le_antisymm (hAll i) (x.property.1 i)\n    have hsum_zero : (\u2211 i, x.val i) = 0 := by simp_rw [hzero]; simp\n    exact zero_ne_one (hsum_zero.symm.trans x.property.2)\n  change 0 < \u2211 b, x.val b * f b\n  have hle : \u2200 b \u2208 (Finset.univ : Finset I), (0 : \ud835\udd5c) \u2264 x.val b * f b :=\n    fun b _ => mul_nonneg (x.property.1 b) (hf b).le\n  have hpos : \u2203 b \u2208 (Finset.univ : Finset I), (0 : \ud835\udd5c) < x.val b * f b :=\n    \u27e8a, Finset.mem_univ _, mul_pos ha (hf a)\u27e9\n  calc (0 : \ud835\udd5c)\n      = \u2211 _ : I, (0 : \ud835\udd5c) := by simp\n    _ < \u2211 b, x.val b * f b := Finset.sum_lt_sum hle hpos\n\n/-- Weighted sum respects `\u2265`. -/\n",
      "column": 1,
      "end": 5186,
      "kind": "theorem",
      "line": 113,
      "module": "EconCSLib.Math.Simplex",
      "name": "wsum_pos",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Math/Simplex.lean",
      "start": 4362
    },
    {
      "body": "theorem wsum_ge_wsum (x : stdSimplex \ud835\udd5c I) {f g : I \u2192 \ud835\udd5c}\n    (h : \u2200 i, f i \u2265 g i) : wsum x f \u2265 wsum x g :=\n  wsum_le_wsum x h\n\n/-- Weighted sum is linear over addition. -/\n",
      "column": 1,
      "end": 5357,
      "kind": "theorem",
      "line": 133,
      "module": "EconCSLib.Math.Simplex",
      "name": "wsum_ge_wsum",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Math/Simplex.lean",
      "start": 5186
    },
    {
      "body": "theorem wsum_add (x : stdSimplex \ud835\udd5c I) (f g : I \u2192 \ud835\udd5c) :\n    wsum x (f + g) = wsum x f + wsum x g := by\n  simp [wsum, dotProduct, mul_add, Finset.sum_add_distrib]\n\n/-- Weighted sum commutes with scalar multiplication. -/\n",
      "column": 1,
      "end": 5575,
      "kind": "theorem",
      "line": 138,
      "module": "EconCSLib.Math.Simplex",
      "name": "wsum_add",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Math/Simplex.lean",
      "start": 5357
    },
    {
      "body": "theorem wsum_smul (x : stdSimplex \ud835\udd5c I) (c : \ud835\udd5c) (f : I \u2192 \ud835\udd5c) :\n    wsum x (c \u2022 f) = c * wsum x f := by\n  simp [wsum, dotProduct, Pi.smul_apply, smul_eq_mul, mul_left_comm, \u2190 Finset.mul_sum]\n\n/-! ### Convex combination of two simplex points (`mix`) -/\n\n/-- Convex combination of two simplex points: `mix \u03b1 h\u03b1\u2080 h\u03b1\u2081 x y = \u03b1\u00b7x + (1-\u03b1)\u00b7y`.\n\nThis is the basic vocabulary for compound lotteries and for any inductive\nargument that interpolates between two mixed strategies (Loomis, Sion,\nfictitious play). The hypotheses are passed as plain `(\u03b1 : \ud835\udd5c) (h\u03b1\u2080 : 0 \u2264 \u03b1)\n(h\u03b1\u2081 : \u03b1 \u2264 1)` rather than via a unit-interval subtype to match Mathlib\nidioms and to keep call sites lightweight. -/\n",
      "column": 1,
      "end": 6248,
      "kind": "theorem",
      "line": 143,
      "module": "EconCSLib.Math.Simplex",
      "name": "wsum_smul",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Math/Simplex.lean",
      "start": 5575
    },
    {
      "body": "def stdSimplex.mix (\u03b1 : \ud835\udd5c) (h\u03b1\u2080 : 0 \u2264 \u03b1) (h\u03b1\u2081 : \u03b1 \u2264 1)\n    (x y : stdSimplex \ud835\udd5c I) : stdSimplex \ud835\udd5c I where\n  val i := \u03b1 * x.val i + (1 - \u03b1) * y.val i\n  property := by\n    refine \u27e8fun i => ?_, ?_\u27e9\n    \u00b7 have hx := x.property.1 i\n      have hy := y.property.1 i\n      have h\u03b1' : 0 \u2264 1 - \u03b1 := by linarith\n      have h\u2081 : 0 \u2264 \u03b1 * x.val i := mul_nonneg h\u03b1\u2080 hx\n      have h\u2082 : 0 \u2264 (1 - \u03b1) * y.val i := mul_nonneg h\u03b1' hy\n      linarith\n    \u00b7 have hxsum := x.property.2\n      have hysum := y.property.2\n      have : (\u2211 i, (\u03b1 * x.val i + (1 - \u03b1) * y.val i))\n          = \u03b1 * (\u2211 i, x.val i) + (1 - \u03b1) * (\u2211 i, y.val i) := by\n        rw [Finset.sum_add_distrib, \u2190 Finset.mul_sum, \u2190 Finset.mul_sum]\n      rw [this, hxsum, hysum]; ring\n\n",
      "column": 1,
      "end": 6968,
      "kind": "def",
      "line": 156,
      "module": "EconCSLib.Math.Simplex",
      "name": "stdSimplex.mix",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Math/Simplex.lean",
      "start": 6248
    },
    {
      "body": "@[simp]\ntheorem stdSimplex.mix_apply (\u03b1 : \ud835\udd5c) (h\u03b1\u2080 : 0 \u2264 \u03b1) (h\u03b1\u2081 : \u03b1 \u2264 1)\n    (x y : stdSimplex \ud835\udd5c I) (i : I) :\n    (stdSimplex.mix \u03b1 h\u03b1\u2080 h\u03b1\u2081 x y).val i = \u03b1 * x.val i + (1 - \u03b1) * y.val i := rfl\n\n/-- Bilinearity of `wsum` over `stdSimplex.mix`:\n`wsum (mix \u03b1 x y) f = \u03b1 \u00b7 wsum x f + (1-\u03b1) \u00b7 wsum y f`. -/\n",
      "column": 1,
      "end": 7269,
      "kind": "theorem",
      "line": 174,
      "module": "EconCSLib.Math.Simplex",
      "name": "stdSimplex.mix_apply",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Math/Simplex.lean",
      "start": 6968
    },
    {
      "body": "theorem wsum_mix (\u03b1 : \ud835\udd5c) (h\u03b1\u2080 : 0 \u2264 \u03b1) (h\u03b1\u2081 : \u03b1 \u2264 1)\n    (x y : stdSimplex \ud835\udd5c I) (f : I \u2192 \ud835\udd5c) :\n    wsum (stdSimplex.mix \u03b1 h\u03b1\u2080 h\u03b1\u2081 x y) f =\n      \u03b1 * wsum x f + (1 - \u03b1) * wsum y f := by\n  change (\u2211 i, (\u03b1 * x.val i + (1 - \u03b1) * y.val i) * f i)\n       = \u03b1 * (\u2211 i, x.val i * f i) + (1 - \u03b1) * (\u2211 i, y.val i * f i)\n  rw [Finset.mul_sum, Finset.mul_sum, \u2190 Finset.sum_add_distrib]\n  apply Finset.sum_congr rfl; intro i _; ring\n\n/-! ### Ordered-field arithmetic helpers about convex combinations\n\nThese work directly on the scalar expression `\u03b1 \u00b7 x + (1-\u03b1) \u00b7 y` without\nreference to `stdSimplex`. They are the algebraic ingredients used to derive\nstrict-monotonicity facts about `wsum_mix` below. -/\n\n/-- If `x < y` and `\u03b1 < 1`, then `\u03b1\u00b7x + (1-\u03b1)\u00b7y > x`. -/\n",
      "column": 1,
      "end": 8016,
      "kind": "theorem",
      "line": 181,
      "module": "EconCSLib.Math.Simplex",
      "name": "wsum_mix",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Math/Simplex.lean",
      "start": 7269
    },
    {
      "body": "theorem linear_comb_gt_left {x y : \ud835\udd5c} (H : x < y) {\u03b1 : \ud835\udd5c} (H\u03b1 : \u03b1 < 1) :\n    x < \u03b1 * x + (1 - \u03b1) * y := by\n  have hpos : 0 < 1 - \u03b1 := by linarith\n  have : 0 < (1 - \u03b1) * (y - x) := mul_pos hpos (by linarith)\n  nlinarith\n\n/-- If `y < x` and `0 < \u03b1`, then `\u03b1\u00b7x + (1-\u03b1)\u00b7y > y`. -/\n",
      "column": 1,
      "end": 8293,
      "kind": "theorem",
      "line": 197,
      "module": "EconCSLib.Math.Simplex",
      "name": "linear_comb_gt_left",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Math/Simplex.lean",
      "start": 8016
    },
    {
      "body": "theorem linear_comb_gt_right {x y : \ud835\udd5c} (H : y < x) {\u03b1 : \ud835\udd5c} (H\u03b1 : 0 < \u03b1) :\n    y < \u03b1 * x + (1 - \u03b1) * y := by\n  have : 0 < \u03b1 * (x - y) := mul_pos H\u03b1 (by linarith)\n  nlinarith\n\n/-- Convex combination of \"\u2265 c\" and \"> c\" stays \"> c\" (provided `\u03b1 \u2265 0` and `\u03b1 < 1`). -/\n",
      "column": 1,
      "end": 8556,
      "kind": "theorem",
      "line": 204,
      "module": "EconCSLib.Math.Simplex",
      "name": "linear_comb_gt_right",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Math/Simplex.lean",
      "start": 8293
    },
    {
      "body": "theorem linear_comb_gt_of_ge_gt (x y c : \ud835\udd5c) (H1 : c \u2264 x) (H2 : c < y)\n    {\u03b1 : \ud835\udd5c} (h\u03b1\u2080 : 0 \u2264 \u03b1) (h\u03b1\u2081 : \u03b1 < 1) :\n    c < \u03b1 * x + (1 - \u03b1) * y := by\n  have hpos : 0 < 1 - \u03b1 := by linarith\n  have hxc : 0 \u2264 \u03b1 * (x - c) := mul_nonneg h\u03b1\u2080 (by linarith)\n  have hyc : 0 < (1 - \u03b1) * (y - c) := mul_pos hpos (by linarith)\n  nlinarith\n\n/-- Convex combination of \"\u2264 c\" and \"< c\" stays \"< c\" (provided `\u03b1 \u2265 0` and `\u03b1 < 1`). -/\n",
      "column": 1,
      "end": 8969,
      "kind": "theorem",
      "line": 210,
      "module": "EconCSLib.Math.Simplex",
      "name": "linear_comb_gt_of_ge_gt",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Math/Simplex.lean",
      "start": 8556
    },
    {
      "body": "theorem linear_comb_lt_of_le_lt (x y c : \ud835\udd5c) (H1 : x \u2264 c) (H2 : y < c)\n    {\u03b1 : \ud835\udd5c} (h\u03b1\u2080 : 0 \u2264 \u03b1) (h\u03b1\u2081 : \u03b1 < 1) :\n    \u03b1 * x + (1 - \u03b1) * y < c := by\n  have hpos : 0 < 1 - \u03b1 := by linarith\n  have hxc : 0 \u2264 \u03b1 * (c - x) := mul_nonneg h\u03b1\u2080 (by linarith)\n  have hyc : 0 < (1 - \u03b1) * (c - y) := mul_pos hpos (by linarith)\n  nlinarith\n\n/-! ### Strict monotonicity of `wsum_mix` -/\n\n/-- `wsum` version of `linear_comb_gt_of_ge_gt`. -/\n",
      "column": 1,
      "end": 9391,
      "kind": "theorem",
      "line": 219,
      "module": "EconCSLib.Math.Simplex",
      "name": "linear_comb_lt_of_le_lt",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Math/Simplex.lean",
      "start": 8969
    },
    {
      "body": "theorem wsum_mix_gt_of_ge_gt {I : Type*} [Fintype I]\n    (f : I \u2192 \ud835\udd5c) (x y : stdSimplex \ud835\udd5c I) (c : \ud835\udd5c)\n    (H1 : c \u2264 wsum x f) (H2 : c < wsum y f)\n    {t : \ud835\udd5c} (ht\u2080 : 0 \u2264 t) (ht\u2081 : t \u2264 1) (Ht : t < 1) :\n    c < wsum (stdSimplex.mix t ht\u2080 ht\u2081 x y) f := by\n  rw [wsum_mix]\n  exact linear_comb_gt_of_ge_gt _ _ c H1 H2 ht\u2080 Ht\n\n/-- `wsum` version of `linear_comb_lt_of_le_lt`. -/\n",
      "column": 1,
      "end": 9762,
      "kind": "theorem",
      "line": 230,
      "module": "EconCSLib.Math.Simplex",
      "name": "wsum_mix_gt_of_ge_gt",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Math/Simplex.lean",
      "start": 9391
    },
    {
      "body": "theorem wsum_mix_lt_of_le_lt {I : Type*} [Fintype I]\n    (f : I \u2192 \ud835\udd5c) (x y : stdSimplex \ud835\udd5c I) (c : \ud835\udd5c)\n    (H1 : wsum x f \u2264 c) (H2 : wsum y f < c)\n    {t : \ud835\udd5c} (ht\u2080 : 0 \u2264 t) (ht\u2081 : t \u2264 1) (Ht : t < 1) :\n    wsum (stdSimplex.mix t ht\u2080 ht\u2081 x y) f < c := by\n  rw [wsum_mix]\n  exact linear_comb_lt_of_le_lt _ _ c H1 H2 ht\u2080 Ht\n\n/-! ### Neighborhood existential for convex combinations\n\nIf `c < x`, then there is an interior `t \u2208 (0,1)` with `c < t\u00b7x + (1-t)\u00b7y`.\nOver a general ordered field this is the elementary fact that the segment\n`s \u21a6 s\u00b7x + (1-s)\u00b7y` from `y` to `x` stays above `c` near `s = 1`; we pick `t`\nexplicitly (no continuity), so it holds for any\n`[Field \ud835\udd5c] [LinearOrder \ud835\udd5c] [IsStrictOrderedRing \ud835\udd5c]`. This is the key\ningredient for the Loomis-style inductive step (perturbing the optimiser a\nlittle in the `y`-direction). -/\n\n/-- Existence of a strictly interior `t` keeping `t\u00b7x + (1-t)\u00b7y > c`, given\n`c < x`. Constructive over any ordered field: pick `t` just above the crossing\nthreshold `(c-y)/(x-y)` (clamped to `0`) when `y < x`, or any interior `t`\nwhen `x \u2264 y`. -/\n",
      "column": 1,
      "end": 10840,
      "kind": "theorem",
      "line": 239,
      "module": "EconCSLib.Math.Simplex",
      "name": "wsum_mix_lt_of_le_lt",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Math/Simplex.lean",
      "start": 9762
    },
    {
      "body": "theorem mix_gt_of_gt_nbh (x y c : \ud835\udd5c) (H : c < x) :\n    \u2203 t : \ud835\udd5c, 0 < t \u2227 t < 1 \u2227 c < t * x + (1 - t) * y := by\n  rcases (lt_or_ge y x).symm with hxy | hyx\n  \u00b7 -- `x \u2264 y`: the whole segment stays above `x > c`; any interior `t` works.\n    refine \u27e81 / 2, by norm_num, by norm_num, ?_\u27e9\n    have hexp : (1 / 2) * x + (1 - 1 / 2) * y = x + (1 / 2) * (y - x) := by ring\n    rw [hexp]\n    have : 0 \u2264 (1 / 2 : \ud835\udd5c) * (y - x) := mul_nonneg (by norm_num) (by linarith)\n    linarith\n  \u00b7 -- `y < x`: pick `t` above the crossing threshold but below `1`.\n    have hd : 0 < x - y := by linarith\n    have hthr_lt_one : (c - y) / (x - y) < 1 := (div_lt_one hd).mpr (by linarith)\n    set a : \ud835\udd5c := max ((c - y) / (x - y)) 0 with ha\n    have ha_lt_one : a < 1 := max_lt hthr_lt_one one_pos\n    have ha_nonneg : 0 \u2264 a := le_max_right _ _\n    have hthr_le_a : (c - y) / (x - y) \u2264 a := le_max_left _ _\n    refine \u27e8(a + 1) / 2, by linarith, by linarith, ?_\u27e9\n    have hthr_lt_t : (c - y) / (x - y) < (a + 1) / 2 := by linarith\n    have hcy : c - y < ((a + 1) / 2) * (x - y) := (div_lt_iff\u2080 hd).mp hthr_lt_t\n    have hexp : ((a + 1) / 2) * x + (1 - (a + 1) / 2) * y\n        = y + ((a + 1) / 2) * (x - y) := by ring\n    rw [hexp]; linarith\n\n/-- Dual: strictly interior `t` keeping `t\u00b7x + (1-t)\u00b7y < c`, given `x < c`.\nObtained from `mix_gt_of_gt_nbh` by negating `x, y, c`. -/\n",
      "column": 1,
      "end": 12186,
      "kind": "theorem",
      "line": 261,
      "module": "EconCSLib.Math.Simplex",
      "name": "mix_gt_of_gt_nbh",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Math/Simplex.lean",
      "start": 10840
    },
    {
      "body": "theorem mix_lt_of_lt_nbh (x y c : \ud835\udd5c) (H : x < c) :\n    \u2203 t : \ud835\udd5c, 0 < t \u2227 t < 1 \u2227 t * x + (1 - t) * y < c := by\n  obtain \u27e8t, ht0, ht1, hgt\u27e9 := mix_gt_of_gt_nbh (-x) (-y) (-c) (by linarith)\n  refine \u27e8t, ht0, ht1, ?_\u27e9\n  have hneg : t * (-x) + (1 - t) * (-y) = -(t * x + (1 - t) * y) := by ring\n  rw [hneg] at hgt\n  linarith\n\n/-- Exchange order of double weighted sums. -/\n",
      "column": 1,
      "end": 12554,
      "kind": "theorem",
      "line": 286,
      "module": "EconCSLib.Math.Simplex",
      "name": "mix_lt_of_lt_nbh",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Math/Simplex.lean",
      "start": 12186
    },
    {
      "body": "theorem wsum_wsum_comm {J : Type*} [Fintype J]\n    (x : stdSimplex \ud835\udd5c I) (y : stdSimplex \ud835\udd5c J)\n    (A : I \u2192 J \u2192 \ud835\udd5c) :\n    wsum x (fun i => wsum y (A i)) = wsum y (fun j => wsum x (fun i => A i j)) := by\n  simp only [wsum, dotProduct, Finset.mul_sum]\n  rw [Finset.sum_comm]\n  congr 1\n  ext j\n  congr 1\n  ext i\n  ring\n\n/-- Point-mass simplex element at `i\u2080`. -/\n",
      "column": 1,
      "end": 12911,
      "kind": "theorem",
      "line": 295,
      "module": "EconCSLib.Math.Simplex",
      "name": "wsum_wsum_comm",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Math/Simplex.lean",
      "start": 12554
    },
    {
      "body": "def stdSimplex.pure [DecidableEq I] (i\u2080 : I) : stdSimplex \ud835\udd5c I where\n  val i := if i = i\u2080 then 1 else 0\n  property := \u27e8fun i => by simp only; split_ifs <;> norm_num,\n               by simp [Finset.sum_ite_eq', Finset.mem_univ]\u27e9\n\n",
      "column": 1,
      "end": 13139,
      "kind": "def",
      "line": 308,
      "module": "EconCSLib.Math.Simplex",
      "name": "stdSimplex.pure",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Math/Simplex.lean",
      "start": 12911
    },
    {
      "body": "@[simp]\ntheorem stdSimplex.pure_apply [DecidableEq I] (i\u2080 i : I) :\n    (stdSimplex.pure (\ud835\udd5c := \ud835\udd5c) i\u2080).val i = if i = i\u2080 then 1 else 0 := rfl\n\n/-- Weighted sum at a point mass evaluates the chosen coordinate. -/\n",
      "column": 1,
      "end": 13349,
      "kind": "theorem",
      "line": 313,
      "module": "EconCSLib.Math.Simplex",
      "name": "stdSimplex.pure_apply",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Math/Simplex.lean",
      "start": 13139
    },
    {
      "body": "@[simp]\ntheorem wsum_pure_apply [DecidableEq I] (i\u2080 : I) (f : I \u2192 \ud835\udd5c) :\n    wsum (stdSimplex.pure (\ud835\udd5c := \ud835\udd5c) i\u2080) f = f i\u2080 := by\n  change (\u2211 i, (if i = i\u2080 then (1 : \ud835\udd5c) else 0) * f i) = f i\u2080\n  simp\n\n/-- Weighted sum with point mass at `i\u2080` equals `f i\u2080`. Legacy form using\nthe inline anonymous-structure point mass. New code should prefer\n`stdSimplex.pure` together with `wsum_pure_apply`. -/\n",
      "column": 1,
      "end": 13737,
      "kind": "theorem",
      "line": 318,
      "module": "EconCSLib.Math.Simplex",
      "name": "wsum_pure_apply",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Math/Simplex.lean",
      "start": 13349
    },
    {
      "body": "theorem wsum_pure [DecidableEq I] (i\u2080 : I) (f : I \u2192 \ud835\udd5c) :\n    wsum \u27e8fun i => if i = i\u2080 then 1 else 0,\n          fun i => by simp only; split_ifs <;> norm_num,\n          by simp [Finset.sum_ite_eq', Finset.mem_univ]\u27e9 f = f i\u2080 :=\n  wsum_pure_apply (\ud835\udd5c := \ud835\udd5c) i\u2080 f\n\n/-! ### Order characterization of `wsum` ranges\n\nThese lemmas turn pointwise bounds on `f : I \u2192 \ud835\udd5c` into bounds on the weighted\nsum `wsum x f` over all simplex points `x`. They are the bridge that lets\nLoomis-style arguments reduce a quantification over mixed strategies to a\nquantification over pure responses. -/\n\n/-- `f \u2265 v` pointwise iff every simplex weighted sum is `\u2265 v`. -/\n",
      "column": 1,
      "end": 14378,
      "kind": "theorem",
      "line": 327,
      "module": "EconCSLib.Math.Simplex",
      "name": "wsum_pure",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Math/Simplex.lean",
      "start": 13737
    },
    {
      "body": "theorem ge_iff_simplex_ge {f : I \u2192 \ud835\udd5c} {v : \ud835\udd5c} :\n    (\u2200 i, v \u2264 f i) \u2194 \u2200 x : stdSimplex \ud835\udd5c I, v \u2264 wsum x f := by\n  classical\n  refine \u27e8fun hi x => ?_, fun H i => ?_\u27e9\n  \u00b7 calc v = wsum x (fun _ => v) := (wsum_const x v).symm\n      _ \u2264 wsum x f := wsum_le_wsum x hi\n  \u00b7 simpa using H (stdSimplex.pure i)\n\n/-- `f \u2264 v` pointwise iff every simplex weighted sum is `\u2264 v`. -/\n",
      "column": 1,
      "end": 14744,
      "kind": "theorem",
      "line": 341,
      "module": "EconCSLib.Math.Simplex",
      "name": "ge_iff_simplex_ge",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Math/Simplex.lean",
      "start": 14378
    },
    {
      "body": "theorem le_iff_simplex_le {f : I \u2192 \ud835\udd5c} {v : \ud835\udd5c} :\n    (\u2200 i, f i \u2264 v) \u2194 \u2200 x : stdSimplex \ud835\udd5c I, wsum x f \u2264 v := by\n  classical\n  refine \u27e8fun hi x => ?_, fun H i => ?_\u27e9\n  \u00b7 calc wsum x f \u2264 wsum x (fun _ => v) := wsum_le_wsum x hi\n      _ = v := wsum_const x v\n  \u00b7 simpa using H (stdSimplex.pure i)\n\n/-! ### Continuity (over \u211d)\n\nFor the simplified Loomis route we need that `x \u21a6 wsum x f` is continuous on\n`stdSimplex \u211d I`. The Mathlib instance `stdSimplex.instCompactSpace_coe` then\nhands us compactness \"for free\", which is the workhorse for existence of\noptimal mixed strategies. -/\n\nsection Topology\nvariable {I : Type*} [Fintype I]\n\n/-- The `i`-th coordinate projection on `stdSimplex \u211d I` is continuous. -/\n",
      "column": 1,
      "end": 15450,
      "kind": "theorem",
      "line": 350,
      "module": "EconCSLib.Math.Simplex",
      "name": "le_iff_simplex_le",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Math/Simplex.lean",
      "start": 14744
    },
    {
      "body": "theorem stdSimplex.continuous_coord (i : I) :\n    Continuous fun x : stdSimplex \u211d I => x.val i :=\n  (continuous_apply i).comp continuous_subtype_val\n\n/-- `wsum (\u00b7) f` is continuous on the standard simplex over \u211d. -/\n",
      "column": 1,
      "end": 15666,
      "kind": "theorem",
      "line": 369,
      "module": "EconCSLib.Math.Simplex",
      "name": "stdSimplex.continuous_coord",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Math/Simplex.lean",
      "start": 15450
    },
    {
      "body": "theorem wsum_continuous (f : I \u2192 \u211d) :\n    Continuous fun x : stdSimplex \u211d I => wsum x f :=\n  continuous_finset_sum _ fun i _ =>\n    (stdSimplex.continuous_coord i).mul continuous_const\n\nend Topology\n\n/-! ### Matrix-game expected payoff\n\n`expectedPayoffMatrix` was previously in `StrategicGame.Simplex`. It is placed\nhere because it is a purely arithmetic definition (bilinear evaluation on the\nsimplex) with no strategic-game vocabulary. -/\n\nvariable {J : Type*}\n\nopen Matrix\n\n/-- Expected payoff in a matrix game `A : I \u2192 J \u2192 \ud835\udd5c` under mixed strategies. -/\n",
      "column": 1,
      "end": 16223,
      "kind": "theorem",
      "line": 374,
      "module": "EconCSLib.Math.Simplex",
      "name": "wsum_continuous",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Math/Simplex.lean",
      "start": 15666
    },
    {
      "body": "def expectedPayoffMatrix (A : I \u2192 J \u2192 \ud835\udd5c) [Fintype J]\n    (x : stdSimplex \ud835\udd5c I) (y : stdSimplex \ud835\udd5c J) : \ud835\udd5c :=\n  x \u2b1d\u1d65 fun i => y \u2b1d\u1d65 A i\n\n/-- Expected payoff is commutative in the summation order. -/\n",
      "column": 1,
      "end": 16417,
      "kind": "def",
      "line": 392,
      "module": "EconCSLib.Math.Simplex",
      "name": "expectedPayoffMatrix",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Math/Simplex.lean",
      "start": 16223
    },
    {
      "body": "theorem expectedPayoffMatrix_comm {J : Type*} [Fintype J]\n    (A : I \u2192 J \u2192 \ud835\udd5c) (x : stdSimplex \ud835\udd5c I) (y : stdSimplex \ud835\udd5c J) :\n    expectedPayoffMatrix A x y =\n    y \u2b1d\u1d65 fun j => x \u2b1d\u1d65 fun i => A i j := by\n  simpa [expectedPayoffMatrix, wsum] using wsum_wsum_comm x y A\n",
      "column": 1,
      "end": 16680,
      "kind": "theorem",
      "line": 397,
      "module": "EconCSLib.Math.Simplex",
      "name": "expectedPayoffMatrix_comm",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Math/Simplex.lean",
      "start": 16417
    }
  ]
}
```

## Intent

- Lean is acting as a counterchecker only.
- Blank or flawed proofs are recorded as incompleteness, not inconsistency.
- Any new lemmata discovered here are proposals for review, not automatic edits.