from .. import ma
from .models import User, Role
from marshmallow.fields import Nested
from ..individuals.schemas import PersonSchema


class RoleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Role


class UserSchema(ma.SQLAlchemyAutoSchema):

    password = ma.auto_field(load_only=True)
    person = Nested(PersonSchema, dump_only=True)
    person_id = ma.auto_field(load_only=True)

    class Meta:
        model = User
        include_fk = True
        include_relationships = True
