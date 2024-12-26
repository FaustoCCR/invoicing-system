import importlib
from apiflask import APIFlask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from src.common.models import Base


db = SQLAlchemy(model_class=Base)
migrate = Migrate()
ma = Marshmallow(app=None)


def import_models():
    """import modules dynamically"""

    MODEL_PATHS = ["src.customers.models", "src.accounts.models"]

    for path in MODEL_PATHS:
        importlib.import_module(path)


def create_app():
    # from src.customers import models
    # from src.accounts import models
    app = APIFlask(__name__, title="Invoicing API")
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    import_models()

    # blueprints
    from .customers import views

    app.register_blueprint(views.bp)

    # create the tables
    """ with app.app_context():
    db.create_all() """
    return app
