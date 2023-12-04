from functools import wraps
from flask import jsonify, session

__all__ = ["authorization_required"]


def authorization_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "user_info" not in session:
            return jsonify({"message": "Access denied", "data": None})
        return func(*args, **kwargs)

    return wrapper
