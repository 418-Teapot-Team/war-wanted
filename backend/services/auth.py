import datetime
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

from db.models import User


auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    if not data.get("email") or not data.get("password"):
        return jsonify(message="Invalid email or password"), 400

    user = User.find_by_email(data["email"])

    if user:
        return jsonify(message="User already exists"), 400
    else:
        user = User(email=data["email"], password=generate_password_hash(data["password"]))
        user.save_to_db()
        access_token = create_access_token(identity=user.email, expires_delta=datetime.timedelta(days=1))
        return jsonify(message="Successfully signed up!", access_token=access_token)


@auth_bp.route("/signin", methods=["POST"])
def signin():
    data = request.get_json()
    if not data.get("email") or not data.get("password"):
        return jsonify(message="Invalid phone or password"), 401

    user = User.find_by_email(data["email"])
    if user and check_password_hash(user.password, data["password"]):
        access_token = create_access_token(identity=user.email, expires_delta=datetime.timedelta(days=1))
        return jsonify(access_token=access_token, message="Successfully signed in!")
    else:
        return jsonify(message="Invalid phone or password"), 401


@auth_bp.route("/whoami", methods=["GET"])
@jwt_required()
def whoami():
    current_user = get_jwt_identity()
    print(current_user)
    user = User.find_by_email(current_user)

    if not user:
        return jsonify(message="User not found"), 404

    return jsonify(user.json())
