from .. import ma
from .models import Person


class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
