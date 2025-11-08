from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    db.init_app(app)

    # Import and register blueprints here if any
    # from .api.routes import api_bp
    # app.register_blueprint(api_bp)

    return app
