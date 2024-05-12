from sqlalchemy.dialects.postgresql import UUID
from db.models.base import db


class PossibleMatch(db.Model):

    __tablename__ = "possible_matches"

    id = db.Column(db.Integer, primary_key=True)
    found_person_id = db.Column(UUID(as_uuid=True), db.ForeignKey("found_persons.id"), nullable=False)
    in_search_person_id = db.Column(UUID(as_uuid=True), db.ForeignKey("in_search_person.id"), nullable=False)
    match_score = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(255), nullable=False, default="pending")

    found_person = db.relationship("FoundPerson", lazy=True)
    in_search_person = db.relationship("InSearchPerson", lazy=True)

    def __init__(self, found_person_id, in_search_person_id, match_score):
        self.found_person_id = found_person_id
        self.in_search_person_id = in_search_person_id
        self.match_score = match_score

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_possible_matches(cls, found_person_id):
        return cls.query.filter_by(found_person_id=found_person_id).all()
