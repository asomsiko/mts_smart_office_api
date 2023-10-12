from app import db
from werkzeug.security import check_password_hash, generate_password_hash

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    surname = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    patronymic = db.Column(db.String, nullable=False)  # отчество
    email = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String)
    phone = db.Column(db.String(11), nullable=False)
    rating = db.Column(db.Integer, default=0)
    state = db.Column(db.Integer, db.ForeignKey("states.id"))

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
    customer = db.Column(db.Integer, db.ForeignKey("users.id"))
    employer = db.Column(db.Integer, db.ForeignKey("users.id"))
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

    def __repr__(self):
        return f"<Reminder {self.title}>"


class Device(db.Model):
    __tablename__ = "devices"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    api_key = db.Column(db.String(128), nullable=False)
    location = db.Column(db.Integer, db.ForeignKey("rooms.id"))


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


class Wish(db.Model):
    __tablename__ = "wishes"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)

    