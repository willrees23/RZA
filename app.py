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
        # check if username is taken
        user = database.get_user_by_username(username)
        if user:
            return render_template(page, error="Username is unavailable.")
        
        # check if password and conf_password match
        if password != conf_password:
            return render_template(page, error="Passwords do not match.")
        
        user = database.create_user(email, username, password)

        return render_template(page, info="Account created successfully.")
    return render_template(page)

@app.route("/login", methods=["GET", "POST"])
def login():
    page = "account/login.html"
    # login functionality
    # if the method is post, they've used the form, if the method is get, they're viewing the page
    if request.method == "POST":
        # get the username and password from the form
        email = request.form["email"]
        password = request.form["password"]
        # check if the user exists in the database
        user = database.get_user_by_email(email)
        # for now, just print the user
        if not user:
            return render_template(page, error="Incorrect email or password.")
        
    else: return render_template(page)


if __name__ == "__main__":
    app.run(debug=True)