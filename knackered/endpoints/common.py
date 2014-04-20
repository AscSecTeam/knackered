__all__ = ["common"]

from flask import Blueprint, current_app, request

common = Blueprint("common", __name__)


@common.before_app_request
def before_request():
    access_key = request.args.get("access_key")
    if access_key != current_app.config.get("ACCESS_KEY"):
        return "no access", 403


@common.app_errorhandler(404)
def not_found(error):
    return "", 404
