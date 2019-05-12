import logging

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_sessionstore import Session
from flask_session_captcha import FlaskSessionCaptcha

db = SQLAlchemy()

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

app.secret_key = 'heh heh mm... https://pp.userapi.com/c855016/v855016469/3342d/qQ3oqKkdnjo.jpg'

logging.info("SQLAlchemy initializing...")
db_ip = "172.18.0.2"
db_port = "3306"
db_user = "root"
db_pw = "asdQWE123"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{user}:{pw}@{ip}:{port}/maindb'.format(user=db_user,
                                                                                                pw=db_pw,
                                                                                                ip=db_ip,
                                                                                                port=db_port)
db.init_app(app)
logging.info("SQLAlchemy initialized")

logging.info("Captcha module initializing...")
app.config["CAPTCHA_ENABLE"] = True
app.config["CAPTCHA_LENGTH"] = 5
app.config["SESSION_TYPE"] = "sqlalchemy"
Session(app)
captcha = FlaskSessionCaptcha(app)
logging.info("Captcha module initialized")

logging.info("Login manager module initializing...")
login_manager = LoginManager()
login_manager.login_view = "auth.login_page"
login_manager.init_app(app)
logging.info("Login manager module initialized")

from models import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


from auth import auth as auth_blueprint

app.register_blueprint(auth_blueprint)

from test_method import test as test_blueprint

app.register_blueprint(test_blueprint)

with app.app_context():
    # create tables for our models
    db.create_all()

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=80)
