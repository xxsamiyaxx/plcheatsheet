# SPDX-FileCopyrightText: 2026 xxsamiyaxx
# SPDX-License-Identifier: GPL-3.0-or-later

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

# makes basic layout of the JS Cheatsheet
def make_jslayout() -> Layout:
    layout = Layout(name="root")

    # Devides layout in three main layouts
    layout.split(
        Layout(name="header", size=3),
        Layout(name="main", ratio=1),
    )

    layout["main"].split_row(
        Layout(name="left", ratio=1),
        Layout(name="center", ratio=1),
        Layout(name="right", ratio=1, minimum_size=55),
    )

    layout["left"].split_column(
        Layout(name="Operators", ratio=2),
        Layout(name="Error Handling", ratio=1, minimum_size=14),
        Layout(name="Functions", ratio=1),
    )

    layout["center"].split_column(
        Layout(name="Classes", ratio=2, minimum_size=13),
        Layout(name="Variables", ratio=1, minimum_size=6),
        Layout(name="Strings", ratio=1, minimum_size=7),
        Layout(name="Loops", ratio=3),
    )

    layout["right"].split_column(
        Layout(name="In- & Output", ratio=2),
        Layout(name="Conditionals", ratio=2, minimum_size=23),
        Layout(name="Arrays", ratio=1, minimum_size=4),
    )

    return layout

# defines Header for Cheatsheet
class Header:
    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="center", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(
            "[bold]  JAVASCRIPT CHEATSHEET[/bold]",
            datetime.now().ctime().replace(":", "[blink]:[/]"),
        )
        return Panel(grid, style="white on yellow")

def make_syntax_inoutput() -> Syntax:
    code = """\
// Output
console.log("Hello World"); // print in console
window.alert("Hello World"); // print as alert box
document.getElementById("demo").innerText \n= "Hello World";
// Input
window.prompt("How are you?");
window.confirm("Are you sure?");
    """
    syntax_inoutput = Syntax(code, "javascript", line_numbers=True)
    return syntax_inoutput

def make_syntax_functions() -> Syntax:
    code = """\
// traditional function declaration
function square(num) {
  return num * num;
}; 
// Arrow function
const square = num => num * num;
square(5); // Calling function
    """
    syntax_functions = Syntax(code, "javascript", line_numbers=True)
    return syntax_functions

def make_syntax_variables() -> Syntax:
    code = """\
// value can be changed
let name = "Ellie"; 
// value & type cannot be changed
const age = 18;
    """
    syntax_variables = Syntax(code, "javascript", line_numbers=True)
    return syntax_variables

def make_syntax_strings() -> Syntax:
    code = """\
let text = 'He\'s pretty';
text.length;
text.toUpperCase();
text.toLowerCase();
text.slice(0, 2);
    """
    syntax_strings = Syntax(code, "javascript", line_numbers=True)
    return syntax_strings

def make_syntax_classes() -> Syntax:
    code = """\
class Car {
  constructor(name, color) {
    this.name = name;
    this.color = color;
  }
   paintWith(newColor) {
    this.color = newColor;
  }
} 
const myCar = new Car("Ford", "RED");
myCar.paintWith("BLUE");
    """
    syntax_classes = Syntax(code, "javascript", line_numbers=True)
    return syntax_classes

def make_syntax_loops() -> Syntax:
    code = """\
// for loop
for (let i = 0; i < 15; i++) {
  text += "Number: " + i + "<br>";
}

// while loop
let i = 0;
while (i < 15) {
  text += "Number: " + i;
  i++;
}
    """
    syntax_loops = Syntax(code, "javascript", line_numbers=True)
    return syntax_loops

def make_syntax_conditionals() -> Syntax:
    code = """\
// Else If Statement
if (time < 10) {
  greeting = "Good morning";
} else if (time < 20) {
  greeting = "Good day";
} else {
  greeting = "Good evening";
}
// Ternary Operator
let text = (age < 18) ? "Minor" : "Adult"; 
// Switch Statement
switch (new Date().getDay()) {
  case 0:
    day = "Sunday";
    break;
  case 1:
    day = "Monday";
    break;
  case 2:
     day = "Tuesday";
    break;
    """
    syntax_conditionals = Syntax(code, "javascript", line_numbers=True)
    return syntax_conditionals

def make_syntax_arrays() -> Syntax:
    code = """\
const cars = ["Ford", "Opel Astra", "VW Golf"];
cars[1] = "Opel Corsa"; // Change element
cars.push("Kia"); // Add new element to array
let car = cars[0]; // Access array element
    """
    syntax_arrays = Syntax(code, "javascript", line_numbers=True)
    return syntax_arrays

def make_syntax_operators() -> Syntax:
    code = """\
// Arithmetic operators
let a = 3;
let x = (384 + 22) * a;
// Assignment operators
let x = 16;
x += 2;
// Comparison operators
let x = 8;
let result = x < 8; // less than
let result = x > 8; // greater than
// Logical operators
// && -> AND
// || -> OR
// ! -> NOT
    """
    syntax_operators = Syntax(code, "javascript", line_numbers=True)
    return syntax_operators

def make_syntax_errorhandling() -> Syntax:
    code = """\
// Try statement
let x = 5;
try {
  x = y + 20;
} catch(err) {
  let errorType = err.name;
  let errorText = err.message;
} finally { // optional
  console.log("Always executed");
}
// Throw statement
throw "Error: The number is to small!"; 
    """
    syntax_errorhandling = Syntax(code, "javascript", line_numbers=True)
    return syntax_errorhandling

def start_fullscreen_js():
    layout = make_jslayout()
    layout["header"].update(Header())
    layout["In- & Output"].update(
        Panel(make_syntax_inoutput(), border_style="yellow", title="[yellow]In- & Output[/yellow]"))
    layout["Functions"].update(
        Panel(make_syntax_functions(), border_style="yellow", title="[yellow]Functions[/yellow]"))
    layout["Variables"].update(
        Panel(make_syntax_variables(), border_style="yellow", title="[yellow]Variables[/yellow]"))
    layout["Strings"].update(Panel(make_syntax_strings(), border_style="yellow", title="[yellow]Strings[/yellow]"))
    layout["Classes"].update(Panel(make_syntax_classes(), border_style="yellow", title="[yellow]Classes[/yellow]"))
    layout["Loops"].update(Panel(make_syntax_loops(), border_style="yellow", title="[yellow]Loops[/yellow]"))
    layout["Conditionals"].update(
        Panel(make_syntax_conditionals(), border_style="yellow", title="[yellow]Conditionals[/yellow]"))
    layout["Arrays"].update(Panel(make_syntax_arrays(), border_style="yellow", title="[yellow]Arrays[/yellow]"))
    layout["Operators"].update(
        Panel(make_syntax_operators(), border_style="yellow", title="[yellow]Operators[/yellow]"))
    layout["Error Handling"].update(
        Panel(make_syntax_errorhandling(), border_style="yellow", title="[yellow]Error Handling[/yellow]"))

    with Live(layout, screen=True, refresh_per_second=1) as live:
        try:
            while True:
                time.sleep(1)
                live.update(layout)
        except KeyboardInterrupt:
            pass