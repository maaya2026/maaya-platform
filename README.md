# MAAYA

**The intelligence behind everything.**

MAAYA is an AI operations platform for small businesses.

The long-term goal is to connect fragmented business workflows such as email, tasks, documents, customers, meetings, recruiting, support, sales, and analytics into one intelligent workspace.

## Current Status

MAAYA is currently in active development.

The engineering foundation currently includes:

- Python backend project
- FastAPI API framework
- Health and readiness API endpoints
- Automated tests with pytest
- Code quality checks with Ruff
- Static type checking with Pyright
- Git version control
- GitHub development workflow
- Modular monolith architecture

## Current Product: Workspace & Authorization

The first MAAYA product is the secure workspace and authorization foundation that future MAAYA modules will build on.

Currently under development:

- User authentication
- Business workspaces
- Workspace memberships
- Roles and permissions
- Protected API endpoints
- Tenant isolation
- Audit logging

## Next Product: MAAYA Inbox

MAAYA Inbox will turn business email into organized, actionable work.

Planned capabilities include:

- Email ingestion
- AI email classification
- Summaries and priority detection
- Task and deadline extraction
- Suggested responses
- Human review before important actions

## Architecture

MAAYA is being built initially as a **modular monolith**.

This means the platform uses one integrated codebase while keeping major business capabilities separated into clear modules.

This allows MAAYA to move quickly during early development without introducing unnecessary microservice complexity.

## Technology

### Currently Used

- Python
- FastAPI
- pytest
- Ruff
- Pyright
- Git
- GitHub

### Planned as the platform develops

- PostgreSQL
- SQLAlchemy
- React
- TypeScript
- AWS
- Large Language Model integrations

## Development Philosophy

MAAYA is being developed as both:

1. A real software product for small businesses.
2. A hands-on engineering project demonstrating backend, AI, cloud, security, and software architecture skills.

The platform is being built incrementally, with each major module designed, tested, documented, and integrated into the larger MAAYA system.

---

**MAAYA — The intelligence behind everything.**