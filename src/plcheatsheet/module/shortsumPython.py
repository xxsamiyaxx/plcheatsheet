from rich.console import Console
from rich.markdown import Markdown
from rich.theme import Theme
from pathlib import Path

py_design = Theme({
    "markdown.h1": "bold blue",
    "markdown.h2": "bold yellow",
    "markdown.strong": "italic blue",
    "markdown.code": "yellow",
})

console = Console(theme=py_design)

def read_summary_py():
    current_file = Path(__file__).resolve()
    src_directory = current_file.parent.parent

    md_path = src_directory / "data" / "shortsumPython.md"

    if not md_path.exists():
        return f"! Error\nThe file was not found under `{md_path}`."

    with open(md_path, "r", encoding="utf-8") as f:
        md = Markdown(f.read())

    return md

def display_shortsummary_py():
    summary = read_summary_py()
    console.print(summary)