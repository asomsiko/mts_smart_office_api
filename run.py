from app import app, db
from app.models import State

with app.app_context():
    db.create_all()
    db.session.add(State())
    db.session.commit()
    app.run(host="localhost", port=3000, debug=True)
