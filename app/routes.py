import requests

from app import app, db, jwt
from app.models import User

from flask import jsonify
from flask import request

from flask_jwt_extended import create_access_token, create_refresh_token
from flask_jwt_extended import jwt_required


@app.route('/signup', methods=['POST'])
def signup_post():
    email = request.json.get('email')
    name = request.json.get('name')
    surname = request.json.get('surname')
    patronymic = request.json.get('patronymic')
    phone = request.json.get('phone')
    rating = request.json.get('rating')
    state = request.json.get('state')
    password = request.json.get('password')

    if not email or not name or not surname or not patronymic or not password or not phone:
        return jsonify({"error": "Missing required fields"}), 400

    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify({"error": "User with this email address already exists"}), 400

    try:
        new_user = User(
        email=email, 
        name=name, 
        surname=surname, 
        patronymic=patronymic, 
        phone=phone, 
        rating=rating, 
        state=state
        )
        new_user.set_password(password=password)
        db.session.add(new_user)
        db.session.commit()

        access_token = create_access_token(identity=new_user.id)
        refresh_token = create_refresh_token(identity=new_user.id)

        return jsonify({"message": "User created", "access_token": access_token, "refresh_token": refresh_token}), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    if not email or not password:
        return jsonify({"error": "Missing required fields"}), 400

    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password=password):
        return jsonify({"error": "Bad login credentials"}), 401

    access_token = create_access_token(identity=user.id)
    refresh_token = create_refresh_token(identity=user.id)
    return jsonify({"access_token": access_token, "refresh_token": refresh_token}), 200

@app.route("/user-profile", methods=["GET"])
@jwt_required(refresh=True)
def user_profile():
    pass

@app.route("/user-profile/achivements", methods=["GET"])
@jwt_required(refresh=True)
def user_achivements():
    pass

@app.route("/user-profile/orders", methods=["GET"])
@jwt_required(refresh=True)
def user_orders():
    pass

@app.route("/user-profile/tasks", methods=["GET"])
@jwt_required(refresh=True)
def user_tasks():
    pass

@app.route("/user-profile/settings", methods=["GET", "POST"])
@jwt_required(refresh=True)
def user_settings():
    pass

@app.route("/services", methods=["GET"])
@jwt_required(refresh=True)
def services():
    pass

@app.route("/services/gpt", methods=["GET"])
@jwt_required(refresh=True)
def gpt():
    pass

@app.route("/services/mts-services", methods=["GET"])
@jwt_required(refresh=True)
def mts():
    pass

@app.route("/services/yandex-services", methods=["GET"])
@jwt_required(refresh=True)
def yandex():
    pass

@app.route("/services/service-order", methods=["GET"])
@jwt_required(refresh=True)
def service_order():
    pass

@app.route("/services/complaint", methods=["GET"])
@jwt_required(refresh=True)
def complaint():
    pass

@app.route("/services/office-devices", methods=["GET"])
@jwt_required(refresh=True)
def office_devices():
    pass

@app.route("/services/office-map", methods=["GET"])
@jwt_required(refresh=True)
def office_map():
    pass

@app.route("/services/schedule", methods=["GET"])
@jwt_required(refresh=True)
def schedule():
    pass

@app.route("/services/reminders", methods=["GET"])
@jwt_required(refresh=True)
def reminders():
    pass

@app.route('/people-count',  methods=["POST"])
def people_count():
    img = request.files['file']
    url = "http://10.193.159.213:3001/predict"
    img_data = img.read()
    response = requests.post(url, files={'file': ('filename.jpg', img_data, 'image/jpeg')})
    data = response.json()
    count = data.get('count')
    return jsonify(count=count)

@app.route('/face-recognition',  methods=["POST"])
def face_recognition():
    img = request.files['file']
    url = "http://10.193.159.213:3002/predict"
    img_data = img.read()
    response = requests.post(url, files={'file': ('filename.jpg', img_data, 'image/jpeg')})
    data = response.json()
    name = data.get('name')
    return jsonify(name=name)
