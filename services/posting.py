from flask import Blueprint, request, jsonify

posting_bp = Blueprint("post", __name__, url_prefix="/post")

@posting_bp.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    return jsonify(message="Invalid role"), 400