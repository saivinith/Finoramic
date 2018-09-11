import click
import subprocess

def install_dependency(dependency):
    dependency = dependency.strip()
    if (not dependency):
        return True
    if (dependency[-1] == ','):
        dependency = dependency[:-1]
    status = not (subprocess.call(['pip', 'install', dependency],stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL))
    if (not status):
        click.echo(click.style(dependency, fg='red'))
    return status
    

@click.command()
@click.argument('filepath')
def main(filepath):
    """This script takes file as input and install the dependencies"""
    try:
        dependencyFile = open(filepath, 'r')
        if (all([install_dependency(i.strip()) for i in dependencyFile.readlines()[2:-2]])):
            click.echo(click.style('success', fg='green'))
    except FileNotFoundError as e:
        click.echo(click.style('File not found', fg='red'))


if __name__ == "__main__":
    
    main()
