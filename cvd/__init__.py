"""
This __init__.py can create global functions that can be called by any modules. Things to investigate include bootstrap js/html for global 
front-end functions, class defintions, and various "app" related functions/variables.
"""
from flask_bootstrap import Bootstrap5      # flask_bootstrap
from flask import Flask


def create_app(test_config = None):
    app = Flask(__name__)
    bootstrap = Bootstrap5(app)

    from . import cvd
    app.register_blueprint(cvd.bp)

    return app

