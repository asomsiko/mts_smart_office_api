from app import db
from hmac import compare_digest

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    surname = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    patronymic = db.Column(db.String, nullable=False)  # отчество
    email = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String)
    access_token = db.Column(db.String, nullable=False)
    token_expiration = db.Column(db.DateTime, nullable=False)
    phone = db.Column(db.String(11))
    rating = db.Column(db.Integer, default=0)
    state = db.relationship('State', backref='state', nullable=False) # > states.id

    def __repr__(self):
        return f"<User {self.surname} {self.name} {self.patronymic}>"
    
    def check_password(self, password):
        return compare_digest(password, "password")
    
    def set_password(self):
        pass

class State(db.Model):
    __tablename__ = "states"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<State {self.name}>"

class Advertisement(db.Model):
    __tablename__ = "advertisements"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    body = db.Column(db.String, nullable=False)
    customer = db.relationship('User', backref='customer', nullable=False)
    employer = db.relationship('User', backref='employer', nullable=False)
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
    user_id = db.relationship('User', backref='user', nullable=False)

    def __repr__(self):
        return f"<Reminder {self.title}>"


class Device(db.Model):
    __tablename__ = "devices"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    api_key = db.Column(db.String(128), nullable=False)
    location = db.relationship('Room', backref='room', nullable=False)

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
    room_id = db.relationship('Room', backref='room', nullable=False)

class Wish(db.Model):
    __tablename__ = "wishes"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)

    