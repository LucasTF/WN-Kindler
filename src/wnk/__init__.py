import click

@click.command
def main():
    click.echo(click.style('Hello World!', fg='green'))

if __name__ == '__main__':
    main()