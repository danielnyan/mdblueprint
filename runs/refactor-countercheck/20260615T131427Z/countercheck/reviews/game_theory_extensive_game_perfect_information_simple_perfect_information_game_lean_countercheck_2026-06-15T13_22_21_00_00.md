---
agent: lean-countercheck
node_id: game_theory.extensive_game.perfect_information.simple_perfect_information_game
created_at: "2026-06-15T13:22:21+00:00"
---

# Lean Countercheck: Simple Perfect-Information Game

## Inputs

- node file: `/home/azureuser/EconCSLib/docs/knowledge/nodes/extensive_game/perfect_information/simple_perfect_information_game.md`
- lean file: `/home/azureuser/EconCSLib/EconCSLib/Examples/SimpleGameTree.lean`
- corpus root: `/home/azureuser/EconCSLib`

## Method Status

- heuristic: used

## Matched Declarations

- `(none)`

## Missing Declarations

- `Examples.SimpleGameTree.sample`
- `Examples.SimpleGameTree.sample_zero_sum`
- `Examples.SimpleGameTree.sample_zermelo_spe`
- `Examples.SimpleGameTree.sample_zermelo_ne`
- `Examples.SimpleGameTree.sample_value_zero_sum`

## Extra Declarations

- `Player`
- `zeroSumLeaf`
- `sample`
- `sample_zero_sum`
- `sample_zermelo_spe`
- `sample_zermelo_ne`
- `sample_zermelo_determinacy`
- `leaf_hasOnlyRootSubgames`
- `leaf_nash_to_spe_on`
- `sample_value_zero_sum`
- `sample_optStrategy_spe_on`
- `sample_strategic_form_has_nash`

## Node Uses vs Extracted Dependencies

- node uses: `game_theory.extensive_game.perfect_information.perfect_information_extensive_game`
- missing uses: `game_theory.extensive_game.perfect_information.perfect_information_extensive_game`
- extra uses: `Player`, `leaf_hasOnlyRootSubgames`, `sample_zero_sum`, `zeroSumLeaf`

## Raw Snapshot

