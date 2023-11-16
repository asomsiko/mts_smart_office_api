from app import app, jwt
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import User, State, UserSchema, Advertisement, AdvertisementSchema, Achivement, AchivementSchema
from flask import jsonify
import requests

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.get(identity)


@app.route("/user-profile/reminders", methods=["GET"])
@jwt_required(refresh=True)
def reminders():
    pass

@app.route("/user-profile", methods=["GET"])
@jwt_required(refresh=True)
def user_profile():
    user_id = get_jwt_identity()
    user = User.query.filter(User.id == user_id)
    user_schema = UserSchema(many = True)
    response = user_schema.dump(user)
    if user.one().is_manager:
        return jsonify(user=response, complaints=requests.get(f"http://localhost:3000/complaints/{user.one().state}").json())
    else:
        return jsonify(user=response)


@app.route("/user-profile/achivements", methods=["GET"])
@jwt_required(refresh=True)
def user_achivements():
    user_id = get_jwt_identity()
    achivements_query = Achivement.query.filter_by(user_id=user_id)
    achivement_schema = AchivementSchema(many = True)
    if not achivements_query:
        return jsonify(orders='Нет достижений')
    achivements = achivement_schema.dump(achivements_query)
    return jsonify(achivements=achivements)

@app.route("/user-profile/<id>/orders", methods=["GET"])
@jwt_required(refresh=True)
def user_orders(id):
    user_id = id
    orders = Advertisement.query.filter_by(customer_id=user_id)
    if not orders:
        return jsonify(orders='Нет объявлений')
    ad_schema = AdvertisementSchema(many = True).dump(orders)

    return jsonify(orders=ad_schema)

@app.route("/user-profile/<id>/tasks", methods=["GET"])
@jwt_required(refresh=True)
def user_tasks(id):
    user_id = id
    tasks = Advertisement.query.filter_by(employer_id=user_id)
    if not tasks:
        return jsonify(tasks='Нет заданий')
    ad_schema = AdvertisementSchema(many = True).dump(tasks)
    return jsonify(tasks=ad_schema)

@app.route("/user-profile/<id>/settings", methods=["GET", "POST"])
@jwt_required(refresh=True)
def user_settings(id):
    pass
