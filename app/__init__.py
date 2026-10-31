from flask import Flask
from app.database import init_db


def create_app():
    app = Flask(__name__)

    init_db()

    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app