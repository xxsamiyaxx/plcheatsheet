# Imports
from rich.layout import Layout
from rich.panel import Panel
from rich.console import Console
from datetime import datetime
from rich.table import Table
from rich.syntax import Syntax
from rich.live import Live
import time

console = Console()

# makes basic layout of the Bash Cheatsheet
def make_shlayout() -> Layout:
    layout = Layout(name="root")

    # Devides layout in three main layouts
    layout.split(
        Layout(name="header", size=3),
        Layout(name="main", ratio=1),
    )
    # Devides layout main (=middle of "app") in two sublayouts in a row
    layout["main"].split_row(
        Layout(name="right", ratio=1),
        Layout(name="left", ratio=1),
        Layout(name="center", ratio=1),
    )

    layout["right"].split_row(
        Layout(name="Loops", ratio=1),
        Layout(name="Data Types", ratio=1),
    )

    layout["left"].split_row(
        Layout(name="Operators", ratio=1),
        Layout(name="Shebang Lines", ratio=1),
    )

    layout["center"].split_row(
        Layout(name="Functions", ratio=1),
        Layout(name="Conditionals", ratio=1),
    )

    return layout