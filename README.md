# MAAYA Platform

> **MAAYA — The intelligence behind everything.**

MAAYA is an early-stage AI operations platform for small businesses. The platform will connect communication, knowledge, tasks, meetings, and business workflows while keeping people in control of consequential AI actions.

This repository begins as a **modular monolith**. Each MAAYA product is documented and demonstrated separately, while sharing one maintainable platform, database foundation, and deployment path.

## Day 1 milestone

- Python project managed with `uv`
- FastAPI application
- Typed settings
- Health and readiness endpoints
- Automated API tests
- Ruff linting and formatting
- Pyright static type checking
- Architecture decision-record template

## Prerequisites

- Git
- `uv`
- Docker Desktop (needed later this week, not required for Day 1)
- A GitHub account
- VS Code or another editor

## Start the application

```bash
uv sync
cp .env.example .env
uv run fastapi dev src/maaya/main.py
```

Open:

- API root: http://127.0.0.1:8000/
- Health: http://127.0.0.1:8000/health
- Readiness: http://127.0.0.1:8000/ready
- API documentation: http://127.0.0.1:8000/docs

## Run quality checks

```bash
uv run ruff format --check .
uv run ruff check .
uv run pyright
uv run pytest
```

To apply formatting:

```bash
uv run ruff format .
```

## Suggested first commit

```bash
git init
git branch -M main
git add .
git commit -m "chore: initialize MAAYA platform foundation"
```

Then create a GitHub repository named `maaya-platform` and follow GitHub's instructions to add the remote and push the `main` branch.

## Current architecture

```text
src/maaya/
├── api/
│   ├── router.py
│   └── routes/
│       └── health.py
├── core/
│   └── config.py
└── main.py
```

Future product modules will live under `src/maaya/modules/`, beginning with `workspace/`, followed by `inbox/` and `tasks/`.
