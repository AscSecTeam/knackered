__all__ = ["config"]

from flask import Blueprint

config = Blueprint("config", __name__)


@config.route("/status")
def status():
    return ""
