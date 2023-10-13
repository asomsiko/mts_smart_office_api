from app import app
from flask_jwt_extended import jwt_required

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
