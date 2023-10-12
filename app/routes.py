from app import app, db, jwt
from app.models import User

from flask import jsonify
from flask import request

from flask_jwt_extended import create_access_token
from flask_jwt_extended import current_user
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token

from werkzeug.security import generate_password_hash


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.filter_by(id=identity).one_or_none()

@app.route('/signup', methods=['POST'])
def signup_post():

    email = request.json.get('email')
    name = request.json.get('name')
    surname = request.json.get('surname')
    patronymic = request.json.get('patronymic')
    phone = request.json.get('phone')
    rating = request.json.get('rating')
    state = request.json.get('state')
    password = request.json.get('password_hash')

    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify({"error": "Email address already exists"}), 400

    new_user = User(email=email, name=name, password_hash=generate_password_hash(password, method='pbkdf2:sha256'),
        surname=surname, patronymic=patronymic, phone=phone, rating=rating, state=state)
    access_token = create_access_token(identity=new_user)
    refresh_token = create_refresh_token(identity=new_user)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created", "access_token": access_token, "refresh_token": refresh_token}), 201

@app.route('/login', methods=['POST'])
def login():
    #TODO: функция которая сырой пароль сравнивает с хэшем
    email = request.json.get('email')
    password = request.json.get('password')
    password = generate_password_hash(password, method='pbkdf2:sha256')
    user = User.query.filter_by(email=email).first()
    if not user or not User.check_password(password=password):
        return jsonify({"error": "Bad login credentials"}), 401
    
    access_token = create_access_token(identity=user)
    refresh_token = create_refresh_token(identity=user)

    return jsonify({"access_token": access_token, "refresh_token": refresh_token}), 200