---
agent: lean-countercheck
node_id: social_choice.fair_division.indivisible.cardinal_instance
created_at: "2026-06-15T06:18:32+00:00"
---

# Lean Countercheck: Indivisible Cardinal Instance

## Inputs

- node file: `/home/azureuser/EconCSLib/docs/knowledge/nodes/social_choice/fair_division/indivisible/cardinal_instance.md`
- lean file: `/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Indivisible/Instance.lean`
- corpus root: `/home/azureuser/EconCSLib`

## Method Status

- heuristic: used

## Matched Declarations

- `SocialChoice.FairDivision.Indivisible.CardinalInstance.toValuation`
- `SocialChoice.FairDivision.Indivisible.CardinalInstance.toGenericCardinalInstance`
- `SocialChoice.FairDivision.Indivisible.CardinalInstance.toShareInstance`
- `SocialChoice.FairDivision.Indivisible.CardinalInstance.IsEnvyFree`
- `SocialChoice.FairDivision.Indivisible.CardinalInstance.IsEF1`
- `SocialChoice.FairDivision.Indivisible.CardinalInstance.IsEFX`
- `SocialChoice.FairDivision.Indivisible.CardinalInstance.IsProportional`
- `SocialChoice.FairDivision.Indivisible.CardinalInstance.IsEquitable`
- `SocialChoice.FairDivision.Indivisible.CardinalInstance.IsMaxminShare`
- `SocialChoice.FairDivision.Indivisible.CardinalInstance.IsParetoOptimal`
- `SocialChoice.FairDivision.Indivisible.CardinalInstance.IsUtilitarianOptimal`
- `SocialChoice.FairDivision.Indivisible.CardinalInstance.IsMaxmin`

## Missing Declarations

- `SocialChoice.FairDivision.Indivisible.CardinalInstance`

## Extra Declarations

- `feasible`
- `feasible`
- `toAdditiveValuation`
- `toCardinalInstance`
- `feasible`

## Node Uses vs Extracted Dependencies

- node uses: `social_choice.fair_division.indivisible.valuation`, `social_choice.fair_division.cardinal_instance`, `social_choice.fair_division.envy_free`, `social_choice.fair_division.proportional`, `social_choice.fair_division.utilitarian_welfare`, `social_choice.fair_division.egalitarian_welfare`
- missing uses: `social_choice.fair_division.indivisible.valuation`, `social_choice.fair_division.cardinal_instance`, `social_choice.fair_division.envy_free`, `social_choice.fair_division.proportional`, `social_choice.fair_division.utilitarian_welfare`, `social_choice.fair_division.egalitarian_welfare`
- extra uses: `toAdditiveValuation`, `toCardinalInstance`, `toGenericCardinalInstance`, `toValuation`

## Raw Snapshot

