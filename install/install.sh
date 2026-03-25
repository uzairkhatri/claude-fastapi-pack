#!/usr/bin/env bash
# claude-fastapi-pack installer
# Usage: curl -sSL <url> | bash
#        curl -sSL <url> | bash -s -- --dir path/to/.claude --merge

set -euo pipefail

REPO="uzairkhatri/claude-fastapi-pack"
BASE_URL="https://raw.githubusercontent.com/$REPO/main/.claude"
TARGET_DIR=".claude"
MERGE_CLAUDE_MD=false

# Parse flags
while [[ $# -gt 0 ]]; do
  case $1 in
    --dir) TARGET_DIR="$2"; shift 2 ;;
    --merge) MERGE_CLAUDE_MD=true; shift ;;
    *) echo "Unknown option: $1"; exit 1 ;;
  esac
done

AGENTS=(fastapi-architect api-implementer async-reviewer migration-guard pr-reviewer)
COMMANDS=(design-api review-api review-async check-migration plan-feature)
SKILLS=(fastapi-architecture sqlalchemy-async alembic-safety rest-response-standard)

# ── helpers ──────────────────────────────────────────────────────────────────

green()  { printf '\033[32m%s\033[0m\n' "$*"; }
yellow() { printf '\033[33m%s\033[0m\n' "$*"; }
bold()   { printf '\033[1m%s\033[0m\n' "$*"; }

download() {
  local url="$1" dest="$2"
  mkdir -p "$(dirname "$dest")"
  if curl -sSfL "$url" -o "$dest" 2>/dev/null; then
    green "  ✓ $dest"
  else
    echo "  ✗ failed: $url" >&2
    exit 1
  fi
}

# ── install ───────────────────────────────────────────────────────────────────

bold ""
bold "claude-fastapi-pack"
echo  "Installing into $TARGET_DIR/"
echo ""

echo "Agents:"
for name in "${AGENTS[@]}"; do
  download "$BASE_URL/agents/$name.md" "$TARGET_DIR/agents/$name.md"
done

echo ""
echo "Commands:"
for name in "${COMMANDS[@]}"; do
  download "$BASE_URL/commands/$name.md" "$TARGET_DIR/commands/$name.md"
done

echo ""
echo "Skills:"
for name in "${SKILLS[@]}"; do
  download "$BASE_URL/skills/$name.md" "$TARGET_DIR/skills/$name.md"
done

# ── CLAUDE.md merge or create ─────────────────────────────────────────────────

CLAUDE_MD="$TARGET_DIR/CLAUDE.md"
PACK_SECTION_START="<!-- claude-fastapi-pack:start -->"
PACK_SECTION_END="<!-- claude-fastapi-pack:end -->"
PACK_BLOCK="$PACK_SECTION_START
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
$PACK_SECTION_END"

echo ""
if [[ "$MERGE_CLAUDE_MD" == true && -f "$CLAUDE_MD" ]]; then
  # Only append if section not already present
  if grep -q "$PACK_SECTION_START" "$CLAUDE_MD" 2>/dev/null; then
    yellow "  ~ $CLAUDE_MD already contains pack section — skipped"
  else
    echo "" >> "$CLAUDE_MD"
    echo "$PACK_BLOCK" >> "$CLAUDE_MD"
    green "  ✓ merged pack standards into $CLAUDE_MD"
  fi
elif [[ ! -f "$CLAUDE_MD" ]]; then
  echo "$PACK_BLOCK" > "$CLAUDE_MD"
  green "  ✓ created $CLAUDE_MD"
else
  yellow "  ~ $CLAUDE_MD exists — run with --merge to append pack standards"
fi

# ── done ─────────────────────────────────────────────────────────────────────

echo ""
bold "Done."
echo ""
echo "Installed:"
echo "  $TARGET_DIR/agents/     (${#AGENTS[@]} agents)"
echo "  $TARGET_DIR/commands/   (${#COMMANDS[@]} commands)"
echo "  $TARGET_DIR/skills/     (${#SKILLS[@]} skills)"
echo ""
echo "Try it:"
echo "  /design-api user authentication with JWT"
echo "  /review-async app/your_service.py"
echo "  /plan-feature your next feature"
