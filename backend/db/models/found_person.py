import uuid
from sqlalchemy.dialects.postgresql import UUID

from db.models.base import db


class FoundPerson(db.Model):
    __tablename__ = "found_persons"

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
    found_date = db.Column(db.DateTime, nullable=True)
    specific_signs = db.Column(db.Text(), nullable=True)
    image_path = db.Column(db.String(200), nullable=True)

    def set_image(self, image_path):
        self.image_path = image_path

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
