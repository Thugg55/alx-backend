#!/usr/bin/env python3
"""
Basic flask_babel app
"""

from flask import Flask, render_template
from flask_babel import Babel

class Config:
    """ Flask app config class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


""" An instance of flask """
app = Flask(__name__)
app.config.from_object(Config)

""" An instance of flask babel """
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index():
    return render_template('1-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

