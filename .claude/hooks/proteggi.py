#!/usr/bin/env python3
"""PreToolUse hook: il codice del prodotto lo scrive lo studente.

Blocca Edit/Write di Claude fuori da studio/ e .claude/ (e dai file di servizio
della radice), a meno che esista il flag studio/.sblocca creato da /sblocca
da meno di FLAG_TTL_SECONDS: uno sblocco dimenticato scade da solo.
Esce con 2 (blocco) e scrive il motivo su stderr, che Claude riceve come feedback.
"""
import json
import os
import sys
import time

ALLOWED_PREFIXES = ("studio/", ".claude/")
ALLOWED_FILES = {"README.md", "CLAUDE.md", "CLAUDE.local.md", ".gitignore"}
FLAG_TTL_SECONDS = 6 * 3600  # una sessione abbondante; /chiudi lo toglie prima


def main() -> int:
    try:
        data = json.load(sys.stdin)
    except Exception:
        return 0  # input inatteso: non bloccare

    tool_input = data.get("tool_input") or {}
    path = tool_input.get("file_path") or tool_input.get("notebook_path") or ""
    if not path:
        return 0

    cwd = data.get("cwd") or os.getcwd()
    root = os.environ.get("CLAUDE_PROJECT_DIR") or cwd
    abs_path = path if os.path.isabs(path) else os.path.join(cwd, path)
    abs_path = os.path.abspath(abs_path)
    try:
        rel = os.path.relpath(abs_path, os.path.abspath(root)).replace("\\", "/")
    except ValueError:
        return 0

    if rel.startswith(".."):
        return 0  # fuori dal repo: non è codice dello studente
    if rel in ALLOWED_FILES or rel.startswith(ALLOWED_PREFIXES):
        return 0
    flag = os.path.join(root, "studio", ".sblocca")
    if os.path.exists(flag):
        if time.time() - os.path.getmtime(flag) < FLAG_TTL_SECONDS:
            return 0
        try:
            os.remove(flag)  # sblocco di una sessione passata: scaduto
        except OSError:
            pass

    sys.stderr.write(
        f"BLOCCATO dal metodo di studio: '{rel}' è codice che scrive lo studente. "
        "Non scriverlo tu: indica file e riga, spiega cosa manca, lascia che lo faccia lui "
        "(CLAUDE.md, regola n.1). Se ha chiesto esplicitamente che lo scriva tu, "
        "digli di eseguire /sblocca <motivo>.\n"
    )
    return 2


if __name__ == "__main__":
    sys.exit(main())
