import os
import redis
from flask import Flask, session, redirect, request
from flask_session import Session

app = Flask(__name__)
app.secret_key = "Makanaki"
app.config["SESSION_TYPE"] = "redis"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_KEY_PREFIX"] = "yuniqua:"
app.config["SESSION_REDIS"] = redis.from_url("redis://localhost:6379")

Session(app)


@app.route("/")
def index():
    if "username" in session:
        return f"Logged in as {session['username']}s"

    return "You are not logged in"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form["username"]
        return redirect("/")

    return """
        <form method="post">
        <p><input type=text name=username>
        <p><input type=submit value=Login>
        </form>
    """


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect("/")


if __name__ == "__main__":
    app.run()
