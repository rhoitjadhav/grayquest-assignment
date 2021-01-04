from src.models import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    email = db.Column(db.String(20))
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(20))
    cookie_consent = db.Column(db.String(10))
