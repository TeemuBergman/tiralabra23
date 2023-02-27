import sys
from invoke import task


# Determines if users OS is Windows
IS_LINUX = sys.platform != 'win32'


@task
def start(ctx):
    # Use different start commands for Linux and Windows
    if IS_LINUX:
        # For Linux
        ctx.run("python3 src/main.py", pty=True)
    else:
        # For Windows
        ctx.run("python src/main.py", pty=False)


@task
def test(ctx):
    ctx.run("pytest src", pty=IS_LINUX)


@task
def linter(ctx):
    ctx.run("pylint src", pty=IS_LINUX)


@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src", pty=IS_LINUX)


@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=IS_LINUX)
    ctx.run("coverage report -m", pty=IS_LINUX)
    ctx.run("coverage html", pty=IS_LINUX)
