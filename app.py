from flask import Flask, render_template, request
from data import database

app = Flask(__name__)

# setup the database
database.setup() 

@app.route("/")
def index():
    # landing page
    return "Hello, World!"

@app.route("/login", methods=["GET", "POST"])
def login():
    # login functionality
    # if the method is post, they've used the form, if the method is get, they're viewing the page
    if request.method == "POST":
        # get the username and password from the form
        email = request.form["email"]
        # check if the user exists in the database
        user = database.get_user(email)
        # for now, just print the user
        print(user)
    else: return render_template("account/login.html")


if __name__ == "__main__":
    app.run(debug=True)