from flask import Flask, redirect, url_for
from src.models import db
from src.routes import auth, dashboard


def create_app(config_file='config.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    db.init_app(app)

    # Blueprints
    app.register_blueprint(auth.bp)
    app.register_blueprint(dashboard.bp)

    # Index page
    @app.route('/')
    def index():
        return redirect(url_for('auth.sign_in'))

    # DB Creation
    from src.models import users
    @app.route('/create-db')
    def create_db():
        db.create_all()
        return "DB Created!"

    return app
    