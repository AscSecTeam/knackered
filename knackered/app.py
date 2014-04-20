from flask import Flask, request

from knackered.settings import Section
from knackered.endpoints import config
from knackered.endpoints import common

def create_app(settings):
    app = Flask(__name__)

    # load "app" namespace as flask settings
    app_settings = getattr(settings, "app", Section("app", {}))
    app.config.update(
        (key.upper(), value)
        for key, value in app_settings.data.iteritems()
    )
    # store all settings under app.config to be able
    # to access settings from anywhere
    #  from flask import current_app
    #  current_app.config.get("settings")
    app.config["settings"] = settings

    app.register_blueprint(common)
    app.register_blueprint(config, url_prefix="/config")

    return app
