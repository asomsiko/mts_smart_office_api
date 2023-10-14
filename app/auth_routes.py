import requests

from app import app, db
from app.models import User, State

from flask import jsonify
from flask import request

from flask_jwt_extended import create_access_token, create_refresh_token
from flask_jwt_extended import jwt_required

@app.route('/signup', methods=['POST'])
def signup_post():
    email = request.json.get('email').strip()
    name = request.json.get('name').strip()
    surname = request.json.get('surname').strip()
    patronymic = request.json.get('patronymic').strip()
    phone = request.json.get('phone').strip()
    rating = request.json.get('rating')
    state = request.json.get('state').strip()
    password = request.json.get('password').strip()
    confirm_password = request.json.get('confirm_password').strip()

    if password != confirm_password:
        return jsonify(error="Пароли не совпадают"), 400
    if not email or not name or not surname or not patronymic or not password or not phone:
        return jsonify({"error": "Missing required fields"}), 400

    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify({"error": "Пользователь с этой почтой уже существует"}), 400

    try:
        new_user = User(
        email=email, 
        name=name, 
        surname=surname, 
        patronymic=patronymic, 
        phone=phone, 
        rating=rating,
        )
        state = State.query.filter(State.name == state).one_or_none()
        if state is None:
            return jsonify({"error": "Указанный штат отсутствует в системе"})
        state = state.id
        new_user.state = state
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
    email = request.json.get('email').strip()
    password = request.json.get('password').strip()

    if not email or not password:
        return jsonify({"error": "Missing required fields"}), 400

    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password=password):
        return jsonify({"error": "Bad login credentials"}), 401

    access_token = create_access_token(identity=user.id)
    refresh_token = create_refresh_token(identity=user.id)
    return jsonify({"access_token": access_token, "refresh_token": refresh_token}), 200

