from rich.console import Console
from rich.markdown import Markdown
from rich.theme import Theme
from pathlib import Path

bash_design = Theme({
    "markdown.h1": "bold green",
    "markdown.h2": "bold green",
    "markdown.strong": "bold white",
    "markdown.code": "green",
})

console = Console(theme=bash_design)

def read_summary_bash():
    current_file = Path(__file__).resolve()
    src_directory = current_file.parent.parent

    md_path = src_directory / "data" / "shortsumBash.md"

    if not md_path.exists():
        return f"! Error\nThe file was not found under `{md_path}`."

    with open(md_path, "r", encoding="utf-8") as f:
        md = Markdown(f.read())

    return md

def display_shortsummary_bash():
    summary = read_summary_bash()
    console.print(summary)