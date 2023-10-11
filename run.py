from app import app, db

# db.create_all()
app.run(host="localhost", port=3000, debug=True)