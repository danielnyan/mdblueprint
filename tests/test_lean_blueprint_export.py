from __future__ import annotations

import subprocess
import textwrap
from pathlib import Path

import yaml

from tools.knowledge.lean_blueprint_export import export_blueprint_tree
from tools.knowledge.parser import parse_file


def _write_lean_repo(root: Path) -> None:
    (root / 'Analysis').mkdir(parents=True)
    (root / 'Analysis' / 'Main.lean').write_text(
        textwrap.dedent('''
            namespace Analysis

            theorem base : True := by
              trivial

            theorem result : True := by
              exact base

            end Analysis
            ''').strip() + '\n',
        encoding='utf-8',
    )
    subprocess.run(['git', 'init'], cwd=root, check=True, capture_output=True)
    subprocess.run(['git', 'config', 'user.email', 'test@example.test'], cwd=root, check=True)
    subprocess.run(['git', 'config', 'user.name', 'Test User'], cwd=root, check=True)
    subprocess.run(['git', 'remote', 'add', 'origin', 'https://github.com/example/lean-repo.git'], cwd=root, check=True)
    subprocess.run(['git', 'add', '.'], cwd=root, check=True)
    subprocess.run(['git', 'commit', '-m', 'fixture'], cwd=root, check=True, capture_output=True)


def _write_source_tree(root: Path, *, with_config: bool) -> None:
    nodes = root / 'nodes' / 'analysis'
    nodes.mkdir(parents=True)
    if with_config:
        (root / 'mdblueprint.yml').write_text(
            textwrap.dedent('''
                site:
                  title: Analysis Blueprint
                ''').strip() + '\n',
            encoding='utf-8',
        )
    base = textwrap.dedent('''
        ---
        id: analysis.base
        title: Base
        kind: theorem
        status: admitted
        uses: []
        primary_topic: analysis
        topics:
          - analysis
        lean:
          modules:
            - Analysis.Main
          declarations:
            - Analysis.base
        ---

        # Base
        ''').strip() + '\n'
    result = textwrap.dedent('''
        ---
        id: analysis.result
        title: Result
        kind: theorem
        status: admitted
        uses: []
        primary_topic: analysis
        topics:
          - analysis
        lean:
          modules:
            - Analysis.Main
          declarations:
            - Analysis.result
        ---

        # Result
        ''').strip() + '\n'
    (nodes / 'base.md').write_text(base, encoding='utf-8')
    (nodes / 'result.md').write_text(result, encoding='utf-8')
    (root / 'nodes' / 'topics.md').write_text('# analysis\n', encoding='utf-8')


def test_export_builds_config_and_infers_uses_from_existing_source_config(tmp_path):
    lean_root = tmp_path / 'lean_repo'
    source_root = tmp_path / 'source'
    output_root = tmp_path / 'output'
    _write_lean_repo(lean_root)
    _write_source_tree(source_root, with_config=True)

    result = export_blueprint_tree(lean_root, source_root, output_root)

    assert result.config_generated is False
    assert result.node_count == 2
    assert result.final_edge_count == 1
    config = yaml.safe_load((output_root / 'mdblueprint.yml').read_text(encoding='utf-8'))
    assert config['site']['title'] == 'Analysis Blueprint'
    assert config['topics'][0]['id'] == 'analysis'
    assert config['lean']['default_repository'] == 'default'
    assert config['lean']['repositories'][0]['web_url'] == 'https://github.com/example/lean-repo'
    exported = parse_file(output_root / 'nodes' / 'analysis' / 'result.md')
    assert exported.uses == ['analysis.base']


def test_export_falls_back_to_lean_config_when_source_config_is_missing(tmp_path):
    lean_root = tmp_path / 'lean_repo'
    source_root = tmp_path / 'source'
    output_root = tmp_path / 'output'
    _write_lean_repo(lean_root)
    _write_source_tree(source_root, with_config=False)

    result = export_blueprint_tree(lean_root, source_root, output_root)

    assert result.config_generated is True
    config = yaml.safe_load((output_root / 'mdblueprint.yml').read_text(encoding='utf-8'))
    assert config['site']['title'] == 'Lean Repo'
    assert config['lean']['default_repository'] == 'default'
    assert config['lean']['repositories'][0]['id'] == 'default'
    assert config['topics'][0]['id'] == 'analysis'
    exported = parse_file(output_root / 'nodes' / 'analysis' / 'result.md')
    assert exported.uses == ['analysis.base']
