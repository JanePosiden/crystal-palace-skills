#!/usr/bin/env python3
"""
Install Crystal Palace into Cursor / Claude Code / Codex / Grok.

Examples:
  python crystal-palace/install_adapters.py --target all
  python crystal-palace/palace_cli.py install --target all
  python crystal-palace/install_adapters.py --target claude --scope user
  python crystal-palace/install_adapters.py --target all --dry-run
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parent
SKILLS_SRC = PACKAGE_ROOT / "skills"
ADAPTERS = PACKAGE_ROOT / "adapters"
SNIPPET = ADAPTERS / "INSTRUCTIONS.snippet.md"
RULE_MDC = ADAPTERS / "crystal-palace.mdc"
GROK_SRC = ADAPTERS / "GROK_CUSTOM_INSTRUCTIONS.md"
MARKER_BEGIN = "<!-- BEGIN CRYSTAL PALACE -->"
MARKER_END = "<!-- END CRYSTAL PALACE -->"
# Legacy markers from earlier drafts — treated as the same section
LEGACY_MARKERS = (
    ("<!-- crystal-palace:begin -->", "<!-- crystal-palace:end -->"),
    (MARKER_BEGIN, MARKER_END),
)
SKILL_NAMES = (
    "palace-orchestrator",
    "crystal-palace-memory",
    "lean-handoff",
    "control-variable-tune",
)
ALL_TARGETS = ("cursor", "claude", "codex", "grok")


def die(msg: str, code: int = 1) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    raise SystemExit(code)


def configure_stdio() -> None:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
        except Exception:
            pass


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def ensure_skills_present() -> None:
    if not SKILLS_SRC.is_dir():
        die(f"missing skills package: {SKILLS_SRC}")
    missing = [n for n in SKILL_NAMES if not (SKILLS_SRC / n / "SKILL.md").exists()]
    if missing:
        die(f"incomplete skills package, missing: {missing}")


def copy_tree(src: Path, dst: Path, dry_run: bool) -> None:
    print(f"  {'DRY ' if dry_run else ''}copy {src} -> {dst}")
    if dry_run:
        return
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def write_text(path: Path, text: str, dry_run: bool) -> None:
    print(f"  {'DRY ' if dry_run else ''}write {path}")
    if dry_run:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text if text.endswith("\n") else text + "\n", encoding="utf-8")


def _strip_all_palace_sections(text: str) -> str:
    """Remove every known Crystal Palace marked block (current + legacy)."""
    import re

    patterns = [
        re.compile(
            r"\n*<!--\s*BEGIN CRYSTAL PALACE\s*-->.*?<!--\s*END CRYSTAL PALACE\s*-->\n*",
            re.S | re.I,
        ),
        re.compile(
            r"\n*<!--\s*crystal-palace:begin\s*-->.*?<!--\s*crystal-palace:end\s*-->\n*",
            re.S | re.I,
        ),
    ]
    out = text
    for pat in patterns:
        out = pat.sub("\n\n", out)
    return out.strip() + ("\n" if out.strip() else "")


def upsert_marked_section(path: Path, snippet: str, dry_run: bool) -> None:
    """Replace any prior Crystal Palace block(s) with a single canonical section."""
    snippet = snippet.strip() + "\n"
    if MARKER_BEGIN not in snippet:
        snippet = f"{MARKER_BEGIN}\n{snippet}\n{MARKER_END}\n"
    # Normalize legacy markers inside snippet to the canonical pair
    snippet = (
        snippet.replace("<!-- crystal-palace:begin -->", MARKER_BEGIN)
        .replace("<!-- crystal-palace:end -->", MARKER_END)
    )

    old = path.read_text(encoding="utf-8") if path.exists() else ""
    stripped = _strip_all_palace_sections(old)
    if stripped.strip():
        new = stripped.rstrip() + "\n\n" + snippet
        action = "replace"
    else:
        new = snippet
        action = "create"

    print(f"  {'DRY ' if dry_run else ''}{action} marked section in {path}")
    if not dry_run:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(new if new.endswith("\n") else new + "\n", encoding="utf-8")


def mdc_to_md(rule_body: str) -> str:
    if rule_body.startswith("---"):
        parts = rule_body.split("---", 2)
        if len(parts) >= 3:
            return parts[2].strip() + "\n"
    return rule_body if rule_body.endswith("\n") else rule_body + "\n"


def install_skills_into(dest_skills: Path, dry_run: bool) -> None:
    if not dry_run:
        dest_skills.mkdir(parents=True, exist_ok=True)
    print(f"Skills → {dest_skills}")
    for name in SKILL_NAMES:
        copy_tree(SKILLS_SRC / name, dest_skills / name, dry_run)


def home_dir() -> Path:
    return Path.home()


def load_snippet() -> str:
    if SNIPPET.exists():
        return SNIPPET.read_text(encoding="utf-8")
    # Fallback minimal block
    return (
        f"{MARKER_BEGIN}\n"
        "# Crystal Palace (PALACE)\n\n"
        "Use `python crystal-palace/palace_cli.py` for Vault / S-Filter / Brief / Handoff / Tune.\n"
        "Load skills: palace-orchestrator, crystal-palace-memory, lean-handoff, control-variable-tune.\n"
        f"{MARKER_END}\n"
    )


def install_cursor(repo_root: Path, scope: str, dry_run: bool) -> None:
    if scope == "repo":
        skills = repo_root / ".cursor" / "skills"
        rules = repo_root / ".cursor" / "rules"
    else:
        skills = home_dir() / ".cursor" / "skills"
        rules = home_dir() / ".cursor" / "rules"
    install_skills_into(skills, dry_run)
    print(f"Rules → {rules}")
    if RULE_MDC.exists():
        write_text(rules / "crystal-palace.mdc", RULE_MDC.read_text(encoding="utf-8"), dry_run)
    else:
        print("  WARN: missing adapters/crystal-palace.mdc")


def install_claude(repo_root: Path, scope: str, dry_run: bool) -> None:
    if scope == "repo":
        skills = repo_root / ".claude" / "skills"
        instr = repo_root / "CLAUDE.md"
        rules_dir = repo_root / ".claude" / "rules"
    else:
        skills = home_dir() / ".claude" / "skills"
        instr = home_dir() / ".claude" / "CRYSTAL_PALACE.md"
        rules_dir = home_dir() / ".claude" / "rules"
    install_skills_into(skills, dry_run)
    print(f"Rules → {rules_dir}")
    rule_body = RULE_MDC.read_text(encoding="utf-8") if RULE_MDC.exists() else ""
    write_text(rules_dir / "crystal-palace.md", mdc_to_md(rule_body), dry_run)
    # Prefer CLAUDE.fragment if present for richer text; else shared snippet
    frag = ADAPTERS / "CLAUDE.fragment.md"
    snippet = frag.read_text(encoding="utf-8") if frag.exists() else load_snippet()
    upsert_marked_section(instr, snippet, dry_run)


def install_codex(repo_root: Path, scope: str, dry_run: bool) -> None:
    if scope == "repo":
        skills = repo_root / ".agents" / "skills"
        instr = repo_root / "AGENTS.md"
    else:
        skills = home_dir() / ".agents" / "skills"
        codex_home = Path(os.environ.get("CODEX_HOME", home_dir() / ".codex"))
        instr = codex_home / "AGENTS.md"
    install_skills_into(skills, dry_run)
    frag = ADAPTERS / "AGENTS.fragment.md"
    snippet = frag.read_text(encoding="utf-8") if frag.exists() else load_snippet()
    upsert_marked_section(instr, snippet, dry_run)


def install_grok(repo_root: Path, scope: str, dry_run: bool) -> None:
    """Grok has no skill host — emit pasteable custom instructions + repo GROK.md."""
    candidates = [
        ADAPTERS / "GROK.custom-instructions.md",
        GROK_SRC,
        ADAPTERS / "GROK_SYSTEM_PROMPT.md",
        PACKAGE_ROOT / "GROK_CUSTOM_INSTRUCTIONS.md",
    ]
    src = next((p for p in candidates if p.exists()), None)
    if src is None:
        body = (
            "# Crystal Palace — paste into Grok custom instructions\n\n"
            + load_snippet()
            .replace(MARKER_BEGIN, "")
            .replace(MARKER_END, "")
            .strip()
            + "\n"
        )
    else:
        body = src.read_text(encoding="utf-8")

    targets = [
        repo_root / "GROK.md",
        PACKAGE_ROOT / "GROK_CUSTOM_INSTRUCTIONS.md",
        ADAPTERS / "GROK_SYSTEM_PROMPT.md",
    ]
    if scope == "user":
        targets.append(home_dir() / "GROK_CRYSTAL_PALACE.md")

    print("Grok (pasteable instructions)")
    for path in targets:
        write_text(path, body, dry_run)
    print("  Tip: paste GROK.md into Grok custom instructions.")
    print("  Tip: Grok-inside-Cursor already uses Cursor skills/rules (model-agnostic).")


def uninstall_target(repo_root: Path, target: str, scope: str, dry_run: bool) -> None:
    """Remove installed skill dirs; strip marked sections from guidance files."""
    print(f"Uninstall {target} (scope={scope})")
    skill_dirs: list[Path] = []
    guidance: list[Path] = []
    if target == "cursor":
        base = repo_root / ".cursor" if scope == "repo" else home_dir() / ".cursor"
        skill_dirs = [base / "skills" / n for n in SKILL_NAMES]
        rule = base / "rules" / "crystal-palace.mdc"
        if rule.exists() or dry_run:
            print(f"  {'DRY ' if dry_run else ''}remove {rule}")
            if not dry_run and rule.exists():
                rule.unlink()
    elif target == "claude":
        base = repo_root / ".claude" if scope == "repo" else home_dir() / ".claude"
        skill_dirs = [base / "skills" / n for n in SKILL_NAMES]
        rule = base / "rules" / "crystal-palace.md"
        if rule.exists() or dry_run:
            print(f"  {'DRY ' if dry_run else ''}remove {rule}")
            if not dry_run and rule.exists():
                rule.unlink()
        guidance = (
            [repo_root / "CLAUDE.md"]
            if scope == "repo"
            else [home_dir() / ".claude" / "CRYSTAL_PALACE.md"]
        )
    elif target == "codex":
        if scope == "repo":
            skill_dirs = [repo_root / ".agents" / "skills" / n for n in SKILL_NAMES]
            guidance = [repo_root / "AGENTS.md"]
        else:
            skill_dirs = [home_dir() / ".agents" / "skills" / n for n in SKILL_NAMES]
            guidance = [Path(os.environ.get("CODEX_HOME", home_dir() / ".codex")) / "AGENTS.md"]
    elif target == "grok":
        for path in (repo_root / "GROK.md", PACKAGE_ROOT / "GROK_CUSTOM_INSTRUCTIONS.md"):
            if path.exists() or dry_run:
                print(f"  {'DRY ' if dry_run else ''}remove {path}")
                if not dry_run and path.exists():
                    path.unlink()
        return
    else:
        die(f"unknown uninstall target: {target}")

    for d in skill_dirs:
        if d.exists() or dry_run:
            print(f"  {'DRY ' if dry_run else ''}rmtree {d}")
            if not dry_run and d.exists():
                shutil.rmtree(d)

    for path in guidance:
        if not path.exists():
            continue
        cleaned = _strip_all_palace_sections(path.read_text(encoding="utf-8"))
        # Drop empty stub files we created
        if cleaned.strip() in ("", "# CLAUDE.md", "# Agent guidance", "# AGENTS.md"):
            print(f"  {'DRY ' if dry_run else ''}remove empty {path}")
            if not dry_run:
                path.unlink()
        else:
            print(f"  {'DRY ' if dry_run else ''}strip Palace block from {path}")
            if not dry_run:
                path.write_text(cleaned if cleaned.endswith("\n") else cleaned + "\n", encoding="utf-8")


def write_manifest(repo_root: Path, targets: list[str], scope: str, dry_run: bool) -> None:
    manifest = {
        "package": "crystal-palace",
        "version": 1,
        "installed_at": utc_now(),
        "targets": targets,
        "scope": scope,
        "skills": list(SKILL_NAMES),
        "package_root": str(PACKAGE_ROOT),
        "repo_root": str(repo_root),
    }
    if (repo_root / "crystal-palace").is_dir():
        path = repo_root / "crystal-palace" / "state" / "install_manifest.json"
    else:
        path = repo_root / ".crystal-palace-install.json"
    print(f"Manifest → {path}")
    if not dry_run:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def parse_targets(raw: str) -> list[str]:
    raw = raw.strip().lower()
    if raw == "all":
        return list(ALL_TARGETS)
    parts = [p.strip() for p in raw.split(",") if p.strip()]
    bad = [p for p in parts if p not in ALL_TARGETS]
    if bad:
        die(f"unknown target(s) {bad}; use {', '.join(ALL_TARGETS)}, or all")
    if not parts:
        die("no targets specified")
    return parts


def main(argv: list[str] | None = None) -> int:
    configure_stdio()
    parser = argparse.ArgumentParser(
        prog="install_adapters",
        description="Install Crystal Palace into Cursor, Claude Code, Codex, and Grok",
    )
    parser.add_argument(
        "--target",
        default="all",
        help="cursor | claude | codex | grok | all | comma-list",
    )
    parser.add_argument(
        "--scope",
        choices=["repo", "user"],
        default="repo",
        help="repo = project dirs; user = home skill dirs",
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=None,
        help="project root (default: parent of crystal-palace/)",
    )
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--init-vault",
        action="store_true",
        help="also run palace_cli.py init after install",
    )
    parser.add_argument(
        "--uninstall",
        action="store_true",
        help="remove installed skills/rules/guidance blocks for the target(s)",
    )
    args = parser.parse_args(argv)

    ensure_skills_present()
    repo_root = (args.repo_root or PACKAGE_ROOT.parent).resolve()
    targets = parse_targets(args.target)

    print("Crystal Palace installer")
    print(f"  package: {PACKAGE_ROOT}")
    print(f"  repo:    {repo_root}")
    print(f"  scope:   {args.scope}")
    print(f"  targets: {', '.join(targets)}")
    print(f"  action:  {'UNINSTALL' if args.uninstall else 'INSTALL'}")
    if args.dry_run:
        print("  mode:    DRY-RUN")

    for t in targets:
        print(f"\n== {t} ==")
        if args.uninstall:
            uninstall_target(repo_root, t, args.scope, args.dry_run)
            continue
        if t == "cursor":
            install_cursor(repo_root, args.scope, args.dry_run)
        elif t == "claude":
            install_claude(repo_root, args.scope, args.dry_run)
        elif t == "codex":
            install_codex(repo_root, args.scope, args.dry_run)
        elif t == "grok":
            install_grok(repo_root, args.scope, args.dry_run)

    if not args.uninstall:
        write_manifest(repo_root, targets, args.scope, args.dry_run)

    if args.init_vault and not args.dry_run and not args.uninstall:
        cli = PACKAGE_ROOT / "palace_cli.py"
        if cli.exists():
            print("\n== init vault ==")
            subprocess.check_call([sys.executable, str(cli), "init"], cwd=str(repo_root))

    print("\nDone.")
    if args.uninstall:
        print("Uninstalled selected targets. Re-install with: python crystal-palace/palace_cli.py install --target all")
        return 0
    print("Next:")
    print("  python crystal-palace/palace_cli.py doctor")
    print("  python crystal-palace/palace_cli.py self-test")
    if "claude" in targets:
        print("  Claude Code: open this repo; skills in .claude/skills/; see CLAUDE.md")
    if "codex" in targets:
        print("  Codex: skills in .agents/skills/; see AGENTS.md")
    if "cursor" in targets:
        print("  Cursor: skills in .cursor/skills/; rule crystal-palace.mdc")
    if "grok" in targets:
        print("  Grok: paste GROK.md into custom instructions (or use Grok inside Cursor)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
