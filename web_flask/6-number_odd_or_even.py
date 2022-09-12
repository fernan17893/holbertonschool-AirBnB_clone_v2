#!/usr/bin/python3
""" Starts Flask Web Application"""
from cgitb import text
from flask import Flask, render_template

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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def c_python(text="is cool"):
    """Displays python followed by text, is cool if no text"""
    text = text.replace('_', " ")
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def a_number(n):
    """Displays a number"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_temp(n):
    """Display html template"""
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    """DIsplay HTML template only if n is integer and show if odd/even"""
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
