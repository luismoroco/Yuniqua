from src.yuniqua.server import app
from src.yuniqua.user.app import user_blueprint
from src.yuniqua.auth.app import auth_blueprint

__all__ = ["app"]

app.register_blueprint(user_blueprint)
app.register_blueprint(auth_blueprint)
