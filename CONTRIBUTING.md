# Contributing to MAAYA

MAAYA is currently founder-led. The workflow still follows professional engineering standards so that the project remains reviewable and scalable.

## Before committing

```bash
uv run ruff format .
uv run ruff check .
uv run pyright
uv run pytest
```

## Commit style

- `feat:` new customer-facing behavior
- `fix:` bug correction
- `test:` test-only change
- `docs:` documentation
- `refactor:` internal change without behavior change
- `chore:` tooling or maintenance

Never commit `.env`, credentials, tokens, customer information, or generated secrets.
