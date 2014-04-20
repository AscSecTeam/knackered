from flask import Flask

from knackered.settings import Section
from knackered.endpoints import config


def create_app(settings):
    app = Flask(__name__)
    app_settings = getattr(settings, "app", Section("app", {}))
    app.config.update(
        (key.upper(), value)
        for key, value in app_settings.data.iteritems()
    )
    app.register_blueprint(config, url_prefix="/config")

    return app
