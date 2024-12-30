from .products import bp as products_bp
from .classification import bp as classifications_bp
from .suppliers import bp as suppliers_bp

products_bp.register_blueprint(classifications_bp)
products_bp.register_blueprint(suppliers_bp)

__all__ = ["products_bp"]
