from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    migrate.init_app(app, db)

    from app.models import (
        Cliente,
        Fabrica,
        Colaborador,
        Socio
    )

    from app.routes.dashboard import dashboard_bp

    app.register_blueprint(dashboard_bp)

    return app