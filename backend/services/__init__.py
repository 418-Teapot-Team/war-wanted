from flask import Blueprint

from .auth import auth_bp
from .founds import found_bp


api_bp = Blueprint("api", __name__, url_prefix="/api")

api_bp.register_blueprint(auth_bp)
api_bp.register_blueprint(found_bp)


__all__ = ["api_bp"]
