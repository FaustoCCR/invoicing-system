import importlib
from apiflask import APIFlask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from src.common.models import Base


db = SQLAlchemy(model_class=Base)
migrate = Migrate()
ma = Marshmallow()
bcrypt = Bcrypt()


def import_models():
    """import modules dynamically"""

    MODEL_PATHS = [
        "src.individuals.models",
        "src.accounts.models",
        "src.products.models",
        "src.invoicing.models",
    ]

    for path in MODEL_PATHS:
        importlib.import_module(path)


def create_app():
    # from src.individuals import models
    # from src.accounts import models
    app = APIFlask(__name__, title="Invoicing API")
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    bcrypt.init_app(app)

    import_models()

    # blueprints
    from .auth.views import auth_bp
    from .individuals.views import bp as ibp
    from .products.views import products_bp
    from .invoicing.views import invoices_bp
    from .accounts.views import users_bp, roles_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(ibp)
    app.register_blueprint(users_bp)
    app.register_blueprint(roles_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(invoices_bp)

    # create the tables
    """ with app.app_context():
    db.create_all() """
    return app
