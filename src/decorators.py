# Packages
from flask import request, url_for, redirect
from functools import wraps


def login_required(func):
    @wraps(func)
    def wrapper():
        cookies = request.cookies.get('session')
        if cookies:
            return func()

        return redirect(url_for('auth.sign_in'))

    print(wrapper.__name__)
    return wrapper
