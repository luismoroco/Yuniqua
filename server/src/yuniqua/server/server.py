import redis
from flask import Flask
from flask_session import Session

__all__ = ["app"]

app = Flask(__name__)

app.secret_key = "MAKANAKY"
app.config["SESSION_TYPE"] = "redis"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_KEY_PREFIX"] = "yuniqua:"
app.config["SESSION_REDIS"] = redis.from_url("redis://localhost:6379")

Session(app)
