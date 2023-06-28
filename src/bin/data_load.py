#!/usr/bin/env python3
import os
import sys
import requests, json

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(parentdir)
sys.path.insert(0, parentdir)

from app import app
from app.models import db, Car
from app.views import car_api


class CarException(Exception):
    def __init__(self, message, code=400):
        self.message = message
        self.code = code


# @car_api.errorhandler(CarException)
# def handle_scheduler_exception(e):
#     app.logger.exception(e)
#     return {"success": False, "error": e.message}, e.code


file_path = "./bin/cars.json"
with open(file_path, 'r') as file: 
    json_data = json.load(file)



def load_data():
    for car in json_data:
        # existing_pokemon = Pokemon.query.filter_by(name=pokemon["Name"]).first()
        # if existing_pokemon:
        #     raise PokemonException(f"Pokemon data already present")
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
