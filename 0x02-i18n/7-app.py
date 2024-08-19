#!/usr/bin/env python3
'''
Basic flask application uses
babel to switch between languages
'''
from flask import Flask, render_template, request, g
from flask_babel import Babel, _


app = Flask(__name__)
babel = Babel(app)


class Config:
    '''
    Configuration file for
    flask babel vars
    '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)  # Configuration initialized in app instance
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.timezoneselector
def get_timezone():
    '''
    Selects time zone to per request
    '''
    try:
        if request.args.get("timezone"):
            timezone = request.args.get("timezone")
            check_tz = pytz.timezone(timezone)

        elif g.user and g.user.get("timezone"):
            timezone = g.user.get("timezone")
            check_tz = pytz.timezone(timezone)
        else:
            timezone = app.config["BABEL_DEFAULT_TIMEZONE"]
            check_tz = pytz.timezone(timezone)
    except pytz.exceptions.UnknownTimeZoneError:
        return app.congig['BABEL_DEFAULT_TIMEZONE']

    return timezone


@babel.localeselector
def get_locale() -> str:
    '''
    selects a locale to use as default
    Detects locale variable in requests
    '''
    supported_locales = app.config['LANGUAGES']
    if 'locale' in request.args:
        locale = request.args.get('locale')
        if locale in supported_locales:
            return locale
    if g.user and g.user.get('locale') in supported_locales:
        return g.user.get('locale')
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def hello_world() -> str:
    '''
    Home route serves index page
    index page
    '''
    return render_template('5-index.html')


@app.before_request
def before_request():
    '''
    Called before all request
    '''
    user_data = get_user()
    print(user_data)
    g.user = user_data


def get_user():
    '''
    Get's users from mock database and returns them appropriately
    '''
    if 'login_as' in request.args:
        id = int(request.args.get('login_as'))
        return users.get(id, None)


if __name__ == "__main__":
    '''
    Starts code if not imported
    '''
    app.run()
