from app import app
from flask_jwt_extended import jwt_required

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