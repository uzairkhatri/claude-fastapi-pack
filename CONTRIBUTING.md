# Contributing

Contributions welcome — new agents, commands, skills, and example improvements.

## What to contribute

**New agents** — specialist subagents for a focused FastAPI concern (e.g. WebSocket reviewer, background task architect). Add to `.claude/agents/`.

**New commands** — slash commands that invoke one or more agents with a strict output format. Add to `.claude/commands/`.

**New skills** — reusable domain knowledge modules. Should read like a senior engineer's internal wiki page, not documentation. Add to `.claude/skills/`.

**Example improvements** — better before/after examples, additional domain modules in the sample app, new walkthrough scenarios.

## Standards

### Agents
- Clear `## Role` — one sentence
- `## Use this agent when` — bullet list of specific triggers
- `## Output format` — strict structure the agent must follow every time
- `## Rules` — explicit constraints on what the agent should and should not do

### Commands
- `## Agents used` — list which agents this command invokes and why
- `## Output format` — copy the exact markdown structure Claude must produce
- Every section labelled with `##`
- Ends with a `## Verdict` or equivalent single-word outcome

### Skills
- Teach, don't describe. Every concept should include a working code example.
- Include a "Common mistakes" section with before/after snippets.
- No fluff. If a line doesn't help someone write better code, cut it.

## Submitting

1. Fork the repo
2. Create a branch: `feature/agent-name` or `fix/command-name`
3. Add your file(s)
4. Open a PR with:
   - What the addition does
   - Which FastAPI problem it solves
   - A sample output (paste the command output from a real test)

## What gets merged

- Solves a real, recurring FastAPI problem
- Follows the output format standard
- Includes at least one concrete code example
- Does not duplicate an existing agent or command
