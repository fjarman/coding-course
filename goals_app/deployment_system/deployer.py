import logging
import os
import signal
from datetime import datetime
from logging.handlers import RotatingFileHandler

from flask import Flask, render_template, request
import subprocess

from git.repo.base import Repo

app = Flask(__name__)


def setup_logging():
    handler = RotatingFileHandler('app.log', maxBytes=10000000, backupCount=3)
    handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    app.logger.addHandler(handler)


def get_current_commit_info(repo_path='.'):
    repo = Repo(repo_path)
    commit = repo.head.commit

    return {
        "commit_hash": commit.hexsha,
        "commit_message": commit.message.strip(),
        "commit_author": commit.author.name
    }

@app.route("/deployer")
def welcome():
    deployment_date = '0000-00-00'
    with open('last_deployment.txt', 'r') as f:
        deployment_date = f.readlines()[0]
    git_info = get_current_commit_info()
    data = {
        'deploy_date': deployment_date,
        'git_hash': git_info['commit_hash'],
        'git_message': git_info['commit_message']
    }
    return render_template('index.html', data=data)


@app.post("/deployer/deploy")
def deploy():
    clean_environ = os.environ.copy()
    clean_environ.pop('WERKZEUG_RUN_MAIN')
    clean_environ.pop('WERKZEUG_SERVER_FD')
    app.logger.info("Running deployment script")
    subprocess.Popen(['bash', 'deployer_redeploy.sh'],
                     env=clean_environ,
                     close_fds=True,
                     preexec_fn=os.setsid,
                     stdout=subprocess.DEVNULL,
                     stderr=subprocess.DEVNULL)
    app.logger.info("Shutting down server")
    os.kill(os.getpid(), signal.SIGINT)
    return 'Server shutting down...'

if __name__ == '__main__':
    app.run(debug=True)
    setup_logging()