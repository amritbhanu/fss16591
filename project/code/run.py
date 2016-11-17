from dist.Handler import Handler
import click, sys, os

@click.group()
def cli():
    pass

@cli.command()
@click.argument('files')
def f(files):
    """
        Enter file or directory path.
    """
    list_of_files = []
    if os.path.isfile(files):
        list_of_files.append(files)
    elif os.path.isdir(files):
        # print os.listdir(files)
        list_of_files = [files+file for file in os.listdir(files)
                         if os.path.isfile(files+file)]
    else:
        click.echo("Unexpected content.")
        sys.exit()
    print list_of_files
    handler = Handler(list_of_files)
    # handler.test()
