# Getting Started

## Prerequisites

- Claude Code CLI installed
- A FastAPI project (or start a new one)

## Installation

### Option 1 — Shell script

```bash
curl -sSL https://raw.githubusercontent.com/uzairkhatri/claude-fastapi-pack/main/install/install.sh | bash
```

### Option 2 — Python script

```bash
python install/install.py
# or target a specific directory
python install/install.py --dir path/to/your/.claude
```

### Option 3 — Manual

Copy the `.claude/` directory from this repo into your project root.

## Verify installation

After installing, your project's `.claude/` should contain:

```
.claude/
├── agents/
│   ├── fastapi-architect.md
│   ├── api-implementer.md
│   ├── async-reviewer.md
│   ├── migration-guard.md
│   └── pr-reviewer.md
├── commands/
│   ├── design-api.md
│   ├── review-api.md
│   ├── review-async.md
│   ├── check-migration.md
│   └── plan-feature.md
└── skills/
    ├── fastapi-architecture.md
    ├── sqlalchemy-async.md
    ├── alembic-safety.md
    └── rest-response-standard.md
```

## First use

```
/design-api user authentication with JWT
```

See the [Commands Guide](commands-guide.md) for all available commands.
