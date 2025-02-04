from flask import Flask, request, session, redirect, url_for
from flask import render_template as flask_render_template
from flask_session import Session
from flask_qrcode import QRcode
from data import database
from bcrypt import checkpw
import re
from datetime import datetime

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
QRcode(app)

ALREADY_LOGGED_IN = "Note: you are already logged in."

# setup the database
database.setup()


def render_template(path: str, **kwargs):
    user = session.get("user")
    return flask_render_template(path, user=user, **kwargs)


@app.template_filter("datetime")
def _format_datetime(timestamp, fmt=None):
    if fmt is None:
        fmt = "%Y-%m-%d %H:%M:%S"
    return datetime.fromtimestamp(timestamp / 1000).strftime(fmt)


@app.route("/")
def index():
    # get the user and pass it into home page, we will change content if user exists
    return render_template("index.html")


@app.route("/bookings/new", methods=["POST", "GET"])
def bookingnew():
    if not session.get("user"):
        return redirect("/login")
    # this is the route in which users will create new bookings
    if request.method == "POST":
        date = request.form["date"]
        time = request.form["time"]
        adults = request.form["adults"]
        children = request.form["children"]
        try:
            dateTimeObject = datetime.strptime(date + " " + time, "%Y-%m-%d %H:%M")
        except:
            return render_template("bookings/new.html", error="Something went wrong...")
        database.create_booking(
            session.get("user").id,
            dateTimeObject.timestamp() * 1000,
            adults,
            children,
            False,
        )
        return render_template("bookings/new.html", info="Booking success.")
    return render_template("bookings/new.html")


@app.route("/bookings")
def bookings():
    if not session.get("user"):
        return redirect("/login")

    bookings = database.get_bookings_from_user(1)
    # this is the route in which users will view their existing bookings
    return render_template("bookings/bookings.html", bookings=bookings)


@app.route("/visit-us")
def visitus():
    return render_template("visit-us.html")


@app.route("/account")
def account():
    user = session.get("user")
    if not user:
        # if not logged in, they can't access account page
        return redirect("/")
    return render_template("account/account.html")


@app.route("/search")
def search():
    return render_template("search.html")


@app.route("/logout")
def logout():
    if session.get("user"):
        # if they have user data, get rid of it and go to home page
        session.clear()
    return redirect("/")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    page = "account/signup.html"
    # signup functionality
    # if the method is post, they've used the form, if the method is get, they're viewing the page
    if request.method == "POST":
        # email, username, password, conf_password
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]
        conf_password = request.form["conf_password"]

        # check if email is taken
        user = database.get_user_by_email(email)
        if user:
            return render_template(page, error="Email is already registered.")

        # using regex, validate username
        if not re.match("^[A-Za-z][A-Za-z0-9_]{3,29}$", username):
            return render_template(
                page,
                error="Username must be 4-30 characters, a-Z, 0-9, only permitted symbol is underscore.",
            )

        # check if username is taken
        user = database.get_user_by_username(username)
        if user:
            return render_template(page, error="Username is unavailable.")

        # check if password and conf_password match
        if password != conf_password:
            return render_template(page, error="Passwords do not match.")

        user = database.create_user(email, username, password)

        return render_template(page, info="Account created successfully.")
    else:
        if user := session.get("user"):
            return render_template(page, info=ALREADY_LOGGED_IN)
        return render_template(page)


@app.route("/login", methods=["GET", "POST"])
def login():
    page = "account/login.html"
    # login functionality
    # if the method is post, they've used the form, if the method is get, they're viewing the page
    if request.method == "POST":
        # get the username and password from the form
        emailusername = request.form["emailusername"]
        password = request.form["password"]
        # check if the user exists in the database
        user = database.get_user_by_email(emailusername)
        # for now, just print the user
        if not user:
            user = database.get_user_by_username(emailusername)
            if not user:
                return render_template(
                    page, error="Incorrect email/username or password."
                )
        if not checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
            return render_template(page, error="Incorrect email/username or password.")

        session["user"] = user
        return redirect("/")
    else:
        if user := session.get("user"):
            return render_template(page, info=ALREADY_LOGGED_IN)
        return render_template(page)


if __name__ == "__main__":
    app.run(debug=True)
