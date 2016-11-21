from dist.Handler import Handler
from config import LEARNERS
import click, sys, os
sys.dont_write_bytecode = True


@click.group()
def cli():
    pass

@cli.command()
@click.argument('files')
@click.option('--cv', nargs=2,
              type=click.IntRange(min=2, max=None, clamp=False),
              help="m x n validations, specify m & n. E.g: --cv 5 5")
@click.option('--l', type=click.Choice([k for k in LEARNERS]), multiple=True,
              help="Learner to be executed. "
                   "If none, all learners will be executed.")
def f(files, cv, l):
    """
        Enter file or directory path.
        Options are:
            1) m x n cross-validations
            2) choice of learner to be executed
    """

    if os.path.isfile(files):
        list_of_files = [files]
    elif os.path.isdir(files):
        list_of_files = [files+file for file in os.listdir(files)
                         if os.path.isfile(files+file)]
    else:
        click.echo("Unexpected content.")
        sys.exit()
    if l:
        list_of_learners = [learner for learner in l]
    else:
        list_of_learners = [k for k in LEARNERS]
    list_of_learners = list(set(list_of_learners))
    m = cv[0] if len(cv) > 0 else 2
    n = cv[1] if len(cv) > 1 else 2
    handler = Handler(list_of_files, m, n, list_of_learners)
