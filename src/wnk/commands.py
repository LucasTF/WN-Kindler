import click

from wnk.sources import Wnsource, get_source_name, create_source

@click.command()
def hello_world():
    click.echo('Hello World')

@click.command()
def list_sources():
    """Prints a list of available web novel sources."""
    click.clear()
    click.echo('Available sources:')
    for i, src in enumerate(Wnsource):
        click.echo(f"{i+1}) {get_source_name(src)}")

@click.command()
@click.option('-s', '--source', required=True, type=int, help="ID of the source found in the list-sources command.")
@click.option('-l', '--limit', default=50, show_default=True, type=int, help="Max number of novels to show.")
def list_novels(source, limit):
    """Prints a list of web novels from a specified source."""

    wnsource = create_source(source)

    if wnsource is None:
        return click.echo("Invalid source!")
    
    click.clear()
    click.echo('Available novels:\n')

    for i, novel in enumerate(wnsource.list_novels()):
        click.echo(f"{i+1}) {novel}")
    
    click.echo("\n-------------------------------------\n")
    click.echo("Page 1 of 1")


