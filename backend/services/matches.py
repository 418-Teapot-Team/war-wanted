from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

from db.models import PossibleMatch, InSearchPerson
from db.models.found_person import FoundPerson


matches_bp = Blueprint("matches", __name__, url_prefix="/matches")


@matches_bp.route("/", methods=["GET"])
@jwt_required()
def get_matches():
    all_found_persons = FoundPerson.query.all()

    result = []

    for found_person in all_found_persons:
        found_person = found_person.to_dict()
        possible_matches = PossibleMatch.get_possible_matches(found_person["id"])
        found_person["possible_matches_num"] = len(possible_matches)
        if len(possible_matches) > 0:
            result.append(found_person)

    return jsonify(result=result), 200


@matches_bp.route("/<string:found_person_id>", methods=["GET"])
@jwt_required()
def get_found_person_matches(found_person_id):
    found_person = FoundPerson.query.get(found_person_id)

    if not found_person:
        return jsonify(message="Person not found"), 404

    possible_matches = PossibleMatch.get_possible_matches(found_person_id)

    return (
        jsonify(
            found_person=found_person.to_dict(),
            possible_matches=[match.in_search_person.to_dict() for match in possible_matches],
        ),
        200,
    )


@matches_bp.route("/wanted/<string:wanted_id>", methods=["GET"])
@jwt_required()
def get_wanted_person_info(wanted_id):
    in_search_person = InSearchPerson.query.get(wanted_id)

    if not in_search_person:
        return jsonify(message="Person not found"), 404

    return jsonify(in_search_person.to_dict()), 200
