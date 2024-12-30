from src import db, bcrypt
from apiflask import APIBlueprint, abort
from ..accounts.schemas import UserSchema
from ..accounts.services import UserService
from ..accounts.repositories import UserRepository
from .schemas import LoginSchema, TokenSchema
from .services import create_access_token


auth_bp = APIBlueprint("auth", __name__, url_prefix="/auth")

# dependencies
repository = UserRepository(db.session)
service = UserService(repository)


@auth_bp.post("/register")
@auth_bp.input(UserSchema)
@auth_bp.output(UserSchema, status_code=201)
def register(json_data):
    return service.create(json_data)


@auth_bp.post("/login")
@auth_bp.input(LoginSchema)
@auth_bp.output(TokenSchema, status_code=200)
def login(json_data):
    username = json_data["username"]
    password = json_data["password"]
    user = service.get_by_username(username)
    if not user or not bcrypt.check_password_hash(user.password, password):
        abort(401, "Incorrect credentials")
    access_token = create_access_token({"username": user.username})
    return {"access_token": access_token}
