# Installed Imports
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Custom Imports
from app import ma, db

@dataclass
class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    miles_per_gallon = db.Column(db.Float)
    cylinders = db.Column(db.Integer)
    displacement = db.Column(db.Float)
    horsepower = db.Column(db.Float)
    weight_in_lbs = db.Column(db.Float)
    acceleration = db.Column(db.Float)
    year = db.Column(db.String(255))
    origin = db.Column(db.String(255))


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
