# SPDX-FileCopyrightText: 2026 xxsamiyaxx
# SPDX-License-Identifier: GPL-3.0-or-later

from rich.console import Console
from rich.markdown import Markdown
from rich.theme import Theme
from pathlib import Path

js_design = Theme({
    "markdown.h1": "bold underline yellow",
    "markdown.h2": "bold yellow",
    "markdown.strong": "bold white",
    "markdown.code": "yellow",
})

console = Console(theme=js_design)

def read_summary_js():
    current_file = Path(__file__).resolve()
    src_directory = current_file.parent.parent

    md_path = src_directory / "data" / "shortsumJS.md"

    if not md_path.exists():
        return f"! Error\nThe file was not found under `{md_path}`."

    with open(md_path, "r", encoding="utf-8") as f:
        md = Markdown(f.read())

    return md

def display_shortsummary_js():
    summary = read_summary_js()
    console.print(summary)