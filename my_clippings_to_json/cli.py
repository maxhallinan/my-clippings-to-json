import app
import click
import sys

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument(
    'input_path',
    required=True,
    type=click.Path(exists=True))
@click.argument(
    'output_path',
    required=True)
@click.option(
    '--start',
    '-s',
    default=1,
    type=int,
    help='start at line number of input file')
def main(input_path, output_path, start):
    last_line_number = app.main(
        input_path, 
        output_path, 
        start_line=start)

    sys.stdout.write(str(last_line_number) + '\n')

if __name__ == '__main__':
    main()
