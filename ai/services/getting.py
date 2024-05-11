from flask import Blueprint, request, jsonify

getting_bp = Blueprint("get", __name__, url_prefix="/get")

@getting_bp.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    return jsonify(message="Invalid role"), 400
