import re
import uuid
import json
from datetime import datetime
from flask import Blueprint, request, jsonify
from google.cloud import storage


from config import Config
from db.models import FoundPerson


found_bp = Blueprint("found", __name__, url_prefix="/found")


@found_bp.route("/add", methods=["POST"])
def add_found_person():
    # data = request.get_json()
    data = json.loads(request.form.get("data", "{}"))

    try:
        validate_input(data)
    except Exception as e:
        return jsonify(error=str(e)), 400

    # get image by key "image" from form-data
    image = request.files.get("image")

    person_id = uuid.uuid4()
    found_person = FoundPerson(
        id=person_id,
        name=data.get("name"),
        surname=data.get("surname"),
        patronymic=data.get("patronymic"),
        country_of_origin=data.get("country_of_origin"),
        age=data.get("age"),
        height=data.get("height"),
        eyes_color=data.get("eyes_color"),
        hair_color=data.get("hair_color"),
        foot_size=data.get("foot_size"),
        found_lat=data.get("found_lat"),
        found_lon=data.get("found_lon"),
        found_by_number=data.get("found_by_number"),
        condition=data.get("condition"),
        appearence=data.get("appearence"),
    )

    if image:
        image_name = f"found/{person_id}.jpg"
        upload_file(image, image_name)
        found_person.set_image(image_name)

    found_person.save_to_db()

    return jsonify(message="Successfully added found person!")


def upload_file(file, name: str):
    storage_client = storage.Client.from_service_account_json("cloud_credentials.json")
    # storage_client = storage.Client()
    bucket = storage_client.get_bucket(Config.GCP_BUCKET)
    blob = bucket.blob(name)
    blob.upload_from_file(file)


def validate_input(data: dict):

    # validate required fields
    if not data.get("found_date"):
        raise Exception("found_date is required")
    if not data.get("found_by_number"):
        raise Exception("found_by_number is required")
    if not data.get("found_lat"):
        raise Exception("found_lat is required")
    if not data.get("found_lon"):
        raise Exception("found_lon is required")

    # validate datetime format
    try:
        datetime.strptime(data.get("found_date", ""), "%Y-%m-%d %H:%M")
    except ValueError:
        raise Exception("Incorrect data format, should be YYYY-MM-DD HH:MM")

    # validate phone number format using regex
    phone_number = data.get("found_by_number")
    if phone_number and not re.match(r"^\+\d{10,13}$", phone_number):
        raise Exception("Invalid phone number format")

    # validate age
    if not 0 < data.get("age", 0) <= 120:
        raise Exception("Invalid age value")

    # validate height
    if not 50 <= data.get("height", 0) <= 250:
        raise Exception("Invalid height value")