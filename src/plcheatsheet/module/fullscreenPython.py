# Imports
from rich.layout import Layout
from rich.panel import Panel
from rich.console import Console
from datetime import datetime
from rich.table import Table
from rich.syntax import Syntax

console = Console()

# makes basic layout of the Python Cheatsheet
def make_pylayout() -> Layout:
    layout = Layout(name="root")

    # Devides layout in three main layouts
    layout.split(
        Layout(name="header", size=3),
        Layout(name="main", ratio=1),
        Layout(name="footer", size=10),
    )
    # Devides layout main (=middle of "app") in two sublayouts in a row
    layout["main"].split_row(
        Layout(name="side"),
        Layout(name="body", ratio=2, minimum_size=60),
    )

    layout["side"].split_column(
        Layout(name="In- & Output", ratio=2),
        Layout(name="Data Structures", ratio=2),
        Layout(name="Operators", ratio=4),
    )

    layout["body"].split_row(
        Layout(name="middle center", ratio=1),
        Layout(name="left center", ratio=1),
    )

    layout["left center"].split_column(
        Layout(name="Classes", ratio=2),
        Layout(name="Loops", ratio=2),
    )

    layout["middle center"].split_column(
        Layout(name="Variables", ratio=1, minimum_size=6),
        Layout(name="Conditionals", ratio=3),
        Layout(name="Strings", ratio=1),
    )

    layout["footer"].split_row(
        Layout(name="Exceptions", ratio=2),
        Layout(name="Functions", ratio=1),
        Layout(name="Imports", ratio=1),
    )

    return layout

# defines Header for Cheatsheet
class Header:
    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="center", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(
            "[bold]  PYTHON CHEATSHEET[/bold]",
            datetime.now().ctime().replace(":", "[blink]:[/]"),
        )
        return Panel(grid, style="white on blue")

# Codeblock for In- & Output
def make_syntax_outinput() -> Syntax:
    code = """\
# Print text
print("Hello world")

# Input
input("What's your favorite number?")
    """
    syntax_outinput = Syntax(code, "python", line_numbers=True)
    return syntax_outinput

# Codeblock for Variables
def make_syntax_variables() -> Syntax:
    code = """\
x = 17           # int        
y = 56.98        # float
name = "Crystal" # string
is_on = True     # boolean
    """
    syntax_variables = Syntax(code, "python", line_numbers=True)
    return syntax_variables

# Codeblock for Data Structures
def make_syntax_datastructures() -> Syntax:
    code = """\
list1 = [1,2,3]       # list
tuple1 = (1,2,3)      # tuple
set1 = set{1,2,3}     # set
dict1 = {"a":1,"b":2} # dictionary
    """
    syntax_datastructures = Syntax(code, "python", line_numbers=True)
    return syntax_datastructures

# Codeblock for Conditionals
def make_syntax_conditionals() -> Syntax:
    code = """\
# if-elif-else
if x > 0:
    print("positive")
elif x == 0:
    print("zero")
else:
    print("negative")

# match-case
match http_code:
    case 200:
        print("OK")
    case 201:
        print("CREATED")
    """
    syntax_conditionals = Syntax(code, "python", line_numbers=True)
    return syntax_conditionals

# Codeblock for Classes
def make_syntax_classes() -> Syntax:
    code = """\
class Car:
    def __init__(self, color):
        self.color = color

    def paint_car(self, new_color):
        self.color = new_color

my_car = Car("WHITE")
my_car.paint_car("BLACK")
    """
    syntax_classes = Syntax(code, "python", line_numbers=True)
    return syntax_classes

# Codeblock for Operators
def make_syntax_operators() -> Syntax:
    code = """\
# arithmetic operators
print(4 / 3) # float division
print(4 // 3) # integer division
print(4 ** 6) # square

# assignment operators
x += 1 # addition
x -= 1 # subtraction

# logical operators
age > 16 and points > 50 # AND
age > 16 or points > 50  # OR
not points > 50          # NEGATION
    """
    syntax_operators = Syntax(code, "python", line_numbers=True)
    return syntax_operators

# Codeblock for Strings
def make_syntax_strings() -> Syntax:
    code = """\
s = "Python"
print(s.lower()) # python
print(s.upper()) # PYTHON
print(s[0:3])    # Pyt
    """
    syntax_strings = Syntax(code, "python", line_numbers=True)
    return syntax_strings

# Codeblock for Loops
def make_syntax_loops() -> Syntax:
    code = """\
# index-based for-loop
for i in range(10, 2):
    print(i)

# value-based for-loop
for current_name in ["Elisa", "Lili"]:
    print(current_name)

# while loop
while x > 0:
    x -= 1
    """
    syntax_loops = Syntax(code, "python", line_numbers=True)
    return syntax_loops

# Codeblock for Imports
def make_syntax_imports() -> Syntax:
    code = """\
# import a library
import random
# import a part of file
from random import randrange
# w/ alias
import numpy as np
# import via path
import src.functions 
# Directory: src/functions.py  
    """
    syntax_imports = Syntax(code, "python", line_numbers=True)
    return syntax_imports

# Codeblock for Functions
def make_syntax_functions() -> Syntax:
    code = """\
# Define own function
def greeting(name):
    print("Hello ", name)

greeting(Nina)
    """
    syntax_functions = Syntax(code, "python", line_numbers=True)
    return syntax_functions

# Codeblock for Exceptions
def make_syntax_exceptions() -> Syntax:
    code = """\
try:
    value = int("532") # Exceptions may occur here
    print(value) 
except ValueError:
    print("Can't parse to integer") 
    # Exceptions will be handled here
finally: 
    print("Hi!") # Always executed; optional
    """
    syntax_exceptions = Syntax(code, "python", line_numbers=True)
    return syntax_exceptions

# Making the layout + update it with the functions + build panels
layout = make_pylayout()
layout["header"].update(Header())
layout["In- & Output"].update(Panel(make_syntax_outinput(), border_style="yellow", title="In- & Output"))
layout["Variables"].update(Panel(make_syntax_variables(), border_style="yellow", title="Variables"))
layout["Data Structures"].update(Panel(make_syntax_datastructures(), border_style="yellow", title="Data Structures"))
layout["Conditionals"].update(Panel(make_syntax_conditionals(), border_style="yellow", title="Conditionals"))
layout["Classes"].update(Panel(make_syntax_classes(), border_style="yellow", title="Classes"))
layout["Operators"].update(Panel(make_syntax_operators(), border_style="yellow", title="Operators"))
layout["Strings"].update(Panel(make_syntax_strings(), border_style="yellow", title="Strings"))
layout["Loops"].update(Panel(make_syntax_loops(), border_style="yellow", title="Loops"))
layout["Imports"].update(Panel(make_syntax_imports(), border_style="yellow", title="Imports"))
layout["Functions"].update(Panel(make_syntax_functions(), border_style="yellow", title="Functions"))
layout["Exceptions"].update(Panel(make_syntax_exceptions(), border_style="yellow", title="Exceptions"))