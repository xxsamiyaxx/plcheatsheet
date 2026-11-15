from rich import print
from rich.layout import Layout
from rich.panel import Panel

def pyBasicSyntaxCheatSheet():

    layout = Layout()

    layout.split_column(
        Layout(name="upper"),
        Layout(name="middle"),
        Layout(name="lower"),
    )

    layout["middle"].split_row(
        Layout(name="Inputs & Outputs"),
        Layout(name="Variables"),
        Layout(name="Functions"),
        Layout(name="Data Structures"),
        Layout(name="Conditionals"),
        Layout(name="Loops")
    )

    layout["Inputs & Outputs"].update(Panel("--", title="Inputs & Outputs"))
    layout["Variables"].update(Panel("--", title="Variables"))
    layout["Functions"].update(Panel("--", title="Functions"))

pyBasicSyntaxCheatSheet()