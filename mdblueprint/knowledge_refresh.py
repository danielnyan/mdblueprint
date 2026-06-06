"""CLI wrapper for generation + verification."""
from __future__ import annotations

from pathlib import Path

from .knowledge_generation import generate_knowledge_tree
from .knowledge_verification import verify_knowledge_tree


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Generate and verify docs/knowledge from Lean sources")
    parser.add_argument("lean_root", type=Path)
    parser.add_argument("output_root", type=Path)
    parser.add_argument("--reference-root", type=Path, default=None)
    parser.add_argument("--verify-against", type=Path, default=None)
    args = parser.parse_args()

    result = generate_knowledge_tree(
        args.lean_root,
        args.output_root,
        reference_root=args.reference_root,
    )
    print(f"generated {result.node_count} nodes")
    if args.verify_against is not None:
        verification = verify_knowledge_tree(args.verify_against, args.output_root)
        print("verification:", "clean" if verification.clean else "dirty")
        for diff in verification.diffs:
            print(diff)


if __name__ == "__main__":
    main()
