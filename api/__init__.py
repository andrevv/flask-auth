from flask import Flask

app = Flask(__name__)


@app.route("/")
def version():
    return '0.1'
