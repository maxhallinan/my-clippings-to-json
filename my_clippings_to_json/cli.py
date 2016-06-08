import click

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument(
    'input',
    required=True,
    type=click.Path(exists=True))
@click.argument(
    'output',
    required=True)
@click.option(
    '--start',
    '-s',
    default=1,
    type=int,
    help='start at line number of input file')
def main(input, output, start):
    click.echo('Hello World!')
