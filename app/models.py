from app import db, ma
from werkzeug.security import check_password_hash, generate_password_hash
from marshmallow_sqlalchemy import fields, auto_field
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    surname = db.Column(db.String, nullable=False)
    patronymic = db.Column(db.String, nullable=False)  # отчество
    email = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String)
    phone = db.Column(db.String(12), nullable=False)
    rating = db.Column(db.Integer, default=0)
    state_id = db.Column(db.Integer, db.ForeignKey("states.id"))
    state = db.relationship("State", foreign_keys=[state_id])
    is_manager = db.Column(db.Boolean)
    def __repr__(self):
        return f"<User {self.surname} {self.name} {self.patronymic}>"
    
    def check_password(self, password):
        return check_password_hash(pwhash=self.password_hash, password=password)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password=password, method='pbkdf2:sha256')
class State(db.Model):
    __tablename__ = "states"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, default="junior")

    def __repr__(self):
        return f"<State {self.name}>"
class Advertisement(db.Model):
    __tablename__ = "advertisements"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    body = db.Column(db.String, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    employer_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    customer = db.relationship("User", foreign_keys=[customer_id])
    employer = db.relationship("User", foreign_keys=[employer_id])

    price = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<Advertisement {self.title}>"
class Reminder(db.Model):
    __tablename__ = "reminders"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    body = db.Column(db.String, nullable=False)
    remind_at = db.Column(db.DateTime, nullable=False)
    deadline = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    owner = db.relationship("User", foreign_keys=[user_id])
    def __repr__(self):
        return f"<Reminder {self.title}>"
class Device(db.Model):
    __tablename__ = "devices"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    api_key = db.Column(db.String(128), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey("rooms.id"))
    location = db.relationship("Room", foreign_keys=[location_id])
class Room(db.Model):
    __tablename__ = "rooms"
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String, default="Work")
    name = db.Column(db.String)
    people_count = db.Column(db.Integer)
class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    body = db.Column(db.String, nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey("rooms.id"))
    room = db.relationship("Room", foreign_keys=[room_id])
class Wish(db.Model):
    __tablename__ = "wishes"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    owner = db.relationship("User", foreign_keys=[user_id])
    
class Complaint(db.Model):
    __tablename__ = "complaints"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    sender_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    target_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    sender = db.relationship("User", foreign_keys=[sender_id])
    target = db.relationship("User", foreign_keys=[target_id])

class Achivement(db.Model):
    __tablename__ = "achivements"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(100))
    description = db.Column(db.String(200))
    date_achieved = db.Column(db.DateTime)
    owner = db.relationship("User", foreign_keys=[user_id])
    

class StateSchema(ma.SQLAlchemySchema):
    class Meta:
        model = State
        load_instance = True

    id = ma.auto_field()
    name = ma.auto_field()
class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True

    id = ma.auto_field()
    name = ma.auto_field()
    surname = ma.auto_field()
    patronymic = ma.auto_field()
    email = ma.auto_field()
    phone = ma.auto_field()
    rating = ma.auto_field()
    state = fields.Nested(StateSchema)

class AchivementSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Achivement
        load_instance = True

    id = ma.auto_field()
    title = ma.auto_field()
    description = ma.auto_field()
    date_achieved = ma.auto_field()
    owner = fields.Nested(UserSchema)

class ComplaintSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Complaint
        load_instance = True

    id = ma.auto_field()
    content = ma.auto_field()
    sender = fields.Nested(UserSchema)
    target = fields.Nested(UserSchema)

class RoomSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Room
        load_instance = True

    id = ma.auto_field()
    type = ma.auto_field()
    name = ma.auto_field()
    people_count = ma.auto_field()
class AdvertisementSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Advertisement
        load_instance = True

    id = ma.auto_field()
    title = ma.auto_field()
    body = ma.auto_field()
    customer = fields.Nested(UserSchema)
    employer = fields.Nested(UserSchema)
    price = ma.auto_field()
    created_at = ma.auto_field()
class ReminderSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Reminder
        load_instance = True

    id = ma.auto_field()
    title = ma.auto_field()
    body = ma.auto_field()
    remind_at = ma.auto_field()
    deadline = ma.auto_field()
    user_id = fields.Nested(UserSchema)
class DeviceSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Device
        load_instance = True

    id = ma.auto_field()
    name = ma.auto_field()
    api_key = ma.auto_field()
    location = fields.Nested(RoomSchema)
class OrderSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Order
        load_instance = True

    id = ma.auto_field()
    title = ma.auto_field()
    body = ma.auto_field()
    room_id = fields.Nested(RoomSchema)
class WishSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Wish
        load_instance = True

    id = ma.auto_field()
    content = ma.auto_field()
    user_id = fields.Nested(UserSchema)