from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app import app, ma, db


# db = SQLAlchemy(app)
# app.app_context().push()
# migrate = Migrate(app, db, compare_type=True)


@dataclass
class Car(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.column(db.Text)
    miles_per_gallon: int = db.column(db.Integer)
    cylinders: int = db.column(db.Integer)
    displacement: int = db.column(db.Integer)
    horsepower: int = db.column(db.Integer)
    weight_in_lbs: int = db.column(db.Integer)
    acceleration: int = db.column(db.Integer)
    year: str = db.column(db.Text)
    origin: str = db.column(db.Text)


class CarSchema(ma.Schema):
    class Meta:
        fields = (
            "name",
            "miles_per_gallon",
            "cylinders",
            "displacement",
            "horsepower",
            "weight_in_lbs",
            "acceleration",
            "year",
            "origin",
        )
        exclude = ("acceleration",)


car_schema = CarSchema()
cars_schema = CarSchema(many=True)
