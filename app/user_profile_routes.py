from app import app, jwt
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import User, State, UserSchema, Advertisement, AdvertisementSchema
from flask import jsonify
import requests

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.get(identity)

@app.route("/user-profile", methods=["GET"])
@jwt_required(refresh=True)
def user_profile():
    user = get_jwt_identity()
    user = User.query.filter(User.id == user)
    user_schema = UserSchema(many = True)
    response = user_schema.dump(user)
    if user.one().is_manager:
        return jsonify(user=response, complaints=requests.get(f"http://localhost:3000/complaints/{user.one().state}").json())
    else:
        return jsonify(user=response)


@app.route("/user-profile/achivements", methods=["GET"])
@jwt_required(refresh=True)
def user_achivements():
    pass

@app.route("/user-profile/orders", methods=["GET"])
@jwt_required(refresh=True)
def user_orders():
    user_id = get_jwt_identity()
    orders = Advertisement.query.filter_by(customer_id=user_id)
    if not orders:
        return jsonify(orders='Нет объявлений')
    ad_schema = AdvertisementSchema(many = True).dump(orders)

    return jsonify(orders=ad_schema)

@app.route("/user-profile/tasks", methods=["GET"])
@jwt_required(refresh=True)
def user_tasks():
    user_id = get_jwt_identity()
    tasks = Advertisement.query.filter_by(employer_id=user_id)
    if not tasks:
        return jsonify(tasks='Нет заданий')
    ad_schema = AdvertisementSchema(many = True).dump(tasks)
    return jsonify(tasks=ad_schema)

@app.route("/user-profile/settings", methods=["GET", "POST"])
@jwt_required(refresh=True)
def user_settings():
    pass
