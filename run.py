from app import app, db, admin
from app.models import *
from flask_admin.contrib.sqla import ModelView

with app.app_context():
    db.create_all()
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(State, db.session))
    admin.add_view(ModelView(Advertisement, db.session))
    admin.add_view(ModelView(Reminder, db.session))
    admin.add_view(ModelView(Device, db.session))
    admin.add_view(ModelView(Room, db.session))
    admin.add_view(ModelView(Order, db.session))
    admin.add_view(ModelView(Wish, db.session))


    app.run(host="localhost", port=3000, debug=True)
