#!/usr/bin/env python3
'''
Basic flask application
'''
from flask import Flask, render_template, request
from flask_babel import Babel, _


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


@babel.localeselector
def get_locale() -> str:
    '''
    selects a locale to use as default
    '''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def hello_world() -> str:
    '''
    Home route serves index page
    '''
    return render_template('3-index.html')


if __name__ == "__main__":
    '''
    Starts code if not imported
    '''
    app.run()
