from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

app = Flask(__name__)


ma = Marshmallow(app)
app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "postgresql+psycopg2://car:car@localhost/cardb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
app.app_context().push()
migrate = Migrate(app, db, compare_type=True)

def create_app():
    blueprints()
    return app


def blueprints():
    from app.views import car_api

    app.register_blueprint(car_api)
