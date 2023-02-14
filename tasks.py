import sys
from invoke import task


# Determines if users OS is Windows
is_linux = sys.platform != 'win32'


@task
def start(ctx):
    # Use different start commands for Linux and Windows
    if is_linux:
        # For Linux
        ctx.run("python3 src/main.py", pty=True)
    else:
        # For Windows
        ctx.run("python src/main.py", pty=False)


@task
def test(ctx):
    ctx.run("pytest src", pty=is_linux)


@task
def lint(ctx):
    ctx.run("pylint src", pty=is_linux)


@task
def format(ctx):  # pylint: disable=redefined-builtin
    ctx.run("autopep8 --in-place --recursive src", pty=is_linux)


@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=is_linux)
    ctx.run("coverage report -m", pty=is_linux)
    ctx.run("coverage html", pty=is_linux)
