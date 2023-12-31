import redis
from flask import Flask
from flask_session import Session
from flask_socketio import SocketIO
from flask_cors import CORS

__all__ = ["app", "app_io"]

app = Flask(__name__)
app_io = SocketIO(app, cors_allowed_origins="*")
CORS(app, resources={r"/*": {"origins": "*"}})

app.secret_key = "MAKANAKY"
app.config["SESSION_TYPE"] = "redis"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_KEY_PREFIX"] = "yuniqua:"
app.config["SESSION_REDIS"] = redis.from_url("redis://redis:6379")

Session(app)
