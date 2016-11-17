from dist.Handler import Handler
import click, sys, os

@click.group()
def cli():
    pass

@cli.command()
@click.argument('files')
@click.option('--cv', nargs=2, type=int,
              help="m x n validations, specify m & n. E.g: --cv 5 5")
@click.option('--l', nargs=2, type=str,
              help="learner code to be executed. "
                   "If none, all learners will be executed.")
def f(files, cv, l):
    """
        Enter file or directory path.
    """
    list_of_files = []
    if os.path.isfile(files):
        list_of_files.append(files)
    elif os.path.isdir(files):
        list_of_files = [files+file for file in os.listdir(files)
                         if os.path.isfile(files+file)]
    else:
        click.echo("Unexpected content.")
        sys.exit()
    # I need to fix this.
    m = cv[0] if len(cv) > 0 else None
    n = cv[1] if len(cv) > 1 else None
    handler = Handler(list_of_files, m, n)
