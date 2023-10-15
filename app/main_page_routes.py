from app import app, db
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request, jsonify
from app.models import Complaint, ComplaintSchema, User

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

@app.route("/services/complaint", methods=["POST"])
@jwt_required(refresh=True)
def complaint():
    user_id = get_jwt_identity()
    content = request.json.get('content').strip()
    sender = user_id
    target = request.json.get('target_id')

    try:
        complaint = Complaint(
            content = content,
            sender_id = sender,
            target_id = target
        )
        complaint.sender = User.query.filter_by(id=sender).one()
        complaint.target = User.query.filter_by(id=target).one()
        db.session.add(complaint)
        db.session.commit()
        return jsonify(message='Complaint created', complaint=ComplaintSchema(many = True).dump(complaint.query))
    except Exception as ex:
        db.session.rollback()
        return jsonify({"error": str(ex)}), 500



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