from flask import session

__all__ = ["authenticated_required"]


def authenticated_required(view_func):
    def wrapper(*args, **kwargs):
        if "user_info" in session:
            return view_func(*args, **kwargs)
        return "Not Authorized"

    return wrapper