```json
{
  "corpus_root": "/home/azureuser/EconCSLib",
  "dependencies": [
    {
      "kind": "hard",
      "module": "EconCSLib.Examples.SimpleGameTree",
      "source": "zeroSumLeaf",
      "target": "Player"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Examples.SimpleGameTree",
      "source": "sample",
      "target": "zeroSumLeaf"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Examples.SimpleGameTree",
      "source": "sample",
      "target": "Player"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Examples.SimpleGameTree",
      "source": "sample_zero_sum",
      "target": "zeroSumLeaf"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Examples.SimpleGameTree",
      "source": "sample_zero_sum",
      "target": "Player"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Examples.SimpleGameTree",
      "source": "sample_zermelo_spe",
      "target": "Player"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Examples.SimpleGameTree",
      "source": "sample_zermelo_ne",
      "target": "sample_zero_sum"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Examples.SimpleGameTree",
      "source": "sample_zermelo_ne",
      "target": "Player"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Examples.SimpleGameTree",
      "source": "sample_zermelo_determinacy",
      "target": "sample_zero_sum"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Examples.SimpleGameTree",
      "source": "sample_zermelo_determinacy",
      "target": "Player"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Examples.SimpleGameTree",
      "source": "leaf_hasOnlyRootSubgames",
      "target": "Player"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Examples.SimpleGameTree",
      "source": "leaf_nash_to_spe_on",
      "target": "leaf_hasOnlyRootSubgames"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Examples.SimpleGameTree",
      "source": "leaf_nash_to_spe_on",
      "target": "Player"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Examples.SimpleGameTree",
      "source": "sample_value_zero_sum",
      "target": "sample_zero_sum"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Examples.SimpleGameTree",
      "source": "sample_optStrategy_spe_on",
      "target": "Player"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.Examples.SimpleGameTree",
      "source": "sample_strategic_form_has_nash",
      "target": "Player"
    }
  ],
  "lean_file": "/home/azureuser/EconCSLib/EconCSLib/Examples/SimpleGameTree.lean",
  "method_status": {
    "heuristic": "used"
  },
  "node": {
    "body": "# Simple Perfect-Information Game\n\nA two-player perfect-information game is simple if its terminal outcomes are\npartitioned into winning sets $(R_1,R_2)$, where reaching a terminal node in $R_i$\nmeans player $i$ wins and the other player loses.\n\nA winning strategy for player $i$ is a strategy $\\sigma_i$ such that, for every\nopponent strategy $\\sigma_{-i}$,\n$$\n  F(\\sigma_i,\\sigma_{-i})\\in R_i.\n$$\n\n## References\n\n- [MFoGT, Section 6.2.4] Laraki, Renault, and Sorin, *Mathematical Foundations of Game Theory*. Two-player simple game with terminal outcomes partitioned into winners.",
    "file_path": "/home/azureuser/EconCSLib/docs/knowledge/nodes/extensive_game/perfect_information/simple_perfect_information_game.md",
    "id": "game_theory.extensive_game.perfect_information.simple_perfect_information_game",
    "kind": "definition",
    "lean": {
      "declarations": [
        "Examples.SimpleGameTree.sample",
        "Examples.SimpleGameTree.sample_zero_sum",
        "Examples.SimpleGameTree.sample_zermelo_spe",
        "Examples.SimpleGameTree.sample_zermelo_ne",
        "Examples.SimpleGameTree.sample_value_zero_sum"
      ],
      "modules": [
        "EconCSLib.Examples.SimpleGameTree"
      ],
      "repository": null
    },
    "status": "formalized",
    "tags": [
      "extensive-game",
      "determinacy"
    ],
    "title": "Simple Perfect-Information Game",
    "uses": [
      "game_theory.extensive_game.perfect_information.perfect_information_extensive_game"
    ]
  },
  "source_root": "/home/azureuser/EconCSLib",
  "theorems": [
    {
      "body": "abbrev Player := Fin 2\n\n/-- Leaf payoff vector \u2014 Player 0 gets `v`, Player 1 gets `-v` (zero-sum). -/\n",
      "column": 1,
      "end": 1272,
      "kind": "abbrev",
      "line": 45,
      "module": "EconCSLib.Examples.SimpleGameTree",
      "name": "Player",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Examples/SimpleGameTree.lean",
      "start": 1170
    },
    {
      "body": "def zeroSumLeaf (v : \u211a) : Player \u2192 \u211a\n  | \u27e80, _\u27e9 => v\n  | \u27e81, _\u27e9 => -v\n\n/-- The sample game tree (see module docstring). -/\n",
      "column": 1,
      "end": 1395,
      "kind": "def",
      "line": 48,
      "module": "EconCSLib.Examples.SimpleGameTree",
      "name": "zeroSumLeaf",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Examples/SimpleGameTree.lean",
      "start": 1272
    },
    {
      "body": "def sample : GameTree Player \u211a :=\n  Node (1 : Player)                                                         -- B's turn\n    (Node (0 : Player)                                                      -- A's subgame\n      (Leaf (zeroSumLeaf 10))\n      (List.cons (Leaf (zeroSumLeaf (-10))) List.nil))\n    (List.cons (Leaf (zeroSumLeaf 3)) List.nil)\n\n-- Sanity: the game is well-typed.\nexample : GameTree Player \u211a := sample\n\n-- `value` is computable (backward induction over the decidable order `\u2264` on `\u211a`),\n-- so the value evaluates and is machine-checkable on this concrete game.\n#eval value\u2080 sample          -- 3  (B picks min{10, 3} = 3)\n#eval value sample 0         -- 3\n#eval value sample 1         -- -3\n\n/-- The player-0 value of the sample is `3`, checked by computation. -/\nexample : value\u2080 sample = 3 := by decide\n\n/-- The zero-sum predicate holds on the sample game. -/\n",
      "column": 1,
      "end": 2273,
      "kind": "def",
      "line": 53,
      "module": "EconCSLib.Examples.SimpleGameTree",
      "name": "sample",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Examples/SimpleGameTree.lean",
      "start": 1395
    },
    {
      "body": "theorem sample_zero_sum : IsZeroSum sample := by\n  simp [sample, IsZeroSum, zeroSumLeaf]\n\n/-- **Existence of an SPE** for the sample game (via `Kuhn_exists_SPE`). -/\nexample : \u2203 \u03c3 : Strategy Player \u211a, IsSubgamePerfect \u03c3 := Kuhn_exists_SPE\n\n/-- Pure root-scoped SPE existence for the sample (Kuhn's theorem; no zero-sum\n    hypothesis required). -/\n",
      "column": 1,
      "end": 2621,
      "kind": "theorem",
      "line": 73,
      "module": "EconCSLib.Examples.SimpleGameTree",
      "name": "sample_zero_sum",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Examples/SimpleGameTree.lean",
      "start": 2273
    },
    {
      "body": "theorem sample_zermelo_spe : \u2203 \u03c3 : Strategy Player \u211a, IsSubgamePerfectOn \u03c3 sample :=\n  zermelo_exists_pure_SPE sample\n\n/-- Pure root Nash existence for the sample (Kuhn's theorem). -/\n",
      "column": 1,
      "end": 2805,
      "kind": "theorem",
      "line": 81,
      "module": "EconCSLib.Examples.SimpleGameTree",
      "name": "sample_zermelo_spe",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Examples/SimpleGameTree.lean",
      "start": 2621
    },
    {
      "body": "theorem sample_zermelo_ne :\n    \u2203 \u03c3 : Strategy Player \u211a, GameTree.IsNashEquilibrium \u03c3 sample :=\n  zermelo_exists_pure_NE sample\n\n/-- **Zermelo determinacy on the sample**: `optStrategy` is a saddle with value\n    `value\u2080 sample` \u2014 player 0 secures it, player 1 caps it. This is the result\n    that genuinely uses the zero-sum hypothesis `sample_zero_sum`. -/\n",
      "column": 1,
      "end": 3164,
      "kind": "theorem",
      "line": 85,
      "module": "EconCSLib.Examples.SimpleGameTree",
      "name": "sample_zermelo_ne",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Examples/SimpleGameTree.lean",
      "start": 2805
    },
    {
      "body": "theorem sample_zermelo_determinacy :\n    (\u2200 \u03c3' : Strategy Player \u211a, IVariant (1 : Player) optStrategy \u03c3' \u2192\n        value\u2080 sample \u2264 outcome \u03c3' sample 0) \u2227\n    (\u2200 \u03c3' : Strategy Player \u211a, IVariant (0 : Player) optStrategy \u03c3' \u2192\n        outcome \u03c3' sample 0 \u2264 value\u2080 sample) :=\n  zermelo_determinacy sample sample_zero_sum\n\n/-- A one-leaf game has only its root as a subgame. -/\n",
      "column": 1,
      "end": 3537,
      "kind": "theorem",
      "line": 92,
      "module": "EconCSLib.Examples.SimpleGameTree",
      "name": "sample_zermelo_determinacy",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Examples/SimpleGameTree.lean",
      "start": 3164
    },
    {
      "body": "theorem leaf_hasOnlyRootSubgames (p : Player \u2192 \u211a) :\n    HasOnlyRootSubgames (Leaf p : GameTree Player \u211a) := by\n  intro s hsub\n  cases hsub\n  rfl\n\n/-- On a game with no proper subgames, root Nash already gives the corresponding\n    root-scoped subgame-perfect condition. This instantiates the pure finite-tree\n    form of MSZ Theorem 7.4 on a one-leaf game. -/\n",
      "column": 1,
      "end": 3897,
      "kind": "theorem",
      "line": 100,
      "module": "EconCSLib.Examples.SimpleGameTree",
      "name": "leaf_hasOnlyRootSubgames",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Examples/SimpleGameTree.lean",
      "start": 3537
    },
    {
      "body": "theorem leaf_nash_to_spe_on (p : Player \u2192 \u211a) {\u03c3 : Strategy Player \u211a}\n    (hnash : GameTree.IsNashAt \u03c3 (Leaf p)) :\n    IsSubgamePerfectOn \u03c3 (Leaf p) :=\n  hnash.toSubgamePerfectOn_of_hasOnlyRootSubgames (leaf_hasOnlyRootSubgames p)\n\n/-- The backward-induction value of the sample remains zero-sum. -/\n",
      "column": 1,
      "end": 4196,
      "kind": "theorem",
      "line": 109,
      "module": "EconCSLib.Examples.SimpleGameTree",
      "name": "leaf_nash_to_spe_on",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Examples/SimpleGameTree.lean",
      "start": 3897
    },
    {
      "body": "theorem sample_value_zero_sum : (value sample) 0 + (value sample) 1 = 0 :=\n  value_zero_sum sample sample_zero_sum\n\n/-- The backward-induction strategy is subgame-perfect on the sample root. -/\n",
      "column": 1,
      "end": 4390,
      "kind": "theorem",
      "line": 115,
      "module": "EconCSLib.Examples.SimpleGameTree",
      "name": "sample_value_zero_sum",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Examples/SimpleGameTree.lean",
      "start": 4196
    },
    {
      "body": "theorem sample_optStrategy_spe_on :\n    IsSubgamePerfectOn (optStrategy : Strategy Player \u211a) sample :=\n  optStrategy_isSubgamePerfect.toSubgamePerfectOn sample\n\n/-- The extracted strategic-form game has a pure Nash equilibrium, and this is\n    exactly the root-scoped Nash predicate on the original tree. -/\n",
      "column": 1,
      "end": 4698,
      "kind": "theorem",
      "line": 119,
      "module": "EconCSLib.Examples.SimpleGameTree",
      "name": "sample_optStrategy_spe_on",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Examples/SimpleGameTree.lean",
      "start": 4390
    },
    {
      "body": "theorem sample_strategic_form_has_nash :\n    \u2203 \u03c3 : (toStrategicGame sample).Profile,\n      IsNashEquilibrium (toStrategicGame sample) \u03c3 \u2227\n        IsNashAt (profileStrategy \u03c3) sample := by\n  have hprofile : profileStrategy (fun _ => optStrategy : (toStrategicGame sample).Profile) =\n      (optStrategy : Strategy Player \u211a) := rfl\n  refine \u27e8fun _ => optStrategy, ?_, ?_\u27e9\n  \u00b7 exact (toStrategicGame_nash_iff_isNashAt sample (fun _ => optStrategy)).mpr\n      (by simpa [hprofile] using optStrategy_isSubgamePerfect.toNE sample)\n  \u00b7 simpa [hprofile] using optStrategy_isSubgamePerfect.toNE sample\n\nend Examples.SimpleGameTree\n",
      "column": 1,
      "end": 5319,
      "kind": "theorem",
      "line": 125,
      "module": "EconCSLib.Examples.SimpleGameTree",
      "name": "sample_strategic_form_has_nash",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/Examples/SimpleGameTree.lean",
      "start": 4698
    }
  ]
}
```

## Intent

- Lean is acting as a counterchecker only.
- Blank or flawed proofs are recorded as incompleteness, not inconsistency.
- Any new lemmata discovered here are proposals for review, not automatic edits.