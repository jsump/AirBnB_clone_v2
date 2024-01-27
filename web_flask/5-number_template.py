#!/usr/bin/python3
"""
Module: 5-number_template.py
This module contains a function that starts a Flask web application
"""


from flask import Flask, render_template
from urllib.parse import unquote
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    This retuens the message after defining the route for the application
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    This returns the message after defining the route for hbnb
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def show_c(text):
    """
    This method displays "C" followed by value of text variable
    (replace underscore "_" symbols with space " ")
    """
    text = unquote(text).replace('_', ' ')
    return 'C ' + text


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show_python(text):
    """
    This method displays "Python" follwed by the value of the text
    variable(replace underscore "_" with spaces " ") after defining
    the route
    """
    text = unquote(text).replace('_', ' ')
    return 'Python ' + text


@app.route('/number/<int:n>', strict_slashes=False)
def show_number(n):
    """
    This method wil display the number "n" if only it is an interger
    after defining the route
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def show_number_template(n):
    """
    This method displays a html page is n is an integer
    """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    """
    Flask application run on 0.0.0.0 on port 5000
    """
    app.run(host='0.0.0.0', port=5000)
