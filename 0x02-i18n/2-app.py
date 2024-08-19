#!/usr/bin/env python3
'''
Basic flask application
'''
from flask import Flask, render_template, request
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


@babel.localeselector
def get_locale():
    '''
    selects a locale to use as default
    '''
    return request.accept_languages.best_match(app.config('LANGUAGES'))


@app.route('/', strict_slashes=False)
def hello_world() -> str:
    '''
    Home route
    '''
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(port=5001)
