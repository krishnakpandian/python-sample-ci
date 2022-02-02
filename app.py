from flask import Flask
from src.controller.slack import create_slack_post
app = Flask(__name__)


@app.route('/')
def hello():
    create_slack_post("Sample Post")
    return 'Hello, World!'
    