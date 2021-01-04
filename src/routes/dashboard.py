# Packages
import random
import requests
from flask import Blueprint, render_template, request, jsonify

# Packages
from src.models.users import Users, db
from src.decorators import login_required

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')


# Dashboard Page
@bp.route('/')
@login_required
def dashboard():
    return render_template('dashboard.html')


# Cookie Consent
@bp.route('/cookie-consent', methods=['POST'])
def cookie_consent():
    consent = request.form['consent']
    username = request.form['user']
    user = Users().query.filter_by(username=username).first()
    if user:
        user.cookie_consent = consent
        db.session.commit()
        if consent == "Accept":
            return jsonify({
                'success': True,
                'message': 'Consent has been recorded',
                'redirect': '/dashboard/memes'
            })
        else:
            return jsonify({
                'success': False,
                'message': 'Sorry Logging you out',
                'redirect': '/auth/sign-out'
            })
    else:
        return jsonify({
            'success': False,
            'message': 'Please Sign-In first',
            'redirect': '/auth/sign-in'
        })


# Memes Page
@bp.route('/memes')
@login_required
def memes():
    response = requests.get('https://api.imgflip.com/get_memes')
    if response.status_code == 200:
        res_data = response.json()
        if res_data['success'] is True:
            memes_list = []
            for sample in random.sample(range(len(res_data['data']['memes'])), 6):
                memes_list.append(res_data['data']['memes'][sample])

            return render_template('memes.html', memes=memes_list)
    return render_template('failed.html', msg="Error while getting memes")
