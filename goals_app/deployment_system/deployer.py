import logging
from logging.handlers import RotatingFileHandler

from flask import Flask, render_template, request

app = Flask(__name__)

# Setup logging
def setup_logging():
    handler = RotatingFileHandler('app.log', maxBytes=10000000, backupCount=3)
    handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    app.logger.addHandler(handler)


@app.route("/deployer/welcome")
def welcome():
    logging.info(request.form)
    return render_template('index.html')


@app.route("/deployer/deploy")
def deploy():
    logging.info(request.form)

if __name__ == '__main__':
    app.run(debug=True)
    setup_logging()