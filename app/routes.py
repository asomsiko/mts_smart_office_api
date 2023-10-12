from app import app, db, jwt, model
from app.models import User

from flask import jsonify
from flask import request

from flask_jwt_extended import create_access_token, create_refresh_token
from flask_jwt_extended import current_user
from flask_jwt_extended import jwt_required

from werkzeug.security import generate_password_hash

import face_recognition
from PIL import Image
import os
import pickle
import numpy as np
from typing import List
import onnxruntime as ort
from insightface.app import FaceAnalysis
import shutil


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
    
@app.route("/recognition", methods=["POST"])
def recognition():
    img = request.files['file']
    img.save(os.path.join('app/save', img.filename))
    predict = model.predict_face(os.path.join('app/save', img.filename))
    return jsonify(predict = predict)