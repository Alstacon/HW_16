import json


from models import User, Order, Offer
from config import db



def load_data(filename) -> list[dict]:
    with open(filename, encoding='UTF-8') as file:
        data = json.load(file)
        return data


def add_user(data):
    for user in data:
        user = User(
            id=user.get("id"),
            first_name=user.get("first_name"),
            last_name=user.get("last_name"),
            age=user.get("age"),
            email=user.get("email"),
            role=user.get("role"),
            phone=user.get("phone"))
        db.session.add(user)
    db.session.commit()



def add_orders(data):
    for order in data:
        order = Order(
            id=order.get("id"),
            name=order.get("name"),
            description=order.get("description"),
            start_date=order.get("start_date"),
            end_date=order.get("end_date"),
            address=order.get("address"),
            price=order.get("price"),
            customer_id=order.get("customer_id"),
            executor_id=order.get("executor_id"),
        )
        db.session.add(order)
    db.session.commit()


def add_offers(data):
    for offer in data:
        offer = Offer(
            id=offer.get("id"),
            order_id=offer.get("order_id"),
            executor_id=offer.get("executor_id")
        )
        db.session.add(offer)
    db.session.commit()


def init_db():
    db.drop_all()
    db.create_all()
    add_user(load_data("data/users.json"))
    add_orders(load_data("data/orders.json"))
    add_offers(load_data("data/offers.json"))


def get_by_id(id, model) -> dict:
    try:
        return db.session.query(model).get(id).make_dict()
    except Exception:
        return {}


def get_all(model) -> list[dict]:
    result = []
    for row in model.query.all():
        result.append(row.make_dict())
    return result


def update_instance(id, model, new_data):
    try:
        db.session.query(model).filter(model.id == id).update(new_data)
        db.session.commit()
    except Exception as e:
        print(e)
        return {}


def delete_instance(id, model):
    try:
        db.session.query(model).filter(model.id == id).delete()
        db.session.commit()
    except Exception as e:
        print(e)
        return {}
