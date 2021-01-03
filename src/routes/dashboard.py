# Packages
import requests
from flask import Blueprint, render_template, session
from src.decorators import login_required

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')


# Dashboard Page
@bp.route('/')
@login_required
def dashboard():
    return render_template('dashboard.html', session=session)


# Memes Page
@bp.route('/memes')
@login_required
def memes():
    response = requests.get('https://api.imgflip.com/get_memes')
    if response.status_code == 200:
        res_data = response.json()
        if res_data['success'] is True:
            memes_list = []
            for i, meme in enumerate(res_data['data']['memes']):
                if i == 5:
                    break

                memes_list.append(meme)

            return render_template('memes.html', memes=memes_list)
    return render_template('failed.html', msg="Error while getting memes")
