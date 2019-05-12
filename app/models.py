from flask_login import UserMixin
from main import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))


class VisitorInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    visit_time = db.Column(db.DateTime)
    ip = db.Column(db.String(15))
    value = db.Column(db.String(255))
    userid = db.Column(db.Integer)
