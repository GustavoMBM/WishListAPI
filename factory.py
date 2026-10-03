from os import path
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from spectree import SpecTree
from flask_migrate import Migrate

db = SQLAlchemy()

api = SpecTree("flask", title = "WishList_API", version = "1.0", path = "docs")

migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    from controllers import WishBlueprint
    app.register_blueprint(WishBlueprint)

    api.register(app)

    migrate.init_app(app, db)

    return app