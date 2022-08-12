from flask import request

from utils import *
from config import app


@app.route("/users", methods=["GET", "POST"])
def users():
    if request.method == "GET":
        return app.response_class(
            response=json.dumps(get_all(User), indent=2),
            status=200,
            mimetype="application/json"
        )
    elif request.method == "POST":
        if isinstance(request.json, list):
            add_user(request.json)
        elif isinstance(request.json, dict):
            add_user([request.json])
        else:
            print("Неверный тип данных")
        return app.response_class(
            response=json.dumps(request.json, indent=2),
            status=200,
            mimetype="application/json"
        )


@app.route("/users/<int:id>", methods=["GET", "PUT", "DELETE"])
def user_by_id(id):
    if request.method == "GET":
        return app.response_class(
            response=json.dumps(get_by_id(id, User), indent=2),
            status=200,
            mimetype="application/json"
        )
    elif request.method == "PUT":
        data = request.json
        data_new = {
            "id": data.get("id"),
            "first_name": data.get("first_name"),
            "last_name": data.get("last_name"),
            "age": data.get("age"),
            "email": data.get("email"),
            "role": data.get("role"),
            "phone": data.get("phone")
        }
        update_instance(id, User, data_new)
        return app.response_class(
            response=json.dumps(["Изменения сохранены"], indent=2),
            status=200,
            mimetype="application/json"
        )
    elif request.method == "DELETE":
        delete_instance(id, User)
        return app.response_class(
            response=json.dumps(["Пользователь удален"], indent=2),
            status=200,
            mimetype="application/json"
        )


@app.route("/offers", methods=["GET", "POST"])
def offers():
    if request.method == "GET":
        return app.response_class(
            response=json.dumps(get_all(Offer), indent=2),
            status=200,
            mimetype="application/json"
        )
    elif request.method == "POST":
        if isinstance(request.json, list):
            add_offers(request.json)
        elif isinstance(request.json, dict):
            add_offers([request.json])
        else:
            print("Неверный тип данных")
        return app.response_class(
            response=json.dumps(request.json, indent=2),
            status=200,
            mimetype="application/json"
        )


@app.route("/offers/<int:id>", methods=["GET", "PUT", "DELETE"])
def offer_by_id(id):
    if request.method == "GET":
        return app.response_class(
            response=json.dumps(get_by_id(id, Offer), indent=2),
            status=200,
            mimetype="application/json"
        )
    elif request.method == "PUT":
        data = request.json
        data_new = {
            "id": data.get("id"),
            "order_id": data.get("order_id"),
            "executor_id": data.get("executor_id")
        }
        update_instance(id, Offer, data_new)
        return app.response_class(
            response=json.dumps(["Изменения сохранены"], indent=2),
            status=200,
            mimetype="application/json"
        )
    elif request.method == "DELETE":
        delete_instance(id, Offer)
        return app.response_class(
            response=json.dumps(["Оффер удален"], indent=2),
            status=200,
            mimetype="application/json"
        )


@app.route("/orders", methods=["GET", "POST"])
def orders():
    if request.method == "GET":
        return app.response_class(
            response=json.dumps(get_all(Order), indent=2),
            status=200,
            mimetype="application/json"
        )
    elif request.method == "POST":
        if isinstance(request.json, list):
            add_orders(request.json)
        elif isinstance(request.json, dict):
            add_orders([request.json])
        else:
            print("Неверный тип данных")
        return app.response_class(
            response=json.dumps(request.json, indent=2),
            status=200,
            mimetype="application/json"
        )


@app.route("/orders/<int:id>", methods=["GET", "PUT", "DELETE"])
def order_by_id(id):
    if request.method == "GET":
        return app.response_class(
            response=json.dumps(get_by_id(id, Order), indent=2),
            status=200,
            mimetype="application/json"
        )
    elif request.method == "PUT":
        data = request.json
        data_new = {
            "id": data.get("id"),
            "name": data.get("name"),
            "description": data.get("description"),
            "start_date": data.get("start_date"),
            "end_date": data.get("end_date"),
            "address": data.get("address"),
            "price": data.get("price"),
            "customer_id": data.get("customer_id"),
            "executor_id": data.get("executor_id"),
        }
        update_instance(id, Order, data_new)
        return app.response_class(
            response=json.dumps(["Изменения сохранены"], indent=2),
            status=200,
            mimetype="application/json"
        )
    elif request.method == "DELETE":
        delete_instance(id, Order)
        return app.response_class(
            response=json.dumps(["Заказ удален"], indent=2),
            status=200,
            mimetype="application/json"
        )


if __name__ == "__main__":
    init_db()
    app.run()
