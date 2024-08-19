#!/usr/bin/env python3
'''
Basic flask application
'''
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world() -> str:
    '''
    Home route
    '''
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(port=5001)
