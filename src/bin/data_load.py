#!/usr/bin/env python3
import os
import sys
import json

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(parentdir)
sys.path.insert(0, parentdir)

from app import app
from app.models import db, Car

file_path = os.path.join(os.path.dirname(__file__), "cars.json")

with open(file_path, "r") as file:
    json_data = json.load(file)


def load_data():
    for car in json_data:
        car_data = Car(
            name=car["Name"],
            miles_per_gallon=car["Miles_per_Gallon"],
            cylinders=car["Cylinders"],
            displacement=car["Displacement"],
            horsepower=car["Horsepower"],
            weight_in_lbs=car["Weight_in_lbs"],
            acceleration=car["Acceleration"],
            year=car["Year"],
            origin=car["Origin"],
        )
        db.session.add(car_data)
    db.session.commit()


load_data()
