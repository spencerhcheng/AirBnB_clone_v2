#!/usr/bin/python3
# Starts flask web application
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    return "HBNB"


@app.route('/c/<text>')
def print_text(text):
    return "C %s" % text.replace('_', ' ')


@app.route('/python/<text>')
@app.route('/python')
def print_python(text="is cool"):
    return "Python {}".format(text.replace('_', ' '))
if (__name__) == "__main__":
    app.run(host='0.0.0.0', port=5000)
