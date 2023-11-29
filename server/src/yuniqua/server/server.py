from flask import Flask
from src.yuniqua.auth import auth_blueprint

__all__ = ["app"]

app = Flask(__name__)

app.register_blueprint(auth_blueprint)
