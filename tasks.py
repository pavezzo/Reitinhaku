import pty
from invoke import task


@task
def start(ctx):
    ctx.run("python3 reitinhaku/main.py", pty=True)


@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest reitinhaku", pty=True)


@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)


@task
def lint(ctx):
    ctx.run("pylint reitinhaku", pty=True)
