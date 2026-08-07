# ADR-0001: Begin MAAYA as a modular monolith

- **Status:** Accepted
- **Date:** 2026-07-14
- **Decision owners:** MAAYA founding team

## Context

MAAYA will contain several independently demonstrable products, including workspace authorization, email intelligence, tasks, knowledge, meetings, and analytics. The platform is currently founder-led and has not yet demonstrated scaling or organizational requirements that justify distributed services.

## Options considered

1. Independent microservice and deployment pipeline for every product
2. One unstructured application
3. A modular monolith with explicit product boundaries

## Decision

Use a modular monolith for the first MAAYA releases.

## Why

It provides one runnable platform, one deployment path, and simpler data consistency, while preserving separate product documentation, modules, tests, APIs, demos, and career stories.

## Consequences

### Positive

- Faster product development
- Lower cloud and operational cost
- Easier local debugging
- Straightforward transactions
- Clear path to integrated customer workflows

### Negative or risky

- Module boundaries require discipline
- A careless implementation could become tightly coupled
- Later extraction may require migration work

## Revisit when

A module requires independent scaling, security boundaries, release cadence, ownership, or a different technology runtime.
