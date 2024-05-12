import uuid
from sqlalchemy.dialects.postgresql import UUID

from db.models.base import db


class InSearchPerson(db.Model):

    __tablename__ = "in_search_person"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(100), nullable=True)
    surname = db.Column(db.String(100), nullable=True)
    patronymic = db.Column(db.String(100), nullable=True)
    country_of_origin = db.Column(db.String(100), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    height = db.Column(db.Integer, nullable=True)
    eyes_color = db.Column(db.String(20), nullable=True)
    hair_color = db.Column(db.String(20), nullable=True)
    foot_size = db.Column(db.Integer, nullable=True)
    found_lat = db.Column(db.Float, nullable=True)
    found_lon = db.Column(db.Float, nullable=True)
    found_by_number = db.Column(db.String(20), nullable=True)
    condition = db.Column(db.String(100), nullable=True)
    appearence = db.Column(db.Text(), nullable=True)
    gender = db.Column(db.String(10), nullable=True)
    posted_date = db.Column(db.DateTime, nullable=True)
    specific_signs = db.Column(db.Text(), nullable=True)
    image_path = db.Column(db.String(200), nullable=True)
    relatives_phone = db.Column(db.String(20), nullable=True)
    status = db.Column(db.String(20), nullable=True, default="in_search")

    def set_image(self, image_path):
        self.image_path = image_path

    def to_dict(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "surname": self.surname,
            "patronymic": self.patronymic,
            "country_of_origin": self.country_of_origin,
            "age": self.age,
            "height": self.height,
            "eyes_color": self.eyes_color,
            "hair_color": self.hair_color,
            "foot_size": self.foot_size,
            "found_lat": self.found_lat,
            "found_lon": self.found_lon,
            "found_by_number": self.found_by_number,
            "condition": self.condition,
            "appearence": self.appearence,
            "gender": self.gender,
            "posted_date": self.posted_date,
            "specific_signs": self.specific_signs,
            "image_path": self.image_path,
            "relatives_phone": self.relatives_phone,
            "status": self.status,
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
