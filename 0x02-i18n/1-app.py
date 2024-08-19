#!/usr/bin/env python3
'''
Basic flask application
'''
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    '''
    Configuration file for flask
    '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/', strict_slashes=False)
def hello_world() -> str:
    '''
    Home route
    '''
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
