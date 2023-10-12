from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_jwt_extended import JWTManager

import face_recognition
from PIL import Image
import os
import pickle
from PIL import Image
import numpy as np
from typing import List
import onnxruntime as ort
from insightface.app import FaceAnalysis
import shutil
from flask_migrate import Migrate

from FaceRecognitionModel.face_recognition import Model
app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "super-pizdec-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)
model = Model()

from app import routes, models
