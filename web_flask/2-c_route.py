#!/usr/bin/python3
""" Starts Flask Web Application"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """Displays Hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """"Displays HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C_text(text):
    """Displays C followed by text"""
    text = text.replace('_', " ")
    return 'C {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
