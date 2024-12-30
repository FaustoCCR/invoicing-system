from src import db
from .models import Role
from .schemas import UserSchema, RoleSchema
from flask.views import MethodView
from apiflask import APIBlueprint
from .repositories import UserRepository
from src.common.repository import SQLAlchemyRepository
from src.common.services import Service
from .services import UserService
from src.auth.services import auth


users_bp = APIBlueprint("users", __name__, url_prefix="/users")
roles_bp = APIBlueprint("roles", __name__, url_prefix="/roles")

# dependencies
user_repository = UserRepository(db.session)
user_service = UserService(user_repository)
role_repository = SQLAlchemyRepository[Role, int](db.session, Role)
role_service = Service(role_repository)


class UserItemView(MethodView):

    decorators = [users_bp.auth_required(auth)]

    def _get_item(self, id):
        return user_service.get_by_id(id)

    @users_bp.output(UserSchema)
    def get(self, id):
        return self._get_item(id)

    @users_bp.input(UserSchema, location="json")
    @users_bp.output(UserSchema)
    def put(self, id, json_data):
        return user_service.update(id, json_data)

    @users_bp.output({}, status_code=204)
    def delete(self, id):
        return user_service.delete(id)


class UsersGroupView(MethodView):

    decorators = [users_bp.auth_required(auth)]

    @users_bp.output(UserSchema(many=True))
    def get(self):
        return user_service.get_all()


users_bp.add_url_rule("/<int:id>", view_func=UserItemView.as_view("users-item"))
users_bp.add_url_rule("", view_func=UsersGroupView.as_view("users-group"))


class RoleItemView(MethodView):

    decorators = [roles_bp.auth_required(auth)]

    def _get_item(self, id):
        return role_service.get_by_id(id)

    @roles_bp.output(RoleSchema)
    def get(self, id):
        return self._get_item(id)

    @roles_bp.input(RoleSchema, location="json")
    @roles_bp.output(RoleSchema)
    def put(self, id, json_data):
        return role_service.update(id, json_data)

    @roles_bp.output({}, status_code=204)
    def delete(self, id):
        return role_service.delete(id)


class RoleGroupView(MethodView):
    @roles_bp.output(RoleSchema(many=True))
    def get(self):
        return role_service.get_all()

    @roles_bp.input(RoleSchema)
    @roles_bp.output(RoleSchema, status_code=201)
    def post(self, json_data):
        return role_service.create(json_data)


roles_bp.add_url_rule("/<int:id>", view_func=RoleItemView.as_view("roles-item"))
roles_bp.add_url_rule("", view_func=RoleGroupView.as_view("roles-group"))
