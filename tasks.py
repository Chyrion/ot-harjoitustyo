from invoke import task


@task
def start(ctx):
    # I'm developing this on Windows, where python starts with 'py'
    # Thus I added the try/except, so it starts on one or the other
    try:
        ctx.run('python3 src\index.py')
    except:
        try:
            ctx.run('py src\index.py')
        except:
            print('Windows/Linux error')


@task
def test(ctx):
    ctx.run('pytest src')


@task
def coverage_report(ctx):
    ctx.run('coverage run --branch -m pytest src')
    ctx.run('coverage html')
