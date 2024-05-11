from flask import Blueprint, jsonify, request

api_bp = Blueprint("api", __name__, url_prefix="/api")

@api_bp.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    return jsonify(message="Invalid role"), 400
