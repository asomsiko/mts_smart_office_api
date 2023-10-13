from app import app
from flask import jsonify, request
from app.models import *

@app.route("/sorted-devices", methods=["GET"])
def get_sorted_devices():
    """
    Возвращает список устройств, отсортированных по переданному в URL полю.
    
    Параметры:
    sort (string): Имя поля, по которому нужно отсортировать устройства.
    
    Возвращает:
    sorted_devices: Список устройств в формате JSON.
    """
    sort_field = request.args.get('sort')
    if sort_field is None: 
        query =  Device.query.all()
        device_schema = DeviceSchema(many = True)
        response = device_schema.dump(query)
        return jsonify(response)
    query = Device.query.order_by(getattr(Device, sort_field)).all()
    device_schema = DeviceSchema(many = True)
    sorted_devices = device_schema.dump(query)
    return jsonify(sorted_devices)


@app.route("/filtered-devices", methods=["GET"])
def get_filtered_devices():
    """
    Возвращает список  устройств, отфильтрованных по переданному в URL полю.
    
    Параметры:
    filter (string): Имя поля, по которому нужно отфильтровать устройства.
    value (string): Значение поля filter, по которому будут фильтроваться устройства.

    
    Возвращает:
    filtered_devices: Список устройств в формате JSON.
    """
    filter_field = request.args.get('filter')
    filter_value = request.args.get('value')
    if filter_field == None:
        query =  Device.query.all()
        device_schema = DeviceSchema(many = True)
        response = device_schema.dump(query)
        return jsonify(response)   
    query = Device.query.filter_by(**{filter_field: filter_value}).all()
    device_schema = DeviceSchema(many = True)
    filtered_devices = device_schema.dump(query)
    return jsonify(filtered_devices)

@app.route("/sorted-reminders", methods=["GET"])
def get_sorted_reminders():
    """
    Возвращает список напоминаний, отсортированных по переданному в URL полю.
    
    Параметры:
    sort (string): Имя поля, по которому нужно отсортировать напоминания.
    
    Возвращает:
    sorted_advertisements: Список напоминаний в формате JSON.
    """
    sort_field = request.args.get('sort')
    if sort_field is None: 
        query =  Reminder.query.all()
        reminder_schema = ReminderSchema(many = True)
        response = reminder_schema.dump(query)
        return jsonify(response)
    query = Reminder.query.order_by(getattr(Reminder, sort_field)).all()
    reminder_schema = ReminderSchema(many = True)
    sorted_reminders = reminder_schema.dump(query)
    return jsonify(sorted_reminders)

@app.route("/filtered-reminders", methods=["GET"])
def get_filtered_reminders():
    """
    Возвращает список  напоминаний, отфильтрованных по переданному в URL полю.
    
    Параметры:
    filter (string): Имя поля, по которому нужно отфильтровать напоминания.
    value (string): Значение поля filter, по которому будут фильтроваться напоминания.

    
    Возвращает:
    filtered_reminders: Список напоминаний в формате JSON.
    """
    filter_field = request.args.get('filter')
    filter_value = request.args.get('value')
    if filter_field == None:
        query =  Reminder.query.all()
        reminder_schema = ReminderSchema(many = True)
        response = reminder_schema.dump(query)
        return jsonify(response)   
    query = Reminder.query.filter_by(**{filter_field: filter_value}).all()
    reminder_schema = AdvertisementSchema(many = True)
    filtered_reminders = reminder_schema.dump(query)
    return jsonify(filtered_reminders)

@app.route("/sorted-advertisements", methods=["GET"])
def get_sorted_advertisements():
    """
    Возвращает список объявлений, отсортированных по переданному в URL полю.
    
    Параметры:
    sort (string): Имя поля, по которому нужно отсортировать объявления.
    
    Возвращает:
    sorted_advertisements: Список объявлений в формате JSON.
    """
    sort_field = request.args.get('sort')
    if sort_field is None: 
        query =  Advertisement.query.all()
        advertisement_schema = AdvertisementSchema(many = True)
        response = advertisement_schema.dump(query)
        return jsonify(response)
    query = Advertisement.query.order_by(getattr(Advertisement, sort_field)).all()
    advertisement_schema = AdvertisementSchema(many = True)
    sorted_advertisements = advertisement_schema.dump(query)
    return jsonify(sorted_advertisements)

