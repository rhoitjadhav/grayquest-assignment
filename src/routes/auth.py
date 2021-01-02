# Packages
from flask import Blueprint, render_template, request, redirect, url_for

# Modules
from src.models.users import Users, db


bp = Blueprint('auth', __name__, url_prefix='/auth')


# Sign In Page
@bp.route('/sign-in', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'GET':
        return render_template('sign_in.html')

    else:
        username = request.form['username']
        password = request.form['password']

        user = Users.query.filter_by(username=username).first()
        if user:
            return redirect(url_for('dashboard.dashboard'))
        else:
            return render_template('failure.html', msg='Username or Password is incorrect')


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
        return redirect(url_for('dashboard.dashboard'))
