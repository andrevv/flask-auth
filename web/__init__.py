from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from os import path
import os

load_dotenv()

db = SQLAlchemy()
DB_NAME = 'database.sqlite'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ['FLASK_APP_SECRET_KEY']
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note
    create_database(app)

    return app


def create_database(app):
    if not path.exists('web/' + DB_NAME):
        db.create_all(app=app)
        print('Database created!')
