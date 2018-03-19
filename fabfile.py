from fabric.api import cd, env, run, task


PROJECT_ROOT = '/srv/app/'
VENV_DIR = '/srv/venv/'
PYTHON = VENV_DIR + 'bin/python'
PIP = VENV_DIR + 'bin/pip'

env.hosts = []
env.forward_agent = True
env.use_ssh_config = True


@task
def production():
    env.hosts = ['app@node-12.rosti.cz:12768']
    env.environment = 'production'
    env.branch = 'master'


@task
def beta():
    env.hosts = ['app@node-13.rosti.cz:13128']
    env.environment = 'beta'
    env.branch = 'beta'


def restart():
    run('supervisorctl restart app')


def managepy(payload):
    run('%s manage.py %s' % (PYTHON, payload))


def pip(payload):
    run('%s %s' % (PIP, payload))


@task
def deploy():
    with cd(PROJECT_ROOT):
        run('git pull origin %s' % env.branch)
        pip('install -r requirements.txt')
        managepy('migrate')
        managepy('collectstatic --no-input --link')

    restart()
