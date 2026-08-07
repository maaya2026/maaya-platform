# Tuesday — Day 1 Checklist

Time budget: **2–3 focused hours**

## Required outcome

By the end of today:

- MAAYA runs locally.
- `/health`, `/ready`, and `/docs` work.
- All automated checks pass.
- The repository has its first Git commit.
- You can explain what an API endpoint and an HTTP status code are.

## Session plan

### 0:00–0:25 — Install and verify tools

```bash
git --version
uv --version
docker --version
```

Install anything missing. Docker is not needed to run today's code but should be ready for PostgreSQL later this week.

### 0:25–0:45 — Open the project

```bash
cd maaya-platform-day1
uv sync
cp .env.example .env
```

`uv sync` creates `.venv`, resolves dependencies, and produces `uv.lock`.

### 0:45–1:10 — Run MAAYA

```bash
uv run fastapi dev src/maaya/main.py
```

Visit:

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/health
- http://127.0.0.1:8000/ready
- http://127.0.0.1:8000/docs

Change the root message temporarily, observe the response, then undo the change.

### 1:10–1:35 — Run tests and quality checks

```bash
uv run pytest
uv run ruff format --check .
uv run ruff check .
uv run pyright
```

Do not continue until all checks pass. Read the output rather than treating commands as magic.

### 1:35–2:00 — Learn the code

Be able to answer:

1. What does `app = create_application()` produce?
2. What is a route?
3. Why does `/health` return JSON?
4. What does status code 200 mean?
5. Why are settings loaded from environment variables?
6. What does each automated test prove?

### 2:00–2:25 — Create the Git history

```bash
git init
git branch -M main
git add .
git status
git commit -m "chore: initialize MAAYA platform foundation"
```

Check:

```bash
git log --oneline
```

### 2:25–3:00 — Optional stretch

- Create an empty GitHub repository named `maaya-platform`.
- Push `main`.
- Add this description: `AI operations platform for small businesses — built module by module.`
- Add topics: `python`, `fastapi`, `ai`, `saas`, `backend`.

## Do not do today

- Do not add PostgreSQL.
- Do not start authentication.
- Do not redesign the folder structure.
- Do not install extra AI libraries.
- Do not copy code without reading it.
