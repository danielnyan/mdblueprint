---
agent: lean-countercheck
node_id: market_design.matching.one_to_one.stability
created_at: "2026-06-15T12:50:28+00:00"
---

# Lean Countercheck: Stability (Individual Rationality + No Blocking Pair)

## Inputs

- node file: `/home/azureuser/EconCSLib/docs/knowledge/nodes/market_design/matching/one_to_one/stability.md`
- lean file: `/home/azureuser/EconCSLib/EconCSLib/MarketDesign/Matching/Basic.lean`
- corpus root: `/home/azureuser/EconCSLib`

## Method Status

- heuristic: used

## Matched Declarations

- `Matching.IsBlocking`
- `Matching.IsStable`

## Missing Declarations

- `(none)`

## Extra Declarations

- `IsIndividuallyRational`

## Node Uses vs Extracted Dependencies

- node uses: `market_design.matching.one_to_one.matching`
- missing uses: `market_design.matching.one_to_one.matching`
- extra uses: `IsBlocking`

## Raw Snapshot

```json
{
  "corpus_root": "/home/azureuser/EconCSLib",
  "dependencies": [
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Basic",
      "source": "IsStable",
      "target": "IsBlocking"
    }
  ],
  "lean_file": "/home/azureuser/EconCSLib/EconCSLib/MarketDesign/Matching/Basic.lean",
  "method_status": {
    "heuristic": "used"
  },
  "node": {
    "body": "# Stability of a Matching\n\nLet $\\mu$ be a matching in a one-to-one matching market $(M, W, \\succ)$.\n\n## Individual Rationality\n\n$\\mu$ is **individually rational** if no participant is matched to an\nunacceptable partner:\n\n- For every $i \\in M$: $\\mu(i) = \\bot$ or $\\mu(i) \\succ_i \\bot_i$.\n- For every $j \\in W$: $\\mu^{-1}(j) = \\bot$ or $\\mu^{-1}(j) \\succ_j \\bot_j$.\n\n## Blocking Pair\n\nA pair $(i, j) \\in M \\times W$ **blocks** $\\mu$ if both members strictly\nprefer each other to their current $\\mu$-partner (treating $\\bot$ as the\nlowest-ranked alternative):\n\n- $j \\succ_i \\mu(i)$ (man $i$ prefers $j$ to his current match), AND\n- $i \\succ_j \\mu^{-1}(j)$ (woman $j$ prefers $i$ to her current match).\n\n## Stability\n\n$\\mu$ is **stable** if it is individually rational and admits no blocking pair.\n\nEquivalently, $\\mu$ is stable iff no pair $(i, j)$ would defect by mutually\nbreaking their current commitments and matching with each other.\n\nIn Lean, the three predicates live in `EconCSLib.MarketDesign.Matching.Basic`\nas `Matching.IsIndividuallyRational`, `Matching.IsBlocking`, and\n`Matching.IsStable`.\n\n## References\n\n- [MSZ Ch.22, Defs 22.3\u201322.5] Maschler, Solan, Zamir, *Game Theory*.",
    "file_path": "/home/azureuser/EconCSLib/docs/knowledge/nodes/market_design/matching/one_to_one/stability.md",
    "id": "market_design.matching.one_to_one.stability",
    "kind": "definition",
    "lean": {
      "declarations": [
        "Matching.IsBlocking",
        "Matching.IsStable"
      ],
      "modules": [
        "EconCSLib.MarketDesign.Matching.Basic"
      ],
      "repository": null
    },
    "status": "formalized",
    "tags": [
      "matching",
      "stability",
      "blocking-pair"
    ],
    "title": "Stability (Individual Rationality + No Blocking Pair)",
    "uses": [
      "market_design.matching.one_to_one.matching"
    ]
  },
  "source_root": "/home/azureuser/EconCSLib",
  "theorems": [
    {
      "body": "def IsBlocking (market : MatchingMarket M W) (\u03bc : Matching M W)\n    (m : M) (w : W) : Prop :=\n  strict (market.prefM m) (some w) (\u03bc.matchM m) \u2227\n  strict (market.prefW w) (some m) (\u03bc.matchW w)\n\n/-- A matching is stable if it has no blocking pair. [MSZ 22.5] -/\n",
      "column": 1,
      "end": 2772,
      "kind": "theorem",
      "line": 73,
      "module": "EconCSLib.MarketDesign.Matching.Basic",
      "name": "IsBlocking",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/MarketDesign/Matching/Basic.lean",
      "start": 2512
    },
    {
      "body": "def IsStable (market : MatchingMarket M W) (\u03bc : Matching M W) : Prop :=\n  \u2200 m : M, \u2200 w : W, \u00ac IsBlocking market \u03bc m w\n\n/-- A matching is individually rational if every matched agent strictly prefers\n    their partner to being unmatched. -/\n",
      "column": 1,
      "end": 3012,
      "kind": "theorem",
      "line": 79,
      "module": "EconCSLib.MarketDesign.Matching.Basic",
      "name": "IsStable",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/MarketDesign/Matching/Basic.lean",
      "start": 2772
    },
    {
      "body": "def IsIndividuallyRational (market : MatchingMarket M W) (\u03bc : Matching M W) : Prop :=\n  (\u2200 m : M, \u2200 w : W, \u03bc.matchM m = some w \u2192 strict (market.prefM m) (some w) none) \u2227\n  (\u2200 w : W, \u2200 m : M, \u03bc.matchW w = some m \u2192 strict (market.prefW w) (some m) none)\n\nend Matching\n",
      "column": 1,
      "end": 3278,
      "kind": "theorem",
      "line": 84,
      "module": "EconCSLib.MarketDesign.Matching.Basic",
      "name": "IsIndividuallyRational",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/MarketDesign/Matching/Basic.lean",
      "start": 3012
    }
  ]
}
```

## Intent

- Lean is acting as a counterchecker only.
- Blank or flawed proofs are recorded as incompleteness, not inconsistency.
- Any new lemmata discovered here are proposals for review, not automatic edits.