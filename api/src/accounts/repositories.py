from src.common.repository import SQLAlchemyRepository
from .models import User


class UserRepository(SQLAlchemyRepository[User, int]):
    def __init__(self, session):
        super().__init__(session, User)

    def find_by_username(self, username: str) -> User | None:
        return User.query.filter_by(username=username).first()
