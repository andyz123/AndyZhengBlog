from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY'] = 'secretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://b3d6a39b7a3e9d:dfcdbd62@us-cdbr-iron-east-03.cleardb.net/heroku_f4b69676d6eb41c'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False

db = SQLAlchemy(app)
Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'

from socialblogproject.core.views import core
from socialblogproject.error_pages.handlers import error_pages
from socialblogproject.users.views import users
from socialblogproject.blog_posts.views import blog_posts

app.register_blueprint(core)
app.register_blueprint(error_pages)
app.register_blueprint(users)
app.register_blueprint(blog_posts)
