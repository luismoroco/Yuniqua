from src.yuniqua.server import app, app_io

from src.yuniqua.user.app import user_blueprint
from src.yuniqua.auth.app import auth_blueprint
from src.yuniqua.editor.app import editor_blueprint
from src.yuniqua.execution.app import execution_blueprint

__all__ = ["app", "app_io"]

# Blueprint

app.register_blueprint(user_blueprint)
app.register_blueprint(auth_blueprint)
app.register_blueprint(editor_blueprint)
app.register_blueprint(execution_blueprint)

# IO


@app_io.on("connect", namespace="/room")
def connect_to_room():
    pass


@app_io.on("message")
def test_message(content: str):
    app_io.emit("message", content)
