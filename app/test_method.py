from datetime import datetime
import logging

from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from main import db
from models import VisitorInfo

test = Blueprint("main", __name__)


@test.route("/test_page")
@login_required
def test_method_page():
    return render_template("test.html")


@test.route("/test", methods=["GET"])
@login_required
def test_method():
    logging.info("User uid={uid} performing test method request".format(uid=current_user.id))
    visitor_value = str(request.args.get("key"))
    visitor_ip = str(request.environ["REMOTE_ADDR"])
    ctime = datetime.utcnow()
    user_id = int(current_user.id)

    new_visitor_info = VisitorInfo(visit_time=ctime, ip=visitor_ip, value=visitor_value, userid=user_id)
    db.session.add(new_visitor_info)  # doesnt save to db
    db.session.commit()

    logging.info("User uid={uid} with ip={ip} successfully send value={value}".format(uid=current_user.id,
                                                                                      ip=visitor_ip,
                                                                                      value=visitor_value))
    return redirect(url_for("main.test_method_page"))
