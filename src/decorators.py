# Packages
from flask import request, url_for, redirect
from functools import wraps


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        cookies = request.cookies.get('sessionId')
        if cookies:
            return func(*args, **kwargs)

        return redirect(url_for('auth.sign_in'))

    return wrapper
