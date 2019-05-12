from datetime import datetime
import logging

from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from __init__ import db
from models import VisitorInfo

main = Blueprint("main", __name__)


@main.route("/test_page")
@login_required
def test_method_page():
    return render_template("test.html")


@main.route("/test", methods=["GET"])
@login_required
def test_method():
    visitor_value = str(request.args.get("key"))
    visitor_ip = str(request.environ["REMOTE_ADDR"])
    ctime = datetime.utcnow()
    user_id = int(current_user.id)

    new_visitor_info = VisitorInfo(visit_time=ctime, ip=visitor_ip, value=visitor_value, userid=user_id)
    db.session.add(new_visitor_info)  # doesnt save to db
    db.session.commit()

    return redirect(url_for("main.test_method_page"))
