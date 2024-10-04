import logging
import os
import signal
from logging.handlers import RotatingFileHandler
from os import environ

from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)


def setup_logging():
    handler = RotatingFileHandler('app.log', maxBytes=10000000, backupCount=3)
    handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    app.logger.addHandler(handler)


@app.route("/deployer/welcome_test")
def welcome():
    app.logger.info(os.environ.get('WERKZEUG_RUN_MAIN'))
    app.logger.info(request.form)
    return render_template('index.html')


@app.post("/deployer/deploy")
def deploy():
    clean_environ = os.environ.copy()
    clean_environ.pop('WERKZEUG_RUN_MAIN')
    clean_environ.pop('WERKZEUG_SERVER_FD')
    app.logger.info("Running deployment script")
    subprocess.Popen(['bash', 'deploy.sh'],
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