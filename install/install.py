#!/usr/bin/env python3
"""
claude-fastapi-pack installer

Usage:
    python install/install.py
    python install/install.py --dir path/to/.claude
    python install/install.py --merge          # append pack standards to existing CLAUDE.md
"""

import argparse
import sys
import urllib.error
import urllib.request
from pathlib import Path

REPO = "uzairkhatri/claude-fastapi-pack"
BASE_URL = f"https://raw.githubusercontent.com/{REPO}/main/.claude"

AGENTS = ["fastapi-architect", "api-implementer", "async-reviewer", "migration-guard", "pr-reviewer"]
COMMANDS = ["design-api", "review-api", "review-async", "check-migration", "plan-feature"]
SKILLS = ["fastapi-architecture", "sqlalchemy-async", "alembic-safety", "rest-response-standard"]

PACK_SECTION_START = "<!-- claude-fastapi-pack:start -->"
PACK_SECTION_END = "<!-- claude-fastapi-pack:end -->"
PACK_STANDARDS = f"""{PACK_SECTION_START}
# FastAPI Pack Standards

## Architecture
- Router → Service → Repository layering
- Business logic in services only
- DB logic in repositories only

## Async SQLAlchemy
- Never hold DB session during external I/O
- Use flush() within a transaction, commit() to close it
- Eager load relationships — no lazy loading in async context

## Error Handling
- Raise structured HTTPException with consistent detail strings
- Use get_or_raise() pattern in repositories

## Code Review Priorities
- correctness, async safety, maintainability, scalability, naming clarity
{PACK_SECTION_END}"""

GREEN = "\033[32m"
YELLOW = "\033[33m"
BOLD = "\033[1m"
RESET = "\033[0m"


def green(msg: str) -> None:
    print(f"{GREEN}  ✓ {msg}{RESET}")


def yellow(msg: str) -> None:
    print(f"{YELLOW}  ~ {msg}{RESET}")


def bold(msg: str) -> None:
    print(f"{BOLD}{msg}{RESET}")


def download(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    try:
        urllib.request.urlretrieve(url, dest)
        green(str(dest))
    except urllib.error.HTTPError as e:
        print(f"  ✗ HTTP {e.code}: {url}", file=sys.stderr)
        sys.exit(1)


def handle_claude_md(claude_md: Path, merge: bool) -> None:
    if merge and claude_md.exists():
        content = claude_md.read_text()
        if PACK_SECTION_START in content:
            yellow(f"{claude_md} already contains pack section — skipped")
        else:
            claude_md.write_text(content.rstrip() + "\n\n" + PACK_STANDARDS + "\n")
            green(f"merged pack standards into {claude_md}")
    elif not claude_md.exists():
        claude_md.write_text(PACK_STANDARDS + "\n")
        green(f"created {claude_md}")
    else:
        yellow(f"{claude_md} exists — run with --merge to append pack standards")


def main() -> None:
    parser = argparse.ArgumentParser(description="Install claude-fastapi-pack")
    parser.add_argument("--dir", default=".claude", help="Target directory (default: .claude)")
    parser.add_argument("--merge", action="store_true", help="Merge pack standards into existing CLAUDE.md")
    args = parser.parse_args()

    target = Path(args.dir)

    bold("")
    bold("claude-fastapi-pack")
    print(f"Installing into {target}/")
    print()

    print("Agents:")
    for name in AGENTS:
        download(f"{BASE_URL}/agents/{name}.md", target / "agents" / f"{name}.md")

    print("\nCommands:")
    for name in COMMANDS:
        download(f"{BASE_URL}/commands/{name}.md", target / "commands" / f"{name}.md")

    print("\nSkills:")
    for name in SKILLS:
        download(f"{BASE_URL}/skills/{name}.md", target / "skills" / f"{name}.md")

    print()
    handle_claude_md(target / "CLAUDE.md", args.merge)

    print()
    bold("Done.")
    print(f"""
Installed:
  {target}/agents/     ({len(AGENTS)} agents)
  {target}/commands/   ({len(COMMANDS)} commands)
  {target}/skills/     ({len(SKILLS)} skills)

Try it:
  /design-api user authentication with JWT
  /review-async app/your_service.py
  /plan-feature your next feature
""")


if __name__ == "__main__":
    main()
