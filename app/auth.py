from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from models import User
from main import db

auth = Blueprint("auth", __name__)


@auth.route("/login")
def login_page():
    return render_template("login.html")


@auth.route("/logout")
@login_required
def logout_page():
    logout_user()
    return redirect(url_for('auth.login_page'))


@auth.route("/register")
def register_page():
    return render_template("register.html")


@auth.route("/register", methods=["POST"])
def register():
    email = request.form.get("email")
    name = request.form.get("name")
    password = request.form.get("password")

    user = User.query.filter_by(email=email).first()

    if user:
        flash("Email address already exists")
        return redirect(url_for("auth.register_page"))

    new_user = User(email=email, name=name, password=generate_password_hash(password, method="sha256"))
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for("auth.login_page"))


@auth.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    some_password = request.form.get("password")
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()
    unsuccessfull_login_msg = "Check your authorization details"
    if not user:
        # if we fail here we won't even try to bother DB
        flash(unsuccessfull_login_msg)
        return redirect(url_for("auth.login_page"))

    encrypted_password = user.password
    password_correct = check_password_hash(encrypted_password, some_password)

    if password_correct:
        login_user(user, remember=remember)
        response = redirect(url_for("main.test_method_page"))
        return response
    else:
        flash(unsuccessfull_login_msg)
        return redirect(url_for("auth.login_page"))
