# Packages
import random
import string
from datetime import datetime, timedelta
from flask import Blueprint, render_template, request, redirect, url_for, make_response, jsonify

# Modules
from src.models.users import Users, db

bp = Blueprint('auth', __name__, url_prefix='/auth')


def random_str():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))


# Sign In Page
@bp.route('/sign-in', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'GET':
        response = make_response(render_template('sign_in.html'))
        return response

    else:
        username = request.form['username']
        password = request.form['password']

        user = Users.query.filter_by(username=username).first()
        if user:
            if username == user.username and user.password == password:
                if user.cookie_consent == "Accept":
                    redirect_url = '/dashboard/memes'
                else:
                    redirect_url = '/dashboard'

                expire_date = datetime.now() + timedelta(days=31)
                return jsonify({
                    'success': True,
                    'message': "You're Signed in!",
                    'redirect': redirect_url,
                    'cookie': {
                        'name': 'sessionId',
                        'value': random_str(),
                        'expires': [expire_date.year, expire_date.month, expire_date.day, expire_date.hour,
                                    expire_date.minute, expire_date.second, 0],
                        'path': '/'
                    }
                })

        return jsonify({
            'success': False,
            'message': 'Username or Password is incorrect'
        })


# Sign Up Page
@bp.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'GET':
        return render_template('sign_up.html')

    else:
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        user = Users(first_name=first_name, last_name=last_name, email=email, username=username, password=password)

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.sign_in'))


# Sign Out Page
@bp.route('/sign-out')
def sign_out():
    msg = request.args.get('msg', '')
    response = make_response(render_template('sign_out.html', msg=msg))
    response.delete_cookie('sessionId')
    return response
