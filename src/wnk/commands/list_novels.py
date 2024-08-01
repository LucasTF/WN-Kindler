import click

from wnk.sources import SourceFactory

@click.command()
@click.option('-s', '--source', required=True, type=int, help="ID of the source found in the list-sources command.")
@click.option('-l', '--limit', default=50, show_default=True, type=int, help="Max number of novels to show.")
def list_novels(source, limit):
    """Prints a list of web novels from a specified source."""

    source_factory = SourceFactory(source)

    if source_factory.source is None:
        return click.echo("Invalid source!")
    
    wnsource = source_factory.create_source()

    if wnsource is None:
        return click.echo("Source unavailable!")
    
    click.clear()
    click.echo('Available novels:\n')

    for i, novel in enumerate(wnsource.list_novels()):
        click.echo(f"{i+1}) {novel}")
    
    click.echo("\n-------------------------------------\n")
    click.echo("Page 1 of 1")