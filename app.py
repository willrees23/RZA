from flask import Flask, render_template, request
from data import database

app = Flask(__name__)

# setup the database
database.setup() 

@app.route("/")
def index():
    # landing page
    return "Hello, World!"

@app.route("/signup", methods=["GET", "POST"])
def signup():
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
            return "Email is already taken"
        # check if username is taken
        user = database.get_user_by_username(username)
        if user:
            return "Username is already taken"
        
        # check if password and conf_password match
        if password != conf_password:
            return "Passwords do not match"
        
        user = database.create_user(email, username, password)

        return user.username + ", you have successfully signed up!"
    return render_template("account/signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    # login functionality
    # if the method is post, they've used the form, if the method is get, they're viewing the page
    if request.method == "POST":
        # get the username and password from the form
        email = request.form["email"]
        # check if the user exists in the database
        user = database.get_user_by_email(email)
        # for now, just print the user
        print(user)
    else: return render_template("account/login.html")


if __name__ == "__main__":
    app.run(debug=True)