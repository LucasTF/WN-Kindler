import click

from wnk.commands import hello_world, list_sources, list_novels

VERSION = "0.0.1"

@click.group
@click.version_option(version=VERSION)
def commands():
    pass

commands.add_command(hello_world)
commands.add_command(list_sources)
commands.add_command(list_novels)

if __name__ == '__main__':
    commands()