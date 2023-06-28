from flask import Blueprint, request, url_for
from sqlalchemy.exc import SQLAlchemyError

from app import app
from app.models import Car, db, CarSchema


car_api = Blueprint("car_api", __name__, url_prefix="/cars")


class CarException(Exception):
    def __init__(self, message, code=400):
        self.message = message
        self.code = code


@car_api.errorhandler(CarException)
def handle_scheduler_exception(e):
    app.logger.exception(e)
    return {"success": False, "error": e.message}, e.code


@car_api.errorhandler(SQLAlchemyError)
def handle_scheduler_exception(e):
    app.logger.exception(e)
    return {"success": False, "error": f"{e.orig}"}, 400


@car_api.route("/", methods=["GET"])
@car_api.route("/<int:car_id>", methods=["GET"])
def get_car(car_id=None):
    limit = request.args.get("limit", app.config.get("PAGE_LIMIT"), type=int)
    page_num = request.args.get("page", 1, type=int)
    sort = request.args.get("sort", "name")
    order = request.args.get("order", "asc")
    search = request.args.get("search")
    horsepower = request.args.get("horsepower")
    origin= request.args.get("origin")
    car_data = Car.query

    if car_id:
        car_data = car_data.filter(car_id.id == car_id)
        if not car_data.first():
            raise CarException(
                f" Car ID {car_id} doesn't exist.",
                404,
            )

    car_data = car_data.order_by(getattr(getattr(Car, sort), order)())

    if search:
        car_data = car_data.filter(Car.name.ilike(f"%{search}%"))

    if horsepower:
        car_data = car_data.filter(Car.horsepower.ilike(f"%{horsepower}%"))

    if origin:
        car_data = car_data.filter(Car.origin.ilike(f"%{origin}%"))


    car_dat = car_data.paginate(
        page=page_num, per_page=limit, error_out=False
    )

    cars_schema = CarSchema(many=True)
    data = cars_schema.dump(car_dat.items)

    if len(data) == 0:
        raise CarException(
            "No Car data Present",
            404,
        )

    if car_dat.has_next:
        next_url = url_for(
            "car_api.get_car", page=car_dat.next_num, _external=True
        )
    else:
        next_url = None

    return {
        "success": True,
        "car_data": data,
        "sort": sort,
        "order": order,
        "page": car_dat.page,
        "next_page": next_url,
        "total_pages": car_dat.pages,
        "total": car_dat.total,
        "message": "Car Data Retrieved Successfully.",
    }, 200



