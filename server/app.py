from typing import Optional

from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__)
app_realtime = SocketIO(app, cors_allowed_origins="*")
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/", methods=["GET"])
def index():
    return "<h1> Editor root </h1>"


@app_realtime.on("message")
def handle_realtime_editor_content(serialized_content: Optional[str] = None):
    app_realtime.emit("message", serialized_content)


if __name__ == "__main__":
    app_realtime.run(app)