```json
{
  "corpus_root": "/home/azureuser/EconCSLib",
  "dependencies": [
    {
      "kind": "hard",
      "module": "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance",
      "source": "toShareInstance",
      "target": "toGenericCardinalInstance"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance",
      "source": "IsEnvyFree",
      "target": "toValuation"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance",
      "source": "IsEF1",
      "target": "toValuation"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance",
      "source": "IsEFX",
      "target": "toValuation"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance",
      "source": "IsProportional",
      "target": "toValuation"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance",
      "source": "IsEquitable",
      "target": "toValuation"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance",
      "source": "IsMaxminShare",
      "target": "toValuation"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance",
      "source": "IsParetoOptimal",
      "target": "toValuation"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance",
      "source": "IsUtilitarianOptimal",
      "target": "toValuation"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance",
      "source": "IsMaxmin",
      "target": "toValuation"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance",
      "source": "toValuation",
      "target": "toAdditiveValuation"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance",
      "source": "toCardinalInstance",
      "target": "toValuation"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance",
      "source": "toGenericCardinalInstance",
      "target": "toCardinalInstance"
    }
  ],
  "lean_file": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Indivisible/Instance.lean",
  "method_status": {
    "heuristic": "used"
  },
  "node": {
    "body": "# Indivisible Cardinal Instance\n\nAn *indivisible cardinal instance* assigns each agent a real-valued\nutility for every bundle:\n$$\n\\mathrm{utility} : N \\to \\mathrm{Finset}\\ G \\to \\mathbb{R}.\n$$\n\nIn Lean: structure `SocialChoice.FairDivision.Indivisible.CardinalInstance N G`\nwith a `utility` field plus the outer good set `allGoods : Finset G`.\n\n## Bridges\n\n- `toValuation` \u2014 wrap as a bare `Valuation`\n  ([[social_choice.fair_division.indivisible.valuation]]).\n- `toGenericCardinalInstance` \u2014 view as a generic real-valued cardinal\n  fair-division instance ([[social_choice.fair_division.cardinal_instance]])\n  over share type $\\mathrm{Finset}\\ G$ and resource value `allGoods`.\n- `toShareInstance` \u2014 compose with `inducedSharePref` to get the\n  underlying indivisible ordinal instance\n  ([[social_choice.fair_division.indivisible.ordinal_instance]]).\n\n## Instance-keyed wrappers\n\nA full menu of instance-keyed fairness and welfare predicates is\nre-exported:\n\n- `IsEnvyFree`, `IsEF1`, `IsEFX`, `IsProportional`, `IsEquitable`,\n  `IsMaxminShare` \u2014 fairness predicates.\n- `IsParetoOptimal`, `IsUtilitarianOptimal`, `IsMaxmin` \u2014 efficiency\n  / welfare-optimality predicates.\n\nAll wrappers are definitional pass-throughs to the corresponding\ngeneric or `Indivisible`-prefixed predicates with $I.\\mathrm{utility}$\nand feasibility supplied from the instance.\n\n## References\n\n- [AGT Chapter 11] Nisan, Roughgarden, Tardos, and Vazirani, *Algorithmic Game Theory*. Cardinal valuations in indivisible fair division.",
    "file_path": "/home/azureuser/EconCSLib/docs/knowledge/nodes/social_choice/fair_division/indivisible/cardinal_instance.md",
    "id": "social_choice.fair_division.indivisible.cardinal_instance",
    "kind": "definition",
    "lean": {
      "declarations": [
        "SocialChoice.FairDivision.Indivisible.CardinalInstance",
        "SocialChoice.FairDivision.Indivisible.CardinalInstance.toValuation",
        "SocialChoice.FairDivision.Indivisible.CardinalInstance.toGenericCardinalInstance",
        "SocialChoice.FairDivision.Indivisible.CardinalInstance.toShareInstance",
        "SocialChoice.FairDivision.Indivisible.CardinalInstance.IsEnvyFree",
        "SocialChoice.FairDivision.Indivisible.CardinalInstance.IsEF1",
        "SocialChoice.FairDivision.Indivisible.CardinalInstance.IsEFX",
        "SocialChoice.FairDivision.Indivisible.CardinalInstance.IsProportional",
        "SocialChoice.FairDivision.Indivisible.CardinalInstance.IsEquitable",
        "SocialChoice.FairDivision.Indivisible.CardinalInstance.IsMaxminShare",
        "SocialChoice.FairDivision.Indivisible.CardinalInstance.IsParetoOptimal",
        "SocialChoice.FairDivision.Indivisible.CardinalInstance.IsUtilitarianOptimal",
        "SocialChoice.FairDivision.Indivisible.CardinalInstance.IsMaxmin"
      ],
      "modules": [
        "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance"
      ],
      "repository": null
    },
    "status": "formalized",
    "tags": [
      "fair-division",
      "indivisible",
      "instance",
      "cardinal"
    ],
    "title": "Indivisible Cardinal Instance",
    "uses": [
      "social_choice.fair_division.indivisible.valuation",
      "social_choice.fair_division.cardinal_instance",
      "social_choice.fair_division.envy_free",
      "social_choice.fair_division.proportional",
      "social_choice.fair_division.utilitarian_welfare",
      "social_choice.fair_division.egalitarian_welfare"
    ]
  },
  "source_root": "/home/azureuser/EconCSLib",
  "theorems": [
    {
      "body": "def feasible {N G : Type*} [Fintype N] [DecidableEq G]\n    (I : Instance N G) (A : Allocation N G) : Prop :=\n  IsAllocation I.allGoods A\n\n/-- View an indivisible ordinal instance as a generic no-externality\n    fair-division share instance. -/\n",
      "column": 1,
      "end": 1647,
      "kind": "theorem",
      "line": 43,
      "module": "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance",
      "name": "feasible",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Indivisible/Instance.lean",
      "start": 1403
    },
    {
      "body": "def toShareInstance {N G : Type*} [Fintype N] [DecidableEq G]\n    (I : Instance N G) :\n    SocialChoice.FairDivision.ShareInstance N (Finset G) (Finset G) where\n  resource := I.allGoods\n  feasible := fun A => IsAllocation I.allGoods A\n  sharePref := I.sharePref\n\nend Instance\n\n/-- A real-valued cardinal indivisible-goods instance. -/\nstructure CardinalInstance (N G : Type*) where\n  /-- The goods that must be allocated. -/\n  allGoods : Finset G\n  /-- Utility assigned by each agent to each bundle. -/\n  utility : N \u2192 Finset G \u2192 \u211d\n\nnamespace CardinalInstance\n\n/-- The raw valuation induced by a cardinal indivisible instance. -/\n",
      "column": 1,
      "end": 2277,
      "kind": "theorem",
      "line": 49,
      "module": "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance",
      "name": "toShareInstance",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Indivisible/Instance.lean",
      "start": 1647
    },
    {
      "body": "def toValuation {N G : Type*}\n    (I : CardinalInstance N G) : Valuation N G where\n  val := I.utility\n\n/-- Feasibility for a cardinal indivisible instance. -/\n",
      "column": 1,
      "end": 2436,
      "kind": "theorem",
      "line": 68,
      "module": "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance",
      "name": "toValuation",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Indivisible/Instance.lean",
      "start": 2277
    },
    {
      "body": "def feasible {N G : Type*} [Fintype N] [DecidableEq G]\n    (I : CardinalInstance N G) (A : Allocation N G) : Prop :=\n  IsAllocation I.allGoods A\n\n/-- View an indivisible cardinal instance as a generic real-valued cardinal\n    fair-division instance. -/\n",
      "column": 1,
      "end": 2689,
      "kind": "theorem",
      "line": 73,
      "module": "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance",
      "name": "feasible",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Indivisible/Instance.lean",
      "start": 2436
    },
    {
      "body": "def toGenericCardinalInstance {N G : Type*} [Fintype N] [DecidableEq G]\n    (I : CardinalInstance N G) :\n    SocialChoice.FairDivision.CardinalInstance N (Finset G) (Finset G) where\n  resource := I.allGoods\n  feasible := fun A => IsAllocation I.allGoods A\n  utility := I.utility\n\n/-- View an indivisible cardinal instance as the induced generic ordinal\n    no-externality instance. -/\n",
      "column": 1,
      "end": 3074,
      "kind": "theorem",
      "line": 79,
      "module": "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance",
      "name": "toGenericCardinalInstance",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Indivisible/Instance.lean",
      "start": 2689
    },
    {
      "body": "def toShareInstance {N G : Type*} [Fintype N] [DecidableEq G]\n    (I : CardinalInstance N G) :\n    SocialChoice.FairDivision.ShareInstance N (Finset G) (Finset G) :=\n  I.toGenericCardinalInstance.toShareInstance\n\n/-! ### Instance-relative fairness and welfare wrappers -/\n\n/-- Envy-freeness for an indivisible cardinal instance. -/\n",
      "column": 1,
      "end": 3406,
      "kind": "theorem",
      "line": 88,
      "module": "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance",
      "name": "toShareInstance",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Indivisible/Instance.lean",
      "start": 3074
    },
    {
      "body": "def IsEnvyFree {N G : Type*}\n    (I : CardinalInstance N G) (A : Allocation N G) : Prop :=\n  SocialChoice.FairDivision.Indivisible.IsEnvyFree I.toValuation A\n\n/-- Envy-freeness up to one good for an indivisible cardinal instance. -/\n",
      "column": 1,
      "end": 3639,
      "kind": "theorem",
      "line": 96,
      "module": "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance",
      "name": "IsEnvyFree",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Indivisible/Instance.lean",
      "start": 3406
    },
    {
      "body": "def IsEF1 {N G : Type*} [DecidableEq G]\n    (I : CardinalInstance N G) (A : Allocation N G) : Prop :=\n  SocialChoice.FairDivision.Indivisible.IsEF1 I.toValuation A\n\n/-- Envy-freeness up to any good for an indivisible cardinal instance. -/\n",
      "column": 1,
      "end": 3878,
      "kind": "theorem",
      "line": 101,
      "module": "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance",
      "name": "IsEF1",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Indivisible/Instance.lean",
      "start": 3639
    },
    {
      "body": "def IsEFX {N G : Type*} [DecidableEq G]\n    (I : CardinalInstance N G) (A : Allocation N G) : Prop :=\n  SocialChoice.FairDivision.Indivisible.IsEFX I.toValuation A\n\n/-- Proportionality for an indivisible cardinal instance, relative to the\n    instance's full set of goods. -/\n",
      "column": 1,
      "end": 4154,
      "kind": "theorem",
      "line": 106,
      "module": "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance",
      "name": "IsEFX",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Indivisible/Instance.lean",
      "start": 3878
    },
    {
      "body": "def IsProportional {N G : Type*}\n    (I : CardinalInstance N G) (n : \u2115) (A : Allocation N G) : Prop :=\n  SocialChoice.FairDivision.Indivisible.IsProportional n I.toValuation I.allGoods A\n\n/-- Equitability for an indivisible cardinal instance. -/\n",
      "column": 1,
      "end": 4400,
      "kind": "theorem",
      "line": 112,
      "module": "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance",
      "name": "IsProportional",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Indivisible/Instance.lean",
      "start": 4154
    },
    {
      "body": "def IsEquitable {N G : Type*}\n    (I : CardinalInstance N G) (A : Allocation N G) : Prop :=\n  SocialChoice.FairDivision.Indivisible.IsEquitable I.toValuation A\n\n/-- Maximin-share guarantee for an indivisible cardinal instance. -/\n",
      "column": 1,
      "end": 4630,
      "kind": "theorem",
      "line": 117,
      "module": "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance",
      "name": "IsEquitable",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Indivisible/Instance.lean",
      "start": 4400
    },
    {
      "body": "def IsMaxminShare {N G : Type*} [Fintype N] [DecidableEq G]\n    (I : CardinalInstance N G) (A : Allocation N G) : Prop :=\n  SocialChoice.FairDivision.Indivisible.IsMaxminShare I.toValuation I.allGoods A\n\n/-- Pareto optimality for an indivisible cardinal instance. -/\n",
      "column": 1,
      "end": 4897,
      "kind": "theorem",
      "line": 122,
      "module": "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance",
      "name": "IsMaxminShare",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Indivisible/Instance.lean",
      "start": 4630
    },
    {
      "body": "def IsParetoOptimal {N G : Type*} [Fintype N] [DecidableEq G]\n    (I : CardinalInstance N G) (A : Allocation N G) : Prop :=\n  SocialChoice.FairDivision.Indivisible.IsParetoOptimal I.toValuation I.allGoods A\n\n/-- Utilitarian welfare for an indivisible cardinal instance. -/\nnoncomputable def utilitarianWelfare {N G : Type*} [Fintype N]\n    (I : CardinalInstance N G) (A : Allocation N G) : \u211d :=\n  SocialChoice.FairDivision.Indivisible.utilitarianWelfare I.toValuation A\n\n/-- Egalitarian welfare for an indivisible cardinal instance. -/\nnoncomputable def egalitarianWelfare {N G : Type*} [Fintype N] [Nonempty N]\n    (I : CardinalInstance N G) (A : Allocation N G) : \u211d :=\n  SocialChoice.FairDivision.Indivisible.egalitarianWelfare I.toValuation A\n\n/-- Utilitarian optimality for an indivisible cardinal instance. -/\n",
      "column": 1,
      "end": 5712,
      "kind": "theorem",
      "line": 127,
      "module": "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance",
      "name": "IsParetoOptimal",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Indivisible/Instance.lean",
      "start": 4897
    },
    {
      "body": "def IsUtilitarianOptimal {N G : Type*} [Fintype N] [DecidableEq G]\n    (I : CardinalInstance N G) (A : Allocation N G) : Prop :=\n  SocialChoice.FairDivision.Indivisible.IsUtilitarianOptimal I.toValuation I.allGoods A\n\n/-- Maximin social-welfare optimality for an indivisible cardinal instance. -/\n",
      "column": 1,
      "end": 6009,
      "kind": "theorem",
      "line": 142,
      "module": "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance",
      "name": "IsUtilitarianOptimal",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Indivisible/Instance.lean",
      "start": 5712
    },
    {
      "body": "def IsMaxmin {N G : Type*} [Fintype N] [Nonempty N] [DecidableEq G]\n    (I : CardinalInstance N G) (A : Allocation N G) : Prop :=\n  SocialChoice.FairDivision.Indivisible.IsMaxmin I.toValuation I.allGoods A\n\nend CardinalInstance\n\n/-- An additive indivisible-goods instance, represented by per-item weights. -/\nstructure AdditiveInstance (N G : Type*) where\n  /-- The goods that must be allocated. -/\n  allGoods : Finset G\n  /-- Per-agent, per-good weights. -/\n  weight : N \u2192 G \u2192 \u211d\n\nnamespace AdditiveInstance\n\n/-- The raw additive valuation induced by additive per-item weights. -/\n",
      "column": 1,
      "end": 6590,
      "kind": "theorem",
      "line": 147,
      "module": "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance",
      "name": "IsMaxmin",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Indivisible/Instance.lean",
      "start": 6009
    },
    {
      "body": "def toAdditiveValuation {N G : Type*}\n    (I : AdditiveInstance N G) : AdditiveValuation N G where\n  weight := I.weight\n\n/-- The abstract valuation induced by additive per-item weights. -/\n",
      "column": 1,
      "end": 6779,
      "kind": "theorem",
      "line": 163,
      "module": "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance",
      "name": "toAdditiveValuation",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Indivisible/Instance.lean",
      "start": 6590
    },
    {
      "body": "def toValuation {N G : Type*}\n    (I : AdditiveInstance N G) : Valuation N G :=\n  I.toAdditiveValuation.toValuation\n\n/-- The cardinal instance induced by additive per-item weights. -/\n",
      "column": 1,
      "end": 6963,
      "kind": "theorem",
      "line": 168,
      "module": "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance",
      "name": "toValuation",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Indivisible/Instance.lean",
      "start": 6779
    },
    {
      "body": "def toCardinalInstance {N G : Type*}\n    (I : AdditiveInstance N G) : CardinalInstance N G where\n  allGoods := I.allGoods\n  utility := I.toValuation.val\n\n/-- View an additive indivisible instance as a generic real-valued cardinal\n    fair-division instance. -/\n",
      "column": 1,
      "end": 7224,
      "kind": "theorem",
      "line": 173,
      "module": "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance",
      "name": "toCardinalInstance",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Indivisible/Instance.lean",
      "start": 6963
    },
    {
      "body": "def toGenericCardinalInstance {N G : Type*} [Fintype N] [DecidableEq G]\n    (I : AdditiveInstance N G) :\n    SocialChoice.FairDivision.CardinalInstance N (Finset G) (Finset G) :=\n  I.toCardinalInstance.toGenericCardinalInstance\n\n/-- View an additive indivisible instance as the induced generic ordinal\n    no-externality instance. -/\n",
      "column": 1,
      "end": 7558,
      "kind": "theorem",
      "line": 180,
      "module": "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance",
      "name": "toGenericCardinalInstance",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Indivisible/Instance.lean",
      "start": 7224
    },
    {
      "body": "def toShareInstance {N G : Type*} [Fintype N] [DecidableEq G]\n    (I : AdditiveInstance N G) :\n    SocialChoice.FairDivision.ShareInstance N (Finset G) (Finset G) :=\n  I.toGenericCardinalInstance.toShareInstance\n\n/-! ### Instance-relative fairness wrappers -/\n\n/-- Envy-freeness for an additive indivisible instance. -/\n",
      "column": 1,
      "end": 7878,
      "kind": "theorem",
      "line": 187,
      "module": "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance",
      "name": "toShareInstance",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Indivisible/Instance.lean",
      "start": 7558
    },
    {
      "body": "def IsEnvyFree {N G : Type*}\n    (I : AdditiveInstance N G) (A : Allocation N G) : Prop :=\n  SocialChoice.FairDivision.Indivisible.IsEnvyFree I.toValuation A\n\n/-- Envy-freeness up to one good for an additive indivisible instance. -/\n",
      "column": 1,
      "end": 8111,
      "kind": "theorem",
      "line": 195,
      "module": "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance",
      "name": "IsEnvyFree",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Indivisible/Instance.lean",
      "start": 7878
    },
    {
      "body": "def IsEF1 {N G : Type*} [DecidableEq G]\n    (I : AdditiveInstance N G) (A : Allocation N G) : Prop :=\n  SocialChoice.FairDivision.Indivisible.IsEF1 I.toValuation A\n\n/-- Envy-freeness up to any good for an additive indivisible instance. -/\n",
      "column": 1,
      "end": 8350,
      "kind": "theorem",
      "line": 200,
      "module": "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance",
      "name": "IsEF1",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Indivisible/Instance.lean",
      "start": 8111
    },
    {
      "body": "def IsEFX {N G : Type*} [DecidableEq G]\n    (I : AdditiveInstance N G) (A : Allocation N G) : Prop :=\n  SocialChoice.FairDivision.Indivisible.IsEFX I.toValuation A\n\n/-- Proportionality for an additive indivisible instance. -/\n",
      "column": 1,
      "end": 8576,
      "kind": "theorem",
      "line": 205,
      "module": "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance",
      "name": "IsEFX",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Indivisible/Instance.lean",
      "start": 8350
    },
    {
      "body": "def IsProportional {N G : Type*}\n    (I : AdditiveInstance N G) (n : \u2115) (A : Allocation N G) : Prop :=\n  SocialChoice.FairDivision.Indivisible.IsProportional n I.toValuation I.allGoods A\n\n/-- Equitability for an additive indivisible instance. -/\n",
      "column": 1,
      "end": 8822,
      "kind": "theorem",
      "line": 210,
      "module": "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance",
      "name": "IsProportional",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Indivisible/Instance.lean",
      "start": 8576
    },
    {
      "body": "def IsEquitable {N G : Type*}\n    (I : AdditiveInstance N G) (A : Allocation N G) : Prop :=\n  SocialChoice.FairDivision.Indivisible.IsEquitable I.toValuation A\n\n/-- Maximin-share guarantee for an additive indivisible instance. -/\n",
      "column": 1,
      "end": 9052,
      "kind": "theorem",
      "line": 215,
      "module": "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance",
      "name": "IsEquitable",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Indivisible/Instance.lean",
      "start": 8822
    },
    {
      "body": "def IsMaxminShare {N G : Type*} [Fintype N] [DecidableEq G]\n    (I : AdditiveInstance N G) (A : Allocation N G) : Prop :=\n  SocialChoice.FairDivision.Indivisible.IsMaxminShare I.toValuation I.allGoods A\n\n/-- Pareto optimality for an additive indivisible instance. -/\n",
      "column": 1,
      "end": 9319,
      "kind": "theorem",
      "line": 220,
      "module": "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance",
      "name": "IsMaxminShare",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Indivisible/Instance.lean",
      "start": 9052
    },
    {
      "body": "def IsParetoOptimal {N G : Type*} [Fintype N] [DecidableEq G]\n    (I : AdditiveInstance N G) (A : Allocation N G) : Prop :=\n  SocialChoice.FairDivision.Indivisible.IsParetoOptimal I.toValuation I.allGoods A\n\n/-- Utilitarian welfare for an additive indivisible instance. -/\nnoncomputable def utilitarianWelfare {N G : Type*} [Fintype N]\n    (I : AdditiveInstance N G) (A : Allocation N G) : \u211d :=\n  SocialChoice.FairDivision.Indivisible.utilitarianWelfare I.toValuation A\n\n/-- Egalitarian welfare for an additive indivisible instance. -/\nnoncomputable def egalitarianWelfare {N G : Type*} [Fintype N] [Nonempty N]\n    (I : AdditiveInstance N G) (A : Allocation N G) : \u211d :=\n  SocialChoice.FairDivision.Indivisible.egalitarianWelfare I.toValuation A\n\n/-- Utilitarian optimality for an additive indivisible instance. -/\n",
      "column": 1,
      "end": 10134,
      "kind": "theorem",
      "line": 225,
      "module": "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance",
      "name": "IsParetoOptimal",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Indivisible/Instance.lean",
      "start": 9319
    },
    {
      "body": "def IsUtilitarianOptimal {N G : Type*} [Fintype N] [DecidableEq G]\n    (I : AdditiveInstance N G) (A : Allocation N G) : Prop :=\n  SocialChoice.FairDivision.Indivisible.IsUtilitarianOptimal I.toValuation I.allGoods A\n\n/-- Maximin social-welfare optimality for an additive indivisible instance. -/\n",
      "column": 1,
      "end": 10431,
      "kind": "theorem",
      "line": 240,
      "module": "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance",
      "name": "IsUtilitarianOptimal",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Indivisible/Instance.lean",
      "start": 10134
    },
    {
      "body": "def IsMaxmin {N G : Type*} [Fintype N] [Nonempty N] [DecidableEq G]\n    (I : AdditiveInstance N G) (A : Allocation N G) : Prop :=\n  SocialChoice.FairDivision.Indivisible.IsMaxmin I.toValuation I.allGoods A\n\n/-- Feasibility for an additive indivisible instance. -/\n",
      "column": 1,
      "end": 10695,
      "kind": "theorem",
      "line": 245,
      "module": "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance",
      "name": "IsMaxmin",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Indivisible/Instance.lean",
      "start": 10431
    },
    {
      "body": "def feasible {N G : Type*} [Fintype N] [DecidableEq G]\n    (I : AdditiveInstance N G) (A : Allocation N G) : Prop :=\n  IsAllocation I.allGoods A\n\nend AdditiveInstance\n\nend Indivisible\nend FairDivision\nend SocialChoice\n",
      "column": 1,
      "end": 10913,
      "kind": "theorem",
      "line": 250,
      "module": "EconCSLib.SocialChoice.FairDivision.Indivisible.Instance",
      "name": "feasible",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Indivisible/Instance.lean",
      "start": 10695
    }
  ]
}
```

## Intent

- Lean is acting as a counterchecker only.
- Blank or flawed proofs are recorded as incompleteness, not inconsistency.
- Any new lemmata discovered here are proposals for review, not automatic edits.