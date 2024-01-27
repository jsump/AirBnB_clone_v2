#!/usr/bin/python3
"""
Module: 0-hello_route

This module contains a function that starts a Falsk web application
"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Define the route
    """
    return 'Hello HBNB!'


if __name__ == '__main__':
    """
    Flask application will be run on 0.0.0.0 port 5000
    """
    app.run(host='0.0.0.0', port=5000)
