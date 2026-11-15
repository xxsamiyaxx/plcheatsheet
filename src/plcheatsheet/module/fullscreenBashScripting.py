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
        Layout(name="left", ratio=1),
        Layout(name="center", ratio=1),
        Layout(name="right", ratio=1),
    )

    layout["left"].split_column(
        Layout(name="top", ratio=2),
        Layout(name="bottom", ratio=1, minimum_size=18),
    )

    layout["top"].split_row(
        Layout(name="Operators", ratio=1),
    )

    layout["bottom"].split_row(
        Layout(name="Error Handling", ratio=1),
    )
    layout["center"].split_column(
        Layout(name="Shebang Lines", ratio=1, minimum_size=5),
        Layout(name="Bashcmds", ratio=2),
        Layout(name="Variables", ratio=1, minimum_size=6),
        Layout(name="Functions", ratio=2),
        Layout(name="Loops", ratio=3),
    )

    layout["right"].split_column(
        Layout(name="In- & Output", ratio=1),
        Layout(name="Conditionals", ratio=3),
        Layout(name="Data Types", ratio=1),
    )

    return layout

# defines Header for Cheatsheet
class Header:
    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="center", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(
            "[bold]$_ BASH SCRIPTING CHEATSHEET[/bold]",
            datetime.now().ctime().replace(":", "[blink]:[/]"),
        )
        return Panel(grid, style="black on white")

def make_syntax_shebanglines() -> Syntax:
    code = """\
#!/bin/sh
#!/bin/bash
#!/usr/bin/env bash
    """
    syntax_shebanglines = Syntax(code, "python", line_numbers=True)
    return syntax_shebanglines

def make_syntax_inoutput() -> Syntax:
    code = """\
# User Input
echo "How old are you?"
read -p age # read -s for a silent input
# Output
echo "Hello World!"
    """
    syntax_inoutput = Syntax(code, "python", line_numbers=True)
    return syntax_inoutput

def make_syntax_conditionals() -> Syntax:
    code = """\
# If-elif-else statement
num=52
if [ $num -gt 2 ]; then
  echo "Number is greater than 2"
elif [ $num -eq 2 ]; then
  echo "Number is exactly 2"
else
  echo "Number is less than 2"
fi

# match case
case $COUNTRY in
    Germany)
        echo "German" ;;
    France)
        echo "French" ;;
    England)
        echo "English" ;;
    *)
        echo "unknown" ;;
esac
    """
    syntax_conditionals = Syntax(code, "python", line_numbers=True)
    return syntax_conditionals

def make_syntax_loops() -> Syntax:
    code = """\
# for loop
for i in {1..5}; do
    echo "Iteration: $i"
done
# while loop
count=1
until [ $count -gt 10 ]; do
  echo "Count is $count"
  ((count++))
done
    """
    syntax_loops = Syntax(code, "python", line_numbers=True)
    return syntax_loops

def make_syntax_functions() -> Syntax:
    code = """\
# define a function
greeting() {
    local name=$1
    echo "Good day, $name!"
}
greeting "Alisa" # Call a function
    """
    syntax_functions = Syntax(code, "python", line_numbers=True)
    return syntax_functions

def make_syntax_variables() -> Syntax:
    code = """\
fav_food="Pizza"
age=12
echo "I liked $fav_food when I was $age
years old!"
    """
    syntax_variables = Syntax(code, "python", line_numbers=True)
    return syntax_variables

def make_syntax_datatypes() -> Syntax:
    code = """\
name="Freya" # string
num1=17 # number
fruits=("cherry" "banana") # array
declare -A colors # associative array
colors[cherry]="red"
colors[banana]="yellow"
    """
    syntax_datatypes = Syntax(code, "python", line_numbers=True)
    return syntax_datatypes

def make_syntax_errorhandling() -> Syntax:
    code = """\
# strict mode
set -e # Abort if error
set -u # Abort if usage of\n# undefined variables
set -o pipefail # -> don't swallow errs
# traps for exception handling
trap 'rm -f /tmp/tempfile; echo "Script\ninterrupted. Cleaning up." >&2' EXIT
trap 'echo -e "\nScript interrupted by user. Exiting\nsafely..."; exit 130' SIGINT
error_handler() {
    echo "Error: Command failed\non line $1"
}
trap 'error_handler $LINENO' ERR
    """
    syntax_errorhandling = Syntax(code, "python", line_numbers=True)
    return syntax_errorhandling

def make_syntax_operators() ->  Syntax:
    code = """\
# Comparison Operators:
# -eq -> Equal to; -ne -> Not equal to
# -lt -> Less than; -gt -> Greater than
# -le -> Less than or equal to; 
# -ge -> Greater than or equal to
# String Comparison Operators:
# = -> Equal to; != -> Not equal to
# < -> Less than; > -> Greater than
# Arithmetic Operators:
# + -> Addition; - -> Subtraction
# * -> Multiplication; / -> Division
# % -> Modulo
# Logical Operators:
# && -> AND; || -> OR; ! -> NOT
# File Test Operators:
# -e -> Checks if file exists
# -d -> Checks if a directory exists
# -f -> Checks if file is regular file
# -s -> Checks if a file is not empty
    """
    syntax_operators = Syntax(code, "python", line_numbers=True)
    return syntax_operators

def make_syntax_bashcmds() -> Syntax:
    code = """\
mkdir -p ~/Projects # creates directory
cd ~/Projects # changes directory
touch main.py # creates file
cp main.py ~/Projects/main.py # copy file/directory
mv main.py mainp.py # move or rename file/directory
rm main.py # remove file/directory
    """
    syntax_bashcmds = Syntax(code, "python", line_numbers=True)
    return syntax_bashcmds

def start_fullscreen_bashscripting():
    layout = make_shlayout()
    layout["header"].update(Header())
    layout["Shebang Lines"].update(Panel(make_syntax_shebanglines(), border_style="white", title="[green]Shebang Lines[/green]"))
    layout["In- & Output"].update(Panel(make_syntax_inoutput(), border_style="white", title="[green]In- & Output[/green]"))
    layout["Conditionals"].update(Panel(make_syntax_conditionals(), border_style="white", title="[green]Conditionals[/green]"))
    layout["Loops"].update(Panel(make_syntax_loops(), border_style="white", title="[green]Loops[/green]"))
    layout["Functions"].update(Panel(make_syntax_functions(), border_style="white", title="[green]Functions[/green]"))
    layout["Variables"].update(Panel(make_syntax_variables(), border_style="white", title="[green]Variables[/green]"))
    layout["Data Types"].update(Panel(make_syntax_datatypes(), border_style="white", title="[green]Data Types[/green]"))
    layout["Error Handling"].update(Panel(make_syntax_errorhandling(), border_style="white", title="[green]Error Handling[/green]"))
    layout["Operators"].update(Panel(make_syntax_operators(), border_style="white", title="[green]Operators[/green]"))
    layout["Bashcmds"].update(Panel(make_syntax_bashcmds(), border_style="white", title="[green]Basic Bash Commands[/green]"))

    with Live(layout, screen=True, refresh_per_second=1) as live:
        try:
            while True:
                time.sleep(1)
                live.update(layout)
        except KeyboardInterrupt:
            pass
