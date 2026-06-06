# Test Fixture Setup

The knowledge-refresh tests use a local EconCSLib checkout as an
ablation fixture.

Expected layout:

```text
tests/fixtures/econcslib/
  EconCSLib/
  docs/
```

Recommended setup:

```bash
mkdir -p tests/fixtures
ln -s /home/azureuser/EconCSLib tests/fixtures/econcslib
```

If you prefer a copy instead of a symlink, clone EconCSLib into the same
ignored path and keep it out of version control.

The integration tests exercise three checks:

1. `mdblueprint.yml` regeneration
2. topic catalog replication
3. node metadata refresh from Lean declarations
