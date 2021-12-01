from flask import Flask
from website.content import bp as content_bp
from website.auth import bp as auth_bp
from website.user_profile import bp as user_bp
from website.errors import bp as error_bp
from website.extensions import db, migrate, login_manager
from config import Config
import os


def create_app(cfg=Config):

    app = Flask(__name__)
    app.config.from_object(cfg)
    register_extensions(app=app)
    register_blueprints(app=app)


    if not os.path.exists('notreddit.db'):
        with app.app_context():
            db.create_all()

    return app

def register_extensions(app):
    db.init_app(app=app)
    migrate.init_app(app=app, db=db)
    login_manager.init_app(app=app)
    login_manager.login_view = 'auth.login_page'

def register_blueprints(app):
    app.register_blueprint(content_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(error_bp)