from flask import Flask
from model import User, db
from flask_login import LoginManager
# from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret-key")
# database_url = os.environ.get("DATABASE_URL")

# if database_url.startswith("postgres://"):
#     database_url = database_url.replace("postgres://", "postgresql://", 1)

# app.config["SQLALCHEMY_DATABASE_URI"] = database_url
database_url = os.environ.get("DATABASE_URL", "sqlite:///users.db")

if database_url and database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)

# with app.app_context():
#     db.create_all()

login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message = "Please log in to access this page"
login_manager.login_message_category = "warning"

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


from routes import *


if __name__ == "__main__":
    app.run(debug=False)
