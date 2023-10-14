from flask import Flask, url_for, redirect, Response
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, AdminIndexView
from flask_basicauth import BasicAuth
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS

from config import Config
app = Flask(__name__)
CORS(app=app)
app.config.from_object(Config)

basic_auth = BasicAuth(app)
db = SQLAlchemy(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)
class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return basic_auth.authenticate()

    def inaccessible_callback(self, name, **kwargs):
        if not self.is_accessible():
            return Response(
                'Could not verify your access level for that URL.\n'
                'You have to login with proper credentials', 401,
                {'WWW-Authenticate': 'Basic realm="Login Required"'})
        return super().inaccessible_callback(name, **kwargs)

admin = Admin(app, name='My App', template_mode='bootstrap3', index_view=MyAdminIndexView())

from app import auth_routes, models, main_page_routes, user_profile_routes, ai_routes, getter_routes
