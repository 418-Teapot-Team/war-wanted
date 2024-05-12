import uuid
import json
from datetime import datetime
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from google.cloud import storage

from config import Config
from db.models import InSearchPerson
from services.external import ml_models


in_search_bp = Blueprint("in_search", __name__, url_prefix="/in_search")


@in_search_bp.route("/add", methods=["POST"])
@jwt_required()
def add_person_in_search():
    data = json.loads(request.form.get("data", "{}"))

    # TODO: validate input
    # try:
    #     validate_input(data)
    # except Exception as e:
    #     return jsonify(error=str(e)), 400

    person_id = str(uuid.uuid4())

    # get image by key "image" from form-data
    image = request.files.get("image")

    in_search_person = InSearchPerson(
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
        relatives_phone=data.get("relatives_phone"),
        posted_date=datetime.now(),
    )

    if image:
        image_name = f"in-search/{person_id}/{person_id}.jpg"
        upload_file(image, image_name)
        in_search_person.set_image(image_name)

    in_search_person.save_to_db()

    ml_models.add_wanted_person(person_id, person_id)

    return jsonify({"message": "Person added to search"}), 201


def upload_file(file, name: str):
    storage_client = storage.Client.from_service_account_json("cloud_credentials.json")
    # storage_client = storage.Client()
    bucket = storage_client.get_bucket(Config.GCP_BUCKET)
    blob = bucket.blob(name)
    blob.upload_from_file(file)
