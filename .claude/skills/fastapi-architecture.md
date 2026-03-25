# Skill: FastAPI Architecture

## Purpose
Provide reusable architectural guidance for FastAPI applications.

## Principles
- Use Router -> Service -> Model/Repository separation
- Keep routes thin and focused on HTTP concerns
- Keep business logic in services
- Keep DB access isolated
- Use schemas for validation and serialization only

## Good Patterns
- one router per domain or resource
- one service per business capability
- shared response helpers if needed
- explicit request and response models
- domain-specific exceptions

## Anti-Patterns
- business logic inside routes
- DB queries directly inside route handlers
- giant service classes doing everything
- schema classes containing business logic
- route functions orchestrating multiple unrelated responsibilities

## Design Heuristics
When implementing a feature, decide:
1. what belongs to the route
2. what belongs to the service
3. what belongs to the schema
4. what belongs to the DB/repository layer
5. what should be reusable

## Route Layer Owns
- request parsing
- dependency injection
- calling service methods
- returning formatted responses

## Service Layer Owns
- business rules
- orchestration
- validation beyond schema-level syntax checks
- permission logic if project pattern supports it

## Data Layer Owns
- create/read/update/delete
- filtering queries
- persistence concerns
- transaction-safe DB interaction
