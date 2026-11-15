# plcheatsheet - CLI tool for quickly looking up programming or scripting languages
# Copyright (C) 2026 xxsamiyaxx
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://gnu.org>.

import click
import plcs.module.fullscreenPython as fp
import plcs.module.fullscreenBashScripting as fb
import plcs.module.fullscreenJS as fj
import plcs.module.shortsumPython as sp
import plcs.module.shortsumBash as sb
import plcs.module.shortsumJS as sj

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(invoke_without_command=True, context_settings=CONTEXT_SETTINGS)
@click.version_option(None, "-v", "--version", package_name="plcheatsheet", message="%(version)s")
@click.pass_context
def main(ctx):
    """plcheatsheet is a CLI tool for searching quickly, fast and effective the syntax of
       several programming or scripting languages."""
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())
        ctx.exit()

@main.command()
@click.argument('language')
@click.option("-f", "--fullscreen", is_flag=True, help="Displays a fullscreen and compact Cheatsheet")
@click.option("-s", "--shortsummary", is_flag=True, help="Displays a short summary about the language")
def lang(language, fullscreen, shortsummary):
    """programming or scripting language which you want to look up or for which you want to look up the syntax"""
    error_message = "You have to give an option, type 'plcs lang --help' to see all options."
    match language.lower():
        case "python" | "py":
            if fullscreen:
                fp.start_fullscreen_py()
            elif shortsummary:
                sp.display_shortsummary_py()
            else:
                print(error_message)
        case "javascript" | "js":
            if fullscreen:
                fj.start_fullscreen_js()
            elif shortsummary:
                sj.display_shortsummary_js()
            else:
                print(error_message)
        case "bash" | "bashscripting" | "bash scripting":
            if fullscreen:
                fb.start_fullscreen_bashscripting()
            elif shortsummary:
                sb.display_shortsummary_bash()
            else:
                print(error_message)
        case _:
            print("""There is no information for this language. Make sure that you write the name of the language correctly and check
in the included_pl.md or the README.md of this repository if the language you are trying to search is supported.""")



