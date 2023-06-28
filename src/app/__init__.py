# Installed Imports
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


ma = Marshmallow()
db = SQLAlchemy()
migrate = Migrate(db, compare_type=True)


def create_app():
    app = Flask(__name__)
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "postgresql+psycopg2://car:car@localhost/cardb"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    app.app_context().push()

    from app.views import car_api

    app.register_blueprint(car_api)
    return app