@app.route("/filtered-advertisements", methods=["GET"])
def get_filtered_advertisements():
    """
    Возвращает список  объявлений, отфильтрованных по переданному в URL полю.
    
    Параметры:
    filter (string): Имя поля, по которому нужно отфильтровать объявления.
    value (string): Значение поля filter, по которому будут фильтроваться объявления.

    
    Возвращает:
    filtered_advertisements: Список объявлений в формате JSON.
    """
    filter_field = request.args.get('filter')
    filter_value = request.args.get('value')
    if filter_field == None:
        query =  Advertisement.query.all()
        advertisement_schema = AdvertisementSchema(many = True)
        response = advertisement_schema.dump(query)
        return jsonify(response)   
    query = Advertisement.query.filter_by(**{filter_field: filter_value}).all()
    advertisement_schema = AdvertisementSchema(many = True)
    filtered_advertisements = advertisement_schema.dump(query)
    return jsonify(filtered_advertisements)

@app.route("/states", methods=["GET"])
def get_states():
    """
    Возвращает список штатов сотрудников.
    """
    query =  State.query.all()
    state_schema = StateSchema(many = True)
    response = state_schema.dump(query)
    return jsonify(response)   

@app.route("/filtered-rooms", methods=["GET"])
def get_filtered_rooms():
    """
    Возвращает список  комнат, отфильтрованных по переданному в URL полю.
    
    Параметры:
    filter (string): Имя поля, по которому нужно отфильтровать комнаты.
    value (string): Значение поля filter, по которому будут фильтроваться комнаты.

    
    Возвращает:
    filtered_users: Список комнат в формате JSON.
    """
    filter_field = request.args.get('filter')
    filter_value = request.args.get('value')
    if filter_field == None:
        query =  Room.query.all()
        room_schema = RoomSchema(many = True)
        response = room_schema.dump(query)
        return jsonify(response)   
    query = Room.query.filter_by(**{filter_field: filter_value}).all()
    room_schema = RoomSchema(many = True)
    filtered_rooms = room_schema.dump(query)
    return jsonify(filtered_rooms)

@app.route("/sorted-rooms", methods=["GET"])
def get_sorted_rooms():
    """
    Возвращает список комнат, отсортированных по переданному в URL полю.
    
    Параметры:
    sort (string): Имя поля, по которому нужно отсортировать комнаты.
    
    Возвращает:
    sorted_rooms: Список комнат в формате JSON.
    """
    sort_field = request.args.get('sort')
    if sort_field is None: 
        query =  Room.query.all()
        room_schema = RoomSchema(many = True)
        response = room_schema.dump(query)
        return jsonify(response)
    query = Room.query.order_by(getattr(Room, sort_field)).all()
    room_schema = RoomSchema(many = True)
    sorted_rooms = room_schema.dump(query)
    return jsonify(sorted_rooms)

@app.route("/sorted-users", methods=["GET"])
def get_sorted_users():
    """
    Возвращает список пользователей, отсортированных по переданному в URL полю.
    
    Параметры:
    sort (string): Имя поля, по которому нужно отсортировать пользователей.
    
    Возвращает:
    sorted_users: Список пользователей в формате JSON.
    """
    sort_field = request.args.get('sort')
    if sort_field is None: 
        query =  User.query.all()
        user_schema = UserSchema(many = True)
        response = user_schema.dump(query)
        return jsonify(response)
    query = User.query.order_by(getattr(User, sort_field)).all()
    user_schema = UserSchema(many = True)
    sorted_users = user_schema.dump(query)
    return jsonify(sorted_users)

@app.route("/filtered-users", methods=["GET"])
def get_filtered_users():
    """
    Возвращает список пользователей, отфильтрованных по переданному в URL полю.
    
    Параметры:
    filter (string): Имя поля, по которому нужно отфильтровать пользователей.
    value (string): Значение поля filter, по которому будут фильтроваться пользователи.

    
    Возвращает:
    filtered_users: Список пользователей в формате JSON.
    """
    filter_field = request.args.get('filter')
    filter_value = request.args.get('value')
    if filter_field == "state":
        filter_value = State.query.filter(State.name == filter_value).one_or_none().id
    if filter_field is None:
        query =  User.query.all()
        user_schema = UserSchema(many = True)
        response = user_schema.dump(query)
        return jsonify(response)    
    query = User.query.filter_by(**{filter_field: filter_value}).all()
    user_schema = UserSchema(many = True)
    filtered_users = user_schema.dump(query)
    return jsonify(filtered_users)