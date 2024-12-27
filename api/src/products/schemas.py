from .. import ma
from .models import Product, Classification, Supplier
from marshmallow_sqlalchemy.fields import Nested
from marshmallow import fields, validate


class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        include_fk = True
        # include_relationships = True
        # load_instance = True


class ClassificationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Classification
        # include_relationships = True

    # Override relationship data to use a nested representation rather than pks
    products = Nested(ProductSchema, many=True, exclude=("classification_id",))


class SupplierSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Supplier
        # include_relationships = True
    
    # override field to add custom validation
    ruc = fields.String(validate=validate.Length(min=9, max=13))
    email = fields.Email()