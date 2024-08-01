import click

from wnk.sources import Wnsource, SourceFactory

@click.command()
def list_sources():
    """Prints a list of available web novel sources."""
    click.clear()
    click.echo('Available sources:')
    for i, src in enumerate(Wnsource):
        click.echo(f"{i+1}) {SourceFactory.get_source_title(src)}")