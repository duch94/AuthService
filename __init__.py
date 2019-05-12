from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import logging

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    logging.basicConfig(level=logging.DEBUG)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:asdQWE123@localhost:3306/maindb'
    app.secret_key = 'heh heh mm... https://pp.userapi.com/c855016/v855016469/3342d/qQ3oqKkdnjo.jpg'
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login_page"
    login_manager.init_app(app)

    from models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from main import main as test_blueprint
    app.register_blueprint(test_blueprint)

    with app.app_context():
        # create tables for our models
        db.create_all()

        return app
