from flask import Flask, render_template, redirect, request, url_for, flash
from flask_mysqldb import MySQL
from models.ModelsUsers import ModelsUsers
from models.entities.users import User
from config import config

app = Flask(__name__)
db = MySQL(app)

@app.route("/")
def index():
    return redirect("login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User(0, request.form["username"], request.form["password"], 0)
        logged_user = ModelsUsers.login(db, user)
        if logged_user != None:
            if logged_user.usertype == 1:
                return redirect(url_for("admin"))
            else:
                return redirect(url_for("home"))
        else:
            flash("Acceso rechazado...")
            return render_template("auth/login.html")
    else:
        return render_template("auth/login.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()

