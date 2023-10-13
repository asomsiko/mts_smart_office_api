from app import app, db, admin
from app.models import *
from flask_admin.contrib.sqla import ModelView
class AdvertisementView(ModelView):
    form_columns = ('title', 'body', 'customer', 'employer', 'price', 'created_at')
    column_list = ('title', 'body', 'customer', 'employer', 'price', 'created_at')

class DeviceView(ModelView):
    form_columns = ('name', 'api_key', 'location')
    column_list = ('name', 'api_key', 'location')

class ReminderView(ModelView):
    form_columns = ('title', 'body', 'remind_at', 'deadline', 'user_id')
    column_list = ('title', 'body', 'remind_at', 'deadline', 'user_id')

class OrderView(ModelView):
    
    form_columns = ('title', 'body', 'room_id')
    column_list = ('title', 'body', 'room_id')

class WishView(ModelView):
    form_columns = ('content', 'user_id')
    column_list = ('content', 'user_id')


with app.app_context():
    db.create_all()
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(State, db.session))
    admin.add_view(AdvertisementView(Advertisement, db.session))
    admin.add_view(ReminderView(Reminder, db.session))
    admin.add_view(DeviceView(Device, db.session))
    admin.add_view(ModelView(Room, db.session))
    admin.add_view(OrderView(Order, db.session))
    admin.add_view(WishView(Wish, db.session))


    app.run(host="localhost", port=3000, debug=True)
