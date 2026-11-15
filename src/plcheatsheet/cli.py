import click
import module.fullscreenPython as fp
import module.fullscreenBashScripting as fb

@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    """plcheatsheet is a CLI tool for searching quickly, fast and effective the syntax of
    several programming languages."""
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())
        ctx.exit()

@main.command()
@click.argument('language')
@click.option("-f", "--fullscreen", is_flag=True, help="Displays a fullscreen and compact Cheatsheet")
def lang(language, fullscreen):
    """Language should be the programming language for which you want to look up the syntax"""
    if language.lower() == "python":
        if fullscreen:
            fp.start_fullscreen_py()
    elif language.lower() == "bash":
        if fullscreen:
            fb.start_fullscreen_bashscripting()


