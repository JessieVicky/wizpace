from fabric.api import *
from fabric.contrib.console import confirm

env.user = 'root'
env.hosts = ['178.62.88.95']
env.colorize_errors = True
env.key_filename = ['~/.ssh/id_rsa']
env.forward_agent = True

def deploy():
  app_dir = '/webapps/wizpace/'
  with cd(app_dir):
    sudo('git pull origin master')
    sudo('chown -R wizpace_admin:webapps /webapps/wizpace/')

app_dir = '/webapps/wizpace/'

def stop_app():
    with cd(app_dir):
        # stop the app
        sudo('supervisorctl stop wizpace_app')

def start_app():
    with cd(app_dir):
        # stop the app
        sudo('supervisorctl start wizpace_app')

def restart_app():
    with cd(app_dir):
        # stop the app
        sudo('supervisorctl restart wizpace_app')

def pull_and_update():
    stop_app()
    with cd(app_dir):
        # pull from master
        sudo('git pull origin master')
        # update requirements with pip
        sudo('./venv/bin/pip install -r requirements.txt')
        sudo('chown -R wizpace_admin:webapps /webapps/wizpace/')
    start_app()

def pull_and_migrate():
    stop_app()
    pull()
    migrate()
    start_app()

def pull():
    with cd(app_dir):
        # pull from master
        sudo('git pull origin master')
        # make wizpace_admin user of the folder
        sudo('chown -R wizpace_admin:webapps /webapps/wizpace/')

def migrate():
    with cd(app_dir):
        # make any migrations nessecary
        sudo('./venv/bin/python wizpace/manage.py makemigrations')
        sudo('./venv/bin/python wizpace/manage.py migrate')
        sudo('chown -R wizpace_admin:webapps /webapps/wizpace/')
    start_app()


def update():
    with cd(app_dir):
        sudo('./venv/bin/pip install -r requirements.txt')
