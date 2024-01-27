#!/usr/bin/python3
"""
Module: 2-c_route.py

This module contains a function that starts a Flask web application
"""


from flask import Flask
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


if __name__ == '__main__':
    """
    Flask application run on 0.0.0.0 on port 5000
    """
    app.run(host='0.0.0.0', port=5000)
