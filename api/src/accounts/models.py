from .. import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Boolean, Integer


class Role(db.Model):
    __tablename__ = "roles"
    role: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    status: Mapped[bool] = mapped_column(Boolean(), default=True)


# association table
roles_users = db.Table('roles_users',
                       db.Column('user_id', Integer(), db.ForeignKey('users.id')),
                       db.Column('role_id', Integer(), db.ForeignKey('roles.id')))


class User(db.Model):
    __tablename__ = "users"
    # id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(60), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(60), nullable=False)
    # FK to link User to Person
    person_id: Mapped[int] = mapped_column(ForeignKey("people.id"))

    # Relationship back to Person unidirectional
    person = relationship("Person", lazy="select")
    roles = relationship("Role", secondary=roles_users, backref="roled")
   