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

    # Importa todos os Models
    from app import models

    # Blueprints
    from app.routes.dashboard import dashboard_bp
    from app.routes.operacoes import operacoes_bp
    from app.routes.clientes import clientes_bp
    from app.routes.fabricas import fabricas_bp
    from app.routes.colaboradores import colaboradores_bp

    app.register_blueprint(dashboard_bp)
    app.register_blueprint(operacoes_bp)
    app.register_blueprint(clientes_bp)
    app.register_blueprint(fabricas_bp)
    app.register_blueprint(colaboradores_bp)

    return app