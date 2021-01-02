# Packages
import requests
from flask import Blueprint, render_template

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')


# Dashboard Page
@bp.route('/')
def dashboard():
    return render_template('dashboard.html')

# Memes Page
@bp.route('/memes')
def memes():

    response = requests.get('https://api.imgflip.com/get_memes')
    if response.status_code == 200:
        res_data = response.json()
        if res_data['success'] is True:
            memes = []
            for i, meme in enumerate(res_data['data']['memes']):
                if i == 5:
                    break

                memes.append(meme)

            return render_template('memes.html', memes=memes)    


    return render_template('failed.html', msg="Error while getting memes")