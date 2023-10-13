from app import app
from flask import jsonify, request
import requests

@app.route('/people-count',  methods=["POST"])
def people_count():
    img = request.files['file']
    url = "http://10.193.159.213:3001/predict"
    img_data = img.read()
    response = requests.post(url, files={'file': ('filename.jpg', img_data, 'image/jpeg')})
    data = response.json()
    count = data.get('count')
    return jsonify(count=count)

@app.route('/face-recognition',  methods=["POST"])
def face_recognition():
    img = request.files['file']
    url = "http://10.193.159.213:3002/predict"
    img_data = img.read()
    response = requests.post(url, files={'file': ('filename.jpg', img_data, 'image/jpeg')})
    data = response.json()
    name = data.get('name')
    return jsonify(name=name)
